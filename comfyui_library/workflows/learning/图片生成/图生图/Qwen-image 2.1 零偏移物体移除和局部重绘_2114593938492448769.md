---
key: 图片生成/图生图/Qwen-image 2.1 零偏移物体移除和局部重绘_2114593938492448769.json
name: Qwen-image 2.1 零偏移物体移除和局部重绘_2114593938492448769
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-image 2.1 零偏移物体移除和局部重绘_2114593938492448769.json
hash: b5a74f314edf81ed
coverage: 0.938776
learned_at: 2026-10-26 22:03:25
nodes: [VAEDecode, RandomNoise, SamplerCustomAdvanced, KSamplerSelect, DF_Text_Box, TextEncodeQwenImage21GH, GH_MaskCropV2, 图像缩放V2_孤海, BasicGuider, ManualSigmas, Get Image Size, GH_CropRestore, GulfSeaImageMergeMask, LayerUtility: ColorImage, 图像缩放范围孤海, UNETLoader, CLIPLoader, QwenImage21SageAttentionT8, VAELoader, SaveImage, Image Comparer (rgthree), LayerUtility: ColorImage, Get Image Size, GulfSeaImageMergeMask, 图像缩放范围孤海, LoraLoaderModelOnly, TextEncodeQwenImage21GH, GH_MaskCropV2, 图像缩放V2_孤海, UNETLoader, CLIPLoader, QwenImage21SageAttentionT8, RandomNoise, SamplerCustomAdvanced, KSamplerSelect, BasicGuider, ManualSigmas, VAELoader, VAEDecode, GH_CropRestore, LoraLoaderModelOnly, SaveImage, Image Comparer (rgthree), Fast Groups Bypasser (rgthree), WujiCleaner, WujiUpscaler2, LoadImage, WujiUpscaler2, WujiCleaner]
patterns: []
missing: []
---

# 图片生成/图生图/Qwen-image 2.1 零偏移物体移除和局部重绘_2114593938492448769.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-image 2.1 零偏移物体移除和局部重绘_2114593938492448769.json`

## 结构

**生成流程**：Model → Sampling → Decode → Process → Output → Other

**节点**（49 个）：
- `VAEDecode` ★核心
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `KSamplerSelect` ★核心
- `DF_Text_Box`
- `TextEncodeQwenImage21GH`
- `GH_MaskCropV2`
- `图像缩放V2_孤海`
- `BasicGuider`
- `ManualSigmas`
- `Get Image Size`
- `GH_CropRestore`
- `GulfSeaImageMergeMask`
- `LayerUtility: ColorImage`
- `图像缩放范围孤海`
- `UNETLoader` ★核心
- `CLIPLoader`
- `QwenImage21SageAttentionT8`
- `VAELoader`
- `SaveImage`
- `Image Comparer (rgthree)`
- `LayerUtility: ColorImage`
- `Get Image Size`
- `GulfSeaImageMergeMask`
- `图像缩放范围孤海`
- `LoraLoaderModelOnly` ★核心
- `TextEncodeQwenImage21GH`
- `GH_MaskCropV2`
- `图像缩放V2_孤海`
- `UNETLoader` ★核心
- `CLIPLoader`
- `QwenImage21SageAttentionT8`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `KSamplerSelect` ★核心
- `BasicGuider`
- `ManualSigmas`
- `VAELoader`
- `VAEDecode` ★核心
- `GH_CropRestore`
- `LoraLoaderModelOnly` ★核心
- `SaveImage`
- `Image Comparer (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `WujiCleaner`
- `WujiUpscaler2`
- `LoadImage`
- `WujiUpscaler2`
- `WujiCleaner`

## 知识

覆盖率 **94%**（46/49）

**有卡**：`VAEDecode`、`RandomNoise`、`SamplerCustomAdvanced`、`KSamplerSelect`、`DF_Text_Box`、`TextEncodeQwenImage21GH`、`GH_MaskCropV2`、`图像缩放V2_孤海`、`BasicGuider`、`ManualSigmas`、`Get Image Size`、`GH_CropRestore`、`GulfSeaImageMergeMask`、`LayerUtility: ColorImage`、`图像缩放范围孤海`、`UNETLoader`、`CLIPLoader`、`QwenImage21SageAttentionT8`、`VAELoader`、`SaveImage`、`LoraLoaderModelOnly`、`WujiCleaner`、`WujiUpscaler2`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader、KSamplerSelect、SamplerCustomAdvanced
