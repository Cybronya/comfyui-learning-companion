---
key: 图片生成/图生图/SVI 2.0长视频制作，1分钟以上视频制作_2005595717286723586.json
name: SVI 2.0长视频制作，1分钟以上视频制作_2005595717286723586
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/SVI 2.0长视频制作，1分钟以上视频制作_2005595717286723586.json
hash: 7fa4ad3799370c50
coverage: 0.663462
learned_at: 2026-10-23 11:24:14
nodes: [VAEDecode, GetNode, VAEDecode, GetNode, VAEDecode, GetNode, GetNode, ImageBatchExtendWithOverlap, KSamplerAdvanced, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, KSamplerAdvanced, Text, Text, Text, ImageResizeKJv2, VAEEncode, Int, Int, LoadImage, Text, Text, RHHiddenNodes, GetNode, CLIPTextEncode, CLIPTextEncode, WanImageToVideoSVIPro, WanImageToVideoSVIPro, CLIPTextEncode, GetNode, GetNode, CLIPTextEncode, WanImageToVideoSVIPro, CLIPTextEncode, CLIPTextEncode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, KSamplerAdvanced, GetNode, GetNode, GetNode, RHHiddenNodes, WanImageToVideoSVIPro, GetNode, GetNode, GetNode, CLIPTextEncode, GetNode, CLIPTextEncode, KSamplerAdvanced, KSamplerAdvanced, WanImageToVideoSVIPro, GetNode, CLIPTextEncode, GetNode, GetNode, CLIPTextEncode, CLIPTextEncode, CLIPTextEncode, GetNode, WanImageToVideoSVIPro, GetNode, GetNode, KSamplerAdvanced, KSamplerAdvanced, GetNode, GetNode, KSamplerAdvanced, KSamplerAdvanced, SetNode, SetNode, INTConstant, INTConstant, KSamplerAdvanced, KSamplerAdvanced, ImageBatchExtendWithOverlap, VAEDecode, ImageBatchExtendWithOverlap, VAEDecode, GetNode, ImageBatchExtendWithOverlap, ImageBatchExtendWithOverlap, VAEDecode, GetNode, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, SetNode, CLIPLoader, VAELoader, SetNode, SetNode, KSamplerAdvanced, Text]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "fixed"}
---

# 图片生成/图生图/SVI 2.0长视频制作，1分钟以上视频制作_2005595717286723586.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/SVI 2.0长视频制作，1分钟以上视频制作_2005595717286723586.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（104 个）：
- `VAEDecode` ★核心
- `GetNode`
- `VAEDecode` ★核心
- `GetNode`
- `VAEDecode` ★核心
- `GetNode`
- `GetNode`
- `ImageBatchExtendWithOverlap`
- `KSamplerAdvanced` ★核心
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `KSamplerAdvanced` ★核心
- `Text`
- `Text`
- `Text`
- `ImageResizeKJv2`
- `VAEEncode` ★核心
- `Int`
- `Int`
- `LoadImage`
- `Text`
- `Text`
- `RHHiddenNodes`
- `GetNode`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `WanImageToVideoSVIPro`
- `WanImageToVideoSVIPro`
- `CLIPTextEncode` ★核心
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `WanImageToVideoSVIPro`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `KSamplerAdvanced` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `RHHiddenNodes`
- `WanImageToVideoSVIPro`
- `GetNode`
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `GetNode`
- `CLIPTextEncode` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `WanImageToVideoSVIPro`
- `GetNode`
- `CLIPTextEncode` ★核心
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `GetNode`
- `WanImageToVideoSVIPro`
- `GetNode`
- `GetNode`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `GetNode`
- `GetNode`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `SetNode`
- `SetNode`
- `INTConstant`
- `INTConstant`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `ImageBatchExtendWithOverlap`
- `VAEDecode` ★核心
- `ImageBatchExtendWithOverlap`
- `VAEDecode` ★核心
- `GetNode`
- `ImageBatchExtendWithOverlap`
- `ImageBatchExtendWithOverlap`
- `VAEDecode` ★核心
- `GetNode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `SetNode`
- `CLIPLoader`
- `VAELoader`
- `SetNode`
- `SetNode`
- `KSamplerAdvanced` ★核心
- `Text`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **66%**（69/104）

**有卡**：`VAEDecode`、`ImageBatchExtendWithOverlap`、`KSamplerAdvanced`、`VHS_VideoCombine`、`Text`、`ImageResizeKJv2`、`VAEEncode`、`Int`、`LoadImage`、`RHHiddenNodes`、`CLIPTextEncode`、`WanImageToVideoSVIPro`、`INTConstant`、`CLIPLoader`、`VAELoader`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、KSamplerAdvanced、VAEEncode、ImageResizeKJv2
