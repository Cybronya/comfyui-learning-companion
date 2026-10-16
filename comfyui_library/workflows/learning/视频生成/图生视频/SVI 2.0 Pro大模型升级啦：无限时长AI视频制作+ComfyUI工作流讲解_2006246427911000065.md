---
key: 视频生成/图生视频/SVI 2.0 Pro大模型升级啦：无限时长AI视频制作+ComfyUI工作流讲解_2006246427911000065.json
name: SVI 2.0 Pro大模型升级啦：无限时长AI视频制作+ComfyUI工作流讲解_2006246427911000065.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2006246427911000065.json
hash: 1ed79f4a09cace16
coverage: 0.577586
learned_at: 2026-10-15 22:34:01
nodes: [SetNode, SetNode, GetNode, GetNode, CLIPTextEncode, GetNode, VAEDecode, VAEDecode, VAEEncode, GetNode, GetNode, GetNode, GetNode, WanImageToVideoSVIPro, GetNode, WanImageToVideoSVIPro, CLIPTextEncode, GetNode, VAEDecode, GetNode, GetNode, GetNode, GetNode, WanImageToVideoSVIPro, GetNode, VAEDecode, GetNode, GetNode, GetNode, WanImageToVideoSVIPro, GetNode, CLIPTextEncode, GetNode, VAEDecode, GetNode, GetNode, WanImageToVideoSVIPro, GetNode, CLIPTextEncode, GetNode, CLIPTextEncode, GetNode, VAEDecode, GetNode, GetNode, KSamplerAdvanced, ImageBatchExtendWithOverlap, GetNode, WanImageToVideoSVIPro, ImageBatchExtendWithOverlap, KSamplerAdvanced, ImageBatchExtendWithOverlap, ImageBatchExtendWithOverlap, KSamplerAdvanced, LoraLoaderModelOnly, KSamplerAdvanced, KSamplerAdvanced, KSamplerAdvanced, KSamplerAdvanced, SetNode, SetNode, INTConstant, INTConstant, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, ImageBatchExtendWithOverlap, CLIPTextEncode, CLIPTextEncode, CLIPTextEncode, SetNode, VHS_VideoCombine, VHS_VideoCombine, KSamplerAdvanced, KSamplerAdvanced, KSamplerAdvanced, KSamplerAdvanced, LoraLoaderModelOnly, SetNode, VHS_VideoCombine, VHS_VideoCombine, LoraLoaderModelOnly, LoraLoaderModelOnly, DiffusionModelLoaderKJ, DiffusionModelLoaderKJ, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, LoadImage, CLIPTextEncode, VHS_VideoCombine, VHS_VideoCombine, CLIPTextEncode, CLIPTextEncode, CLIPTextEncode, ImageResizeKJv2, CLIPLoader, VAELoader, KSamplerAdvanced, GetNode, GetNode, GetNode, GetNode, VHS_VideoCombine, GetNode, SetNode, Label (rgthree), Label (rgthree)]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "fixed"}
---

# 视频生成/图生视频/SVI 2.0 Pro大模型升级啦：无限时长AI视频制作+ComfyUI工作流讲解_2006246427911000065.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2006246427911000065.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（116 个）：
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `GetNode`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `VAEEncode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanImageToVideoSVIPro`
- `GetNode`
- `WanImageToVideoSVIPro`
- `CLIPTextEncode` ★核心
- `GetNode`
- `VAEDecode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanImageToVideoSVIPro`
- `GetNode`
- `VAEDecode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `WanImageToVideoSVIPro`
- `GetNode`
- `CLIPTextEncode` ★核心
- `GetNode`
- `VAEDecode` ★核心
- `GetNode`
- `GetNode`
- `WanImageToVideoSVIPro`
- `GetNode`
- `CLIPTextEncode` ★核心
- `GetNode`
- `CLIPTextEncode` ★核心
- `GetNode`
- `VAEDecode` ★核心
- `GetNode`
- `GetNode`
- `KSamplerAdvanced` ★核心
- `ImageBatchExtendWithOverlap`
- `GetNode`
- `WanImageToVideoSVIPro`
- `ImageBatchExtendWithOverlap`
- `KSamplerAdvanced` ★核心
- `ImageBatchExtendWithOverlap`
- `ImageBatchExtendWithOverlap`
- `KSamplerAdvanced` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `SetNode`
- `SetNode`
- `INTConstant`
- `INTConstant`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageBatchExtendWithOverlap`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `SetNode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `DiffusionModelLoaderKJ`
- `DiffusionModelLoaderKJ`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ImageResizeKJv2`
- `CLIPLoader`
- `VAELoader`
- `KSamplerAdvanced` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `GetNode`
- `SetNode`
- `Label (rgthree)`
- `Label (rgthree)`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **58%**（67/116）

**有卡**：`CLIPTextEncode`、`VAEDecode`、`VAEEncode`、`WanImageToVideoSVIPro`、`KSamplerAdvanced`、`ImageBatchExtendWithOverlap`、`LoraLoaderModelOnly`、`INTConstant`、`VHS_VideoCombine`、`DiffusionModelLoaderKJ`、`LoadImage`、`ImageResizeKJv2`、`CLIPLoader`、`VAELoader`、`Label (rgthree)`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、KSamplerAdvanced、VAEEncode
