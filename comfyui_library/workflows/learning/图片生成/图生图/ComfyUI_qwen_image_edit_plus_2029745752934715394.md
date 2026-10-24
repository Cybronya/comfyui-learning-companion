---
key: 图片生成/图生图/ComfyUI_qwen_image_edit_plus_2029745752934715394.json
name: ComfyUI_qwen_image_edit_plus_2029745752934715394
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/ComfyUI_qwen_image_edit_plus_2029745752934715394.json
hash: e46f75d5d503b91d
coverage: 0.928571
learned_at: 2026-10-23 10:51:59
nodes: [CLIPLoader, VAELoader, CLIPTextEncode, VAEDecode, EmptyLatentImage, PreviewImage, AIO_Preprocessor, TextEncodeQwenImageEditPlus, KSampler, UNETLoader, LoadImage, SaveImage, LoadImage, LoadImage]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1.5, "denoise": 1, "height": 1080, "sampler_name": "euler", "scheduler": "simple", "seed": 140648346875750, "steps": 20, "width": 1920}
---

# 图片生成/图生图/ComfyUI_qwen_image_edit_plus_2029745752934715394.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/ComfyUI_qwen_image_edit_plus_2029745752934715394.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（14 个）：
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `EmptyLatentImage` ★核心
- `PreviewImage`
- `AIO_Preprocessor`
- `TextEncodeQwenImageEditPlus`
- `KSampler` ★核心
- `UNETLoader` ★核心
- `LoadImage`
- `SaveImage`
- `LoadImage`
- `LoadImage`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `1920`
- `height` = `1080`
- `batch_size` = `1`
- `seed` = `140648346875750`
- `steps` = `20`
- `cfg` = `1.5`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **93%**（13/14）

**有卡**：`CLIPLoader`、`VAELoader`、`CLIPTextEncode`、`VAEDecode`、`EmptyLatentImage`、`AIO_Preprocessor`、`TextEncodeQwenImageEditPlus`、`KSampler`、`UNETLoader`、`LoadImage`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage、UNETLoader
