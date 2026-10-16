---
key: 视频生成/文生视频/Wan2.1 T2V 文生视频_1930553645908021250.json
name: Wan2.1 T2V 文生视频_1930553645908021250.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/1930553645908021250.json
hash: babbaa990de6ca6d
coverage: 1
learned_at: 2026-10-15 22:43:26
nodes: [CLIPLoader, UNETLoader, CLIPTextEncode, CLIPTextEncode, KSampler, VAELoader, VAEDecode, VHS_VideoCombine, EmptyHunyuanLatentVideo]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 863583319227156, "steps": 30}
---

# 视频生成/文生视频/Wan2.1 T2V 文生视频_1930553645908021250.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1930553645908021250.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（9 个）：
- `CLIPLoader`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `VAELoader`
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `EmptyHunyuanLatentVideo`

## 关键参数

- `seed` = `863583319227156`
- `steps` = `30`
- `cfg` = `6`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（9/9）

**有卡**：`CLIPLoader`、`UNETLoader`、`CLIPTextEncode`、`KSampler`、`VAELoader`、`VAEDecode`、`VHS_VideoCombine`、`EmptyHunyuanLatentVideo`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、EmptyHunyuanLatentVideo、VHS_VideoCombine
