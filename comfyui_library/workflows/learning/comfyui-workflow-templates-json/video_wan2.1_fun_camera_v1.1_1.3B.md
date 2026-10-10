---
key: comfyui-workflow-templates-json/video_wan2.1_fun_camera_v1.1_1.3B.json
name: video_wan2.1_fun_camera_v1.1_1.3B
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/video_wan2.1_fun_camera_v1.1_1.3B.json
hash: b559883f34a79f7d
official: true
coverage: 0.941176
learned_at: 2026-10-10 22:50:33
nodes: [CLIPVisionLoader, VAELoader, CLIPLoader, UNETLoader, LoadImage, ModelSamplingSD3, KSampler, CLIPVisionEncode, CreateVideo, VAEDecode, SaveAnimatedWEBP, SaveVideo, WanCameraEmbedding, CLIPTextEncode, WanCameraImageToVideo, CLIPTextEncode, MarkdownNote]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 987948718394762, "steps": 20}
---

# comfyui-workflow-templates-json/video_wan2.1_fun_camera_v1.1_1.3B.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/video_wan2.1_fun_camera_v1.1_1.3B.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（17 个）：
- `CLIPVisionLoader`
- `VAELoader`
- `CLIPLoader`
- `UNETLoader` ★核心
- `LoadImage`
- `ModelSamplingSD3`
- `KSampler` ★核心
- `CLIPVisionEncode`
- `CreateVideo`
- `VAEDecode` ★核心
- `SaveAnimatedWEBP`
- `SaveVideo`
- `WanCameraEmbedding`
- `CLIPTextEncode` ★核心
- `WanCameraImageToVideo`
- `CLIPTextEncode` ★核心
- `MarkdownNote`

## 关键参数

- `seed` = `987948718394762`
- `steps` = `20`
- `cfg` = `6`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **94%**（16/17）

**有卡**：`CLIPVisionLoader`、`VAELoader`、`CLIPLoader`、`UNETLoader`、`LoadImage`、`ModelSamplingSD3`、`KSampler`、`CLIPVisionEncode`、`CreateVideo`、`VAEDecode`、`SaveAnimatedWEBP`、`SaveVideo`、`WanCameraEmbedding`、`CLIPTextEncode`、`WanCameraImageToVideo`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、CLIPVisionEncode
