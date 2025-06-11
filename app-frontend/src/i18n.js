import i18n from 'i18next';
import { initReactI18next } from 'react-i18next';
import Backend from 'i18next-http-backend';
import LanguageDetector from 'i18next-browser-languagedetector';

// بارگذاری فایل‌های JSON ترجمه
import en from './locales/en.json';
import fa from './locales/fa.json';

i18n
  .use(Backend)
  .use(LanguageDetector)
  .use(initReactI18next)
  .init({
    resources: {
      en: {
        translation: en
      },
      fa: {
        translation: fa
      }
    },
    fallbackLng: 'en', // زبان پیش‌فرض
    interpolation: {
      escapeValue: false
    }
  });

export default i18n;
