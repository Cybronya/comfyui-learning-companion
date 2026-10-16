---
key: 视频生成/文生视频/万相wan2.1 文生视频 官方版工作流_1895270735554412545.json
name: 万相wan2.1 文生视频 官方版工作流_1895270735554412545.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/1895270735554412545.json
hash: a9c92b22623441ee
coverage: 1
learned_at: 2026-10-15 22:43:20
nodes: [CLIPTextEncode, KSampler, CLIPTextEncode, CLIPLoader, TextInput_, VAELoader, VAEDecode, VHS_VideoCombine, EmptyHunyuanLatentVideo, UNETLoader]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 119551802584214, "steps": 30}
---

# 视频生成/文生视频/万相wan2.1 文生视频 官方版工作流_1895270735554412545.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1895270735554412545.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（10 个）：
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `TextInput_`
- `VAELoader`
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `EmptyHunyuanLatentVideo`
- `UNETLoader` ★核心

## 关键参数

- `seed` = `119551802584214`
- `steps` = `30`
- `cfg` = `6`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（10/10）

**有卡**：`CLIPTextEncode`、`KSampler`、`CLIPLoader`、`TextInput_`、`VAELoader`、`VAEDecode`、`VHS_VideoCombine`、`EmptyHunyuanLatentVideo`、`UNETLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、EmptyHunyuanLatentVideo、TextInput_
