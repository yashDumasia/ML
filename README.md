# Machine Learning Practice Repository 🤖

A comprehensive collection of Machine Learning fundamentals, data preprocessing techniques, and practical projects built with Python and scikit-learn.

## 📌 Quick Navigation

### 🎯 Complete Projects
- **[Placement.ipynb](./Placement.ipynb)** - Placement prediction using classification | _Binary Classification Project_
- **[MixData.ipynb](./MixData.ipynb)** - Mixed data handling and analysis

### 📊 ML Pipelines & Workflows
- **[With_using_Pipeline.ipynb](./With_using_Pipeline.ipynb)** - Complete ML pipeline with preprocessing → model → evaluation ⭐
- **[WithOut_using_Pipeline.ipynb](./WithOut_using_Pipeline.ipynb)** - Step-by-step manual approach

---

## 📚 Learning Modules

### 1️⃣ Data Understanding & Exploration
- [Data_Understanding.ipynb](./Data_Understanding.ipynb) - EDA fundamentals, statistical analysis
- [Panpas_Profiling.ipynb](./Panpas_Profiling.ipynb) - Automated profiling report generation

### 2️⃣ Data Preprocessing & Cleaning
| Topic | Notebook |
|-------|----------|
| Missing Values | [Missing_Value/](./Missing_Value/) |
| Outlier Detection | [Outliers/](./Outliers/) |
| Categorical Encoding | [Encoding.ipynb](./Encoding.ipynb) |
| Feature Scaling | [Standardization.ipynb](./Standardization.ipynb), [Normalization.ipynb](./Normalization.ipynb) |
| Date & Time Features | [Date_and_Time.ipynb](./Date_and_Time.ipynb) |

### 3️⃣ Feature Engineering
- [Feature_Construction.ipynb](./Feature_Construction.ipynb) - Creating new features
- [Feature_Spliting.ipynb](./Feature_Spliting.ipynb) - Train-test splitting strategies
- [Column_Transformer.ipynb](./Column_Transformer.ipynb) - Advanced feature transformation with ColumnTransformer

### 4️⃣ Core ML Algorithms
| Algorithm | Folder |
|-----------|--------|
| Linear Regression | [Linear_Regression/](./Linear_Regression/) |
| Logistic Regression | [Logistic_Regression/](./Logistic_Regression/) |
| Lasso Regression | [Lasso_Regression/](./Lasso_Regression/) |
| Gradient Descent | [Gradient_Descent/](./Gradient_Descent/) |

### 5️⃣ Advanced Topics
- [Regularization/](./Regularization/) - Ridge, Lasso, Elastic Net
- [Transformers.ipynb](./Transformers.ipynb) - Feature transformation techniques

---

## 🛠️ Tech Stack

- **Python 3.x**
- **Jupyter Notebooks** - Interactive learning & documentation
- **pandas** - Data manipulation
- **NumPy** - Numerical computing
- **scikit-learn** - ML algorithms & preprocessing
- **matplotlib/seaborn** - Data visualization
- **pandas-profiling** - Automated EDA

---

## 📖 Learning Path (Recommended Order)

1. Start with **Data_Understanding.ipynb** - Learn data exploration
2. **Encoding.ipynb** & **Standardization.ipynb** - Master preprocessing
3. **Linear_Regression/** - Understand regression fundamentals
4. **Logistic_Regression/** - Learn classification
5. **With_using_Pipeline.ipynb** - See complete workflow
6. **Placement.ipynb** - Real-world project application

---

## 📊 Project Structure

```
ML/
├── README.md                          # This file
├── Placement.ipynb                    # ⭐ Main project
├── With_using_Pipeline.ipynb          # Complete ML workflow
├── Data_Understanding.ipynb           # EDA tutorial
├── Encoding.ipynb                     # Categorical encoding
├── Standardization.ipynb              # Feature scaling - Standard
├── Normalization.ipynb                # Feature scaling - Min-Max
├── Date_and_Time.ipynb                # Temporal feature engineering
├── Feature_Construction.ipynb         # Feature creation
├── Column_Transformer.ipynb           # Advanced transformation
├── Transformers.ipynb                 # Transformer techniques
├── Panpas_Profiling.ipynb             # Automated data profiling
├── MixData.ipynb                      # Mixed data handling
│
├── Linear_Regression/                 # Regression algorithms
├── Logistic_Regression/               # Classification
├── Lasso_Regression/                  # Regularization
├── Gradient_Descent/                  # Optimization algorithm
├── Regularization/                    # Advanced regularization
├── Missing_Value/                     # Handling missing data
├── Outliers/                          # Outlier detection
│
├── placement_data.csv                 # Dataset for Placement.ipynb
├── Steps.csv                          # Reference data
├── model.pkl                          # Serialized model
└── BoxPlat_Data.png                   # Visualization output
```

---

## 🚀 Getting Started

### Clone & Setup
```bash
git clone https://github.com/yashDumasia/ML.git
cd ML

# Install dependencies
pip install pandas numpy scikit-learn matplotlib seaborn pandas-profiling jupyter

# Launch Jupyter
jupyter notebook
```

### Run a Notebook
1. Open any `.ipynb` file above
2. Run cells sequentially (Shift + Enter)
3. Modify data/parameters and experiment!

---

## 🎓 Key Concepts Covered

✅ Exploratory Data Analysis (EDA)  
✅ Missing Value Imputation  
✅ Outlier Detection & Removal  
✅ Categorical Encoding (One-Hot, Label, Target)  
✅ Feature Scaling (Standardization, Normalization)  
✅ Temporal Feature Engineering  
✅ Train-Test Split & Cross-Validation  
✅ Linear Regression  
✅ Logistic Regression  
✅ Regularization (Ridge, Lasso, Elastic Net)  
✅ Gradient Descent Optimization  
✅ scikit-learn Pipelines  
✅ Model Evaluation Metrics  

---

## 📈 Next Steps

- [ ] Add more real-world classification projects
- [ ] Implement ensemble methods (Random Forest, Gradient Boosting)
- [ ] Explore deep learning (TensorFlow/PyTorch)
- [ ] Deploy models as API endpoints
- [ ] Add unit tests for preprocessing functions

---

## 📝 Notes

- All notebooks are interactive - run them yourself to learn!
- Datasets included in repository (mostly CSV format)
- Each notebook includes explanations and code comments
- Topics are organized from basics → advanced

---

## 📧 Questions or Suggestions?

Feel free to open an issue or fork this repository to contribute!

---

**Happy Learning! 🚀**
