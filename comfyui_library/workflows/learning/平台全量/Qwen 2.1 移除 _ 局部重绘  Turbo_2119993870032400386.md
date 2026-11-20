---
key: 平台全量/Qwen 2.1 移除 _ 局部重绘  Turbo_2119993870032400386.json
name: Qwen 2.1 移除 _ 局部重绘  Turbo_2119993870032400386
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Qwen 2.1 移除 _ 局部重绘  Turbo_2119993870032400386.json
hash: 7d6bbda57728340f
coverage: 0.897436
learned_at: 2026-11-14 00:49:11
nodes: [CLIPLoader, VAELoader, UNETLoader, VAEDecode, GetNode, Image Comparer (rgthree), LoraLoaderModelOnly, RandomNoise, SamplerCustomAdvanced, SamplerCustomAdvanced, KSamplerSelect, DF_Text_Box, GoohaiDisplayAny, QwenImagePromptOptimizer, 忽略多组孤海, easy ifElse, GoohaiAnyExists, TextEncodeQwenImage21GH, LoadImageGoohai, GH_MaskCropV2, 图像缩放V2_孤海, VAEDecode, BasicGuider, GH_CropRestore, SetNode, TextEncodeQwenImage21GH, GH_MaskCropV2, 图像缩放V2_孤海, BasicGuider, ManualSigmas, Get Image Size, GH_CropRestore, GulfSeaImageMergeMask, LayerUtility: ColorImage, Get Image Size, LoraLoaderModelOnly, 图像缩放范围孤海, 图像缩放范围孤海, SaveImage]
patterns: []
missing: []
---

# 平台全量/Qwen 2.1 移除 _ 局部重绘  Turbo_2119993870032400386.json

> 来源文件 `comfyui_library/workflows/平台全量/Qwen 2.1 移除 _ 局部重绘  Turbo_2119993870032400386.json`

## 结构

**生成流程**：Model → Sampling → Decode → Process → Output → Other

**节点**（39 个）：
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
- `图像缩放范围孤海`
- `图像缩放范围孤海`
- `SaveImage`

## 知识

覆盖率 **90%**（35/39）

**有卡**：`CLIPLoader`、`VAELoader`、`UNETLoader`、`VAEDecode`、`LoraLoaderModelOnly`、`RandomNoise`、`SamplerCustomAdvanced`、`KSamplerSelect`、`DF_Text_Box`、`GoohaiDisplayAny`、`QwenImagePromptOptimizer`、`忽略多组孤海`、`GoohaiAnyExists`、`TextEncodeQwenImage21GH`、`LoadImageGoohai`、`GH_MaskCropV2`、`图像缩放V2_孤海`、`BasicGuider`、`GH_CropRestore`、`ManualSigmas`、`Get Image Size`、`GulfSeaImageMergeMask`、`LayerUtility: ColorImage`、`图像缩放范围孤海`、`SaveImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、UNETLoader、KSamplerSelect、SamplerCustomAdvanced、TextEncodeQwenImage21GH
