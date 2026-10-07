---
key: comfyui-workflow-templates-json/video_wan2.1_fun_camera_v1.1_14B.json
name: video_wan2.1_fun_camera_v1.1_14B
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/video_wan2.1_fun_camera_v1.1_14B.json
hash: 5b2c8d5e4a589943
official: true
coverage: 0.9375
learned_at: 2026-10-07 21:37:12
nodes: [ModelSamplingSD3, CLIPVisionEncode, CreateVideo, VAEDecode, SaveVideo, WanCameraImageToVideo, UNETLoader, CLIPLoader, VAELoader, CLIPVisionLoader, KSampler, WanCameraEmbedding, CLIPTextEncode, CLIPTextEncode, MarkdownNote, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 536456977716011, "steps": 20}
---

# comfyui-workflow-templates-json/video_wan2.1_fun_camera_v1.1_14B.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/video_wan2.1_fun_camera_v1.1_14B.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（16 个）：
- `ModelSamplingSD3`
- `CLIPVisionEncode`
- `CreateVideo`
- `VAEDecode` ★核心
- `SaveVideo`
- `WanCameraImageToVideo`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `CLIPVisionLoader`
- `KSampler` ★核心
- `WanCameraEmbedding`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `MarkdownNote`
- `LoadImage`

## 关键参数

- `seed` = `536456977716011`
- `steps` = `20`
- `cfg` = `6`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **94%**（15/16）

**有卡**：`ModelSamplingSD3`、`CLIPVisionEncode`、`CreateVideo`、`VAEDecode`、`SaveVideo`、`WanCameraImageToVideo`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`CLIPVisionLoader`、`KSampler`、`WanCameraEmbedding`、`CLIPTextEncode`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、CLIPVisionEncode
