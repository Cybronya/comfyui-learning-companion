---
key: 视频生成/图生视频/视频首尾帧_wan2.2_smoothmix_1981920767082414081.json
name: 视频首尾帧_wan2.2_smoothmix_1981920767082414081.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/视频首尾帧_wan2.2_smoothmix_1981920767082414081.json
hash: 3bc20ce090803285
coverage: 0.978261
learned_at: 2026-10-15 22:32:39
nodes: [Note, Int, easy setNode, CLIPLoader, UNETLoader, easy setNode, easy setNode, UNETLoader, easy setNode, easy getNode, easy getNode, easy setNode, easy getNode, easy getNode, easy setNode, easy setNode, easy getNode, easy setNode, LoadImage, easy setNode, LoadImage, easy getNode, Get resolution [Crystools], easy getNode, SimpleMath+, SimpleMath+, easy getNode, easy getNode, easy getNode, easy getNode, easy setNode, easy setNode, easy setNode, WanFirstLastFrameToVideo, easy getNode, easy getNode, VAEDecode, CLIPTextEncode, CLIPTextEncode, ModelSamplingSD3, ModelSamplingSD3, easy getNode, KSamplerAdvanced, VAELoader, VHS_VideoCombine, KSamplerAdvanced]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/视频首尾帧_wan2.2_smoothmix_1981920767082414081.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1981920767082414081.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（46 个）：
- `Note`
- `Int`
- `easy setNode`
- `CLIPLoader`
- `UNETLoader` ★核心
- `easy setNode`
- `easy setNode`
- `UNETLoader` ★核心
- `easy setNode`
- `easy getNode`
- `easy getNode`
- `easy setNode`
- `easy getNode`
- `easy getNode`
- `easy setNode`
- `easy setNode`
- `easy getNode`
- `easy setNode`
- `LoadImage`
- `easy setNode`
- `LoadImage`
- `easy getNode`
- `Get resolution [Crystools]`
- `easy getNode`
- `SimpleMath+`
- `SimpleMath+`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `easy setNode`
- `easy setNode`
- `easy setNode`
- `WanFirstLastFrameToVideo`
- `easy getNode`
- `easy getNode`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `easy getNode`
- `KSamplerAdvanced` ★核心
- `VAELoader`
- `VHS_VideoCombine`
- `KSamplerAdvanced` ★核心

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **98%**（45/46）

**有卡**：`Int`、`easy setNode`、`CLIPLoader`、`UNETLoader`、`easy getNode`、`LoadImage`、`Get resolution [Crystools]`、`SimpleMath+`、`WanFirstLastFrameToVideo`、`VAEDecode`、`CLIPTextEncode`、`ModelSamplingSD3`、`KSamplerAdvanced`、`VAELoader`、`VHS_VideoCombine`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、Get resolution [Crystools]
