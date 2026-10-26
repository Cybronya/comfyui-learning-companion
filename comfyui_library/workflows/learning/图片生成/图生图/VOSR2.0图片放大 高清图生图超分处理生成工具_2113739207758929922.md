---
key: 图片生成/图生图/VOSR2.0图片放大 高清图生图超分处理生成工具_2113739207758929922.json
name: VOSR2.0图片放大 高清图生图超分处理生成工具_2113739207758929922
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/VOSR2.0图片放大 高清图生图超分处理生成工具_2113739207758929922.json
hash: 6d2f41a17629e32d
coverage: 0.846154
learned_at: 2026-10-26 22:03:52
nodes: [easy imageSizeByLongerSide, int _O, VOSR2ModelLoader, MathExpression|pysssss, LayerUtility: ImageScaleByAspectRatio V2, VOSR2Upscale, LoadImage, SaveImage, Reroute, Image Comparer (rgthree), 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, CLIPTextEncode, CLIPTextEncode, CLIPLoader, JjkText, VAEDecode, EmptyLatentImage, VAELoader, solarL_SaveImagesToZip, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/VOSR2.0图片放大 高清图生图超分处理生成工具_2113739207758929922.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/VOSR2.0图片放大 高清图生图超分处理生成工具_2113739207758929922.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（39 个）：
- `easy imageSizeByLongerSide`
- `int _O`
- `VOSR2ModelLoader`
- `MathExpression|pysssss`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VOSR2Upscale`
- `LoadImage`
- `SaveImage`
- `Reroute`
- `Image Comparer (rgthree)`
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

覆盖率 **85%**（33/39）

**有卡**：`easy imageSizeByLongerSide`、`int _O`、`VOSR2ModelLoader`、`MathExpression|pysssss`、`LayerUtility: ImageScaleByAspectRatio V2`、`VOSR2Upscale`、`LoadImage`、`SaveImage`、`UNETLoader`、`LoraLoaderModelOnly`、`KSampler`、`CLIPTextEncode`、`CLIPLoader`、`VAEDecode`、`EmptyLatentImage`、`VAELoader`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
