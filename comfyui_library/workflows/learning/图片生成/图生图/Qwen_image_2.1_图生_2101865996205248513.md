---
key: 图片生成/图生图/Qwen_image_2.1_图生_2101865996205248513.json
name: Qwen_image_2.1_图生_2101865996205248513
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen_image_2.1_图生_2101865996205248513.json
hash: b476aa7cdd025d85
coverage: 0.869565
learned_at: 2026-10-21 00:44:02
nodes: [CLIPLoader, UNETLoader, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, EmptyLatentImage, VAELoader, KSampler, VAEDecode, MarkdownNote, Note, QwenImage21Cache, ComfySwitchNode, LoadImage, LoadImage, LoadImage, ResolutionSelector, SaveImage, TextEncodeQwenImage21]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 468151185485131, "steps": 25, "width": 1024}
---

# 图片生成/图生图/Qwen_image_2.1_图生_2101865996205248513.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen_image_2.1_图生_2101865996205248513.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（23 个）：
- `CLIPLoader`
- `UNETLoader` ★核心
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `EmptyLatentImage` ★核心
- `VAELoader`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `MarkdownNote`
- `Note`
- `QwenImage21Cache`
- `ComfySwitchNode`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `ResolutionSelector`
- `SaveImage`
- `TextEncodeQwenImage21`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `468151185485131`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **87%**（20/23）

**有卡**：`CLIPLoader`、`UNETLoader`、`LoadImage`、`EmptyLatentImage`、`VAELoader`、`KSampler`、`VAEDecode`、`QwenImage21Cache`、`ResolutionSelector`、`SaveImage`、`TextEncodeQwenImage21`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
