---
key: 视频生成/图生视频/🐳SVI2.0PRO长视频生成 图生视频 KJ优化无限对接版 25-12-29🦋_2005505528635817986.json
name: 🐳SVI2.0PRO长视频生成 图生视频 KJ优化无限对接版 25-12-29🦋_2005505528635817986.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/🐳SVI2.0PRO长视频生成 图生视频 KJ优化无限对接版 25-12-29🦋_2005505528635817986.json
hash: 676a49a923ec33a9
coverage: 0.548387
learned_at: 2026-10-15 22:33:57
nodes: [SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, CLIPTextEncode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, KSamplerAdvanced, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, KSamplerAdvanced, SetNode, DiffusionModelLoaderKJ, DiffusionModelLoaderKJ, SetNode, SetNode, CLIPLoader, VAELoader, GetNode, GetNode, SetNode, SetNode, SetNode, ImageResizeKJv2, VAEEncode, SetNode, INTConstant, INTConstant, SetNode, GetNode, GetNode, CLIPTextEncode, CLIPTextEncode, GetNode, KSamplerAdvanced, KSamplerAdvanced, VAEDecode, GetNode, GetNode, KSamplerAdvanced, GetNode, GetNode, GetNode, CLIPTextEncode, CLIPTextEncode, GetNode, WanImageToVideoSVIPro, KSamplerAdvanced, VAEDecode, VHS_VideoCombine, CLIPTextEncode, GetNode, GetNode, WanImageToVideoSVIPro, KSamplerAdvanced, GetNode, GetNode, VAEDecode, GetNode, VHS_VideoCombine, CLIPTextEncode, ImageBatchExtendWithOverlap, ImageBatchExtendWithOverlap, WanImageToVideoSVIPro, VHS_VideoCombine, KSamplerAdvanced, KSamplerAdvanced, WanImageToVideoSVIPro, CLIPTextEncode, ImageBatchExtendWithOverlap, GetNode, GetNode, VAEDecode, GetNode, GetNode, CLIPTextEncode, VHS_VideoCombine, GetNode, GetNode, CLIPTextEncode, KSamplerAdvanced, VAEDecode, ImageBatchExtendWithOverlap, WanImageToVideoSVIPro, KSamplerAdvanced, VHS_VideoCombine, CLIPTextEncode, CLIPTextEncode, GetNode, WanImageToVideoSVIPro, GetNode, GetNode, GetNode, KSamplerAdvanced, GetNode, VAEDecode, VHS_VideoCombine, ImpactInt, ImpactInt, Note Plus (mtb), MarkdownNote, ImageBatchExtendWithOverlap, LoadImage, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, GetNode]
patterns: []
missing: []
parameters: {"cfg": 14, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/🐳SVI2.0PRO长视频生成 图生视频 KJ优化无限对接版 25-12-29🦋_2005505528635817986.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2005505528635817986.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（124 个）：
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `KSamplerAdvanced` ★核心
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `KSamplerAdvanced` ★核心
- `SetNode`
- `DiffusionModelLoaderKJ`
- `DiffusionModelLoaderKJ`
- `SetNode`
- `SetNode`
- `CLIPLoader`
- `VAELoader`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `ImageResizeKJv2`
- `VAEEncode` ★核心
- `SetNode`
- `INTConstant`
- `INTConstant`
- `SetNode`
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `GetNode`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `GetNode`
- `GetNode`
- `KSamplerAdvanced` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `GetNode`
- `WanImageToVideoSVIPro`
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心
- `GetNode`
- `GetNode`
- `WanImageToVideoSVIPro`
- `KSamplerAdvanced` ★核心
- `GetNode`
- `GetNode`
- `VAEDecode` ★核心
- `GetNode`
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心
- `ImageBatchExtendWithOverlap`
- `ImageBatchExtendWithOverlap`
- `WanImageToVideoSVIPro`
- `VHS_VideoCombine`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `WanImageToVideoSVIPro`
- `CLIPTextEncode` ★核心
- `ImageBatchExtendWithOverlap`
- `GetNode`
- `GetNode`
- `VAEDecode` ★核心
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `ImageBatchExtendWithOverlap`
- `WanImageToVideoSVIPro`
- `KSamplerAdvanced` ★核心
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `GetNode`
- `WanImageToVideoSVIPro`
- `GetNode`
- `GetNode`
- `GetNode`
- `KSamplerAdvanced` ★核心
- `GetNode`
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `ImpactInt`
- `ImpactInt`
- `Note Plus (mtb)`
- `MarkdownNote`
- `ImageBatchExtendWithOverlap`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `GetNode`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `14`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **55%**（68/124）

**有卡**：`CLIPTextEncode`、`KSamplerAdvanced`、`DiffusionModelLoaderKJ`、`CLIPLoader`、`VAELoader`、`ImageResizeKJv2`、`VAEEncode`、`INTConstant`、`VAEDecode`、`WanImageToVideoSVIPro`、`VHS_VideoCombine`、`ImageBatchExtendWithOverlap`、`ImpactInt`、`Note Plus (mtb)`、`LoadImage`、`LoraLoaderModelOnly`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、KSamplerAdvanced、VAEEncode
