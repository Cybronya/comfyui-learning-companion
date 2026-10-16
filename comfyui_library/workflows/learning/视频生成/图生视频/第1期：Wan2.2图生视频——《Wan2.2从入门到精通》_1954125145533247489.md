---
key: 视频生成/图生视频/第1期：Wan2.2图生视频——《Wan2.2从入门到精通》_1954125145533247489.json
name: 第1期：Wan2.2图生视频——《Wan2.2从入门到精通》_1954125145533247489.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1954125145533247489.json
hash: 59220e11c5e33539
coverage: 0.888889
learned_at: 2026-10-15 22:31:06
nodes: [CLIPLoader, KSamplerAdvanced, KSamplerAdvanced, VAEDecode, SaveVideo, CLIPTextEncode, VAELoader, ModelSamplingSD3, ModelSamplingSD3, MarkdownNote, CreateVideo, UNETLoader, UNETLoader, Note, LoadImage, WanImageToVideo, CLIPTextEncode, Label (rgthree)]
patterns: []
missing: []
parameters: {"cfg": 20, "denoise": "simple", "sampler_name": 3.5, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 视频生成/图生视频/第1期：Wan2.2图生视频——《Wan2.2从入门到精通》_1954125145533247489.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1954125145533247489.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（18 个）：
- `CLIPLoader`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `SaveVideo`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `MarkdownNote`
- `CreateVideo`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `Note`
- `LoadImage`
- `WanImageToVideo`
- `CLIPTextEncode` ★核心
- `Label (rgthree)`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `20`
- `sampler_name` = `3.5`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **89%**（16/18）

**有卡**：`CLIPLoader`、`KSamplerAdvanced`、`VAEDecode`、`SaveVideo`、`CLIPTextEncode`、`VAELoader`、`ModelSamplingSD3`、`CreateVideo`、`UNETLoader`、`LoadImage`、`WanImageToVideo`、`Label (rgthree)`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、SaveVideo
