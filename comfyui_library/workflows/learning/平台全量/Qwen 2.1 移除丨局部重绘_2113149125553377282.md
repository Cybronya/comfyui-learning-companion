---
key: 平台全量/Qwen 2.1 移除丨局部重绘_2113149125553377282.json
name: Qwen 2.1 移除丨局部重绘_2113149125553377282
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Qwen 2.1 移除丨局部重绘_2113149125553377282.json
hash: 166263c38943b89e
coverage: 0.837209
learned_at: 2026-11-14 00:49:12
nodes: [VAEDecode, GH_CropRestore, SamplerCustomAdvanced, SamplerCustomAdvanced, TextEncodeQwenImage21GH, SetNode, Get Image Size, LoraLoaderModelOnly, BasicGuider, GetNode, ManualSigmas, KSamplerSelect, VAELoader, CLIPLoader, GH_MaskCropV2, 图像缩放V2_孤海, VAEDecode, Get Image Size, RandomNoise, UNETLoader, easy ifElse, Image Comparer (rgthree), INTConstant, LoadImage, LoraLoaderModelOnly, BasicGuider, DF_Text_Box, 忽略多组孤海, 图像缩放范围孤海, TextEncodeQwenImage21GH, PreviewImage, GulfSeaImageMergeMask, GH_MaskCropV2, LayerUtility: ColorImage, SaveImage, 图像缩放V2_孤海, GH_CropRestore, 图像缩放范围孤海, GoohaiAnyExists, QwenImagePromptOptimizer, ImpactSwitch, GoohaiDisplayAny, ShowText|pysssss]
patterns: []
missing: []
---

# 平台全量/Qwen 2.1 移除丨局部重绘_2113149125553377282.json

> 来源文件 `comfyui_library/workflows/平台全量/Qwen 2.1 移除丨局部重绘_2113149125553377282.json`

## 结构

**生成流程**：Model → Sampling → Decode → Process → Output → Other

**节点**（43 个）：
- `VAEDecode` ★核心
- `GH_CropRestore`
- `SamplerCustomAdvanced` ★核心
- `SamplerCustomAdvanced` ★核心
- `TextEncodeQwenImage21GH`
- `SetNode`
- `Get Image Size`
- `LoraLoaderModelOnly` ★核心
- `BasicGuider`
- `GetNode`
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `VAELoader`
- `CLIPLoader`
- `GH_MaskCropV2`
- `图像缩放V2_孤海`
- `VAEDecode` ★核心
- `Get Image Size`
- `RandomNoise`
- `UNETLoader` ★核心
- `easy ifElse`
- `Image Comparer (rgthree)`
- `INTConstant`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `BasicGuider`
- `DF_Text_Box`
- `忽略多组孤海`
- `图像缩放范围孤海`
- `TextEncodeQwenImage21GH`
- `PreviewImage`
- `GulfSeaImageMergeMask`
- `GH_MaskCropV2`
- `LayerUtility: ColorImage`
- `SaveImage`
- `图像缩放V2_孤海`
- `GH_CropRestore`
- `图像缩放范围孤海`
- `GoohaiAnyExists`
- `QwenImagePromptOptimizer`
- `ImpactSwitch`
- `GoohaiDisplayAny`
- `ShowText|pysssss`

## 知识

覆盖率 **84%**（36/43）

**有卡**：`VAEDecode`、`GH_CropRestore`、`SamplerCustomAdvanced`、`TextEncodeQwenImage21GH`、`Get Image Size`、`LoraLoaderModelOnly`、`BasicGuider`、`ManualSigmas`、`KSamplerSelect`、`VAELoader`、`CLIPLoader`、`GH_MaskCropV2`、`图像缩放V2_孤海`、`RandomNoise`、`UNETLoader`、`INTConstant`、`LoadImage`、`DF_Text_Box`、`忽略多组孤海`、`图像缩放范围孤海`、`GulfSeaImageMergeMask`、`LayerUtility: ColorImage`、`SaveImage`、`GoohaiAnyExists`、`QwenImagePromptOptimizer`、`GoohaiDisplayAny`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader、KSamplerSelect、SamplerCustomAdvanced
