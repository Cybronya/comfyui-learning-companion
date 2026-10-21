---
key: 图片生成/图生图/FireRed-Image-Edit_1.1-人物面部+全身三视图-高清直出_2105497558364807170.json
name: FireRed-Image-Edit_1.1-人物面部+全身三视图-高清直出_2105497558364807170
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FireRed-Image-Edit_1.1-人物面部+全身三视图-高清直出_2105497558364807170.json
hash: f32485f8fb319aac
coverage: 0.882353
learned_at: 2026-10-21 00:39:21
nodes: [PrimitiveNode, TextEncodeQwenImageEditPlus, CLIPTextEncode, UNETLoader, LoraLoaderModelOnly, CLIPLoader, VAELoader, KSampler, SaveImage, EmptyLatentImage, VAEDecode, RunningHub Deepcleaner, JjkText, SeedVR2, CustomAddLabel, SaveImage, LoadImage]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1080, "sampler_name": "euler", "scheduler": "simple", "seed": 450020013499120, "steps": 8, "width": 1920}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/FireRed-Image-Edit_1.1-人物面部+全身三视图-高清直出_2105497558364807170.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FireRed-Image-Edit_1.1-人物面部+全身三视图-高清直出_2105497558364807170.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（17 个）：
- `PrimitiveNode`
- `TextEncodeQwenImageEditPlus`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `VAELoader`
- `KSampler` ★核心
- `SaveImage`
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `RunningHub Deepcleaner`
- `JjkText`
- `SeedVR2`
- `CustomAddLabel`
- `SaveImage`
- `LoadImage`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `450020013499120`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1920`
- `height` = `1080`
- `batch_size` = `1`

## 知识

覆盖率 **88%**（15/17）

**有卡**：`TextEncodeQwenImageEditPlus`、`CLIPTextEncode`、`UNETLoader`、`LoraLoaderModelOnly`、`CLIPLoader`、`VAELoader`、`KSampler`、`SaveImage`、`EmptyLatentImage`、`VAEDecode`、`RunningHub Deepcleaner`、`SeedVR2`、`CustomAddLabel`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
