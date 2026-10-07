---
key: comfyui-workflow-templates-json/video_wan2_2_14B_fun_camera.json
name: video_wan2_2_14B_fun_camera
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/video_wan2_2_14B_fun_camera.json
hash: a18eaacc5c94a6e3
official: true
coverage: 0.918919
learned_at: 2026-10-07 21:37:14
nodes: [UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, WanCameraImageToVideo, CLIPTextEncode, ModelSamplingSD3, ModelSamplingSD3, VAEDecode, CreateVideo, SaveVideo, WanCameraEmbedding, LoadImage, WanCameraImageToVideo, CLIPTextEncode, UNETLoader, UNETLoader, VAELoader, CLIPLoader, CLIPLoader, VAELoader, WanCameraEmbedding, CLIPTextEncode, KSamplerAdvanced, KSamplerAdvanced, CLIPTextEncode, MarkdownNote, MarkdownNote, LoadImage, VAEDecode, CreateVideo, KSamplerAdvanced, KSamplerAdvanced, ModelSamplingSD3, ModelSamplingSD3, SaveVideo, Note]
patterns: []
missing: []
parameters: {"cfg": 20, "denoise": "simple", "sampler_name": 3.5, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# comfyui-workflow-templates-json/video_wan2_2_14B_fun_camera.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/video_wan2_2_14B_fun_camera.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（37 个）：
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `WanCameraImageToVideo`
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `VAEDecode` ★核心
- `CreateVideo`
- `SaveVideo`
- `WanCameraEmbedding`
- `LoadImage`
- `WanCameraImageToVideo`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `VAELoader`
- `CLIPLoader`
- `CLIPLoader`
- `VAELoader`
- `WanCameraEmbedding`
- `CLIPTextEncode` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `MarkdownNote`
- `MarkdownNote`
- `LoadImage`
- `VAEDecode` ★核心
- `CreateVideo`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `SaveVideo`
- `Note`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `20`
- `sampler_name` = `3.5`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **92%**（34/37）

**有卡**：`UNETLoader`、`LoraLoaderModelOnly`、`WanCameraImageToVideo`、`CLIPTextEncode`、`ModelSamplingSD3`、`VAEDecode`、`CreateVideo`、`SaveVideo`、`WanCameraEmbedding`、`LoadImage`、`VAELoader`、`CLIPLoader`、`KSamplerAdvanced`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
