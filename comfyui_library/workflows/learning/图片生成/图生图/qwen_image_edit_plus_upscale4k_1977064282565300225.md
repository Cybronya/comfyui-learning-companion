---
key: 图片生成/图生图/qwen_image_edit_plus_upscale4k_1977064282565300225.json
name: qwen_image_edit_plus_upscale4k_1977064282565300225
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/qwen_image_edit_plus_upscale4k_1977064282565300225.json
hash: f16ffd4092079568
coverage: 0.923077
learned_at: 2026-10-23 11:44:09
nodes: [CLIPTextEncode, VAEDecode, CLIPLoader, VAELoader, Note, TextEncodeQwenImageEditPlus, SaveImage, KSampler, LoadImage, EmptyLatentImage, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1080, "sampler_name": "euler", "scheduler": "simple", "seed": 1045892270851827, "steps": 8, "width": 1920}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/qwen_image_edit_plus_upscale4k_1977064282565300225.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/qwen_image_edit_plus_upscale4k_1977064282565300225.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（13 个）：
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `CLIPLoader`
- `VAELoader`
- `Note`
- `TextEncodeQwenImageEditPlus`
- `SaveImage`
- `KSampler` ★核心
- `LoadImage`
- `EmptyLatentImage` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `1045892270851827`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1920`
- `height` = `1080`
- `batch_size` = `1`

## 知识

覆盖率 **92%**（12/13）

**有卡**：`CLIPTextEncode`、`VAEDecode`、`CLIPLoader`、`VAELoader`、`TextEncodeQwenImageEditPlus`、`SaveImage`、`KSampler`、`LoadImage`、`EmptyLatentImage`、`UNETLoader`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
