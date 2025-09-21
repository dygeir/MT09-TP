import json
import re

def clean_ipynb(filepath, output_path=None):
    """
    扫描并清理 ipynb 文件中的非法字符
    - 替换常见问题字符 (�, 不间断空格, 弯引号等)
    """
    with open(filepath, "r", encoding="utf-8", errors="replace") as f:
        data = json.load(f)

    fixed = False  # 记录是否修复过

    def clean_text(text):
        nonlocal fixed
        original = text
        text = text.replace("�", "é")       # 典型非法字符 → é
        text = text.replace("\u00A0", " ")  # 不间断空格 → 普通空格
        text = re.sub(r"[“”]", '"', text)   # 弯双引号 → 英文 "
        text = text.replace("’", "'")       # 弯单引号 → 英文 '
        if text != original:
            fixed = True
            print(f"⚠️ 修复: {original.strip()} -> {text.strip()}")
        return text

    # 遍历所有 cell
    for cell in data.get("cells", []):
        if "source" in cell:
            cell["source"] = [clean_text(line) for line in cell["source"]]

    if not output_path:
        if filepath.endswith(".ipynb"):
            output_path = filepath.replace(".ipynb", "_clean.ipynb")
        else:
            output_path = filepath + "_clean"

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    if fixed:
        print(f"\n✅ 清理完成，结果已保存到: {output_path}")
    else:
        print("✨ 未发现非法字符，文件保持不变。")


# 使用方法：
clean_ipynb("tp01.ipynb")  # 生成 notebook_clean.ipynb
# clean_ipynb("notebook.ipynb", "notebook.ipynb")  # 覆盖原文件
