use pyo3::prelude::*;
use std::path::Path;

fn main() -> PyResult<()> {
    // Initialize Python
    pyo3::prepare_freethreaded_python();
    
    // Get the current directory
    let current_dir = std::env::current_dir()?;
    let python_script = current_dir.join("python").join("test_bridge.py");
    
    if !python_script.exists() {
        eprintln!("Error: Python script not found at {:?}", python_script);
        return Ok(());
    }
    
    println!("Running Python script: {:?}", python_script);
    
    // Run Python script with arguments
    let name = "Rust";
    let output = std::process::Command::new("python3")
        .arg(python_script.to_str().unwrap())
        .arg(name)
        .output()?;
    
    println!("Python script output:");
    if !output.stdout.is_empty() {
        println!("stdout: {}", String::from_utf8_lossy(&output.stdout));
    }
    if !output.stderr.is_empty() {
        eprintln!("stderr: {}", String::from_utf8_lossy(&output.stderr));
    }
    
    Ok(())
}
