---
key: 图片生成/文生图/qwen image 2.1文生图生_2101747084268498945.json
name: qwen image 2.1文生图生_2101747084268498945
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/qwen image 2.1文生图生_2101747084268498945.json
hash: 37a05e7cf77c959a
coverage: 0.807692
learned_at: 2026-10-20 01:51:53
nodes: [CLIPLoader, Note, 孤海注释, UNETLoader, 孤海注释, VAELoader, LoadImage, QwenImage21Cache, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, KSampler, SaveImage, VAEDecode, LoadImage, LoadImage, TextEncodeQwenImage21, EmptyLatentImage, ResolutionSelector, ComfySwitchNode, MarkdownNote, CR Text]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 311119304913349, "steps": 25, "width": 1024}
---

# 图片生成/文生图/qwen image 2.1文生图生_2101747084268498945.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/qwen image 2.1文生图生_2101747084268498945.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（26 个）：
- `CLIPLoader`
- `Note`
- `孤海注释`
- `UNETLoader` ★核心
- `孤海注释`
- `VAELoader`
- `LoadImage`
- `QwenImage21Cache`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `KSampler` ★核心
- `SaveImage`
- `VAEDecode` ★核心
- `LoadImage`
- `LoadImage`
- `TextEncodeQwenImage21`
- `EmptyLatentImage` ★核心
- `ResolutionSelector`
- `ComfySwitchNode`
- `MarkdownNote`
- `CR Text`

## 关键参数

- `seed` = `311119304913349`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **81%**（21/26）

**有卡**：`CLIPLoader`、`UNETLoader`、`VAELoader`、`LoadImage`、`QwenImage21Cache`、`KSampler`、`SaveImage`、`VAEDecode`、`TextEncodeQwenImage21`、`EmptyLatentImage`、`ResolutionSelector`、`CR Text`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
