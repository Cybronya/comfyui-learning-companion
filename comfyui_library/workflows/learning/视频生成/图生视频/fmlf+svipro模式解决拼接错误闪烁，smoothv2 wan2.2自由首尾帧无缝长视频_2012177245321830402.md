---
key: 视频生成/图生视频/fmlf+svipro模式解决拼接错误闪烁，smoothv2 wan2.2自由首尾帧无缝长视频_2012177245321830402.json
name: fmlf+svipro模式解决拼接错误闪烁，smoothv2 wan2.2自由首尾帧无缝长视频_2012177245321830402.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/fmlf+svipro模式解决拼接错误闪烁，smoothv2 wan2.2自由首尾帧无缝长视频_2012177245321830402.json
hash: ffaee04c18a03220
coverage: 0.496403
learned_at: 2026-10-15 22:34:26
nodes: [SetNode, SetNode, PrimitiveInt, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, SetNode, GetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, ModelSamplingSD3, PathchSageAttentionKJ, easy globalSeed, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, INTConstant, INTConstant, SetNode, GetNode, KSamplerAdvanced, KSamplerAdvanced, KSamplerAdvanced, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, UNETLoader, PathchSageAttentionKJ, SetNode, SetNode, LoraLoaderModelOnly, LoraLoaderModelOnly, PathchSageAttentionKJ, SetNode, SetNode, PathchSageAttentionKJ, SetNode, SetNode, LayerUtility: ImageScaleByAspectRatio V2, GetNode, VHS_GetImageCount, easy showAnything, GetImageSizeAndCount, Reroute, CLIPTextEncode, GetNode, GetNode, KSamplerAdvanced, Reroute, GetNode, GetNode, GetNode, Reroute, KSamplerAdvanced, Reroute, PlaySound|pysssss, Reroute, Note, GetNode, Fast Groups Bypasser (rgthree), Note, Note, CLIPTextEncode, CLIPTextEncode, PreviewImage, GetNode, ImageBatchExtendWithOverlap, PreviewImage, Reroute, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, easy int, LoadImage, PrimitiveInt, LoadImage, LoadImage, SetNode, LoadImage, LoadImage, CLIPTextEncode, CLIPTextEncode, LoadLatent, SaveLatent, Reroute, LoadImage, VAEDecode, VAEDecode, Anything Everywhere, Anything Everywhere, CRTFirstLastFrameSelector, CRTFirstLastFrameSelector, VAEDecode, ImageBatchExtendWithOverlap, CLIPLoader, VAELoader, LoraLoaderModelOnly, LoadImage, CLIPTextEncode, SetNode, CLIPTextEncode, CLIPTextEncode, GetNode, LoraLoaderModelOnly, Reroute, VideoCombine_Adv, VideoCombine_Adv, VideoCombine_Adv, easy showAnything, ModelSamplingSD3, ModelSamplingSD3, ModelSamplingSD3, GetNode, GetNode, KSamplerAdvanced, Note, VideoCombine_Adv, CRTFirstLastFrameSelector, SaveImage, GetNode, WanAdvancedI2V, WanAdvancedI2V, WanAdvancedI2V, GetNode]
patterns: []
missing: []
parameters: {"cfg": 10, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/fmlf+svipro模式解决拼接错误闪烁，smoothv2 wan2.2自由首尾帧无缝长视频_2012177245321830402.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2012177245321830402.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（139 个）：
- `SetNode`
- `SetNode`
- `PrimitiveInt`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `easy globalSeed`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `INTConstant`
- `INTConstant`
- `SetNode`
- `GetNode`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`
- `SetNode`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `SetNode`
- `SetNode`
- `PathchSageAttentionKJ`
- `SetNode`
- `SetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetNode`
- `VHS_GetImageCount`
- `easy showAnything`
- `GetImageSizeAndCount`
- `Reroute`
- `CLIPTextEncode` ★核心
- `GetNode`
- `GetNode`
- `KSamplerAdvanced` ★核心
- `Reroute`
- `GetNode`
- `GetNode`
- `GetNode`
- `Reroute`
- `KSamplerAdvanced` ★核心
- `Reroute`
- `PlaySound|pysssss`
- `Reroute`
- `Note`
- `GetNode`
- `Fast Groups Bypasser (rgthree)`
- `Note`
- `Note`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `PreviewImage`
- `GetNode`
- `ImageBatchExtendWithOverlap`
- `PreviewImage`
- `Reroute`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `easy int`
- `LoadImage`
- `PrimitiveInt`
- `LoadImage`
- `LoadImage`
- `SetNode`
- `LoadImage`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LoadLatent`
- `SaveLatent`
- `Reroute`
- `LoadImage`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `Anything Everywhere`
- `Anything Everywhere`
- `CRTFirstLastFrameSelector`
- `CRTFirstLastFrameSelector`
- `VAEDecode` ★核心
- `ImageBatchExtendWithOverlap`
- `CLIPLoader`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `CLIPTextEncode` ★核心
- `SetNode`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `GetNode`
- `LoraLoaderModelOnly` ★核心
- `Reroute`
- `VideoCombine_Adv`
- `VideoCombine_Adv`
- `VideoCombine_Adv`
- `easy showAnything`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `GetNode`
- `GetNode`
- `KSamplerAdvanced` ★核心
- `Note`
- `VideoCombine_Adv`
- `CRTFirstLastFrameSelector`
- `SaveImage`
- `GetNode`
- `WanAdvancedI2V`
- `WanAdvancedI2V`
- `WanAdvancedI2V`
- `GetNode`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `10`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **50%**（69/139）

**有卡**：`ModelSamplingSD3`、`PathchSageAttentionKJ`、`easy globalSeed`、`INTConstant`、`KSamplerAdvanced`、`LoraLoaderModelOnly`、`UNETLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`VHS_GetImageCount`、`GetImageSizeAndCount`、`CLIPTextEncode`、`PlaySound|pysssss`、`ImageBatchExtendWithOverlap`、`easy int`、`LoadImage`、`LoadLatent`、`SaveLatent`、`VAEDecode`、`CRTFirstLastFrameSelector`、`CLIPLoader`、`VAELoader`、`VideoCombine_Adv`、`SaveImage`、`WanAdvancedI2V`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
