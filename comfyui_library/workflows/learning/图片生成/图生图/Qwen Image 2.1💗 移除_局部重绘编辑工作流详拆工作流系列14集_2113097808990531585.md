---
key: 图片生成/图生图/Qwen Image 2.1💗 移除_局部重绘编辑工作流详拆工作流系列14集_2113097808990531585.json
name: Qwen Image 2.1💗 移除_局部重绘编辑工作流详拆工作流系列14集_2113097808990531585
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1💗 移除_局部重绘编辑工作流详拆工作流系列14集_2113097808990531585.json
hash: f045bb9d434fe981
coverage: 0.74026
learned_at: 2026-10-26 22:03:06
nodes: [Image Comparer (rgthree), 图像缩放范围孤海, SaveImage, GH_MaskCropV2, UNETLoader, VAELoader, CLIPLoader, easy getNode, GulfSeaImageMergeMask, 图像缩放范围孤海, 图像缩放V2_孤海, easy setNode, RandomNoise, LoraLoaderModelOnly, KSamplerSelect, easy setNode, easy setNode, INTConstant, easy setNode, easy setNode, easy getNode, easy getNode, easy getNode, Get Image Size, easy setNode, Get Image Size, ManualSigmas, easy setNode, GH_MaskCropV2, easy getNode, LayerUtility: ColorImage, TextEncodeQwenImage21GH, easy getNode, easy getNode, BasicGuider, easy getNode, SamplerCustomAdvanced, easy getNode, GH_CropRestore, PreviewImage, VAEDecode, 孤海注释, easy getNode, easy getNode, easy getNode, BasicGuider, 孤海注释, 孤海注释, 孤海注释, 孤海注释, 孤海注释, 孤海注释, 孤海注释, 忽略多组孤海, GoohaiDisplayAny, LoraLoaderModelOnly, QwenImagePromptOptimizer, 图像缩放V2_孤海, SetNode, TextEncodeQwenImage21GH, PreviewImage, SamplerCustomAdvanced, easy getNode, VAEDecode, easy getNode, PreviewImage, LoadImageGoohai, GH_CropRestore, easy ifElse, GetNode, GoohaiAnyExists, DF_Text_Box, Fast Groups Bypasser (rgthree), 孤海注释, 孤海注释, 孤海注释, 孤海注释]
patterns: []
missing: []
---

# 图片生成/图生图/Qwen Image 2.1💗 移除_局部重绘编辑工作流详拆工作流系列14集_2113097808990531585.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1💗 移除_局部重绘编辑工作流详拆工作流系列14集_2113097808990531585.json`

## 结构

**生成流程**：Model → Sampling → Decode → Process → Output → Other

**节点**（77 个）：
- `Image Comparer (rgthree)`
- `图像缩放范围孤海`
- `SaveImage`
- `GH_MaskCropV2`
- `UNETLoader` ★核心
- `VAELoader`
- `CLIPLoader`
- `easy getNode`
- `GulfSeaImageMergeMask`
- `图像缩放范围孤海`
- `图像缩放V2_孤海`
- `easy setNode`
- `RandomNoise`
- `LoraLoaderModelOnly` ★核心
- `KSamplerSelect` ★核心
- `easy setNode`
- `easy setNode`
- `INTConstant`
- `easy setNode`
- `easy setNode`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `Get Image Size`
- `easy setNode`
- `Get Image Size`
- `ManualSigmas`
- `easy setNode`
- `GH_MaskCropV2`
- `easy getNode`
- `LayerUtility: ColorImage`
- `TextEncodeQwenImage21GH`
- `easy getNode`
- `easy getNode`
- `BasicGuider`
- `easy getNode`
- `SamplerCustomAdvanced` ★核心
- `easy getNode`
- `GH_CropRestore`
- `PreviewImage`
- `VAEDecode` ★核心
- `孤海注释`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `BasicGuider`
- `孤海注释`
- `孤海注释`
- `孤海注释`
- `孤海注释`
- `孤海注释`
- `孤海注释`
- `孤海注释`
- `忽略多组孤海`
- `GoohaiDisplayAny`
- `LoraLoaderModelOnly` ★核心
- `QwenImagePromptOptimizer`
- `图像缩放V2_孤海`
- `SetNode`
- `TextEncodeQwenImage21GH`
- `PreviewImage`
- `SamplerCustomAdvanced` ★核心
- `easy getNode`
- `VAEDecode` ★核心
- `easy getNode`
- `PreviewImage`
- `LoadImageGoohai`
- `GH_CropRestore`
- `easy ifElse`
- `GetNode`
- `GoohaiAnyExists`
- `DF_Text_Box`
- `Fast Groups Bypasser (rgthree)`
- `孤海注释`
- `孤海注释`
- `孤海注释`
- `孤海注释`

## 知识

覆盖率 **74%**（57/77）

**有卡**：`图像缩放范围孤海`、`SaveImage`、`GH_MaskCropV2`、`UNETLoader`、`VAELoader`、`CLIPLoader`、`easy getNode`、`GulfSeaImageMergeMask`、`图像缩放V2_孤海`、`easy setNode`、`RandomNoise`、`LoraLoaderModelOnly`、`KSamplerSelect`、`INTConstant`、`Get Image Size`、`ManualSigmas`、`LayerUtility: ColorImage`、`TextEncodeQwenImage21GH`、`BasicGuider`、`SamplerCustomAdvanced`、`GH_CropRestore`、`VAEDecode`、`忽略多组孤海`、`GoohaiDisplayAny`、`QwenImagePromptOptimizer`、`LoadImageGoohai`、`GoohaiAnyExists`、`DF_Text_Box`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、UNETLoader、KSamplerSelect、SamplerCustomAdvanced、TextEncodeQwenImage21GH
