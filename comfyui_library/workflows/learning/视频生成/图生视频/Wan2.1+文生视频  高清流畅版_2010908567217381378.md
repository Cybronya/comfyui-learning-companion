---
key: 视频生成/图生视频/Wan2.1+文生视频  高清流畅版_2010908567217381378.json
name: Wan2.1+文生视频  高清流畅版_2010908567217381378.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2010908567217381378.json
hash: 5e76d7a5ee196a6f
coverage: 1
learned_at: 2026-10-15 22:34:18
nodes: [VAEDecode, VHS_VideoCombine, KSampler, WanVideoTeaCacheKJ, UNETLoader, CLIPLoader, VAELoader, EmptyHunyuanLatentVideo, CLIPTextEncode, CLIPTextEncode]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": 1, "sampler_name": "dpmpp_2m", "scheduler": "sgm_uniform", "seed": 519900529370337, "steps": 30}
---

# 视频生成/图生视频/Wan2.1+文生视频  高清流畅版_2010908567217381378.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2010908567217381378.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（10 个）：
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `KSampler` ★核心
- `WanVideoTeaCacheKJ`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `EmptyHunyuanLatentVideo`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心

## 关键参数

- `seed` = `519900529370337`
- `steps` = `30`
- `cfg` = `6`
- `sampler_name` = `dpmpp_2m`
- `scheduler` = `sgm_uniform`
- `denoise` = `1`

## 知识

覆盖率 **100%**（10/10）

**有卡**：`VAEDecode`、`VHS_VideoCombine`、`KSampler`、`WanVideoTeaCacheKJ`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`EmptyHunyuanLatentVideo`、`CLIPTextEncode`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、EmptyHunyuanLatentVideo、VHS_VideoCombine
