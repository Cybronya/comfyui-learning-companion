---
key: 视频生成/文生视频/WAN2.1文生视频_1977308765202587649.json
name: WAN2.1文生视频_1977308765202587649
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/WAN2.1文生视频_1977308765202587649.json
hash: d82da39eab89c0a0
coverage: 1
learned_at: 2026-10-10 23:05:53
nodes: [ModelSamplingSD3, CLIPLoader, UNETLoader, VAELoader, CLIPTextEncode, KSampler, VAEDecode, VHS_VideoCombine, EmptyHunyuanLatentVideo, CLIPTextEncode]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 236696653865582, "steps": 30}
---

# 视频生成/文生视频/WAN2.1文生视频_1977308765202587649.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/WAN2.1文生视频_1977308765202587649.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（10 个）：
- `ModelSamplingSD3`
- `CLIPLoader`
- `UNETLoader` ★核心
- `VAELoader`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `EmptyHunyuanLatentVideo`
- `CLIPTextEncode` ★核心

## 关键参数

- `seed` = `236696653865582`
- `steps` = `30`
- `cfg` = `6`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（10/10）

**有卡**：`ModelSamplingSD3`、`CLIPLoader`、`UNETLoader`、`VAELoader`、`CLIPTextEncode`、`KSampler`、`VAEDecode`、`VHS_VideoCombine`、`EmptyHunyuanLatentVideo`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、EmptyHunyuanLatentVideo、ModelSamplingSD3
