import json, os, datetime, shutil, uuid

with open("config.json") as f:
    config = json.load(f)

today = datetime.date.today().isoformat()
base_dir = f"sites/{today}-{uuid.uuid4().hex[:6]}"
os.makedirs(base_dir, exist_ok=True)

shutil.copytree("template", base_dir, dirs_exist_ok=True)

title = config["site_title_prefix"] + config["niche"].replace("-", " ").title()

index_path = os.path.join(base_dir, "index.html")

with open(index_path, "r", encoding="utf-8") as f:
    html = f.read()

html = html.replace("{{TITLE}}", title)
html = html.replace("{{DESCRIPTION}}", f"Useful {config['niche']} tool for modern users.")
html = html.replace("{{KEYWORDS}}", f"{config['niche']}, online tool, free tool")

with open(index_path, "w", encoding="utf-8") as f:
    f.write(html)

print("Site generated:", base_dir)