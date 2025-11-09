# toDocxGenerator.py
import os
import pypandoc

MARKDOWN_DIR = "markdown"
OUTPUT_DIR = "output"

def convert_md_to_docx():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    for file in os.listdir(MARKDOWN_DIR):
        if file.endswith(".md"):
            md_path = os.path.join(MARKDOWN_DIR, file)
            docx_path = os.path.join(OUTPUT_DIR, file.replace(".md", ".docx"))

            print(f"Converting: {file} → {docx_path}")
            try:
                # Read markdown content
                with open(md_path, 'r', encoding='utf-8') as f:
                    md_content = f.read()

                # Convert with pypandoc
                pypandoc.convert_text(
                    md_content,
                    'docx',
                    format='md',
                    outputfile=docx_path,
                    extra_args=[
                        '--standalone',
                        '--dpi=300'
                    ]
                )
                print(f"✅ Success: {docx_path}")
            except Exception as e:
                print(f"❌ Failed: {e}")

if __name__ == "__main__":
    convert_md_to_docx()
    print("✅ Conversion Completed.")