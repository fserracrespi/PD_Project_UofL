# 📘 Multilevel Stacking Architecture for Parkinson's Disease Prediction

This repository proposes a **stacked ensemble learning architecture**
designed to address the **heterogeneous**, **high-dimensional**, and
**multimodal** nature of clinical data used in Parkinson's disease (PD)
analysis.\
The framework integrates **five major clinical domains** using a
two-level predictive architecture.

------------------------------------------------------------------------

## 🚀 Overview

To effectively fuse information from diverse clinical sources, we
implement a **two-level stacking ensemble**, composed of:

### **🔹 Level 0 - Domain-Specific Models**

Independent predictive models operate on each clinical block:

-   **Motor clinical data**
-   **Non-motor clinical data**
-   **Sleep-related data**
-   **General medical data**
-   **Adverse events (AE) data**

Each model outputs a **probability** or **risk score**, serving as a
compressed and meaningful representation of its domain.

### **🔹 Level 1 - Meta-Learner**

A meta-model integrates the outputs from Level 0 and produces the final
prediction for:

-   **Classification tasks** (diagnosis, categorization)\
-   **Regression tasks** (severity estimation, progression modeling)

------------------------------------------------------------------------

## 📂 Level 0: Domain-Specific Predictive Models

Let:

-   `X_motor`: Motor clinical features\
-   `X_nonmotor`: Non-motor clinical features\
-   `X_sleep`: Sleep-related features\
-   `X_medical`: General medical features\
-   `X_AE`: Adverse events features

Each domain is processed by its own model:

$$
p_{motor} = f_{motor}(X_{motor})
$$

$$
p_{nonmotor} = f_{nonmotor}(X_{nonmotor})
$$

$$
p_{sleep} = f_{sleep}(X_{sleep})
$$

$$
p_{medical} = f_{medical}(X_{medical})
$$

$$
p_{AE} = f_{AE}(X_{AE})
$$

These models act as **learned feature compressors**, extracting
high-level representations tailored to each domain's statistical
structure.

------------------------------------------------------------------------

## 🧠 Level 1: Meta-Learner Integration

The outputs of the Level 0 models are concatenated into a compact
representation:

$$
z = [
p_{motor},
p_{nonmotor},
p_{sleep},
p_{medical},
p_{AE}
]
$$

A meta-learning model `g(z)` produces the final prediction:

### **For Classification**

$$
\hat{y} = g(z)
$$

### **For Regression**

$$
\hat{y} = g(z)
$$

This level captures **cross-domain interactions**, improving overall
performance and robustness.

------------------------------------------------------------------------

## 🎯 Key Advantages

-   **Dimensionality reduction inside each domain**
-   **Improved generalization via ensemble learning**
-   **Scalable to additional clinical modalities**
-   **Effective multimodal fusion**
-   **Robust to heterogeneity across medical datasets**
