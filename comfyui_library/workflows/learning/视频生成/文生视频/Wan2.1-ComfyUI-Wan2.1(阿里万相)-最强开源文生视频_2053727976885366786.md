---
key: 视频生成/文生视频/Wan2.1-ComfyUI-Wan2.1(阿里万相)-最强开源文生视频_2053727976885366786.json
name: Wan2.1-ComfyUI-Wan2.1(阿里万相)-最强开源文生视频_2053727976885366786
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.1-ComfyUI-Wan2.1(阿里万相)-最强开源文生视频_2053727976885366786.json
hash: 962371a381059b43
coverage: 0.666667
learned_at: 2026-10-11 19:49:43
nodes: [VAEDecodeTiled, Fast Groups Bypasser (rgthree), VHS_VideoCombine, CLIPTextEncode, VAELoader, EmptyHunyuanLatentVideo, Primitive integer [Crystools], Primitive integer [Crystools], Primitive integer [Crystools], Primitive integer [Crystools], CLIPLoader, KSampler, CM_IntToFloat, CLIPTextEncode, UNETLoader]
patterns: []
missing: [Primitive integer [Crystools], Primitive integer [Crystools], Primitive integer [Crystools], Primitive integer [Crystools]]
problems: [[high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 6, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 581159692480175, "steps": 30}
discoveries: [次要节点 `Primitive integer [Crystools]` 知识库中没有该节点类型的任何知识, 次要节点 `Primitive integer [Crystools]` 知识库中没有该节点类型的任何知识, 次要节点 `Primitive integer [Crystools]` 知识库中没有该节点类型的任何知识, 次要节点 `Primitive integer [Crystools]` 知识库中没有该节点类型的任何知识, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 视频生成/文生视频/Wan2.1-ComfyUI-Wan2.1(阿里万相)-最强开源文生视频_2053727976885366786.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.1-ComfyUI-Wan2.1(阿里万相)-最强开源文生视频_2053727976885366786.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（15 个）：
- `VAEDecodeTiled` ★核心
- `Fast Groups Bypasser (rgthree)`
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `EmptyHunyuanLatentVideo`
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`
- `CLIPLoader`
- `KSampler` ★核心
- `CM_IntToFloat`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心

## 关键参数

- `seed` = `581159692480175`
- `steps` = `30`
- `cfg` = `6`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **67%**（10/15）

**有卡**：`VAEDecodeTiled`、`VHS_VideoCombine`、`CLIPTextEncode`、`VAELoader`、`EmptyHunyuanLatentVideo`、`CLIPLoader`、`KSampler`、`CM_IntToFloat`、`UNETLoader`

**缺卡**（4）：`Primitive integer [Crystools]`、`Primitive integer [Crystools]`、`Primitive integer [Crystools]`、`Primitive integer [Crystools]`

**用到的条目**：KSampler、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、VAEDecodeTiled、EmptyHunyuanLatentVideo、CM_IntToFloat

## 参数体检

发现 1 个问题：
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- 次要节点 `Primitive integer [Crystools]` 知识库中没有该节点类型的任何知识
- 次要节点 `Primitive integer [Crystools]` 知识库中没有该节点类型的任何知识
- 次要节点 `Primitive integer [Crystools]` 知识库中没有该节点类型的任何知识
- 次要节点 `Primitive integer [Crystools]` 知识库中没有该节点类型的任何知识
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换
