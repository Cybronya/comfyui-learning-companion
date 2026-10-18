---
key: 视频生成/文生视频/WAN2.1 comfyui原生版幻_1895473564030205954.json
name: WAN2.1 comfyui原生版幻_1895473564030205954.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/WAN2.1 comfyui原生版幻_1895473564030205954.json
hash: ec84597fab98c17f
coverage: 0.925926
learned_at: 2026-10-15 22:43:20
nodes: [CLIPTextEncode, CLIPVisionEncode, CLIPTextEncode, VAELoader, UNETLoader, Joy_caption_two_advanced, ShowText|pysssss, Joy_extra_options, KSampler, VAEDecode, CLIPTextEncode, EmptyHunyuanLatentVideo, CLIPTextEncode, Joy_caption_two_load, VHS_VideoCombine, KSampler, VAELoader, VAEDecode, Note, CLIPVisionLoader, VHS_VideoCombine, CLIPLoader, UNETLoader, WanImageToVideo, LoadImage, CLIPLoader, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 219969260616089, "steps": 20}
---

# 视频生成/文生视频/WAN2.1 comfyui原生版幻_1895473564030205954.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1895473564030205954.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（27 个）：
- `CLIPTextEncode` ★核心
- `CLIPVisionEncode`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `UNETLoader` ★核心
- `Joy_caption_two_advanced`
- `ShowText|pysssss`
- `Joy_extra_options`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `EmptyHunyuanLatentVideo`
- `CLIPTextEncode` ★核心
- `Joy_caption_two_load`
- `VHS_VideoCombine`
- `KSampler` ★核心
- `VAELoader`
- `VAEDecode` ★核心
- `Note`
- `CLIPVisionLoader`
- `VHS_VideoCombine`
- `CLIPLoader`
- `UNETLoader` ★核心
- `WanImageToVideo`
- `LoadImage`
- `CLIPLoader`
- `LoadImage`

## 关键参数

- `seed` = `219969260616089`
- `steps` = `20`
- `cfg` = `6`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **93%**（25/27）

**有卡**：`CLIPTextEncode`、`CLIPVisionEncode`、`VAELoader`、`UNETLoader`、`Joy_caption_two_advanced`、`Joy_extra_options`、`KSampler`、`VAEDecode`、`EmptyHunyuanLatentVideo`、`Joy_caption_two_load`、`VHS_VideoCombine`、`CLIPVisionLoader`、`CLIPLoader`、`WanImageToVideo`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、CLIPVisionEncode
