---
key: 图片生成/图生图/Qwen Image2.1移除局部重绘编辑详解，系列教程第14集工作流_2115013983219576834.json
name: Qwen Image2.1移除局部重绘编辑详解，系列教程第14集工作流_2115013983219576834
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image2.1移除局部重绘编辑详解，系列教程第14集工作流_2115013983219576834.json
hash: 11d3b25f1da49795
coverage: 0.870968
learned_at: 2026-10-30 17:50:52
nodes: [Image Comparer (rgthree), 图像缩放范围孤海, SaveImage, GH_MaskCropV2, UNETLoader, VAELoader, CLIPLoader, easy getNode, GulfSeaImageMergeMask, 图像缩放范围孤海, 图像缩放V2_孤海, easy setNode, RandomNoise, LoraLoaderModelOnly, KSamplerSelect, easy setNode, easy setNode, INTConstant, easy setNode, easy setNode, easy getNode, easy getNode, easy getNode, Get Image Size, easy setNode, Get Image Size, ManualSigmas, easy setNode, GH_MaskCropV2, easy getNode, LayerUtility: ColorImage, TextEncodeQwenImage21GH, easy getNode, easy getNode, BasicGuider, easy getNode, SamplerCustomAdvanced, easy getNode, GH_CropRestore, PreviewImage, VAEDecode, easy getNode, easy getNode, easy getNode, BasicGuider, GoohaiDisplayAny, LoraLoaderModelOnly, QwenImagePromptOptimizer, 图像缩放V2_孤海, SetNode, TextEncodeQwenImage21GH, PreviewImage, SamplerCustomAdvanced, easy getNode, VAEDecode, easy getNode, PreviewImage, LoadImageGoohai, GH_CropRestore, easy ifElse, GetNode, GoohaiAnyExists, DF_Text_Box, Fast Groups Bypasser (rgthree), 孤海注释, 孤海注释, VAELoader, VAEDecode, solarL_SaveImagesToZip, CLIPTextEncode, CLIPTextEncode, JjkText, KSampler, EmptyLatentImage, CLIPLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen Image2.1移除局部重绘编辑详解，系列教程第14集工作流_2115013983219576834.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image2.1移除局部重绘编辑详解，系列教程第14集工作流_2115013983219576834.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（93 个）：
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
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `BasicGuider`
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
- `VAELoader`
- `VAEDecode` ★核心
- `solarL_SaveImagesToZip`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `JjkText`
- `KSampler` ★核心
- `EmptyLatentImage` ★核心
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `Note`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`
- `width` = `80`
- `height` = `80`
- `batch_size` = `1`

## 知识

覆盖率 **87%**（81/93）

**有卡**：`图像缩放范围孤海`、`SaveImage`、`GH_MaskCropV2`、`UNETLoader`、`VAELoader`、`CLIPLoader`、`easy getNode`、`GulfSeaImageMergeMask`、`图像缩放V2_孤海`、`easy setNode`、`RandomNoise`、`LoraLoaderModelOnly`、`KSamplerSelect`、`INTConstant`、`Get Image Size`、`ManualSigmas`、`LayerUtility: ColorImage`、`TextEncodeQwenImage21GH`、`BasicGuider`、`SamplerCustomAdvanced`、`GH_CropRestore`、`VAEDecode`、`GoohaiDisplayAny`、`QwenImagePromptOptimizer`、`LoadImageGoohai`、`GoohaiAnyExists`、`DF_Text_Box`、`solarL_SaveImagesToZip`、`CLIPTextEncode`、`KSampler`、`EmptyLatentImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
