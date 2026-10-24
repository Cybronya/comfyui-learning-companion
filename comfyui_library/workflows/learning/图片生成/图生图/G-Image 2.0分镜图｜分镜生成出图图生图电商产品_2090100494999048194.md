---
key: 图片生成/图生图/G-Image 2.0分镜图｜分镜生成出图图生图电商产品_2090100494999048194.json
name: G-Image 2.0分镜图｜分镜生成出图图生图电商产品_2090100494999048194
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/G-Image 2.0分镜图｜分镜生成出图图生图电商产品_2090100494999048194.json
hash: 043115d7e34139bf
coverage: 0.860465
learned_at: 2026-10-23 11:02:29
nodes: [LoadImage, CR Text, RH_LLMAPI_Pro_Node, easy showAnything, RH_Nano_Banana2_Image2Image, SaveImage, LoadImage, CR Text, CR Text, CR Text, easy showAnything, SaveImage, LoadImage, LoadImage, RH_LLMAPI_Pro_Node, RH_RhartImageG2ImageToImage, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, JjkText, solarL_SaveImagesToZip, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/G-Image 2.0分镜图｜分镜生成出图图生图电商产品_2090100494999048194.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/G-Image 2.0分镜图｜分镜生成出图图生图电商产品_2090100494999048194.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（43 个）：
- `LoadImage`
- `CR Text`
- `RH_LLMAPI_Pro_Node`
- `easy showAnything`
- `RH_Nano_Banana2_Image2Image`
- `SaveImage`
- `LoadImage`
- `CR Text`
- `CR Text`
- `CR Text`
- `easy showAnything`
- `SaveImage`
- `LoadImage`
- `LoadImage`
- `RH_LLMAPI_Pro_Node`
- `RH_RhartImageG2ImageToImage`
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `JjkText`
- `solarL_SaveImagesToZip`
- `CLIPTextEncode` ★核心
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

覆盖率 **86%**（37/43）

**有卡**：`LoadImage`、`CR Text`、`RH_LLMAPI_Pro_Node`、`RH_Nano_Banana2_Image2Image`、`SaveImage`、`RH_RhartImageG2ImageToImage`、`UNETLoader`、`CLIPLoader`、`CLIPTextEncode`、`VAELoader`、`EmptyLatentImage`、`KSampler`、`VAEDecode`、`solarL_SaveImagesToZip`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
