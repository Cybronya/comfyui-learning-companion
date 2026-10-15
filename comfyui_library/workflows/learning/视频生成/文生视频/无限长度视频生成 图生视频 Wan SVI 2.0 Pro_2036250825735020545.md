---
key: 视频生成/文生视频/无限长度视频生成 图生视频 Wan SVI 2.0 Pro_2036250825735020545.json
name: 无限长度视频生成 图生视频 Wan SVI 2.0 Pro_2036250825735020545
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/无限长度视频生成 图生视频 Wan SVI 2.0 Pro_2036250825735020545.json
hash: 6ff8a00825e45d8e
coverage: 0.631579
learned_at: 2026-10-15 22:48:46
nodes: [SetNode, GetNode, VAELoader, CLIPLoader, LoraLoaderModelOnly, SetNode, DiffusionModelLoaderKJ, GetNode, CLIPTextEncode, CLIPTextEncode, KSamplerAdvanced, WanImageToVideoSVIPro, GetNode, GetNode, VAEDecode, KSamplerAdvanced, SetNode, SetNode, LoraLoaderModelOnly, GetNode, VAEDecode, WanImageToVideoSVIPro, GetNode, KSamplerAdvanced, KSamplerAdvanced, GetNode, VHS_VideoCombine, VHS_VideoCombine, ImageBatchExtendWithOverlap, SetNode, GetNode, VAEEncode, GetNode, WanVideoImageResizeToClosest, DiffusionModelLoaderKJ, VHS_VideoCombine, LoadImage, CR Text]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "beta", "sampler_name": 1, "scheduler": "sa_solver", "seed": "disable", "steps": "fixed"}
---

# 视频生成/文生视频/无限长度视频生成 图生视频 Wan SVI 2.0 Pro_2036250825735020545.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/无限长度视频生成 图生视频 Wan SVI 2.0 Pro_2036250825735020545.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（38 个）：
- `SetNode`
- `GetNode`
- `VAELoader`
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `DiffusionModelLoaderKJ`
- `GetNode`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `KSamplerAdvanced` ★核心
- `WanImageToVideoSVIPro`
- `GetNode`
- `GetNode`
- `VAEDecode` ★核心
- `KSamplerAdvanced` ★核心
- `SetNode`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `GetNode`
- `VAEDecode` ★核心
- `WanImageToVideoSVIPro`
- `GetNode`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `GetNode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `ImageBatchExtendWithOverlap`
- `SetNode`
- `GetNode`
- `VAEEncode` ★核心
- `GetNode`
- `WanVideoImageResizeToClosest`
- `DiffusionModelLoaderKJ`
- `VHS_VideoCombine`
- `LoadImage`
- `CR Text`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `sa_solver`
- `denoise` = `beta`

## 知识

覆盖率 **63%**（24/38）

**有卡**：`VAELoader`、`CLIPLoader`、`LoraLoaderModelOnly`、`DiffusionModelLoaderKJ`、`CLIPTextEncode`、`KSamplerAdvanced`、`WanImageToVideoSVIPro`、`VAEDecode`、`VHS_VideoCombine`、`ImageBatchExtendWithOverlap`、`VAEEncode`、`WanVideoImageResizeToClosest`、`LoadImage`、`CR Text`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、KSamplerAdvanced、VAEEncode
