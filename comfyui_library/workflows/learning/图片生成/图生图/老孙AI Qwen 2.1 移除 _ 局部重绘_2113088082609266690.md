---
key: 图片生成/图生图/老孙AI Qwen 2.1 移除 _ 局部重绘_2113088082609266690.json
name: 老孙AI Qwen 2.1 移除 _ 局部重绘_2113088082609266690
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/老孙AI Qwen 2.1 移除 _ 局部重绘_2113088082609266690.json
hash: 13cbf35b9cf06769
coverage: 0.878049
learned_at: 2026-10-26 22:06:49
nodes: [CLIPLoader, VAELoader, UNETLoader, VAEDecode, GetNode, Image Comparer (rgthree), LoraLoaderModelOnly, RandomNoise, 孤海注释, SamplerCustomAdvanced, SamplerCustomAdvanced, KSamplerSelect, DF_Text_Box, GoohaiDisplayAny, QwenImagePromptOptimizer, 忽略多组孤海, easy ifElse, GoohaiAnyExists, TextEncodeQwenImage21GH, LoadImageGoohai, GH_MaskCropV2, 图像缩放V2_孤海, VAEDecode, BasicGuider, GH_CropRestore, SetNode, TextEncodeQwenImage21GH, GH_MaskCropV2, 图像缩放V2_孤海, BasicGuider, ManualSigmas, Get Image Size, GH_CropRestore, GulfSeaImageMergeMask, LayerUtility: ColorImage, Get Image Size, LoraLoaderModelOnly, GoohaiUniversalSlider, 图像缩放范围孤海, 图像缩放范围孤海, SaveImage]
patterns: []
missing: []
---

# 图片生成/图生图/老孙AI Qwen 2.1 移除 _ 局部重绘_2113088082609266690.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/老孙AI Qwen 2.1 移除 _ 局部重绘_2113088082609266690.json`

## 结构

**生成流程**：Model → Sampling → Decode → Process → Output → Other

**节点**（41 个）：
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `GetNode`
- `Image Comparer (rgthree)`
- `LoraLoaderModelOnly` ★核心
- `RandomNoise`
- `孤海注释`
- `SamplerCustomAdvanced` ★核心
- `SamplerCustomAdvanced` ★核心
- `KSamplerSelect` ★核心
- `DF_Text_Box`
- `GoohaiDisplayAny`
- `QwenImagePromptOptimizer`
- `忽略多组孤海`
- `easy ifElse`
- `GoohaiAnyExists`
- `TextEncodeQwenImage21GH`
- `LoadImageGoohai`
- `GH_MaskCropV2`
- `图像缩放V2_孤海`
- `VAEDecode` ★核心
- `BasicGuider`
- `GH_CropRestore`
- `SetNode`
- `TextEncodeQwenImage21GH`
- `GH_MaskCropV2`
- `图像缩放V2_孤海`
- `BasicGuider`
- `ManualSigmas`
- `Get Image Size`
- `GH_CropRestore`
- `GulfSeaImageMergeMask`
- `LayerUtility: ColorImage`
- `Get Image Size`
- `LoraLoaderModelOnly` ★核心
- `GoohaiUniversalSlider`
- `图像缩放范围孤海`
- `图像缩放范围孤海`
- `SaveImage`

## 知识

覆盖率 **88%**（36/41）

**有卡**：`CLIPLoader`、`VAELoader`、`UNETLoader`、`VAEDecode`、`LoraLoaderModelOnly`、`RandomNoise`、`SamplerCustomAdvanced`、`KSamplerSelect`、`DF_Text_Box`、`GoohaiDisplayAny`、`QwenImagePromptOptimizer`、`忽略多组孤海`、`GoohaiAnyExists`、`TextEncodeQwenImage21GH`、`LoadImageGoohai`、`GH_MaskCropV2`、`图像缩放V2_孤海`、`BasicGuider`、`GH_CropRestore`、`ManualSigmas`、`Get Image Size`、`GulfSeaImageMergeMask`、`LayerUtility: ColorImage`、`GoohaiUniversalSlider`、`图像缩放范围孤海`、`SaveImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、UNETLoader、KSamplerSelect、SamplerCustomAdvanced、TextEncodeQwenImage21GH
