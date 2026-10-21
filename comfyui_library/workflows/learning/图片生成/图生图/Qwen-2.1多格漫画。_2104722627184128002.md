---
key: 图片生成/图生图/Qwen-2.1多格漫画。_2104722627184128002.json
name: Qwen-2.1多格漫画。_2104722627184128002
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-2.1多格漫画。_2104722627184128002.json
hash: 77591c3899539380
coverage: 0.736842
learned_at: 2026-10-21 00:43:06
nodes: [MarkdownNote, MarkdownNote, MarkdownNote, Label (rgthree), VAELoader, TextEncodeQwenImage21, QwenImage21Cache, EmptyLatentImage, MultiTextConcatenate, VAEDecode, JjkText, UNETLoader, CLIPLoader, ResolutionSelector, LoadImage, LoadImage, KSampler, JjkText, SaveImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 867582715661677, "steps": 40, "width": 1024}
---

# 图片生成/图生图/Qwen-2.1多格漫画。_2104722627184128002.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-2.1多格漫画。_2104722627184128002.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（19 个）：
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `Label (rgthree)`
- `VAELoader`
- `TextEncodeQwenImage21`
- `QwenImage21Cache`
- `EmptyLatentImage` ★核心
- `MultiTextConcatenate`
- `VAEDecode` ★核心
- `JjkText`
- `UNETLoader` ★核心
- `CLIPLoader`
- `ResolutionSelector`
- `LoadImage`
- `LoadImage`
- `KSampler` ★核心
- `JjkText`
- `SaveImage`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `867582715661677`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **74%**（14/19）

**有卡**：`Label (rgthree)`、`VAELoader`、`TextEncodeQwenImage21`、`QwenImage21Cache`、`EmptyLatentImage`、`MultiTextConcatenate`、`VAEDecode`、`UNETLoader`、`CLIPLoader`、`ResolutionSelector`、`LoadImage`、`KSampler`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
