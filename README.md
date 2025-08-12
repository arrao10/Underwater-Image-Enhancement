# 🌊 Underwater-Image-Enhancement

<p>
  🔗 🌐 Open Published Paper:
  <a href="https://doi.one/10.1729/Journal.36503" target="_blank" rel="noopener">
    Revealing the Mysteries of the Deep – Underwater Image Enhancement
  </a>
</p>

### 📖 **Introduction**: 
Images captured underwater are frequently degraded by environmental conditions and limitations of camera gear. Common issues include reduced visibility, low brightness, low contrast, noise and strong color shifts. While many techniques have been explored over the past few decades, challenges remain in achieving consistent, natural enhancement across diverse underwater scenes. Building on what works and where prior methods fall short, this project proposes a practical enhancement pipeline focused on effective pre-processing: improving contrast and brightness, denoising and recovering texture detail. The approach addresses overand under brightness problems, restores fine structures and produces more balanced colors resulting in a robust improvement to underwater image clarity and overall visual quality.

### 📸 **Impact**:
Clearer, brighter, more natural underwater photos revealing hidden details for research, inspection and storytelling.

### 📂 **Dataset Details**: 
- **Purpose**: Train on general (**non-underwater**) images and evaluate on underwater scenes for enhancement.
- **Total Images**: **1696** photos. <br>
- **Format**: All images are in **.jpg** format to maintain uniformity.
- **Resolution**: All images are uniformly resized to **256 × 256 pixels**.
- **Test Composition**: The test set contains **only underwater images** to assess clarity, color balance and detail recovery; After inference, results are organized into three folders - Testing Dataset with Good Results, Challengingly Poor Results and Average Results based on visual quality.

### 📊 **Results**:
- The Evaluation/Image Quality Metrics used used here are **PSNR (Peak Signal-to-Noise Ratio)** and S**SIM (Structural Similarity Index)**. Our model achieves an average **PSNR of 23.71dB** and **SSIM of 0.8816**.
<br>
<h4 align="center">The Output images below shows: (a) → Original Underwater Image; (b) → Enhanced Underwater Image</h4>
<p align="center">
  <img width="70%" alt="Result" src="https://github.com/user-attachments/assets/b20f188d-47bd-480e-9f3f-d8a2351dcdfd" />
</p>
