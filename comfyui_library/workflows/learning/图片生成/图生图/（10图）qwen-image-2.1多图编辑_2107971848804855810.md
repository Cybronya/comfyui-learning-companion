---
key: 图片生成/图生图/（10图）qwen-image-2.1多图编辑_2107971848804855810.json
name: （10图）qwen-image-2.1多图编辑_2107971848804855810
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/（10图）qwen-image-2.1多图编辑_2107971848804855810.json
hash: 0978a7d167995db9
coverage: 0.909091
learned_at: 2026-10-21 00:57:10
nodes: [MarkdownNote, MarkdownNote, KSampler, QwenImage21Cache, UNETLoader, VAEDecode, CLIPLoader, CR Text, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, TextEncodeQwenImage21, VAELoader, CR Text, SaveImage, LoadImage, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 156970172599593, "steps": 25}
---

# 图片生成/图生图/（10图）qwen-image-2.1多图编辑_2107971848804855810.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/（10图）qwen-image-2.1多图编辑_2107971848804855810.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（22 个）：
- `MarkdownNote`
- `MarkdownNote`
- `KSampler` ★核心
- `QwenImage21Cache`
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `CLIPLoader`
- `CR Text`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `TextEncodeQwenImage21`
- `VAELoader`
- `CR Text`
- `SaveImage`
- `LoadImage`
- `LoadImage`

## 关键参数

- `seed` = `156970172599593`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **91%**（20/22）

**有卡**：`KSampler`、`QwenImage21Cache`、`UNETLoader`、`VAEDecode`、`CLIPLoader`、`CR Text`、`LoadImage`、`TextEncodeQwenImage21`、`VAELoader`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、LoadImage、QwenImage21Cache、UNETLoader
