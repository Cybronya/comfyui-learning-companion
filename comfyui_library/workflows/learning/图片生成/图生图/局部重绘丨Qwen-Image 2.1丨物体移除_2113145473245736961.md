---
key: 图片生成/图生图/局部重绘丨Qwen-Image 2.1丨物体移除_2113145473245736961.json
name: 局部重绘丨Qwen-Image 2.1丨物体移除_2113145473245736961
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/局部重绘丨Qwen-Image 2.1丨物体移除_2113145473245736961.json
hash: 4297d9098c8a0801
coverage: 0.9
learned_at: 2026-10-26 22:05:59
nodes: [CLIPLoader, VAELoader, UNETLoader, VAEDecode, GetNode, Image Comparer (rgthree), LoraLoaderModelOnly, RandomNoise, SamplerCustomAdvanced, SamplerCustomAdvanced, KSamplerSelect, DF_Text_Box, GoohaiDisplayAny, QwenImagePromptOptimizer, 忽略多组孤海, easy ifElse, GoohaiAnyExists, TextEncodeQwenImage21GH, LoadImage, GH_MaskCropV2, 图像缩放V2_孤海, VAEDecode, BasicGuider, GH_CropRestore, SetNode, TextEncodeQwenImage21GH, GH_MaskCropV2, 图像缩放V2_孤海, BasicGuider, ManualSigmas, Get Image Size, GH_CropRestore, GulfSeaImageMergeMask, LayerUtility: ColorImage, Get Image Size, LoraLoaderModelOnly, GoohaiUniversalSlider, 图像缩放范围孤海, 图像缩放范围孤海, SaveImage]
patterns: []
missing: []
---

# 图片生成/图生图/局部重绘丨Qwen-Image 2.1丨物体移除_2113145473245736961.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/局部重绘丨Qwen-Image 2.1丨物体移除_2113145473245736961.json`

## 结构

**生成流程**：Model → Sampling → Decode → Process → Output → Other

**节点**（40 个）：
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `GetNode`
- `Image Comparer (rgthree)`
- `LoraLoaderModelOnly` ★核心
- `RandomNoise`
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
- `LoadImage`
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

覆盖率 **90%**（36/40）

**有卡**：`CLIPLoader`、`VAELoader`、`UNETLoader`、`VAEDecode`、`LoraLoaderModelOnly`、`RandomNoise`、`SamplerCustomAdvanced`、`KSamplerSelect`、`DF_Text_Box`、`GoohaiDisplayAny`、`QwenImagePromptOptimizer`、`忽略多组孤海`、`GoohaiAnyExists`、`TextEncodeQwenImage21GH`、`LoadImage`、`GH_MaskCropV2`、`图像缩放V2_孤海`、`BasicGuider`、`GH_CropRestore`、`ManualSigmas`、`Get Image Size`、`GulfSeaImageMergeMask`、`LayerUtility: ColorImage`、`GoohaiUniversalSlider`、`图像缩放范围孤海`、`SaveImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader、KSamplerSelect、SamplerCustomAdvanced
