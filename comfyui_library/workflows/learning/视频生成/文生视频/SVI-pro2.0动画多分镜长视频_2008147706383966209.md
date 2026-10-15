---
key: 视频生成/文生视频/SVI-pro2.0动画多分镜长视频_2008147706383966209.json
name: SVI-pro2.0动画多分镜长视频_2008147706383966209
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/SVI-pro2.0动画多分镜长视频_2008147706383966209.json
hash: bb09530c154146d3
coverage: 0.409091
learned_at: 2026-10-15 22:46:57
nodes: [PathchSageAttentionKJ, PathchSageAttentionKJ, ModelPatchTorchSettings, ModelPatchTorchSettings, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, GetNode, KSamplerAdvanced, GetNode, GetNode, GetNode, GetNode, KSamplerAdvanced, KSamplerAdvanced, KSamplerAdvanced, KSamplerAdvanced, KSamplerAdvanced, KSamplerAdvanced, KSamplerAdvanced, KSamplerAdvanced, GetNode, GetNode, KSamplerAdvanced, GetNode, WanImageToVideoSVIPro, GetNode, GetNode, VAEEncode, GetNode, GetNode, ImageResizeKJv2, GetNode, VAEEncode, GetNode, ImageResizeKJv2, GetNode, VAEEncode, GetNode, GetNode, ImageResizeKJv2, GetNode, VAEEncode, GetNode, GetNode, ImageResizeKJv2, GetNode, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, WanImageToVideoSVIPro, WanImageToVideoSVIPro, WanImageToVideoSVIPro, Fast Groups Bypasser (rgthree), Note, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, VAEDecode, SetNode, VAEDecode, SetNode, SetNode, VAEDecode, GetNode, GetNode, GetNode, GetNode, GetNode, ImageBatchExtendWithOverlap, ImageBatchExtendWithOverlap, ImageBatchExtendWithOverlap, ImageBatchExtendWithOverlap, GetNode, GetNode, VHS_VideoCombine, VHS_VideoCombine, GetNode, ImageResizeKJv2, CLIPTextEncode, GetNode, SetNode, SetNode, SetNode, INTConstant, SetNode, INTConstant, INTConstant, SetNode, WanImageToVideoSVIPro, CLIPTextEncode, CLIPTextEncode, GetNode, GetNode, GetNode, GetNode, CLIPTextEncode, GetNode, GetNode, GetNode, GetNode, CLIPTextEncode, CLIPTextEncode, GetNode, GetNode, GetNode, GetNode, CLIPTextEncode, CLIPTextEncode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, VHS_VideoCombine, SetNode, GetNode, GetNode, KSamplerAdvanced, KSamplerAdvanced, WanImageToVideoSVIPro, VAEDecode, GetNode, GetNode, CLIPTextEncode, CLIPTextEncode, GetNode, GetNode, GetNode, VAEDecode, ImageBatchExtendWithOverlap, SetNode, GetNode, INTConstant, INTConstant, SetNode, SetNode, VHS_VideoCombine, easy indexAnything, easy indexAnything, easy indexAnything, easy indexAnything, easy indexAnything, SetNode, SetNode, SetNode, SetNode, SetNode, CLIPTextEncode, CLIPTextEncode, UNETLoader, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPLoader, VAELoader, VHS_VideoCombine, PlaySound|pysssss, Note, SetNode, SetNode, UNETLoader, SetNode, GetNode, PainterI2V, GetNode, PainterI2V, VAEDecode, PainterI2V, GetNode, PainterI2V, GetNode, PainterI2V, GetNode, PainterI2V, GetNode, GetNode, VHS_VideoCombine, GetNode, easy float, easy float, easy float, easy float, easy float, LoadImage, LoadImage, LoadImage, LoadImage, GetNode, LoadImage, SetNode, LoadImage, SetNode, VAEEncode, VAEEncode, GetNode, GetNode, GetNode, ImageResizeKJv2, GetNode, SetNode, GetNode, GetNode, GetNode, SetNode, SetNode, GetNode, easy promptList]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 2.5, "scheduler": "euler", "seed": "enable", "steps": "fixed"}
---

# 视频生成/文生视频/SVI-pro2.0动画多分镜长视频_2008147706383966209.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/SVI-pro2.0动画多分镜长视频_2008147706383966209.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（242 个）：
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `ModelPatchTorchSettings`
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
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `KSamplerAdvanced` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `GetNode`
- `GetNode`
- `KSamplerAdvanced` ★核心
- `GetNode`
- `WanImageToVideoSVIPro`
- `GetNode`
- `GetNode`
- `VAEEncode` ★核心
- `GetNode`
- `GetNode`
- `ImageResizeKJv2`
- `GetNode`
- `VAEEncode` ★核心
- `GetNode`
- `ImageResizeKJv2`
- `GetNode`
- `VAEEncode` ★核心
- `GetNode`
- `GetNode`
- `ImageResizeKJv2`
- `GetNode`
- `VAEEncode` ★核心
- `GetNode`
- `GetNode`
- `ImageResizeKJv2`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanImageToVideoSVIPro`
- `WanImageToVideoSVIPro`
- `WanImageToVideoSVIPro`
- `Fast Groups Bypasser (rgthree)`
- `Note`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `VAEDecode` ★核心
- `SetNode`
- `VAEDecode` ★核心
- `SetNode`
- `SetNode`
- `VAEDecode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageBatchExtendWithOverlap`
- `ImageBatchExtendWithOverlap`
- `ImageBatchExtendWithOverlap`
- `ImageBatchExtendWithOverlap`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `GetNode`
- `ImageResizeKJv2`
- `CLIPTextEncode` ★核心
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `INTConstant`
- `SetNode`
- `INTConstant`
- `INTConstant`
- `SetNode`
- `WanImageToVideoSVIPro`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `SetNode`
- `GetNode`
- `GetNode`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `WanImageToVideoSVIPro`
- `VAEDecode` ★核心
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `VAEDecode` ★核心
- `ImageBatchExtendWithOverlap`
- `SetNode`
- `GetNode`
- `INTConstant`
- `INTConstant`
- `SetNode`
- `SetNode`
- `VHS_VideoCombine`
- `easy indexAnything`
- `easy indexAnything`
- `easy indexAnything`
- `easy indexAnything`
- `easy indexAnything`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `VAELoader`
- `VHS_VideoCombine`
- `PlaySound|pysssss`
- `Note`
- `SetNode`
- `SetNode`
- `UNETLoader` ★核心
- `SetNode`
- `GetNode`
- `PainterI2V`
- `GetNode`
- `PainterI2V`
- `VAEDecode` ★核心
- `PainterI2V`
- `GetNode`
- `PainterI2V`
- `GetNode`
- `PainterI2V`
- `GetNode`
- `PainterI2V`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `GetNode`
- `easy float`
- `easy float`
- `easy float`
- `easy float`
- `easy float`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `GetNode`
- `LoadImage`
- `SetNode`
- `LoadImage`
- `SetNode`
- `VAEEncode` ★核心
- `VAEEncode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageResizeKJv2`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `easy promptList`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `2.5`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **41%**（99/242）

**有卡**：`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`KSamplerAdvanced`、`WanImageToVideoSVIPro`、`VAEEncode`、`ImageResizeKJv2`、`VAEDecode`、`ImageBatchExtendWithOverlap`、`VHS_VideoCombine`、`CLIPTextEncode`、`INTConstant`、`easy indexAnything`、`UNETLoader`、`LoraLoaderModelOnly`、`CLIPLoader`、`VAELoader`、`PlaySound|pysssss`、`PainterI2V`、`easy float`、`LoadImage`、`easy promptList`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
