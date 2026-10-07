---
key: comfyui-workflow-templates-json/video_wan2_2_14B_flf2v.json
name: video_wan2_2_14B_flf2v
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/video_wan2_2_14B_flf2v.json
hash: 0325fe7832674530
official: true
coverage: 0.85
learned_at: 2026-10-07 21:37:14
nodes: [CLIPLoader, CLIPTextEncode, LoadImage, CreateVideo, CLIPLoader, ModelSamplingSD3, ModelSamplingSD3, UNETLoader, UNETLoader, CLIPTextEncode, VAELoader, WanFirstLastFrameToVideo, VAEDecode, CreateVideo, Note, CLIPTextEncode, UNETLoader, UNETLoader, VAEDecode, ModelSamplingSD3, LoraLoaderModelOnly, LoraLoaderModelOnly, ModelSamplingSD3, KSamplerAdvanced, KSamplerAdvanced, SaveVideo, VAELoader, WanFirstLastFrameToVideo, CLIPTextEncode, LoadImage, SaveVideo, Note, Note, LoadImage, LoadImage, MarkdownNote, KSamplerAdvanced, KSamplerAdvanced, MarkdownNote, MarkdownNote]
patterns: []
missing: []
parameters: {"cfg": 20, "denoise": "simple", "sampler_name": 4, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# comfyui-workflow-templates-json/video_wan2_2_14B_flf2v.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/video_wan2_2_14B_flf2v.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（40 个）：
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `CreateVideo`
- `CLIPLoader`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `VAELoader`
- `WanFirstLastFrameToVideo`
- `VAEDecode` ★核心
- `CreateVideo`
- `Note`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `ModelSamplingSD3`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `SaveVideo`
- `VAELoader`
- `WanFirstLastFrameToVideo`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `SaveVideo`
- `Note`
- `Note`
- `LoadImage`
- `LoadImage`
- `MarkdownNote`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `MarkdownNote`
- `MarkdownNote`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `20`
- `sampler_name` = `4`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **85%**（34/40）

**有卡**：`CLIPLoader`、`CLIPTextEncode`、`LoadImage`、`CreateVideo`、`ModelSamplingSD3`、`UNETLoader`、`VAELoader`、`WanFirstLastFrameToVideo`、`VAEDecode`、`LoraLoaderModelOnly`、`KSamplerAdvanced`、`SaveVideo`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
