---
key: 视频生成/图生视频/Wan2.2_图生视频4步LoRA加速-B站UP主@好奇漫步_1983147421196820482.json
name: Wan2.2_图生视频4步LoRA加速-B站UP主@好奇漫步_1983147421196820482.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1983147421196820482.json
hash: a07a305b1eabfdb5
coverage: 0.871795
learned_at: 2026-10-15 22:32:43
nodes: [CLIPLoader, CLIPTextEncode, VAELoader, ModelSamplingSD3, ModelSamplingSD3, CLIPTextEncode, WanImageToVideo, LoadImage, ModelSamplingSD3, CLIPTextEncode, LoadImage, MarkdownNote, Note, CreateVideo, VAEDecode, SaveVideo, KSamplerAdvanced, KSamplerAdvanced, KSamplerAdvanced, CreateVideo, VAEDecode, KSamplerAdvanced, SaveVideo, VAELoader, CLIPLoader, ModelSamplingSD3, UNETLoader, UNETLoader, Note, LoadImage, MarkdownNote, LoadImage, CLIPTextEncode, WanImageToVideo, MarkdownNote, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, UNETLoader]
patterns: []
missing: []
parameters: {"cfg": 20, "denoise": "simple", "sampler_name": 3.5, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 视频生成/图生视频/Wan2.2_图生视频4步LoRA加速-B站UP主@好奇漫步_1983147421196820482.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1983147421196820482.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（39 个）：
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `WanImageToVideo`
- `LoadImage`
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `MarkdownNote`
- `Note`
- `CreateVideo`
- `VAEDecode` ★核心
- `SaveVideo`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `CreateVideo`
- `VAEDecode` ★核心
- `KSamplerAdvanced` ★核心
- `SaveVideo`
- `VAELoader`
- `CLIPLoader`
- `ModelSamplingSD3`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `Note`
- `LoadImage`
- `MarkdownNote`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `WanImageToVideo`
- `MarkdownNote`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `20`
- `sampler_name` = `3.5`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **87%**（34/39）

**有卡**：`CLIPLoader`、`CLIPTextEncode`、`VAELoader`、`ModelSamplingSD3`、`WanImageToVideo`、`LoadImage`、`CreateVideo`、`VAEDecode`、`SaveVideo`、`KSamplerAdvanced`、`UNETLoader`、`LoraLoaderModelOnly`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
