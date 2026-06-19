/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.html",
    "./static/js/**/*.js",
  ],
  theme: {
    extend: {
      colors: {
        'pekim-blue': '#0062ff',
        'tech-gray': '#f8fafc',
      },
      fontFamily: {
        'mono': ['Space Mono', 'monospace'],
        'sans': ['Inter', 'sans-serif'],
      },
      backgroundImage: {
        /* Using %23 instead of # for the hex code ensures the SVG renders in all browsers */
        'dot-grid': "url(\"data:image/svg+xml,%3Csvg width='20' height='20' viewBox='0 0 20 20' xmlns='http://www.w3.org/2000/svg'%3E%3Ccircle cx='2' cy='2' r='0.5' fill='%230062ff' fill-opacity='0.1' /%3E%3C/svg%3E\")",
      }
    },
  },
  plugins: [],
}


