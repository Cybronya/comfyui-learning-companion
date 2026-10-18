---
key: 视频生成/图生视频/图生视频-SVI 2.0 Pro-无限长度视频生成_2005789262182313985.json
name: 图生视频-SVI 2.0 Pro-无限长度视频生成_2005789262182313985.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/图生视频-SVI 2.0 Pro-无限长度视频生成_2005789262182313985.json
hash: deacaaa1f8985118
coverage: 0.666667
learned_at: 2026-10-15 22:33:58
nodes: [SetNode, WanVideoImageResizeToClosest, SetNode, VAEEncode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, WanImageToVideoSVIPro, VAELoader, CLIPLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, SetNode, LoadImage, CR Text, DiffusionModelLoaderKJ, DiffusionModelLoaderKJ, DiffusionModelLoaderKJ, LoraLoaderModelOnly, LoraLoaderModelOnly, DiffusionModelLoaderKJ, SetNode, KSamplerAdvanced, GetNode, CLIPTextEncode, CLIPTextEncode, GetNode, KSamplerAdvanced, WanImageToVideoSVIPro, GetNode, GetNode, KSamplerAdvanced, VHS_VideoCombine, VAEDecode, VAEDecode, ImageBatchExtendWithOverlap, KSamplerAdvanced, VHS_VideoCombine, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "beta", "sampler_name": 1, "scheduler": "sa_solver", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/图生视频-SVI 2.0 Pro-无限长度视频生成_2005789262182313985.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2005789262182313985.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（42 个）：
- `SetNode`
- `WanVideoImageResizeToClosest`
- `SetNode`
- `VAEEncode` ★核心
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanImageToVideoSVIPro`
- `VAELoader`
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `LoadImage`
- `CR Text`
- `DiffusionModelLoaderKJ`
- `DiffusionModelLoaderKJ`
- `DiffusionModelLoaderKJ`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `DiffusionModelLoaderKJ`
- `SetNode`
- `KSamplerAdvanced` ★核心
- `GetNode`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `GetNode`
- `KSamplerAdvanced` ★核心
- `WanImageToVideoSVIPro`
- `GetNode`
- `GetNode`
- `KSamplerAdvanced` ★核心
- `VHS_VideoCombine`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `ImageBatchExtendWithOverlap`
- `KSamplerAdvanced` ★核心
- `VHS_VideoCombine`
- `VHS_VideoCombine`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `sa_solver`
- `denoise` = `beta`

## 知识

覆盖率 **67%**（28/42）

**有卡**：`WanVideoImageResizeToClosest`、`VAEEncode`、`WanImageToVideoSVIPro`、`VAELoader`、`CLIPLoader`、`LoraLoaderModelOnly`、`LoadImage`、`CR Text`、`DiffusionModelLoaderKJ`、`KSamplerAdvanced`、`CLIPTextEncode`、`VHS_VideoCombine`、`VAEDecode`、`ImageBatchExtendWithOverlap`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、KSamplerAdvanced、VAEEncode
