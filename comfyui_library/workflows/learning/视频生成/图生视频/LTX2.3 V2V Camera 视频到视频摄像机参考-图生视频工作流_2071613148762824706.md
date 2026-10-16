---
key: 视频生成/图生视频/LTX2.3 V2V Camera 视频到视频摄像机参考-图生视频工作流_2071613148762824706.json
name: LTX2.3 V2V Camera 视频到视频摄像机参考-图生视频工作流_2071613148762824706.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2071613148762824706.json
hash: e910afd9a41b0b7b
coverage: 0.526316
learned_at: 2026-10-15 22:40:46
nodes: [SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, MathExpression|pysssss, GetNode, GetNode, LTXVCropGuides, LTXVConcatAVLatent, GetNode, SetNode, ManualSigmas, SetNode, SetNode, LTXVChunkFeedForward, GetNode, GetImageSizeAndCount, SetNode, LTXVConditioning, LTX2_NAG, GetNode, EmptyLTXVLatentVideo, LTXAddVideoICLoRAGuide, LTXVEmptyLatentAudio, GetNode, GetNode, GetNode, SimpleMath+, ResizeImageMaskNode, GetImageSizeAndCount, CLIPTextEncode, GetNode, SetNode, KSamplerSelect, SetNode, SetNode, LTXVImgToVideoConditionOnly, VAEDecode, LTXVSeparateAVLatent, LTXVAudioVAEDecode, GetNode, GetNode, easy clearCacheAll, easy cleanGpuUsed, SetNode, PrimitiveInt, PrimitiveInt, SamplerCustom, PathchSageAttentionKJ, LTX2MemoryEfficientSageAttentionPatch, LTXICLoRALoaderModelOnly, VAELoader, SetNode, VAELoader, SetNode, DualCLIPLoader, LoraLoaderModelOnly, UNETLoader, LoadImage, ImageResizeKJv2, SetNode, CR Float To Integer, PrimitiveFloat, SetNode, GetNode, VHS_LoadVideoPath, VHS_LoadVideo, GetNode, GetNode, ResizeImageMaskNode, GetImageSizeAndCount, GetNode, CLIPTextEncode, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX2.3 V2V Camera 视频到视频摄像机参考-图生视频工作流_2071613148762824706.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2071613148762824706.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（76 个）：
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `MathExpression|pysssss`
- `GetNode`
- `GetNode`
- `LTXVCropGuides`
- `LTXVConcatAVLatent`
- `GetNode`
- `SetNode`
- `ManualSigmas`
- `SetNode`
- `SetNode`
- `LTXVChunkFeedForward`
- `GetNode`
- `GetImageSizeAndCount`
- `SetNode`
- `LTXVConditioning`
- `LTX2_NAG`
- `GetNode`
- `EmptyLTXVLatentVideo`
- `LTXAddVideoICLoRAGuide`
- `LTXVEmptyLatentAudio` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `SimpleMath+`
- `ResizeImageMaskNode`
- `GetImageSizeAndCount`
- `CLIPTextEncode` ★核心
- `GetNode`
- `SetNode`
- `KSamplerSelect` ★核心
- `SetNode`
- `SetNode`
- `LTXVImgToVideoConditionOnly`
- `VAEDecode` ★核心
- `LTXVSeparateAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `GetNode`
- `GetNode`
- `easy clearCacheAll`
- `easy cleanGpuUsed`
- `SetNode`
- `PrimitiveInt`
- `PrimitiveInt`
- `SamplerCustom` ★核心
- `PathchSageAttentionKJ`
- `LTX2MemoryEfficientSageAttentionPatch`
- `LTXICLoRALoaderModelOnly` ★核心
- `VAELoader`
- `SetNode`
- `VAELoader`
- `SetNode`
- `DualCLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `LoadImage`
- `ImageResizeKJv2`
- `SetNode`
- `CR Float To Integer`
- `PrimitiveFloat`
- `SetNode`
- `GetNode`
- `VHS_LoadVideoPath`
- `VHS_LoadVideo`
- `GetNode`
- `GetNode`
- `ResizeImageMaskNode`
- `GetImageSizeAndCount`
- `GetNode`
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **53%**（40/76）

**有卡**：`MathExpression|pysssss`、`LTXVCropGuides`、`LTXVConcatAVLatent`、`ManualSigmas`、`LTXVChunkFeedForward`、`GetImageSizeAndCount`、`LTXVConditioning`、`LTX2_NAG`、`EmptyLTXVLatentVideo`、`LTXAddVideoICLoRAGuide`、`LTXVEmptyLatentAudio`、`SimpleMath+`、`ResizeImageMaskNode`、`CLIPTextEncode`、`KSamplerSelect`、`LTXVImgToVideoConditionOnly`、`VAEDecode`、`LTXVSeparateAVLatent`、`LTXVAudioVAEDecode`、`easy clearCacheAll`、`easy cleanGpuUsed`、`SamplerCustom`、`PathchSageAttentionKJ`、`LTX2MemoryEfficientSageAttentionPatch`、`LTXICLoRALoaderModelOnly`、`VAELoader`、`DualCLIPLoader`、`LoraLoaderModelOnly`、`UNETLoader`、`LoadImage`、`ImageResizeKJv2`、`CR Float To Integer`、`VHS_LoadVideoPath`、`VHS_LoadVideo`、`VHS_VideoCombine`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、KSamplerSelect、SamplerCustom
