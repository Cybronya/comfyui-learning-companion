---
key: 图片生成/图生图/Qwen 2.1移除局部重绘Turbo 遮罩擦除图生图工具_2113354024144695298.json
name: Qwen 2.1移除局部重绘Turbo 遮罩擦除图生图工具_2113354024144695298
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen 2.1移除局部重绘Turbo 遮罩擦除图生图工具_2113354024144695298.json
hash: 10d3ce66b9f69467
coverage: 0.882353
learned_at: 2026-10-26 22:02:53
nodes: [CLIPLoader, VAELoader, UNETLoader, VAEDecode, GetNode, Image Comparer (rgthree), LoraLoaderModelOnly, RandomNoise, SamplerCustomAdvanced, SamplerCustomAdvanced, KSamplerSelect, DF_Text_Box, GoohaiDisplayAny, QwenImagePromptOptimizer, easy ifElse, GoohaiAnyExists, TextEncodeQwenImage21GH, LoadImageGoohai, GH_MaskCropV2, 图像缩放V2_孤海, VAEDecode, BasicGuider, GH_CropRestore, SetNode, TextEncodeQwenImage21GH, GH_MaskCropV2, 图像缩放V2_孤海, BasicGuider, ManualSigmas, Get Image Size, GH_CropRestore, GulfSeaImageMergeMask, LayerUtility: ColorImage, Get Image Size, LoraLoaderModelOnly, GoohaiUniversalSlider, 图像缩放范围孤海, 图像缩放范围孤海, SaveImage, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, CLIPTextEncode, CLIPTextEncode, CLIPLoader, JjkText, VAEDecode, EmptyLatentImage, VAELoader, solarL_SaveImagesToZip, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen 2.1移除局部重绘Turbo 遮罩擦除图生图工具_2113354024144695298.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen 2.1移除局部重绘Turbo 遮罩擦除图生图工具_2113354024144695298.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（68 个）：
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
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
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
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `JjkText`
- `VAEDecode` ★核心
- `EmptyLatentImage` ★核心
- `VAELoader`
- `solarL_SaveImagesToZip`
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

覆盖率 **88%**（60/68）

**有卡**：`CLIPLoader`、`VAELoader`、`UNETLoader`、`VAEDecode`、`LoraLoaderModelOnly`、`RandomNoise`、`SamplerCustomAdvanced`、`KSamplerSelect`、`DF_Text_Box`、`GoohaiDisplayAny`、`QwenImagePromptOptimizer`、`GoohaiAnyExists`、`TextEncodeQwenImage21GH`、`LoadImageGoohai`、`GH_MaskCropV2`、`图像缩放V2_孤海`、`BasicGuider`、`GH_CropRestore`、`ManualSigmas`、`Get Image Size`、`GulfSeaImageMergeMask`、`LayerUtility: ColorImage`、`GoohaiUniversalSlider`、`图像缩放范围孤海`、`SaveImage`、`KSampler`、`CLIPTextEncode`、`EmptyLatentImage`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
