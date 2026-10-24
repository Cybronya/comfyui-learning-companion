---
key: 图片生成/图生图/qwen_image_edit_plus_nextscene_v2_1982130472799084545.json
name: qwen_image_edit_plus_nextscene_v2_1982130472799084545
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/qwen_image_edit_plus_nextscene_v2_1982130472799084545.json
hash: 4e27c11df173bf99
coverage: 0.888889
learned_at: 2026-10-23 11:44:08
nodes: [KSampler, VAEDecode, SaveImage, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoadImage, VAELoader, TextEncodeQwenImageEditPlus, CLIPTextEncode, GetImageSize, EmptyLatentImage, PreviewAny, CLIPLoader, PreviewAny, easy promptLine, StringReplace, AILab_QwenVL]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1920, "sampler_name": "euler", "scheduler": "simple", "seed": 458948334438946, "steps": 8, "width": 1080}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/qwen_image_edit_plus_nextscene_v2_1982130472799084545.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/qwen_image_edit_plus_nextscene_v2_1982130472799084545.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（18 个）：
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `VAELoader`
- `TextEncodeQwenImageEditPlus`
- `CLIPTextEncode` ★核心
- `GetImageSize`
- `EmptyLatentImage` ★核心
- `PreviewAny`
- `CLIPLoader`
- `PreviewAny`
- `easy promptLine`
- `StringReplace`
- `AILab_QwenVL`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `458948334438946`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1080`
- `height` = `1920`
- `batch_size` = `1`

## 知识

覆盖率 **89%**（16/18）

**有卡**：`KSampler`、`VAEDecode`、`SaveImage`、`UNETLoader`、`LoraLoaderModelOnly`、`LoadImage`、`VAELoader`、`TextEncodeQwenImageEditPlus`、`CLIPTextEncode`、`GetImageSize`、`EmptyLatentImage`、`CLIPLoader`、`easy promptLine`、`StringReplace`、`AILab_QwenVL`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
