---
key: 图片生成/图生图/qwen image 2.1多图编辑_2101719348938362882.json
name: qwen image 2.1多图编辑_2101719348938362882
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/qwen image 2.1多图编辑_2101719348938362882.json
hash: 609160267ffc4398
coverage: 0.761905
learned_at: 2026-10-21 00:46:01
nodes: [CLIPLoader, QwenImage21Cache, Note, 孤海注释, UNETLoader, MarkdownNote, 孤海注释, SaveImage, SaveImageAdvanced, LoadImage, LoadImage, TextEncodeQwenImage21, VAELoader, VAEDecode, KSampler, EmptyLatentImage, ComfySwitchNode, CR Text, ResolutionSelector, LoadImage, LoadImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 703931504972558, "steps": 40, "width": 1024}
---

# 图片生成/图生图/qwen image 2.1多图编辑_2101719348938362882.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/qwen image 2.1多图编辑_2101719348938362882.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（21 个）：
- `CLIPLoader`
- `QwenImage21Cache`
- `Note`
- `孤海注释`
- `UNETLoader` ★核心
- `MarkdownNote`
- `孤海注释`
- `SaveImage`
- `SaveImageAdvanced`
- `LoadImage`
- `LoadImage`
- `TextEncodeQwenImage21`
- `VAELoader`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `EmptyLatentImage` ★核心
- `ComfySwitchNode`
- `CR Text`
- `ResolutionSelector`
- `LoadImage`
- `LoadImage`

## 关键参数

- `seed` = `703931504972558`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **76%**（16/21）

**有卡**：`CLIPLoader`、`QwenImage21Cache`、`UNETLoader`、`SaveImage`、`SaveImageAdvanced`、`LoadImage`、`TextEncodeQwenImage21`、`VAELoader`、`VAEDecode`、`KSampler`、`EmptyLatentImage`、`CR Text`、`ResolutionSelector`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
