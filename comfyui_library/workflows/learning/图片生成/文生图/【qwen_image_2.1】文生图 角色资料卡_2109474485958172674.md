---
key: 图片生成/文生图/【qwen_image_2.1】文生图 角色资料卡_2109474485958172674.json
name: 【qwen_image_2.1】文生图 角色资料卡_2109474485958172674
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/【qwen_image_2.1】文生图 角色资料卡_2109474485958172674.json
hash: 597e9b85f584f8f3
coverage: 0.7
learned_at: 2026-10-21 02:58:01
nodes: [CLIPLoader, VAELoader, QwenImage21Cache, StringConcatenate, CLIPLoader, PrimitiveStringMultiline, JjkText, ModelAttentionBackend, TextGenerate, EmptyLatentImage, SaveImage, UNETLoader, PreviewAny, VAEDecode, JjkText, ResolutionSelector, KSampler, TextEncodeQwenImage21, JjkText, JjkText]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 390916660281449, "steps": 60, "width": 1024}
---

# 图片生成/文生图/【qwen_image_2.1】文生图 角色资料卡_2109474485958172674.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/【qwen_image_2.1】文生图 角色资料卡_2109474485958172674.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（20 个）：
- `CLIPLoader`
- `VAELoader`
- `QwenImage21Cache`
- `StringConcatenate`
- `CLIPLoader`
- `PrimitiveStringMultiline`
- `JjkText`
- `ModelAttentionBackend`
- `TextGenerate`
- `EmptyLatentImage` ★核心
- `SaveImage`
- `UNETLoader` ★核心
- `PreviewAny`
- `VAEDecode` ★核心
- `JjkText`
- `ResolutionSelector`
- `KSampler` ★核心
- `TextEncodeQwenImage21`
- `JjkText`
- `JjkText`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `390916660281449`
- `steps` = `60`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **70%**（14/20）

**有卡**：`CLIPLoader`、`VAELoader`、`QwenImage21Cache`、`StringConcatenate`、`ModelAttentionBackend`、`TextGenerate`、`EmptyLatentImage`、`SaveImage`、`UNETLoader`、`VAEDecode`、`ResolutionSelector`、`KSampler`、`TextEncodeQwenImage21`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、QwenImage21Cache
