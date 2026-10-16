---
key: 视频生成/图生视频/Wan2.1_Fun_V1.1_Control_Camera_1.3B_I2V_2038456404972933122.json
name: Wan2.1_Fun_V1.1_Control_Camera_1.3B_I2V_2038456404972933122.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2038456404972933122.json
hash: 9afb0676287ec5c1
coverage: 0.9375
learned_at: 2026-10-15 22:36:02
nodes: [ModelSamplingSD3, CLIPTextEncode, MarkdownNote, UNETLoader, CLIPLoader, VAELoader, CLIPVisionLoader, SaveVideo, CreateVideo, VAEDecode, WanCameraImageToVideo, KSampler, LoadImage, CLIPVisionEncode, CLIPTextEncode, WanCameraEmbedding]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 987948718394762, "steps": 20}
---

# 视频生成/图生视频/Wan2.1_Fun_V1.1_Control_Camera_1.3B_I2V_2038456404972933122.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2038456404972933122.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（16 个）：
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `MarkdownNote`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `CLIPVisionLoader`
- `SaveVideo`
- `CreateVideo`
- `VAEDecode` ★核心
- `WanCameraImageToVideo`
- `KSampler` ★核心
- `LoadImage`
- `CLIPVisionEncode`
- `CLIPTextEncode` ★核心
- `WanCameraEmbedding`

## 关键参数

- `seed` = `987948718394762`
- `steps` = `20`
- `cfg` = `6`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **94%**（15/16）

**有卡**：`ModelSamplingSD3`、`CLIPTextEncode`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`CLIPVisionLoader`、`SaveVideo`、`CreateVideo`、`VAEDecode`、`WanCameraImageToVideo`、`KSampler`、`LoadImage`、`CLIPVisionEncode`、`WanCameraEmbedding`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、CLIPVisionEncode
