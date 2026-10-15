---
key: 图片生成/文生图/qwen_image_edit_plus_Miniature_Worlds_1977407979249127426.json
name: qwen_image_edit_plus_Miniature_Worlds_1977407979249127426
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/qwen_image_edit_plus_Miniature_Worlds_1977407979249127426.json
hash: f52f0fa815518007
coverage: 0.923077
learned_at: 2026-10-10 20:59:25
nodes: [VAEDecode, PreviewAny, SaveImage, UNETLoader, LoraLoaderModelOnly, CLIPLoader, VAELoader, CLIPTextEncode, EmptyLatentImage, KSampler, TextEncodeQwenImageEditPlus, AILab_QwenVL, LoraLoaderModelOnly]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1080, "sampler_name": "euler", "scheduler": "simple", "seed": 1092637010212909, "steps": 8, "width": 1920}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/qwen_image_edit_plus_Miniature_Worlds_1977407979249127426.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/qwen_image_edit_plus_Miniature_Worlds_1977407979249127426.json`

## 结构

**节点**（13 个）：
- `VAEDecode`
- `PreviewAny`
- `SaveImage`
- `UNETLoader`
- `LoraLoaderModelOnly`
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `TextEncodeQwenImageEditPlus`
- `AILab_QwenVL`
- `LoraLoaderModelOnly`

**识别到的模式**：text_to_image

## 关键参数

- `batch_size` = `1`
- `cfg` = `1`
- `denoise` = `1`
- `height` = `1080`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `seed` = `1092637010212909`
- `steps` = `8`
- `width` = `1920`

## 知识

覆盖率 **92%**（12/13）

**有卡**：`VAEDecode`、`PreviewAny`、`SaveImage`、`UNETLoader`、`LoraLoaderModelOnly`、`CLIPLoader`、`VAELoader`、`CLIPTextEncode`、`EmptyLatentImage`、`KSampler`、`TextEncodeQwenImageEditPlus`、`AILab_QwenVL`

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
