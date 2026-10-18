---
key: 视频生成/图生视频/SVI 2.0超强长视频生成-10秒版_2008158274641731586.json
name: SVI 2.0超强长视频生成-10秒版_2008158274641731586.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/SVI 2.0超强长视频生成-10秒版_2008158274641731586.json
hash: 7ac538ef6121467f
coverage: 0.5
learned_at: 2026-10-15 22:34:06
nodes: [CLIPTextEncode, PathchSageAttentionKJ, PathchSageAttentionKJ, ModelPatchTorchSettings, ModelPatchTorchSettings, LoraLoaderModelOnly, Fast Groups Bypasser (rgthree), Note, SetNode, VAELoader, SetNode, ImageResizeKJv2, SetNode, VAEEncode, INTConstant, SetNode, SetNode, GetNode, SetNode, GetNode, GetNode, SetNode, CLIPTextEncode, SetNode, SetNode, SetNode, GetNode, GetNode, CLIPTextEncode, WanImageToVideoSVIPro, GetNode, CLIPTextEncode, CLIPTextEncode, GetNode, WanImageToVideoSVIPro, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, VAEDecode, GetNode, GetNode, GetNode, GetNode, CLIPTextEncode, GetNode, GetNode, WanImageToVideoSVIPro, GetNode, VAEDecode, VHS_VideoCombine, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, UNETLoader, SetNode, CLIPLoader, LoraLoaderModelOnly, UNETLoader, ImageBatchExtendWithOverlap, VAEDecode, ImageBatchExtendWithOverlap, SetNode, PlaySound|pysssss, UNETLoader, INTConstant, INTConstant, KSamplerAdvanced, KSamplerAdvanced, KSamplerAdvanced, KSamplerAdvanced, KSamplerAdvanced, KSamplerAdvanced, LoadImage, INTConstant, SetNode, INTConstant, CR Prompt Text, CR Prompt Text, CR Prompt Text]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/SVI 2.0超强长视频生成-10秒版_2008158274641731586.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2008158274641731586.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（94 个）：
- `CLIPTextEncode` ★核心
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `ModelPatchTorchSettings`
- `LoraLoaderModelOnly` ★核心
- `Fast Groups Bypasser (rgthree)`
- `Note`
- `SetNode`
- `VAELoader`
- `SetNode`
- `ImageResizeKJv2`
- `SetNode`
- `VAEEncode` ★核心
- `INTConstant`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `CLIPTextEncode` ★核心
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `WanImageToVideoSVIPro`
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
- `GetNode`
- `GetNode`
- `GetNode`
- `VAEDecode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `GetNode`
- `GetNode`
- `WanImageToVideoSVIPro`
- `GetNode`
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `UNETLoader` ★核心
- `SetNode`
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `ImageBatchExtendWithOverlap`
- `VAEDecode` ★核心
- `ImageBatchExtendWithOverlap`
- `SetNode`
- `PlaySound|pysssss`
- `UNETLoader` ★核心
- `INTConstant`
- `INTConstant`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `LoadImage`
- `INTConstant`
- `SetNode`
- `INTConstant`
- `CR Prompt Text`
- `CR Prompt Text`
- `CR Prompt Text`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **50%**（47/94）

**有卡**：`CLIPTextEncode`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`LoraLoaderModelOnly`、`VAELoader`、`ImageResizeKJv2`、`VAEEncode`、`INTConstant`、`WanImageToVideoSVIPro`、`VAEDecode`、`VHS_VideoCombine`、`UNETLoader`、`CLIPLoader`、`ImageBatchExtendWithOverlap`、`PlaySound|pysssss`、`KSamplerAdvanced`、`LoadImage`、`CR Prompt Text`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
