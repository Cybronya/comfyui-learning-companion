---
key: 视频生成/图生视频/【老金驿站】Comfyui原生支持WAN2.1-i2v_1895293426588385281.json
name: 【老金驿站】Comfyui原生支持WAN2.1-i2v_1895293426588385281.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1895293426588385281.json
hash: 945cc310fa45624b
coverage: 1
learned_at: 2026-10-15 22:29:17
nodes: [CLIPVisionEncode, VAELoader, CLIPTextEncode, CLIPLoader, VAEDecode, UNETLoader, WanImageToVideo, CLIPVisionLoader, LoadImage, KSampler, CLIPTextEncode, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 542096711350029, "steps": 20}
---

# 视频生成/图生视频/【老金驿站】Comfyui原生支持WAN2.1-i2v_1895293426588385281.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1895293426588385281.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（12 个）：
- `CLIPVisionEncode`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `WanImageToVideo`
- `CLIPVisionLoader`
- `LoadImage`
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`

## 关键参数

- `seed` = `542096711350029`
- `steps` = `20`
- `cfg` = `6`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（12/12）

**有卡**：`CLIPVisionEncode`、`VAELoader`、`CLIPTextEncode`、`CLIPLoader`、`VAEDecode`、`UNETLoader`、`WanImageToVideo`、`CLIPVisionLoader`、`LoadImage`、`KSampler`、`VHS_VideoCombine`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、CLIPVisionEncode
