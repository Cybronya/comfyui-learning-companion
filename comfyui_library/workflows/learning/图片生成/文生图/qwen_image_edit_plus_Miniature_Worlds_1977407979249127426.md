---
key: 图片生成/文生图/qwen_image_edit_plus_Miniature_Worlds_1977407979249127426.json
name: qwen_image_edit_plus_Miniature_Worlds_1977407979249127426.json
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/qwen_image_edit_plus_Miniature_Worlds_1977407979249127426.json
hash: f52f0fa815518007
coverage: 0.923077
learned_at: 2026-10-09 19:50:54
nodes: [VAEDecode, PreviewAny, SaveImage, UNETLoader, LoraLoaderModelOnly, CLIPLoader, VAELoader, CLIPTextEncode, EmptyLatentImage, KSampler, TextEncodeQwenImageEditPlus, AILab_QwenVL, LoraLoaderModelOnly]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1080, "sampler_name": "euler", "scheduler": "simple", "seed": 1092637010212909, "steps": 8, "width": 1920}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/qwen_image_edit_plus_Miniature_Worlds_1977407979249127426.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/1977407979249127426.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（13 个）：
- `VAEDecode` ★核心
- `PreviewAny`
- `SaveImage`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `TextEncodeQwenImageEditPlus`
- `AILab_QwenVL`
- `LoraLoaderModelOnly` ★核心

**识别到的模式**：text_to_image

## 关键参数

- `width` = `1920`
- `height` = `1080`
- `batch_size` = `1`
- `seed` = `1092637010212909`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **92%**（12/13）

**有卡**：`VAEDecode`、`SaveImage`、`UNETLoader`、`LoraLoaderModelOnly`、`CLIPLoader`、`VAELoader`、`CLIPTextEncode`、`EmptyLatentImage`、`KSampler`、`TextEncodeQwenImageEditPlus`、`AILab_QwenVL`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
