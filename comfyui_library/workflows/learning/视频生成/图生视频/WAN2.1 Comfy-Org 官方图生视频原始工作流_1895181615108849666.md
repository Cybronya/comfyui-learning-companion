---
key: 视频生成/图生视频/WAN2.1 Comfy-Org 官方图生视频原始工作流_1895181615108849666.json
name: WAN2.1 Comfy-Org 官方图生视频原始工作流_1895181615108849666.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/WAN2.1 Comfy-Org 官方图生视频原始工作流_1895181615108849666.json
hash: d9f5502397f52bd5
coverage: 1
learned_at: 2026-10-15 22:29:17
nodes: [CLIPTextEncode, KSampler, CLIPTextEncode, VAELoader, VAEDecode, CLIPVisionLoader, CLIPLoader, WanImageToVideo, UNETLoader, VHS_VideoCombine, LoadImage, CLIPVisionEncode]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 700366301648769, "steps": 20}
---

# 视频生成/图生视频/WAN2.1 Comfy-Org 官方图生视频原始工作流_1895181615108849666.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1895181615108849666.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（12 个）：
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `VAELoader`
- `VAEDecode` ★核心
- `CLIPVisionLoader`
- `CLIPLoader`
- `WanImageToVideo`
- `UNETLoader` ★核心
- `VHS_VideoCombine`
- `LoadImage`
- `CLIPVisionEncode`

## 关键参数

- `seed` = `700366301648769`
- `steps` = `20`
- `cfg` = `6`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（12/12）

**有卡**：`CLIPTextEncode`、`KSampler`、`VAELoader`、`VAEDecode`、`CLIPVisionLoader`、`CLIPLoader`、`WanImageToVideo`、`UNETLoader`、`VHS_VideoCombine`、`LoadImage`、`CLIPVisionEncode`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、CLIPVisionEncode
