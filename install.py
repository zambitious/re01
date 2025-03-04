import subprocess

failed_packages = []

with open("requirements3.txt", "r", encoding="utf-8") as f:
    for line in f:
        pkg = line.strip()
        # 忽略空行和注释
        if not pkg or pkg.startswith("#"):
            continue

        print(f"正在安装：{pkg}")
        result = subprocess.run(["pip", "install", pkg])
        if result.returncode != 0:
            print(f"安装失败：{pkg}")
            failed_packages.append(pkg)

if failed_packages:
    print("\n以下包安装失败：")
    for pkg in failed_packages:
        print(pkg)
else:
    print("\n所有包均已成功安装。")
