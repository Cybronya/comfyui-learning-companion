---
key: 视频生成/文生视频/Wan2.1文生视频工作流_1934444729025327105.json
name: Wan2.1文生视频工作流_1934444729025327105.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/1934444729025327105.json
hash: 9cf4cd92c831d687
coverage: 1
learned_at: 2026-10-15 22:43:27
nodes: [CLIPTextEncode, VAEDecode, CLIPLoader, VAELoader, KSampler, VHS_VideoCombine, CLIPTextEncode, UNETLoader, EmptyHunyuanLatentVideo]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 162018917956784, "steps": 30}
---

# 视频生成/文生视频/Wan2.1文生视频工作流_1934444729025327105.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1934444729025327105.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（9 个）：
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `CLIPLoader`
- `VAELoader`
- `KSampler` ★核心
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `EmptyHunyuanLatentVideo`

## 关键参数

- `seed` = `162018917956784`
- `steps` = `30`
- `cfg` = `6`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（9/9）

**有卡**：`CLIPTextEncode`、`VAEDecode`、`CLIPLoader`、`VAELoader`、`KSampler`、`VHS_VideoCombine`、`UNETLoader`、`EmptyHunyuanLatentVideo`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、EmptyHunyuanLatentVideo、VHS_VideoCombine
