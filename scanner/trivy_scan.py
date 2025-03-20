import os
import subprocess

def scan_image(image_name):
    report_path = f"reports/{image_name.replace(':', '_')}.txt"
    
    print(f"Scanning image: {image_name}")
    result = subprocess.run(["trivy", "image", "--severity", "HIGH,CRITICAL", "--format", "table", image_name], capture_output=True, text=True)

    with open(report_path, "w") as report_file:
        report_file.write(result.stdout)
    
    print(f"Scan complete. Report saved to {report_path}")

if __name__ == "__main__":
    image = input("Enter Docker image name (e.g., nginx:latest): ")
    scan_image(image)

