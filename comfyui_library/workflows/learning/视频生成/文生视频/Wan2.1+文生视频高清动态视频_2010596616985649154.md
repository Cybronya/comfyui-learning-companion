---
key: 视频生成/文生视频/Wan2.1+文生视频高清动态视频_2010596616985649154.json
name: Wan2.1+文生视频高清动态视频_2010596616985649154
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.1+文生视频高清动态视频_2010596616985649154.json
hash: 36fdfb222f50a268
coverage: 1
learned_at: 2026-10-11 03:07:12
nodes: [VAEDecode, VHS_VideoCombine, KSampler, WanVideoTeaCacheKJ, UNETLoader, CLIPLoader, VAELoader, EmptyHunyuanLatentVideo, CLIPTextEncode, CLIPTextEncode]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": 1, "sampler_name": "dpmpp_2m", "scheduler": "sgm_uniform", "seed": 400176677484015, "steps": 30}
---

# 视频生成/文生视频/Wan2.1+文生视频高清动态视频_2010596616985649154.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.1+文生视频高清动态视频_2010596616985649154.json`

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

- `seed` = `400176677484015`
- `steps` = `30`
- `cfg` = `6`
- `sampler_name` = `dpmpp_2m`
- `scheduler` = `sgm_uniform`
- `denoise` = `1`

## 知识

覆盖率 **100%**（10/10）

**有卡**：`VAEDecode`、`VHS_VideoCombine`、`KSampler`、`WanVideoTeaCacheKJ`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`EmptyHunyuanLatentVideo`、`CLIPTextEncode`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、EmptyHunyuanLatentVideo、VHS_VideoCombine
