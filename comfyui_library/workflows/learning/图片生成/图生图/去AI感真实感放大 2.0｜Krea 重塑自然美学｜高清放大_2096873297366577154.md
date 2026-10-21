---
key: 图片生成/图生图/去AI感真实感放大 2.0｜Krea 重塑自然美学｜高清放大_2096873297366577154.json
name: 去AI感真实感放大 2.0｜Krea 重塑自然美学｜高清放大_2096873297366577154
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/去AI感真实感放大 2.0｜Krea 重塑自然美学｜高清放大_2096873297366577154.json
hash: e7ccfebe40824b9e
coverage: 0.831461
learned_at: 2026-10-21 00:50:49
nodes: [Image Comparer (rgthree), VAELoader, LayerColor: Color of Shadow & Highlight, LayerColor: Color of Shadow & Highlight, SaveImage, PrimitiveFloat, CLIPLoader, CLIPTextEncode, PrimitiveFloat, Int, UNETLoader_Any, KSampler, easy imageColorMatch, ImageResize+, LoadImage, SaveImage, PreviewImage, PreviewImage, PreviewImage, SaveImage, PreviewImage, SaveImage, easy boolean, Int, PrimitiveFloat, RHHiddenNodes, easy imageColorMatch, easy ifElse, RHHiddenNodes, Int, Int, PrimitiveFloat, easy cleanGpuUsed, VAEEncode, CLIPTextEncode, VAEDecode, KuwaharaBlur, VAEDecode, easy cleanGpuUsed, LayerColor: RGB, KSamplerAdvanced, ShowText|pysssss, AILab_QwenVL, CR Text, GroupExecutor, LoraLoaderModelOnly, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, solarL_SaveImagesToZip, JjkText, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, Note]
patterns: [text_to_image, image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/去AI感真实感放大 2.0｜Krea 重塑自然美学｜高清放大_2096873297366577154.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/去AI感真实感放大 2.0｜Krea 重塑自然美学｜高清放大_2096873297366577154.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（89 个）：
- `Image Comparer (rgthree)`
- `VAELoader`
- `LayerColor: Color of Shadow & Highlight`
- `LayerColor: Color of Shadow & Highlight`
- `SaveImage`
- `PrimitiveFloat`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `PrimitiveFloat`
- `Int`
- `UNETLoader_Any` ★核心
- `KSampler` ★核心
- `easy imageColorMatch`
- `ImageResize+`
- `LoadImage`
- `SaveImage`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `SaveImage`
- `PreviewImage`
- `SaveImage`
- `easy boolean`
- `Int`
- `PrimitiveFloat`
- `RHHiddenNodes`
- `easy imageColorMatch`
- `easy ifElse`
- `RHHiddenNodes`
- `Int`
- `Int`
- `PrimitiveFloat`
- `easy cleanGpuUsed`
- `VAEEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `KuwaharaBlur`
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `LayerColor: RGB`
- `KSamplerAdvanced` ★核心
- `ShowText|pysssss`
- `AILab_QwenVL`
- `CR Text`
- `GroupExecutor`
- `LoraLoaderModelOnly` ★核心
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `solarL_SaveImagesToZip`
- `JjkText`
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
- `CLIPTextEncode` ★核心
- `Note`

**识别到的模式**：text_to_image、image_to_image

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

覆盖率 **83%**（74/89）

**有卡**：`VAELoader`、`LayerColor: Color of Shadow & Highlight`、`SaveImage`、`CLIPLoader`、`CLIPTextEncode`、`Int`、`UNETLoader_Any`、`KSampler`、`easy imageColorMatch`、`ImageResize+`、`LoadImage`、`easy boolean`、`RHHiddenNodes`、`easy cleanGpuUsed`、`VAEEncode`、`VAEDecode`、`KuwaharaBlur`、`LayerColor: RGB`、`KSamplerAdvanced`、`AILab_QwenVL`、`CR Text`、`GroupExecutor`、`LoraLoaderModelOnly`、`UNETLoader`、`EmptyLatentImage`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
