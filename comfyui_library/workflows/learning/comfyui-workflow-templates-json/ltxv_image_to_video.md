---
key: comfyui-workflow-templates-json/ltxv_image_to_video.json
name: ltxv_image_to_video
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/ltxv_image_to_video.json
hash: 8d41217612e91b4e
official: true
coverage: 0.866667
learned_at: 2026-10-07 21:36:14
nodes: [CLIPLoader, LTXVConditioning, Note, CLIPTextEncode, LTXVScheduler, KSamplerSelect, SamplerCustom, SaveVideo, CheckpointLoaderSimple, CreateVideo, VAEDecode, CLIPTextEncode, LoadImage, LTXVImgToVideo, MarkdownNote]
patterns: []
missing: []
parameters: {"checkpoint": "ltx-video-2b-v0.9.5.safetensors"}
---

# comfyui-workflow-templates-json/ltxv_image_to_video.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/ltxv_image_to_video.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（15 个）：
- `CLIPLoader`
- `LTXVConditioning`
- `Note`
- `CLIPTextEncode` ★核心
- `LTXVScheduler`
- `KSamplerSelect` ★核心
- `SamplerCustom` ★核心
- `SaveVideo`
- `CheckpointLoaderSimple` ★核心
- `CreateVideo`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `LoadImage`
- `LTXVImgToVideo`
- `MarkdownNote`

## 关键参数

- `checkpoint` = `ltx-video-2b-v0.9.5.safetensors`

## 知识

覆盖率 **87%**（13/15）

**有卡**：`CLIPLoader`、`LTXVConditioning`、`CLIPTextEncode`、`LTXVScheduler`、`KSamplerSelect`、`SamplerCustom`、`SaveVideo`、`CheckpointLoaderSimple`、`CreateVideo`、`VAEDecode`、`LoadImage`、`LTXVImgToVideo`

**用到的条目**：VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、CLIPLoader、LoadImage、KSamplerSelect、SamplerCustom、LTXVConditioning
