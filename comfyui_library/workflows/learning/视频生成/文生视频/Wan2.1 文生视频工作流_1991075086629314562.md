---
key: 视频生成/文生视频/Wan2.1 文生视频工作流_1991075086629314562.json
name: Wan2.1 文生视频工作流_1991075086629314562
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.1 文生视频工作流_1991075086629314562.json
hash: 5882c5dbc06ea33d
coverage: 1
learned_at: 2026-10-15 22:47:08
nodes: [Primitive integer [Crystools], VAELoader, UNETLoader, CLIPLoader, CLIPTextEncode, EmptyHunyuanLatentVideo, VAEDecodeTiled, KSampler, VHS_VideoCombine, Primitive integer [Crystools], Primitive integer [Crystools], CM_IntToFloat, CLIPTextEncode, Primitive integer [Crystools]]
patterns: []
missing: []
problems: [[high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 6, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 7, "steps": 30}
discoveries: [[high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 视频生成/文生视频/Wan2.1 文生视频工作流_1991075086629314562.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.1 文生视频工作流_1991075086629314562.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（14 个）：
- `Primitive integer [Crystools]`
- `VAELoader`
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `EmptyHunyuanLatentVideo`
- `VAEDecodeTiled` ★核心
- `KSampler` ★核心
- `VHS_VideoCombine`
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`
- `CM_IntToFloat`
- `CLIPTextEncode` ★核心
- `Primitive integer [Crystools]`

## 关键参数

- `seed` = `7`
- `steps` = `30`
- `cfg` = `6`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（14/14）

**有卡**：`Primitive integer [Crystools]`、`VAELoader`、`UNETLoader`、`CLIPLoader`、`CLIPTextEncode`、`EmptyHunyuanLatentVideo`、`VAEDecodeTiled`、`KSampler`、`VHS_VideoCombine`、`CM_IntToFloat`

**用到的条目**：KSampler、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、VAEDecodeTiled、EmptyHunyuanLatentVideo、CM_IntToFloat

## 参数体检

发现 1 个问题：
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换
