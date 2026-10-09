---
key: 图片生成/文生图/Wan2.2 14B FLF2V工作流程示例_1952243604368642050.json
name: Wan2.2 14B FLF2V工作流程示例_1952243604368642050.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Wan2.2 14B FLF2V工作流程示例_1952243604368642050.json
hash: f6a266121148cd87
coverage: 0.857143
learned_at: 2026-10-07 23:04:36
nodes: [CLIPLoader, ModelSamplingSD3, MarkdownNote, CLIPTextEncode, VAELoader, CLIPTextEncode, WanFirstLastFrameToVideo, Note, SaveVideo, VAEDecode, CreateVideo, Note, LoadImage, LoadImage, UNETLoader, LoraLoaderModelOnly, UNETLoader, LoraLoaderModelOnly, KSamplerAdvanced, ModelSamplingSD3, KSamplerAdvanced]
patterns: []
missing: []
parameters: {"cfg": 20, "denoise": "simple", "sampler_name": 4, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 图片生成/文生图/Wan2.2 14B FLF2V工作流程示例_1952243604368642050.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/1952243604368642050.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（21 个）：
- `CLIPLoader`
- `ModelSamplingSD3`
- `MarkdownNote`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `CLIPTextEncode` ★核心
- `WanFirstLastFrameToVideo`
- `Note`
- `SaveVideo`
- `VAEDecode` ★核心
- `CreateVideo`
- `Note`
- `LoadImage`
- `LoadImage`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSamplerAdvanced` ★核心
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `20`
- `sampler_name` = `4`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **86%**（18/21）

**有卡**：`CLIPLoader`、`ModelSamplingSD3`、`CLIPTextEncode`、`VAELoader`、`WanFirstLastFrameToVideo`、`SaveVideo`、`VAEDecode`、`CreateVideo`、`LoadImage`、`UNETLoader`、`LoraLoaderModelOnly`、`KSamplerAdvanced`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
