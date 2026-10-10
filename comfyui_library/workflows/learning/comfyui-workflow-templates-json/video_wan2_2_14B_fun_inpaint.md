---
key: comfyui-workflow-templates-json/video_wan2_2_14B_fun_inpaint.json
name: video_wan2_2_14B_fun_inpaint
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/video_wan2_2_14B_fun_inpaint.json
hash: 9233091ea1891c03
official: true
coverage: 0.894737
learned_at: 2026-10-10 22:50:39
nodes: [CLIPLoader, VAELoader, UNETLoader, CLIPTextEncode, LoraLoaderModelOnly, ModelSamplingSD3, LoraLoaderModelOnly, ModelSamplingSD3, KSamplerAdvanced, KSamplerAdvanced, VAEDecode, CLIPLoader, VAELoader, UNETLoader, UNETLoader, LoadImage, LoadImage, WanFunInpaintToVideo, VAEDecode, CreateVideo, SaveVideo, KSamplerAdvanced, ModelSamplingSD3, ModelSamplingSD3, CLIPTextEncode, KSamplerAdvanced, UNETLoader, WanFunInpaintToVideo, Note, MarkdownNote, CreateVideo, SaveVideo, CLIPTextEncode, CLIPTextEncode, Note, MarkdownNote, LoadImage, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 20, "denoise": "simple", "sampler_name": 3.5, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# comfyui-workflow-templates-json/video_wan2_2_14B_fun_inpaint.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/video_wan2_2_14B_fun_inpaint.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（38 个）：
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoadImage`
- `LoadImage`
- `WanFunInpaintToVideo`
- `VAEDecode` ★核心
- `CreateVideo`
- `SaveVideo`
- `KSamplerAdvanced` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `KSamplerAdvanced` ★核心
- `UNETLoader` ★核心
- `WanFunInpaintToVideo`
- `Note`
- `MarkdownNote`
- `CreateVideo`
- `SaveVideo`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `Note`
- `MarkdownNote`
- `LoadImage`
- `LoadImage`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `20`
- `sampler_name` = `3.5`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **89%**（34/38）

**有卡**：`CLIPLoader`、`VAELoader`、`UNETLoader`、`CLIPTextEncode`、`LoraLoaderModelOnly`、`ModelSamplingSD3`、`KSamplerAdvanced`、`VAEDecode`、`LoadImage`、`WanFunInpaintToVideo`、`CreateVideo`、`SaveVideo`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
