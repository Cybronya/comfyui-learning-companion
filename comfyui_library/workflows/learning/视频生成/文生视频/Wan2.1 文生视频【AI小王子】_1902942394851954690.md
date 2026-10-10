---
key: 视频生成/文生视频/Wan2.1 文生视频【AI小王子】_1902942394851954690.json
name: Wan2.1 文生视频【AI小王子】_1902942394851954690
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.1 文生视频【AI小王子】_1902942394851954690.json
hash: 3658650d5119bdeb
coverage: 1
learned_at: 2026-10-10 23:06:30
nodes: [CLIPTextEncode, VAEDecode, VHS_VideoCombine, KSampler, WanVideoTeaCacheKJ, UNETLoader, CLIPLoader, VAELoader, CLIPTextEncode, EmptyHunyuanLatentVideo]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": 1, "sampler_name": "dpmpp_2m", "scheduler": "sgm_uniform", "seed": 263191718110493, "steps": 30}
---

# 视频生成/文生视频/Wan2.1 文生视频【AI小王子】_1902942394851954690.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.1 文生视频【AI小王子】_1902942394851954690.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（10 个）：
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `KSampler` ★核心
- `WanVideoTeaCacheKJ`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `EmptyHunyuanLatentVideo`

## 关键参数

- `seed` = `263191718110493`
- `steps` = `30`
- `cfg` = `6`
- `sampler_name` = `dpmpp_2m`
- `scheduler` = `sgm_uniform`
- `denoise` = `1`

## 知识

覆盖率 **100%**（10/10）

**有卡**：`CLIPTextEncode`、`VAEDecode`、`VHS_VideoCombine`、`KSampler`、`WanVideoTeaCacheKJ`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`EmptyHunyuanLatentVideo`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、EmptyHunyuanLatentVideo、VHS_VideoCombine
