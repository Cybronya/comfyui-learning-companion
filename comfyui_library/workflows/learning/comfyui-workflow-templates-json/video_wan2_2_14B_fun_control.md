---
key: comfyui-workflow-templates-json/video_wan2_2_14B_fun_control.json
name: video_wan2_2_14B_fun_control
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/video_wan2_2_14B_fun_control.json
hash: 5275224792c2648f
official: true
coverage: 0.863636
learned_at: 2026-10-10 22:50:38
nodes: [CreateVideo, VAEDecode, UNETLoader, UNETLoader, CLIPLoader, VAELoader, GetVideoComponents, PreviewImage, Canny, CreateVideo, VAEDecode, CLIPLoader, VAELoader, UNETLoader, UNETLoader, CLIPTextEncode, Wan22FunControlToVideo, GetVideoComponents, Canny, KSamplerAdvanced, KSamplerAdvanced, ModelSamplingSD3, LoraLoaderModelOnly, ModelSamplingSD3, LoraLoaderModelOnly, CLIPTextEncode, CLIPTextEncode, LoadImage, Wan22FunControlToVideo, KSamplerAdvanced, ModelSamplingSD3, ModelSamplingSD3, KSamplerAdvanced, SaveVideo, SaveVideo, PreviewImage, LoadVideo, CLIPTextEncode, LoadImage, LoadVideo, MarkdownNote, Note, MarkdownNote, MarkdownNote]
patterns: []
missing: []
parameters: {"cfg": 20, "denoise": "simple", "sampler_name": 3.5, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# comfyui-workflow-templates-json/video_wan2_2_14B_fun_control.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/video_wan2_2_14B_fun_control.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（44 个）：
- `CreateVideo`
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `GetVideoComponents`
- `PreviewImage`
- `Canny`
- `CreateVideo`
- `VAEDecode` ★核心
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `Wan22FunControlToVideo`
- `GetVideoComponents`
- `Canny`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `ModelSamplingSD3`
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LoadImage`
- `Wan22FunControlToVideo`
- `KSamplerAdvanced` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `SaveVideo`
- `SaveVideo`
- `PreviewImage`
- `LoadVideo`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `LoadVideo`
- `MarkdownNote`
- `Note`
- `MarkdownNote`
- `MarkdownNote`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `20`
- `sampler_name` = `3.5`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **86%**（38/44）

**有卡**：`CreateVideo`、`VAEDecode`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`GetVideoComponents`、`Canny`、`CLIPTextEncode`、`Wan22FunControlToVideo`、`KSamplerAdvanced`、`ModelSamplingSD3`、`LoraLoaderModelOnly`、`LoadImage`、`SaveVideo`、`LoadVideo`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、Canny
