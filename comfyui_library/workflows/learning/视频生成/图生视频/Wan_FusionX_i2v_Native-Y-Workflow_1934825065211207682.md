---
key: 视频生成/图生视频/Wan_FusionX_i2v_Native-Y-Workflow_1934825065211207682.json
name: Wan_FusionX_i2v_Native-Y-Workflow_1934825065211207682.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan_FusionX_i2v_Native-Y-Workflow_1934825065211207682.json
hash: 39af8ae8982b2b7b
coverage: 0.928571
learned_at: 2026-10-15 22:30:19
nodes: [ModelSamplingSD3, UNETLoader, CLIPTextEncode, CLIPVisionEncode, LoadImage, WanImageToVideo, VAEDecode, VAELoader, MarkdownNote, VHS_VideoCombine, CLIPTextEncode, CLIPVisionLoader, CLIPLoader, KSampler]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 662150111465353, "steps": 10}
---

# 视频生成/图生视频/Wan_FusionX_i2v_Native-Y-Workflow_1934825065211207682.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1934825065211207682.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（14 个）：
- `ModelSamplingSD3`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `CLIPVisionEncode`
- `LoadImage`
- `WanImageToVideo`
- `VAEDecode` ★核心
- `VAELoader`
- `MarkdownNote`
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心
- `CLIPVisionLoader`
- `CLIPLoader`
- `KSampler` ★核心

## 关键参数

- `seed` = `662150111465353`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **93%**（13/14）

**有卡**：`ModelSamplingSD3`、`UNETLoader`、`CLIPTextEncode`、`CLIPVisionEncode`、`LoadImage`、`WanImageToVideo`、`VAEDecode`、`VAELoader`、`VHS_VideoCombine`、`CLIPVisionLoader`、`CLIPLoader`、`KSampler`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、CLIPVisionEncode
