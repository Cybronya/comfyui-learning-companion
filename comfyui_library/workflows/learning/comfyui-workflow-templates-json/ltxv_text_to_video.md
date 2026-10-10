---
key: comfyui-workflow-templates-json/ltxv_text_to_video.json
name: ltxv_text_to_video
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/ltxv_text_to_video.json
hash: 8bbd5219ec8351fc
official: true
coverage: 0.857143
learned_at: 2026-10-10 22:48:49
nodes: [CLIPLoader, CheckpointLoaderSimple, CLIPTextEncode, CLIPTextEncode, Note, EmptyLTXVLatentVideo, SamplerCustom, KSamplerSelect, LTXVScheduler, LTXVConditioning, VAEDecode, CreateVideo, SaveVideo, MarkdownNote]
patterns: []
missing: []
parameters: {"checkpoint": "ltx-video-2b-v0.9.safetensors"}
---

# comfyui-workflow-templates-json/ltxv_text_to_video.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/ltxv_text_to_video.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（14 个）：
- `CLIPLoader`
- `CheckpointLoaderSimple` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `Note`
- `EmptyLTXVLatentVideo`
- `SamplerCustom` ★核心
- `KSamplerSelect` ★核心
- `LTXVScheduler`
- `LTXVConditioning`
- `VAEDecode` ★核心
- `CreateVideo`
- `SaveVideo`
- `MarkdownNote`

## 关键参数

- `checkpoint` = `ltx-video-2b-v0.9.safetensors`

## 知识

覆盖率 **86%**（12/14）

**有卡**：`CLIPLoader`、`CheckpointLoaderSimple`、`CLIPTextEncode`、`EmptyLTXVLatentVideo`、`SamplerCustom`、`KSamplerSelect`、`LTXVScheduler`、`LTXVConditioning`、`VAEDecode`、`CreateVideo`、`SaveVideo`

**用到的条目**：VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、CLIPLoader、KSamplerSelect、SamplerCustom、EmptyLTXVLatentVideo、LTXVConditioning
