---
key: 视频生成/图生视频/万相-Wan2.1-图生视频_1901974657921081346.json
name: 万相-Wan2.1-图生视频_1901974657921081346.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/万相-Wan2.1-图生视频_1901974657921081346.json
hash: cfa796d5c111a254
coverage: 1
learned_at: 2026-10-15 22:29:24
nodes: [CLIPLoader, ModelSamplingSD3, VAELoader, KSampler, UNETLoader, CLIPVisionLoader, VAEDecode, VHS_VideoCombine, WanImageToVideo, CLIPTextEncode, CLIPTextEncode, LoadImage, CLIPVisionEncode, ImageResizeKJ]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 286567222179321, "steps": 20}
---

# 视频生成/图生视频/万相-Wan2.1-图生视频_1901974657921081346.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1901974657921081346.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（14 个）：
- `CLIPLoader`
- `ModelSamplingSD3`
- `VAELoader`
- `KSampler` ★核心
- `UNETLoader` ★核心
- `CLIPVisionLoader`
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `WanImageToVideo`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LoadImage`
- `CLIPVisionEncode`
- `ImageResizeKJ`

## 关键参数

- `seed` = `286567222179321`
- `steps` = `20`
- `cfg` = `6`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（14/14）

**有卡**：`CLIPLoader`、`ModelSamplingSD3`、`VAELoader`、`KSampler`、`UNETLoader`、`CLIPVisionLoader`、`VAEDecode`、`VHS_VideoCombine`、`WanImageToVideo`、`CLIPTextEncode`、`LoadImage`、`CLIPVisionEncode`、`ImageResizeKJ`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、CLIPVisionEncode
