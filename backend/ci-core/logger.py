def write_log(log_path, message):
    try:
        with open(log_path, 'a',encoding="utf-8") as log_file:
            log_file.write(message + '\n')
    except Exception as e:
        print(f"[ERROR] Failed to write log: {str(e)}")
