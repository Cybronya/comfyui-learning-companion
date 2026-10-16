---
key: 视频生成/图生视频/Wan2.1 FL2fV 首尾帧_1948615618990866434.json
name: Wan2.1 FL2fV 首尾帧_1948615618990866434.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1948615618990866434.json
hash: 964e564398c25a89
coverage: 0.944444
learned_at: 2026-10-15 22:30:47
nodes: [VAELoader, CLIPVisionEncode, CLIPVisionLoader, CLIPVisionEncode, ModelSamplingSD3, WanFirstLastFrameToVideo, CLIPTextEncode, CLIPLoader, UNETLoader, LoadImage, LoadImage, KSampler, VAEDecode, VHS_VideoCombine, CLIPTextEncode, Note Plus (mtb), MarkdownNote, LoadImageFromUrl]
patterns: []
missing: []
parameters: {"cfg": 3, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 792708652505709, "steps": 20}
---

# 视频生成/图生视频/Wan2.1 FL2fV 首尾帧_1948615618990866434.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1948615618990866434.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（18 个）：
- `VAELoader`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CLIPVisionEncode`
- `ModelSamplingSD3`
- `WanFirstLastFrameToVideo`
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `UNETLoader` ★核心
- `LoadImage`
- `LoadImage`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心
- `Note Plus (mtb)`
- `MarkdownNote`
- `LoadImageFromUrl`

## 关键参数

- `seed` = `792708652505709`
- `steps` = `20`
- `cfg` = `3`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **94%**（17/18）

**有卡**：`VAELoader`、`CLIPVisionEncode`、`CLIPVisionLoader`、`ModelSamplingSD3`、`WanFirstLastFrameToVideo`、`CLIPTextEncode`、`CLIPLoader`、`UNETLoader`、`LoadImage`、`KSampler`、`VAEDecode`、`VHS_VideoCombine`、`Note Plus (mtb)`、`LoadImageFromUrl`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、CLIPVisionEncode
