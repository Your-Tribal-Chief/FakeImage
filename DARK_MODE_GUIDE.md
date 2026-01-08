# 🌙 Dark Mode Setup Guide

## How to Enable Dark Mode

Streamlit has built-in dark mode support. Here are three ways to use it:

### Method 1: Using Streamlit Settings (Recommended)
1. Run the app: `streamlit run app.py`
2. Click the **hamburger menu** (☰) in the top-right corner
3. Click **Settings**
4. Under **Theme**, select:
   - **Light** - Force light mode
   - **Dark** - Force dark mode
   - **Use system setting** - Auto-detect from your OS

### Method 2: Browser System Preference (Automatic)
The app will automatically detect your system's dark mode setting if you choose "Use system setting"

**On macOS:**
- System Preferences → General → Appearance → Dark

**On Windows:**
- Settings → Personalization → Colors → Choose your mode → Dark

**On Linux:**
- Depends on your desktop environment (usually in System Settings)

### Method 3: Configuration File
Edit `.streamlit/config.toml` in your project folder:

```toml
[theme]
base = "dark"  # Change to "dark" for default dark mode
primaryColor = "#667eea"
backgroundColor = "#0e1117"
secondaryBackgroundColor = "#262730"
textColor = "#fafafa"
```

Then restart the app.

---

## Custom Dark Mode Colors

If you want to customize the dark mode colors, edit `.streamlit/config.toml`:

### Purple/Blue Theme (Current)
```toml
[theme]
base = "dark"
primaryColor = "#667eea"
backgroundColor = "#0e1117"
secondaryBackgroundColor = "#262730"
textColor = "#fafafa"
```

### Green Theme
```toml
[theme]
base = "dark"
primaryColor = "#38ef7d"
backgroundColor = "#0e1117"
secondaryBackgroundColor = "#1a2332"
textColor = "#fafafa"
```

### Orange Theme
```toml
[theme]
base = "dark"
primaryColor = "#ff6a00"
backgroundColor = "#0e1117"
secondaryBackgroundColor = "#262730"
textColor = "#fafafa"
```

---

## Testing Dark Mode

1. **Start the app:**
   ```bash
   streamlit run app.py
   ```

2. **Toggle dark mode:**
   - Click ☰ (top-right) → Settings → Theme → Dark

3. **Verify the following:**
   - ✅ Info cards have dark background
   - ✅ Text is readable (light colored)
   - ✅ Gradient header looks good
   - ✅ Buttons are visible
   - ✅ Result cards (green/red) display correctly
   - ✅ Sidebar is readable

---

## Dark Mode Features in the App

### Automatic Adjustments:
- 📊 **Info cards** - Dark gradient backgrounds
- 📝 **Text** - Light colored for readability
- 🔘 **Buttons** - Maintain gradient styling
- 🎨 **Result cards** - Green/red gradients work in both modes
- 📈 **Progress bars** - Purple gradient visible in both modes
- 🎯 **Header** - Purple gradient looks great in both modes

### CSS Media Query (Automatic):
```css
@media (prefers-color-scheme: dark) {
    .info-card {
        background: linear-gradient(135deg, #2d3748 0%, #1a202c 100%);
        color: #e2e8f0;
    }
}
```

This automatically adjusts when you toggle dark mode!

---

## Troubleshooting

### Issue: Dark mode not applying
**Solution:**
1. Clear browser cache (Ctrl+Shift+R or Cmd+Shift+R)
2. Restart Streamlit server
3. Check `.streamlit/config.toml` exists
4. Try using Settings menu instead of system preference

### Issue: Text is hard to read
**Solution:**
1. Edit `.streamlit/config.toml`
2. Adjust `textColor` to `"#fafafa"` (brighter)
3. Adjust `backgroundColor` to `"#0e1117"` (darker)
4. Restart app

### Issue: Cards look weird in dark mode
**Solution:**
The CSS has media queries that should handle this automatically. If not:
1. Clear browser cache
2. Ensure you're using a modern browser (Chrome, Firefox, Safari)
3. Check browser console for CSS errors (F12)

---

## Quick Test

Run this to test dark mode instantly:

```bash
# Force dark mode via config
echo '[theme]
base = "dark"
primaryColor = "#667eea"
backgroundColor = "#0e1117"
secondaryBackgroundColor = "#262730"
textColor = "#fafafa"' > .streamlit/config.toml

# Run app
streamlit run app.py
```

---

## Screenshots Comparison

### Light Mode Features:
- 🎨 Light gradient info cards (#f5f7fa to #c3cfe2)
- 📝 Dark text (#262730)
- 🌈 Colorful gradients pop on white background
- 🎯 Clean, professional look

### Dark Mode Features:
- 🌙 Dark gradient info cards (#2d3748 to #1a202c)
- ✨ Light text (#e2e8f0)
- 🌈 Gradients still vibrant on dark background
- 🎯 Modern, sleek appearance

---

## Pro Tips

1. **Use "Use system setting"** - Automatically matches your OS
2. **Test both modes** - Ensure app looks good in both
3. **Gradients work great** - Result cards look amazing in dark mode
4. **Don't override system** - Let users choose their preference
5. **CSS media queries** - Handle automatic adjustments

---

## Default Behavior

The app now:
1. ✅ Starts in light mode (default)
2. ✅ Respects user's Streamlit theme setting
3. ✅ Automatically adjusts colors via CSS media queries
4. ✅ Looks great in both light and dark modes
5. ✅ Maintains gradient styling in both modes

---

**To use dark mode: Click ☰ → Settings → Theme → Dark** 🌙

Enjoy your beautiful deepfake detector in dark mode! 🚀
