---
key: 平台全量/VOSR高清修复两倍放大（image2.5自然修复）_2097612365612273666.json
name: VOSR高清修复两倍放大（image2.5自然修复）_2097612365612273666
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/VOSR高清修复两倍放大（image2.5自然修复）_2097612365612273666.json
hash: e56a0d7683e6be0d
coverage: 0.733333
learned_at: 2026-11-14 01:03:07
nodes: [ImageScaleBy, VOSR2ModelLoader, VOSR2Upscale, UltralyticsDetectorProvider, BboxDetectorCombined_v2, ImageCompositeMasked, MaskToImage, PreviewImage, SaveImage, PreviewImage, Note, Note, ImpactGaussianBlurMask, ImageBlend, LoadImage]
patterns: []
missing: []
---

# 平台全量/VOSR高清修复两倍放大（image2.5自然修复）_2097612365612273666.json

> 来源文件 `comfyui_library/workflows/平台全量/VOSR高清修复两倍放大（image2.5自然修复）_2097612365612273666.json`

## 结构

**生成流程**：Model → Process → Output → Other

**节点**（15 个）：
- `ImageScaleBy`
- `VOSR2ModelLoader`
- `VOSR2Upscale`
- `UltralyticsDetectorProvider`
- `BboxDetectorCombined_v2`
- `ImageCompositeMasked`
- `MaskToImage`
- `PreviewImage`
- `SaveImage`
- `PreviewImage`
- `Note`
- `Note`
- `ImpactGaussianBlurMask`
- `ImageBlend`
- `LoadImage`

## 知识

覆盖率 **73%**（11/15）

**有卡**：`ImageScaleBy`、`VOSR2ModelLoader`、`VOSR2Upscale`、`UltralyticsDetectorProvider`、`BboxDetectorCombined_v2`、`ImageCompositeMasked`、`MaskToImage`、`SaveImage`、`ImpactGaussianBlurMask`、`ImageBlend`、`LoadImage`

**用到的条目**：LoadImage、VOSR2Upscale、SaveImage、BboxDetectorCombined_v2、ImageBlend、ImageCompositeMasked、ImageScaleBy、ImpactGaussianBlurMask
