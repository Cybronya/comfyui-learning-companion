---
key: 视频生成/文生视频/wan2.1基础文生视频001_1909164954489135106.json
name: wan2.1基础文生视频001_1909164954489135106.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/wan2.1基础文生视频001_1909164954489135106.json
hash: c33df3c2001efc91
coverage: 1
learned_at: 2026-10-15 22:43:22
nodes: [CLIPTextEncode, CLIPLoader, VAEDecode, VHS_VideoCombine, VAELoader, KSampler, EmptyHunyuanLatentVideo, CLIPTextEncode, UNETLoader]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 543430891238774, "steps": 30}
---

# 视频生成/文生视频/wan2.1基础文生视频001_1909164954489135106.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1909164954489135106.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（9 个）：
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `VAELoader`
- `KSampler` ★核心
- `EmptyHunyuanLatentVideo`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心

## 关键参数

- `seed` = `543430891238774`
- `steps` = `30`
- `cfg` = `6`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（9/9）

**有卡**：`CLIPTextEncode`、`CLIPLoader`、`VAEDecode`、`VHS_VideoCombine`、`VAELoader`、`KSampler`、`EmptyHunyuanLatentVideo`、`UNETLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、EmptyHunyuanLatentVideo、VHS_VideoCombine
