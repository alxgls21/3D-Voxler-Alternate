# 🌍 3D Γεωλογική Οπτικοποίηση με Python - Voxler Alternative

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![PyVista](https://img.shields.io/badge/PyVista-0.42+-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

Ένα ολοκληρωμένο εργαλείο για τρισδιάστατη απεικόνιση γεωλογικών και περιβαλλοντικών δεδομένων, εμπνευσμένο από το επαγγελματικό λογισμικό **Voxler** της Golden Software. Δημιουργημένο εξ ολοκλήρου με **Python** και **PyVista**.

## 🌟 Βασικά Χαρακτηριστικά!

### 🎯 Επαγγελματική 3D Οπτικοποίηση
- **3D Isosurfaces** με προσαρμόσιμη διαφάνεια και χρωματικές κλίμακες
- **Orthogonal Slices** για εσωτερικές τομές του μοντέλου
- **Borehole Visualization** με αναλυτικά labels και κυλινδρικές αναπαραστάσεις
- **Custom Axes & Grid** με χρωματικούς άξονες (X: κόκκινο, Y: πράσινο, Z: μπλε)

### ⚡ Διαδραστικότητα & Animation
- **Interactive Widgets** για real-time προσαρμογή isosurface levels
- **Time-series Animations** για χρονική εξέλιξη δεδομένων
- **Multiple View Exports** (front, back, left, right, top, bottom)

### 📊 Επιστημονική Αξιολόγηση
- **Cross-Validation** για αξιολόγηση αξιοπιστίας interpolation (R², MSE)
- **Bootstrap Uncertainty Analysis** για confidence intervals
- **Στατιστικές Αναφορές** σε HTML format

## 🚀 Γρήγορη Εκκίνηση

### Προαπαιτούμενα
- **Python 3.7+**
- **macOS/Linux/Windows**
- **8GB+ RAM** (συνιστάται για μεγάλα datasets)

### Εγκατάσταση
Clone το repository
git clone https://github.com/yourusername/3d-geo-visualization.git
cd 3d-geo-visualization

Δημιουργία virtual environment
python3 -m venv env
source env/bin/activate # Linux/macOS

ή
env\Scripts\activate # Windows

Εγκατάσταση dependencies
pip install -r requirements.txt


### Πρώτη Εκτέλεση
1. Καθαρισμός δεδομένων (μόνο την πρώτη φορά)
python scripts/clean_csv.py

2. Κύρια 3D οπτικοποίηση
python scripts/pyvista_voxler.py


## 📂 Δομή Project
3d-geo-visualization/
├── 📁 data/
│ ├── bruse.csv # Αρχικά δεδομένα (raw)
│ └── bruse_clean.csv # Καθαρισμένα δεδομένα
├── 📁 scripts/
│ ├── clean_csv.py # Καθαρισμός & προεπεξεργασία δεδομένων
│ ├── explore_csv.py # Στατιστική ανάλυση δεδομένων
│ ├── pyvista_voxler.py # 🎯 ΚΥΡΙΑ 3D ΟΠΤΙΚΟΠΟΙΗΣΗ
│ ├── validation.py # Cross-validation & uncertainty
│ ├── interactive_widgets.py # Διαδραστικό PyVista με sliders
│ ├── animation_time.py # Time-series animations
│ ├── export_utils.py # Εξαγωγή εικόνων & αναφορών
│ ├── isosurface_plot.py # Plotly 3D visualization
│ ├── plot3d_scatter.py # Matplotlib scatter plot
│ └── config.py # Ρυθμίσεις και παράμετροι
├── 📁 outputs/ # Αποτελέσματα & αναφορές (auto-generated)
│ ├── 3d_voxler_style.png
│ ├── time_evolution.gif
│ ├── validation_report.html
│ └── multiple_views/
├── 📁 env/ # Python virtual environment
├── README.md # Αυτό το αρχείο
└── requirements.txt # Python dependencies


## 🎮 Τι να Τρέξεις Τώρα

### 🏃‍♂️ Για Γρήγορα Αποτελέσματα
python scripts/pyvista_voxler.py

**Αποτέλεσμα:** Πλήρης 3D visualization με isosurfaces, boreholes, slices

### 🔬 Για Επιστημονική Αξιολόγηση
python scripts/validation.py

**Αποτέλεσμα:** R² score, MSE, uncertainty analysis

### 🎬 Για Animation (Time-series)
python scripts/animation_time.py

**Αποτέλεσμα:** `time_evolution.gif` με χρονική εξέλιξη

### 🎛️ Για Διαδραστικότητα
python scripts/interactive_widgets.py

**Αποτέλεσμα:** Interactive sliders για real-time control

## 📊 Τύποι Δεδομένων που Υποστηρίζονται

### Ελάχιστες Απαιτήσεις CSV
| Στήλη | Περιγραφή | Τύπος |
|-------|-----------|-------|
| `x` | X συντεταγμένη | float |
| `y` | Y συντεταγμένη ή τιμή μέτρησης | float |
| `z` | Z συντεταγμένη | float |

### Προαιρετικές Στήλες
| Στήλη | Περιγραφή | Τύπος |
|-------|-----------|-------|
| `time` | Χρονική διάσταση | float |
| `x_coords` | Grid coordinates X | int |
| `y_coords` | Grid coordinates Y | float |

## ⚙️ Ρυθμίσεις & Προσαρμογή

Επεξεργαστείτε το `scripts/config.py` για:
- **Grid Resolution:** `GRID_RESOLUTION = 60`
- **Isosurface Levels:** `ISOSURFACE_LEVELS = [0.5, 1.0, 1.5, ...]`
- **Colormap:** `COLORMAP = 'jet'` (επιλογές: 'viridis', 'plasma', 'rainbow')
- **Image Quality:** `IMAGE_RESOLUTION = [1920, 1080]`

## 🔧 Αντιμετώπιση Προβλημάτων

### Κοινά Σφάλματα
ModuleNotFoundError
pip install -r requirements.txt

Άδειο visualization
Μειώστε το GRID_RESOLUTION στο config.py
Πολύ αργή εκτέλεση
Μειώστε τον αριθμό των isosurfaces


### Performance Tips
- **Μεγάλα datasets (>10K points):** Χρησιμοποιήστε `GRID_RESOLUTION = 40`
- **Γρήγορο preview:** Χρησιμοποιήστε `plot3d_scatter.py` πρώτα
- **Animation:** Περιορίστε τα time steps στο `animation_time.py`

## 📈 Validation & Αξιοπιστία

Το σύστημα περιλαμβάνει ενσωματωμένους ελέγχους αξιοπιστίας:

### Cross-Validation Metrics
- **R² > 0.8:** ✅ Υψηλή αξιοπιστία
- **R² 0.6-0.8:** ⚠️ Μέτρια αξιοπιστία  
- **R² < 0.6:** ❌ Χαμηλή αξιοπιστία

### Bootstrap Uncertainty
- Confidence intervals για κάθε prediction
- Εντοπισμός περιοχών με υψηλή αβεβαιότητα

## 🎨 Gallery Αποτελεσμάτων

| Τύπος Visualization | Αρχείο | Περιγραφή |
|-------------------|--------|-----------|
| 3D Isosurfaces | `pyvista_voxler.py` | Κύρια οπτικοποίηση |
| Interactive | `interactive_widgets.py` | Real-time control |
| Time Animation | `animation_time.py` | GIF animation |
| Statistical | `validation.py` | R², MSE analysis |

## 🤝 Συνεισφορές & Support

### Contributing
1. Fork το repository
2. Δημιουργήστε feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open Pull Request

### Issues & Bug Reports
Αναφέρετε προβλήματα στο [GitHub Issues](https://github.com/yourusername/3d-geo-visualization/issues)

## 📚 Τεχνική Τεκμηρίωση

### Χρησιμοποιούμενες Βιβλιοθήκες
- **PyVista:** 3D visualization & mesh processing
- **SciPy:** Interpolation algorithms
- **Plotly:** Interactive web-based plots  
- **Matplotlib:** 2D/3D plotting
- **Pandas:** Data manipulation
- **Scikit-learn:** Cross-validation & metrics

### Interpolation Methods
- **Nearest:** Γρήγορη, κατάλληλη για sparse data
- **Linear:** Ομαλή, καλή για dense data
- **Cubic:** Πολύ ομαλή, απαιτεί πυκνά δεδομένα

## 📄 License

Αυτό το project διατίθεται υπό την [MIT License](LICENSE) - δείτε το αρχείο LICENSE για λεπτομέρειες.

## 🙏 Acknowledgments

- **Golden Software Voxler** για την έμπνευση του UI/UX
- **PyVista Community** για το εξαιρετικό 3D visualization framework
- **VTK Development Team** για τη βάση του PyVista

---

**🚀 Τρέξτε τώρα `python scripts/pyvista_voxler.py` και δείτε το magic να συμβαίνει!**

---
