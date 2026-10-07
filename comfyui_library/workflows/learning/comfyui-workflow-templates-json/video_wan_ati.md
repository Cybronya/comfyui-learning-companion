---
key: comfyui-workflow-templates-json/video_wan_ati.json
name: video_wan_ati
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/video_wan_ati.json
hash: 2495a1985aa0781f
official: true
coverage: 0.777778
learned_at: 2026-10-07 21:37:20
nodes: [UNETLoader, CLIPLoader, WanTrackToVideo, CLIPTextEncode, CLIPVisionEncode, VAELoader, CLIPVisionLoader, SaveVideo, LoadImage, MarkdownNote, CreateVideo, KSampler, ModelSamplingSD3, MarkdownNote, VAEDecode, CLIPTextEncode, PrimitiveStringMultiline, MarkdownNote]
patterns: []
missing: []
parameters: {"cfg": 3, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 48, "steps": 20}
---

# comfyui-workflow-templates-json/video_wan_ati.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/video_wan_ati.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（18 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `WanTrackToVideo`
- `CLIPTextEncode` ★核心
- `CLIPVisionEncode`
- `VAELoader`
- `CLIPVisionLoader`
- `SaveVideo`
- `LoadImage`
- `MarkdownNote`
- `CreateVideo`
- `KSampler` ★核心
- `ModelSamplingSD3`
- `MarkdownNote`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `PrimitiveStringMultiline`
- `MarkdownNote`

## 关键参数

- `seed` = `48`
- `steps` = `20`
- `cfg` = `3`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **78%**（14/18）

**有卡**：`UNETLoader`、`CLIPLoader`、`WanTrackToVideo`、`CLIPTextEncode`、`CLIPVisionEncode`、`VAELoader`、`CLIPVisionLoader`、`SaveVideo`、`LoadImage`、`CreateVideo`、`KSampler`、`ModelSamplingSD3`、`VAEDecode`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、CLIPVisionEncode
