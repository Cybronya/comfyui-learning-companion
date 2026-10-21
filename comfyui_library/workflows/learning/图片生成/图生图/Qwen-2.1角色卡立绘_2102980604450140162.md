---
key: 图片生成/图生图/Qwen-2.1角色卡立绘_2102980604450140162.json
name: Qwen-2.1角色卡立绘_2102980604450140162
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-2.1角色卡立绘_2102980604450140162.json
hash: 92fb1f7787a12ff0
coverage: 0.76
learned_at: 2026-10-21 00:43:06
nodes: [MarkdownNote, MarkdownNote, MarkdownNote, Label (rgthree), VAELoader, TextEncodeQwenImage21, QwenImage21Cache, EmptyLatentImage, SaveImage, UNETLoader, CLIPLoader, ResolutionSelector, llama_cpp_instruct_adv, llama_cpp_parameters, easy clearCacheAll, easy clearCacheAll, llama_cpp_model_loader, LoadImage, PreviewAny, KSampler, JjkText, PreviewImage, easy imageConcat, ImageScaleBy, VAEDecode]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 1098808909404966, "steps": 30, "width": 1024}
---

# 图片生成/图生图/Qwen-2.1角色卡立绘_2102980604450140162.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-2.1角色卡立绘_2102980604450140162.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（25 个）：
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `Label (rgthree)`
- `VAELoader`
- `TextEncodeQwenImage21`
- `QwenImage21Cache`
- `EmptyLatentImage` ★核心
- `SaveImage`
- `UNETLoader` ★核心
- `CLIPLoader`
- `ResolutionSelector`
- `llama_cpp_instruct_adv`
- `llama_cpp_parameters`
- `easy clearCacheAll`
- `easy clearCacheAll`
- `llama_cpp_model_loader`
- `LoadImage`
- `PreviewAny`
- `KSampler` ★核心
- `JjkText`
- `PreviewImage`
- `easy imageConcat`
- `ImageScaleBy`
- `VAEDecode` ★核心

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `1098808909404966`
- `steps` = `30`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **76%**（19/25）

**有卡**：`Label (rgthree)`、`VAELoader`、`TextEncodeQwenImage21`、`QwenImage21Cache`、`EmptyLatentImage`、`SaveImage`、`UNETLoader`、`CLIPLoader`、`ResolutionSelector`、`llama_cpp_instruct_adv`、`llama_cpp_parameters`、`easy clearCacheAll`、`llama_cpp_model_loader`、`LoadImage`、`KSampler`、`easy imageConcat`、`ImageScaleBy`、`VAEDecode`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
