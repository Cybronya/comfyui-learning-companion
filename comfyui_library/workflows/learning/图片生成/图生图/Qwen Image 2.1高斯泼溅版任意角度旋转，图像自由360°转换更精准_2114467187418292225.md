---
key: 图片生成/图生图/Qwen Image 2.1高斯泼溅版任意角度旋转，图像自由360°转换更精准_2114467187418292225.json
name: Qwen Image 2.1高斯泼溅版任意角度旋转，图像自由360°转换更精准_2114467187418292225
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1高斯泼溅版任意角度旋转，图像自由360°转换更精准_2114467187418292225.json
hash: c02d4a6ebf2a6fc2
coverage: 0.886792
learned_at: 2026-10-26 22:03:06
nodes: [LoadSharpModel, SharpPredict, LayerUtility: ImageScaleByAspectRatio V2, GetImageSize, ShowText|pysssss, LoadImage, CLIPLoader, UNETLoader, LoadImage, INTConstant, LoadImage, LoraLoaderModelOnly, Image Comparer (rgthree), SaveImage, QwenImage21Cache, VAELoader, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, EmptyLatentImage, KSampler, TextEncodeQwenImage21, YCGaussianPreview, VAEDecode, SaveImage, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, CLIPTextEncode, CLIPTextEncode, CLIPLoader, JjkText, VAEDecode, EmptyLatentImage, VAELoader, solarL_SaveImagesToZip, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen Image 2.1高斯泼溅版任意角度旋转，图像自由360°转换更精准_2114467187418292225.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1高斯泼溅版任意角度旋转，图像自由360°转换更精准_2114467187418292225.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（53 个）：
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

覆盖率 **89%**（47/53）

**有卡**：`LoadSharpModel`、`SharpPredict`、`LayerUtility: ImageScaleByAspectRatio V2`、`GetImageSize`、`LoadImage`、`CLIPLoader`、`UNETLoader`、`INTConstant`、`LoraLoaderModelOnly`、`SaveImage`、`QwenImage21Cache`、`VAELoader`、`EmptyLatentImage`、`KSampler`、`TextEncodeQwenImage21`、`YCGaussianPreview`、`VAEDecode`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
