import requests

# Expanded array of common paths to crawl, including security-related ones
common_paths = [
  "admin",
  "login",
  "dashboard",
  "config",
  "api",
  "user",
  "register",
  "home",
  "about",
  "contact",
  "robots.txt",
  "sitemap.xml",
  "backup",
  "db",
  "database",
  "test",
  "staging",
  "old",
  "temp",
  "debug",
  "logs",
  "error",
  "server-status",
  "phpinfo.php",
  ".env",
  ".git",
  ".htaccess",
  ".htpasswd",
  "wp-admin",
  "wp-login.php",
  "admin.php",
  "config.php",
  "config.json",
  "setup",
  "install",
  "shell",
  "upload",
  "uploads",
  "cgi-bin",
  "private",
  "secure",
  "hidden",
  "secrets",
  "keys",
  "token",
  "auth",
  "vulnerabilities",
  "password",
  "change-password",
  "forgot-password",
  "reset-password"
]

def crawl_website(base_url, output_file):
  found_urls = []
  failed_urls = []

  with open(output_file, 'w') as file:
    file.write("Crawling results:\n\n")

    for path in common_paths:
      url = f"{base_url.rstrip('/')}/{path}"
      try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
          found_urls.append(url)
          file.write(f"FOUND: {url}\n")
        else:
          failed_urls.append(url)
          file.write(f"FAILED: {url} (Status Code: {response.status_code})\n")
      except requests.RequestException as e:
        failed_urls.append(url)
        file.write(f"FAILED: {url} (Error: {e})\n")

  print("Crawling completed.")
  print(f"Found URLs: {len(found_urls)}")
  print(f"Failed URLs: {len(failed_urls)}")
  print(f"Results written to {output_file}")

if __name__ == "__main__":
  target_url = input("Enter the base URL to crawl (e.g., https://example.com): ").strip()
  output_file = "crawl_results.txt"
  crawl_website(target_url, output_file)