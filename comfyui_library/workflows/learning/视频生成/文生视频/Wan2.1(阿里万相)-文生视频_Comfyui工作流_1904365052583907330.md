---
key: 视频生成/文生视频/Wan2.1(阿里万相)-文生视频_Comfyui工作流_1904365052583907330.json
name: Wan2.1(阿里万相)-文生视频_Comfyui工作流_1904365052583907330.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/1904365052583907330.json
hash: b339e2739c7dbf8a
coverage: 1
learned_at: 2026-10-15 22:43:21
nodes: [VAEDecodeTiled, VHS_VideoCombine, KSampler, EmptyHunyuanLatentVideo, CM_IntToFloat, CLIPTextEncode, CLIPTextEncode, UNETLoader, CLIPLoader, VAELoader, Primitive integer [Crystools], Primitive integer [Crystools], Primitive integer [Crystools], Primitive integer [Crystools]]
patterns: []
missing: []
problems: [[high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 6, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 974533743485011, "steps": 30}
discoveries: [[high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 视频生成/文生视频/Wan2.1(阿里万相)-文生视频_Comfyui工作流_1904365052583907330.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1904365052583907330.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（14 个）：
- `VAEDecodeTiled` ★核心
- `VHS_VideoCombine`
- `KSampler` ★核心
- `EmptyHunyuanLatentVideo`
- `CM_IntToFloat`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`

## 关键参数

- `seed` = `974533743485011`
- `steps` = `30`
- `cfg` = `6`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（14/14）

**有卡**：`VAEDecodeTiled`、`VHS_VideoCombine`、`KSampler`、`EmptyHunyuanLatentVideo`、`CM_IntToFloat`、`CLIPTextEncode`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`Primitive integer [Crystools]`

**用到的条目**：KSampler、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、VAEDecodeTiled、EmptyHunyuanLatentVideo、CM_IntToFloat

## 参数体检

发现 1 个问题：
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换
