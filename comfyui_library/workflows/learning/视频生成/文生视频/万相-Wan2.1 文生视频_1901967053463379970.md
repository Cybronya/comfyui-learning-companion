---
key: 视频生成/文生视频/万相-Wan2.1 文生视频_1901967053463379970.json
name: 万相-Wan2.1 文生视频_1901967053463379970.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/万相-Wan2.1 文生视频_1901967053463379970.json
hash: d5c54bdbbdb28b6f
coverage: 1
learned_at: 2026-10-15 22:43:21
nodes: [ModelSamplingSD3, KSampler, VAELoader, VAEDecode, VHS_VideoCombine, CLIPLoader, CLIPTextEncode, CLIPTextEncode, EmptyHunyuanLatentVideo, UNETLoader]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 55670793340509, "steps": 20}
---

# 视频生成/文生视频/万相-Wan2.1 文生视频_1901967053463379970.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1901967053463379970.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（10 个）：
- `ModelSamplingSD3`
- `KSampler` ★核心
- `VAELoader`
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `EmptyHunyuanLatentVideo`
- `UNETLoader` ★核心

## 关键参数

- `seed` = `55670793340509`
- `steps` = `20`
- `cfg` = `6`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（10/10）

**有卡**：`ModelSamplingSD3`、`KSampler`、`VAELoader`、`VAEDecode`、`VHS_VideoCombine`、`CLIPLoader`、`CLIPTextEncode`、`EmptyHunyuanLatentVideo`、`UNETLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、EmptyHunyuanLatentVideo、ModelSamplingSD3
