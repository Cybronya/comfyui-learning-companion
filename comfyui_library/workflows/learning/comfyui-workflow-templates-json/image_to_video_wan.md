---
key: comfyui-workflow-templates-json/image_to_video_wan.json
name: image_to_video_wan
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/image_to_video_wan.json
hash: 2dfc90d0972c850e
official: true
coverage: 0.933333
learned_at: 2026-10-07 21:36:04
nodes: [UNETLoader, CLIPLoader, VAELoader, CLIPVisionLoader, CLIPTextEncode, ModelSamplingSD3, CreateVideo, KSampler, VAEDecode, SaveVideo, WanImageToVideo, CLIPVisionEncode, CLIPTextEncode, MarkdownNote, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 987948718394761, "steps": 20}
---

# comfyui-workflow-templates-json/image_to_video_wan.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/image_to_video_wan.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（15 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `CLIPVisionLoader`
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `CreateVideo`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveVideo`
- `WanImageToVideo`
- `CLIPVisionEncode`
- `CLIPTextEncode` ★核心
- `MarkdownNote`
- `LoadImage`

## 关键参数

- `seed` = `987948718394761`
- `steps` = `20`
- `cfg` = `6`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **93%**（14/15）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`CLIPVisionLoader`、`CLIPTextEncode`、`ModelSamplingSD3`、`CreateVideo`、`KSampler`、`VAEDecode`、`SaveVideo`、`WanImageToVideo`、`CLIPVisionEncode`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、CLIPVisionEncode
