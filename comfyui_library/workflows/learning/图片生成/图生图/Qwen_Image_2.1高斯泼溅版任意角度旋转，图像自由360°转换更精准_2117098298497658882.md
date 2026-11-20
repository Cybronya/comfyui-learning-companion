---
key: 图片生成/图生图/Qwen_Image_2.1高斯泼溅版任意角度旋转，图像自由360°转换更精准_2117098298497658882.json
name: Qwen_Image_2.1高斯泼溅版任意角度旋转，图像自由360°转换更精准_2117098298497658882
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen_Image_2.1高斯泼溅版任意角度旋转，图像自由360°转换更精准_2117098298497658882.json
hash: a7dac79ce4e56132
coverage: 0.921569
learned_at: 2026-11-02 19:13:02
nodes: [LoadSharpModel, SharpPredict, LayerUtility: ImageScaleByAspectRatio V2, GetImageSize, ShowText|pysssss, LoadImage, CLIPLoader, UNETLoader, LoadImage, INTConstant, LoadImage, LoraLoaderModelOnly, Image Comparer (rgthree), SaveImage, QwenImage21Cache, VAELoader, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, EmptyLatentImage, KSampler, TextEncodeQwenImage21, YCGaussianPreview, VAEDecode, SaveImage, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, CLIPTextEncode, CLIPTextEncode, CLIPLoader, JjkText, VAEDecode, EmptyLatentImage, VAELoader, solarL_SaveImagesToZip, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen_Image_2.1高斯泼溅版任意角度旋转，图像自由360°转换更精准_2117098298497658882.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen_Image_2.1高斯泼溅版任意角度旋转，图像自由360°转换更精准_2117098298497658882.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（51 个）：
- `LoadSharpModel`
- `SharpPredict`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetImageSize`
- `ShowText|pysssss`
- `LoadImage`
- `CLIPLoader`
- `UNETLoader` ★核心
- `LoadImage`
- `INTConstant`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `Image Comparer (rgthree)`
- `SaveImage`
- `QwenImage21Cache`
- `VAELoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `TextEncodeQwenImage21`
- `YCGaussianPreview`
- `VAEDecode` ★核心
- `SaveImage`
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

- `width` = `80`
- `height` = `80`
- `batch_size` = `1`
- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **92%**（47/51）

**有卡**：`LoadSharpModel`、`SharpPredict`、`LayerUtility: ImageScaleByAspectRatio V2`、`GetImageSize`、`LoadImage`、`CLIPLoader`、`UNETLoader`、`INTConstant`、`LoraLoaderModelOnly`、`SaveImage`、`QwenImage21Cache`、`VAELoader`、`EmptyLatentImage`、`KSampler`、`TextEncodeQwenImage21`、`YCGaussianPreview`、`VAEDecode`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、TextEncodeQwenImage21、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
