#![cfg_attr(
    all(not(debug_assertions), target_os = "windows"),
    windows_subsystem = "windows"
)]

use tauri::Manager;
use serde::Serialize;
use std::sync::Mutex;
use std::path::PathBuf;
use anyhow::Result;

// Import our Python bridge
mod python_bridge;
use python_bridge::{initialize_ai_engine, process_ai_query};

// Prevents additional console window on Windows in release
#[cfg_attr(not(debug_assertions), windows_subsystem = "windows")]

// Learn more about Tauri commands at https://tauri.app/v1/guides/features/command
#[tauri::command]
async fn greet(name: &str) -> String {
    println!("Received greeting request from: {}", name);
    format!("Hello, {}! Welcome to WellnessMate 🚀", name)
}

#[tauri::command]
async fn ask_ai(query: String) -> Result<String, String> {
    println!("Processing AI query: {}", query);
    
    match process_ai_query(&query) {
        Ok(response) => Ok(response),
        Err(e) => {
            eprintln!("Error processing AI query: {}", e);
            Err(format!("Failed to process your request: {}", e))
        }
    }
}

fn main() {
    // Initialize the AI engine
    if let Err(e) = initialize_ai_engine() {
        eprintln!("Failed to initialize AI engine: {}", e);
        // We'll continue running even if AI initialization fails
        // The app can still function with reduced functionality
    }

    tauri::Builder::default()
        .setup(|app| {
            let main_window = app.get_window("main").unwrap();
            
            // You can add initialization code here
            println!("WellnessMate application started!");
            
            // Initialize the Python environment
            if let Err(e) = python_bridge::initialize_python() {
                eprintln!("Warning: Failed to initialize Python: {}", e);
            }
            
            Ok(())
        })
        .invoke_handler(tauri::generate_handler![greet, ask_ai])
        .run(tauri::generate_context!())
        .expect("error while running tauri application");
}
