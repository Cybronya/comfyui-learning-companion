---
key: 视频生成/图生视频/【Supermate】优化WAN2.2-SVI 2.0-全自动-单图文字5段采样长视频_2006611754909962242.json
name: 【Supermate】优化WAN2.2-SVI 2.0-全自动-单图文字5段采样长视频_2006611754909962242.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/【Supermate】优化WAN2.2-SVI 2.0-全自动-单图文字5段采样长视频_2006611754909962242.json
hash: 0e6a76d4d73f0e6e
coverage: 0.468085
learned_at: 2026-10-15 22:34:02
nodes: [CLIPTextEncode, PathchSageAttentionKJ, PathchSageAttentionKJ, ModelPatchTorchSettings, ModelPatchTorchSettings, LoraLoaderModelOnly, VAELoader, ImageResizeKJv2, VAEEncode, GetNode, GetNode, GetNode, VAEDecode, GetNode, CLIPTextEncode, WanImageToVideoSVIPro, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, VAEDecode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, CLIPTextEncode, GetNode, GetNode, GetNode, GetNode, WanImageToVideoSVIPro, VAEDecode, ImageBatchExtendWithOverlap, CLIPTextEncode, GetNode, GetNode, GetNode, GetNode, WanImageToVideoSVIPro, WanImageToVideoSVIPro, SetNode, GetNode, SetNode, CLIPLoader, SetNode, GetNode, KSamplerAdvanced, KSamplerAdvanced, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, UNETLoader, LoraLoaderModelOnly, UNETLoader, ImageBatchExtendWithOverlap, KSamplerAdvanced, KSamplerAdvanced, KSamplerAdvanced, UNETLoader, GetNode, KSamplerAdvanced, KSamplerAdvanced, KSamplerAdvanced, KSamplerAdvanced, KSamplerAdvanced, CLIPTextEncode, GetNode, CR Text Concatenate, SomethingToString, PreviewAny, Qwen3_VQA, Note, Split String, MemoryCleaner, CLIPTextEncode, GetNode, GetNode, CLIPTextEncode, GetNode, CLIPTextEncode, GetNode, CLIPTextEncode, CLIPTextEncode, GetNode, WanImageToVideoSVIPro, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, ShowText|pysssss, ShowText|pysssss, ShowText|pysssss, ShowText|pysssss, SetNode, SetNode, SetNode, SetNode, SetNode, INTConstant, INTConstant, VHS_VideoCombine, VHS_VideoCombine, ImageBatchExtendWithOverlap, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, CR Prompt Text, LoadImage, VAEDecode, GetNode, VAEDecode, ImageBatchExtendWithOverlap, GetNode, SetNode, VHS_VideoCombine, CR Prompt Text, Note, Fast Groups Bypasser (rgthree), SetNode, SetNode, INTConstant, INTConstant, INTConstant, SetNode, SetNode, SetNode, SetNode, SetNode, ShowText|pysssss]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 2.5, "scheduler": "euler", "seed": "enable", "steps": "fixed"}
---

# 视频生成/图生视频/【Supermate】优化WAN2.2-SVI 2.0-全自动-单图文字5段采样长视频_2006611754909962242.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2006611754909962242.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（141 个）：
- `CLIPTextEncode` ★核心
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `ModelPatchTorchSettings`
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `ImageResizeKJv2`
- `VAEEncode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `VAEDecode` ★核心
- `GetNode`
- `CLIPTextEncode` ★核心
- `WanImageToVideoSVIPro`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VAEDecode` ★核心
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
- `WanImageToVideoSVIPro`
- `VAEDecode` ★核心
- `ImageBatchExtendWithOverlap`
- `CLIPTextEncode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanImageToVideoSVIPro`
- `WanImageToVideoSVIPro`
- `SetNode`
- `GetNode`
- `SetNode`
- `CLIPLoader`
- `SetNode`
- `GetNode`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `ImageBatchExtendWithOverlap`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `UNETLoader` ★核心
- `GetNode`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `GetNode`
- `CR Text Concatenate`
- `SomethingToString`
- `PreviewAny`
- `Qwen3_VQA`
- `Note`
- `Split String`
- `MemoryCleaner`
- `CLIPTextEncode` ★核心
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `GetNode`
- `CLIPTextEncode` ★核心
- `GetNode`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `GetNode`
- `WanImageToVideoSVIPro`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ShowText|pysssss`
- `ShowText|pysssss`
- `ShowText|pysssss`
- `ShowText|pysssss`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `INTConstant`
- `INTConstant`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `ImageBatchExtendWithOverlap`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `CR Prompt Text`
- `LoadImage`
- `VAEDecode` ★核心
- `GetNode`
- `VAEDecode` ★核心
- `ImageBatchExtendWithOverlap`
- `GetNode`
- `SetNode`
- `VHS_VideoCombine`
- `CR Prompt Text`
- `Note`
- `Fast Groups Bypasser (rgthree)`
- `SetNode`
- `SetNode`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `ShowText|pysssss`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `2.5`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **47%**（66/141）

**有卡**：`CLIPTextEncode`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`LoraLoaderModelOnly`、`VAELoader`、`ImageResizeKJv2`、`VAEEncode`、`VAEDecode`、`WanImageToVideoSVIPro`、`ImageBatchExtendWithOverlap`、`CLIPLoader`、`KSamplerAdvanced`、`UNETLoader`、`CR Text Concatenate`、`SomethingToString`、`Qwen3_VQA`、`Split String`、`MemoryCleaner`、`INTConstant`、`VHS_VideoCombine`、`CR Prompt Text`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
