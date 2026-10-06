---
key: 图片生成/文生图/Qwen Image 2.1 ｜生图及编辑_2101865008786395137.json
name: Qwen Image 2.1 ｜生图及编辑_2101865008786395137
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1 ｜生图及编辑_2101865008786395137.json
hash: f8c2a46298fdcda8
coverage: 0.690909
learned_at: 2026-10-07 02:16:27
nodes: [VAELoader, VAEDecode, EmptyLatentImage, ResolutionSelector, UNETLoader, CLIPLoader, Note, MarkdownNote, Note, SaveImage, TextEncodeQwenImage21, SaveImageAdvanced, KSampler, EmptyLatentImage, VAELoader, CLIPLoader, VAEDecode, Note, MarkdownNote, QwenImage21Cache, ResolutionSelector, MarkdownNote, Note, SaveImage, KSampler, SaveImageAdvanced, UNETLoader, TextEncodeQwenImage21, Note, ComfySwitchNode, LoraLoaderModelOnly, MarkdownNote, LoadImage, LoadImage, EmptyLatentImage, VAELoader, CLIPLoader, VAEDecode, Note, MarkdownNote, QwenImage21Cache, ResolutionSelector, Note, SaveImage, KSampler, SaveImageAdvanced, UNETLoader, Note, ComfySwitchNode, TextEncodeQwenImage21, LoadImage, LoadImage, MarkdownNote, MarkdownNote, LoraLoaderModelOnly]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 3.5, "denoise": 1, "height": 1024, "sampler_name": "er_sde", "scheduler": "bong_tangent", "seed": 508989342402138, "steps": 50, "width": 1024}
---

# 图片生成/文生图/Qwen Image 2.1 ｜生图及编辑_2101865008786395137.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1 ｜生图及编辑_2101865008786395137.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（55 个）：
- `VAELoader`
- `VAEDecode` ★核心
- `EmptyLatentImage` ★核心
- `ResolutionSelector`
- `UNETLoader` ★核心
- `CLIPLoader`
- `Note`
- `MarkdownNote`
- `Note`
- `SaveImage`
- `TextEncodeQwenImage21`
- `SaveImageAdvanced`
- `KSampler` ★核心
- `EmptyLatentImage` ★核心
- `VAELoader`
- `CLIPLoader`
- `VAEDecode` ★核心
- `Note`
- `MarkdownNote`
- `QwenImage21Cache`
- `ResolutionSelector`
- `MarkdownNote`
- `Note`
- `SaveImage`
- `KSampler` ★核心
- `SaveImageAdvanced`
- `UNETLoader` ★核心
- `TextEncodeQwenImage21`
- `Note`
- `ComfySwitchNode`
- `LoraLoaderModelOnly` ★核心
- `MarkdownNote`
- `LoadImage`
- `LoadImage`
- `EmptyLatentImage` ★核心
- `VAELoader`
- `CLIPLoader`
- `VAEDecode` ★核心
- `Note`
- `MarkdownNote`
- `QwenImage21Cache`
- `ResolutionSelector`
- `Note`
- `SaveImage`
- `KSampler` ★核心
- `SaveImageAdvanced`
- `UNETLoader` ★核心
- `Note`
- `ComfySwitchNode`
- `TextEncodeQwenImage21`
- `LoadImage`
- `LoadImage`
- `MarkdownNote`
- `MarkdownNote`
- `LoraLoaderModelOnly` ★核心

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `508989342402138`
- `steps` = `50`
- `cfg` = `3.5`
- `sampler_name` = `er_sde`
- `scheduler` = `bong_tangent`
- `denoise` = `1`

## 知识

覆盖率 **69%**（38/55）

**有卡**：`VAELoader`、`VAEDecode`、`EmptyLatentImage`、`ResolutionSelector`、`UNETLoader`、`CLIPLoader`、`SaveImage`、`TextEncodeQwenImage21`、`SaveImageAdvanced`、`KSampler`、`QwenImage21Cache`、`LoraLoaderModelOnly`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、ResolutionSelector
