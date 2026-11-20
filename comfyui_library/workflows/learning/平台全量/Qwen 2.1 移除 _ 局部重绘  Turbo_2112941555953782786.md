---
key: 平台全量/Qwen 2.1 移除 _ 局部重绘  Turbo_2112941555953782786.json
name: Qwen 2.1 移除 _ 局部重绘  Turbo_2112941555953782786
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Qwen 2.1 移除 _ 局部重绘  Turbo_2112941555953782786.json
hash: f51be9f3a8186121
coverage: 0.869565
learned_at: 2026-11-14 00:49:10
nodes: [CLIPLoader, VAELoader, UNETLoader, LayerUtility: ColorImage, Get Image Size, 图像缩放V2_孤海, GH_CropRestore, GoohaiAnyExists, easy ifElse, Mask Invert, Get Image Size, GH_MaskCropV2, 图像缩放V2_孤海, GH_CropRestore, TextEncodeQwenImage21GH, VAEDecode, BasicGuider, VAEDecode, BasicGuider, GetNode, Image Comparer (rgthree), LoraLoaderModelOnly, ManualSigmas, 图像缩放范围孤海, GH_MaskCropV2, RandomNoise, LoraLoaderModelOnly, 孤海注释, SamplerCustomAdvanced, SamplerCustomAdvanced, KSamplerSelect, DF_Text_Box, GoohaiDisplayAny, QwenImagePromptOptimizer, 忽略多组孤海, GoohaiUniversalSlider, easy ifElse, LayerColor: Brightness & Contrast, LayerColor: Brightness & Contrast, GulfSeaImageMergeMask, SetNode, GoohaiAnyExists, TextEncodeQwenImage21GH, SaveImage, 图像缩放范围孤海, LoadImageGoohai]
patterns: []
missing: []
---

# 平台全量/Qwen 2.1 移除 _ 局部重绘  Turbo_2112941555953782786.json

> 来源文件 `comfyui_library/workflows/平台全量/Qwen 2.1 移除 _ 局部重绘  Turbo_2112941555953782786.json`

## 结构

**生成流程**：Model → Sampling → Decode → Process → Output → Other

**节点**（46 个）：
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `LayerUtility: ColorImage`
- `Get Image Size`
- `图像缩放V2_孤海`
- `GH_CropRestore`
- `GoohaiAnyExists`
- `easy ifElse`
- `Mask Invert`
- `Get Image Size`
- `GH_MaskCropV2`
- `图像缩放V2_孤海`
- `GH_CropRestore`
- `TextEncodeQwenImage21GH`
- `VAEDecode` ★核心
- `BasicGuider`
- `VAEDecode` ★核心
- `BasicGuider`
- `GetNode`
- `Image Comparer (rgthree)`
- `LoraLoaderModelOnly` ★核心
- `ManualSigmas`
- `图像缩放范围孤海`
- `GH_MaskCropV2`
- `RandomNoise`
- `LoraLoaderModelOnly` ★核心
- `孤海注释`
- `SamplerCustomAdvanced` ★核心
- `SamplerCustomAdvanced` ★核心
- `KSamplerSelect` ★核心
- `DF_Text_Box`
- `GoohaiDisplayAny`
- `QwenImagePromptOptimizer`
- `忽略多组孤海`
- `GoohaiUniversalSlider`
- `easy ifElse`
- `LayerColor: Brightness & Contrast`
- `LayerColor: Brightness & Contrast`
- `GulfSeaImageMergeMask`
- `SetNode`
- `GoohaiAnyExists`
- `TextEncodeQwenImage21GH`
- `SaveImage`
- `图像缩放范围孤海`
- `LoadImageGoohai`

## 知识

覆盖率 **87%**（40/46）

**有卡**：`CLIPLoader`、`VAELoader`、`UNETLoader`、`LayerUtility: ColorImage`、`Get Image Size`、`图像缩放V2_孤海`、`GH_CropRestore`、`GoohaiAnyExists`、`Mask Invert`、`GH_MaskCropV2`、`TextEncodeQwenImage21GH`、`VAEDecode`、`BasicGuider`、`LoraLoaderModelOnly`、`ManualSigmas`、`图像缩放范围孤海`、`RandomNoise`、`SamplerCustomAdvanced`、`KSamplerSelect`、`DF_Text_Box`、`GoohaiDisplayAny`、`QwenImagePromptOptimizer`、`忽略多组孤海`、`GoohaiUniversalSlider`、`LayerColor: Brightness & Contrast`、`GulfSeaImageMergeMask`、`SaveImage`、`LoadImageGoohai`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、UNETLoader、KSamplerSelect、SamplerCustomAdvanced、TextEncodeQwenImage21GH
