//! Python-Rust bridge for WellnessMate
//! Handles communication between the Tauri backend and Python AI components

use pyo3::prelude::*;
use pyo3::types::PyDict;
use std::path::Path;
use std::sync::Once;
use anyhow::{Result, Context};

static START: Once = Once::new();
static mut PYTHON_INITIALIZED: bool = false;

/// Initialize the Python interpreter and set up the Python path
pub fn initialize_python() -> Result<()> {
    START.call_once(|| {
        // Add the python directory to the Python path
        let python_dir = std::env::current_dir()
            .expect("Failed to get current directory")
            .parent()
            .expect("Failed to get parent directory")
            .join("python");

        let python_path = python_dir.to_str()
            .context("Failed to convert Python path to string")?;

        std::env::set_var("PYTHONPATH", python_path);
        
        // Initialize Python
        pyo3::prepare_freethreaded_python();
        
        unsafe {
            PYTHON_INITIALIZED = true;
        }
    });

    Ok(())
}

/// Call a Python function with the given arguments
pub fn call_python_function(
    module_name: &str,
    function_name: &str,
    args: Option<&[&str]>,
    kwargs: Option<&[(&str, &str)]>,
) -> Result<String> {
    Python::with_gil(|py| {
        // Import the module
        let module = PyModule::import(py, module_name)?;
        
        // Get the function
        let func = module.getattr(function_name)?;
        
        // Prepare arguments
        let py_args = match args {
            Some(args) => {
                let py_list = PyList::new(py, args);
                py_list.into()
            }
            None => pyo3::types::PyTuple::empty(py).into(),
        };
        
        // Prepare keyword arguments
        let py_kwargs = PyDict::new(py);
        if let Some(kwargs) = kwargs {
            for (k, v) in kwargs {
                py_kwargs.set_item(k, v)?;
            }
        }
        
        // Call the function
        let result = func.call(py, py_args, Some(py_kwargs))?;
        
        // Convert the result to a string
        let result_str = result.to_string();
        Ok(result_str)
    })
}

/// Initialize the AI Engine in Python
pub fn initialize_ai_engine() -> Result<()> {
    initialize_python()?;
    
    Python::with_gil(|py| {
        // Import the AI engine
        let module = PyModule::import(py, "ai_engine")?;
        
        // Get the AI engine instance
        let ai_engine = module.getattr("ai_engine")?;
        
        // Call the initialize method
        ai_engine.call_method0("initialize")?;
        
        Ok(())
    })
}

/// Process a query using the AI Engine
pub fn process_ai_query(query: &str) -> Result<String> {
    initialize_python()?;
    
    Python::with_gil(|py| {
        // Import the AI engine
        let module = PyModule::import(py, "ai_engine")?;
        
        // Get the AI engine instance
        let ai_engine = module.getattr("ai_engine")?;
        
        // Call the process_query method
        let result = ai_engine.call_method1("process_query", (query,))?;
        
        // Convert the result to a string
        let result_str = result.to_string();
        Ok(result_str)
    })
}
