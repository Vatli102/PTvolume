import glob
import re

SCRIPT_TEMPLATE = '''        function googleTranslateElementInit() {
            new google.translate.TranslateElement({
                pageLanguage: 'vi',
                includedLanguages: 'en,vi',
                autoDisplay: false
            }, 'google_translate_element');
        }

        function setLanguage(lang) {
            localStorage.setItem('ptvolume_lang', lang);
            updateLangButtons(lang);

            // Set cookies
            document.cookie = "googtrans=/vi/" + lang + "; path=/;";
            if (window.location.hostname && window.location.hostname !== '') {
                document.cookie = "googtrans=/vi/" + lang + "; path=/; domain=" + window.location.hostname;
            }

            // Trigger Google Translate dropdown
            const select = document.querySelector('.goog-te-combo');
            if (select) {
                select.value = lang;
                select.dispatchEvent(new Event('change'));
            } else {
                window.location.reload();
            }
        }

        function updateLangButtons(lang) {
            const btnVi = document.getElementById('btn-lang-vi');
            const btnEn = document.getElementById('btn-lang-en');
            if (btnVi && btnEn) {
                if (lang === 'en') {
                    btnEn.classList.add('active');
                    btnVi.classList.remove('active');
                } else {
                    btnVi.classList.add('active');
                    btnEn.classList.remove('active');
                }
            }
        }

        function applyStoredLanguage() {
            const currentLang = localStorage.getItem('ptvolume_lang') || 'vi';
            updateLangButtons(currentLang);
            if (currentLang === 'en') {
                let attempts = 0;
                const checkCombo = setInterval(() => {
                    const select = document.querySelector('.goog-te-combo');
                    if (select) {
                        select.value = 'en';
                        select.dispatchEvent(new Event('change'));
                        clearInterval(checkCombo);
                    }
                    attempts++;
                    if (attempts > 30) clearInterval(checkCombo);
                }, 200);
            }
        }

        document.addEventListener('DOMContentLoaded', () => {
            applyStoredLanguage();
            loadSavedComments();
        });'''

def update_scripts():
    all_files = glob.glob('posts/*.html') + glob.glob('pages/*.html')
    for filepath in all_files:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Replace setLanguage / DOMContentLoaded block
        pattern = re.compile(r'function googleTranslateElementInit\(\) \{.*?document\.addEventListener\(\'DOMContentLoaded\', \(\) => \{.*?loadSavedComments\(\);\s*\}\);', re.DOTALL)
        if pattern.search(content):
            content = pattern.sub(SCRIPT_TEMPLATE, content)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated script in: {filepath}")

if __name__ == '__main__':
    update_scripts()
