---
key: 视频生成/图生视频/LTX2.0 4模型对比_2018295552026349570.json
name: LTX2.0 4模型对比_2018295552026349570.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.0 4模型对比_2018295552026349570.json
hash: f2e02f9fd1f9742b
coverage: 0.753731
learned_at: 2026-10-15 22:34:56
nodes: [FL_IntToFloat, LTXVSeparateAVLatent, EmptyLTXVLatentVideo, LTXVEmptyLatentAudio, LTXVConcatAVLatent, CLIPTextEncode, LTXVConditioning, PathchSageAttentionKJ, LTXVCropGuides, LTXVCropGuides, Reroute, KSampler, KSampler, LTXVAudioVAEDecode, CheckpointLoaderSimple, LTXVSeparateAVLatent, AddLabel, LTXVAddGuideMulti, LoraLoaderModelOnly, CLIPTextEncode, LTXVEmptyLatentAudio, LTXVConcatAVLatent, KSamplerSelect, Reroute, LTXVCropGuides, ManualSigmas, PrimitiveString, VAELoaderKJ, PrimitiveString, AudioConcat, PrimitiveInt, LTXVAudioVAEDecode, VHS_SelectImages, VAEDecodeTiled, PrimitiveFloat, PrimitiveFloat, LTXVSeparateAVLatent, Reroute, PrimitiveInt, LTXVPreprocess, FL_IntToFloat, CLIPTextEncode, LTXVChunkFeedForward, CheckpointLoaderSimple, PrimitiveStringMultiline, LTXVAddGuideMulti, LTXVConcatAVLatent, KSamplerSelect, Reroute, LTXVCropGuides, LTXVConditioning, CFGGuider, ManualSigmas, PrimitiveString, VAELoaderKJ, PrimitiveString, AudioConcat, LTXVAudioVAEDecode, VHS_SelectImages, VAEDecodeTiled, ImageScale, PrimitiveInt, PrimitiveFloat, PrimitiveFloat, LTXVSeparateAVLatent, Reroute, Note, LTXVNormalizingSampler, LTXVPreprocess, FL_IntToFloat, LTXVChunkFeedForward, Float to Int, PrimitiveStringMultiline, LTXVAddGuideMulti, CheckpointLoaderSimple, ConditioningZeroOut, RandomNoise, Note, PrimitiveInt, ConditioningZeroOut, RandomNoise, PrimitiveInt, DualCLIPLoader, LTXAVTextEncoderLoader, LTXVAudioVAELoader, AddLabel, AddLabel, AddLabel, LayerUtility: PurgeVRAM, VAEDecodeTiled, LayerUtility: PurgeVRAM, VAEDecodeTiled, CFGGuider, LTXVConditioning, FL_RIFE, LayerUtility: PurgeVRAM, VHS_VideoCombine, LoadImage, easy anythingIndexSwitch, PrimitiveInt, EmptyLTXVLatentVideo, ImageScale, EmptyLTXVLatentVideo, FL_RIFE, RH_LLMAPI_Pro_Node, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, LTXVAudioVAEDecode, LayerUtility: PurgeVRAM, Reroute, LayerUtility: PurgeVRAM, Float to Int, LayerUtility: PurgeVRAM, Reroute, LayerUtility: PurgeVRAM, Reroute, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, PrimitiveInt, LayerUtility: PurgeVRAM, Reroute, ImageConcatMulti, Note, VHS_VideoCombine, Reroute, LTXVNormalizingSampler, Reroute, PrimitiveInt, CLIPTextEncode, LTXVEmptyLatentAudio, VHS_VideoCombine, PrimitiveInt, JWInteger, LayerUtility: ImageScaleByAspectRatio V2]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"batch_size": 1, "cfg": 1, "checkpoint": "ltx2-phr00tmerge-nsfw-v62.safetensors", "denoise": 1, "height": 20, "sampler_name": "lcm", "scheduler": "sgm_uniform", "seed": 937, "steps": 8, "width": 93}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 视频生成/图生视频/LTX2.0 4模型对比_2018295552026349570.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2018295552026349570.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（134 个）：
- `FL_IntToFloat`
- `LTXVSeparateAVLatent`
- `EmptyLTXVLatentVideo`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVConcatAVLatent`
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `PathchSageAttentionKJ`
- `LTXVCropGuides`
- `LTXVCropGuides`
- `Reroute`
- `KSampler` ★核心
- `KSampler` ★核心
- `LTXVAudioVAEDecode` ★核心
- `CheckpointLoaderSimple` ★核心
- `LTXVSeparateAVLatent`
- `AddLabel`
- `LTXVAddGuideMulti`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `LTXVEmptyLatentAudio` ★核心
- `LTXVConcatAVLatent`
- `KSamplerSelect` ★核心
- `Reroute`
- `LTXVCropGuides`
- `ManualSigmas`
- `PrimitiveString`
- `VAELoaderKJ`
- `PrimitiveString`
- `AudioConcat`
- `PrimitiveInt`
- `LTXVAudioVAEDecode` ★核心
- `VHS_SelectImages`
- `VAEDecodeTiled` ★核心
- `PrimitiveFloat`
- `PrimitiveFloat`
- `LTXVSeparateAVLatent`
- `Reroute`
- `PrimitiveInt`
- `LTXVPreprocess`
- `FL_IntToFloat`
- `CLIPTextEncode` ★核心
- `LTXVChunkFeedForward`
- `CheckpointLoaderSimple` ★核心
- `PrimitiveStringMultiline`
- `LTXVAddGuideMulti`
- `LTXVConcatAVLatent`
- `KSamplerSelect` ★核心
- `Reroute`
- `LTXVCropGuides`
- `LTXVConditioning`
- `CFGGuider`
- `ManualSigmas`
- `PrimitiveString`
- `VAELoaderKJ`
- `PrimitiveString`
- `AudioConcat`
- `LTXVAudioVAEDecode` ★核心
- `VHS_SelectImages`
- `VAEDecodeTiled` ★核心
- `ImageScale`
- `PrimitiveInt`
- `PrimitiveFloat`
- `PrimitiveFloat`
- `LTXVSeparateAVLatent`
- `Reroute`
- `Note`
- `LTXVNormalizingSampler` ★核心
- `LTXVPreprocess`
- `FL_IntToFloat`
- `LTXVChunkFeedForward`
- `Float to Int`
- `PrimitiveStringMultiline`
- `LTXVAddGuideMulti`
- `CheckpointLoaderSimple` ★核心
- `ConditioningZeroOut`
- `RandomNoise`
- `Note`
- `PrimitiveInt`
- `ConditioningZeroOut`
- `RandomNoise`
- `PrimitiveInt`
- `DualCLIPLoader`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAELoader`
- `AddLabel`
- `AddLabel`
- `AddLabel`
- `LayerUtility: PurgeVRAM`
- `VAEDecodeTiled` ★核心
- `LayerUtility: PurgeVRAM`
- `VAEDecodeTiled` ★核心
- `CFGGuider`
- `LTXVConditioning`
- `FL_RIFE`
- `LayerUtility: PurgeVRAM`
- `VHS_VideoCombine`
- `LoadImage`
- `easy anythingIndexSwitch`
- `PrimitiveInt`
- `EmptyLTXVLatentVideo`
- `ImageScale`
- `EmptyLTXVLatentVideo`
- `FL_RIFE`
- `RH_LLMAPI_Pro_Node`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `LTXVAudioVAEDecode` ★核心
- `LayerUtility: PurgeVRAM`
- `Reroute`
- `LayerUtility: PurgeVRAM`
- `Float to Int`
- `LayerUtility: PurgeVRAM`
- `Reroute`
- `LayerUtility: PurgeVRAM`
- `Reroute`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `PrimitiveInt`
- `LayerUtility: PurgeVRAM`
- `Reroute`
- `ImageConcatMulti`
- `Note`
- `VHS_VideoCombine`
- `Reroute`
- `LTXVNormalizingSampler` ★核心
- `Reroute`
- `PrimitiveInt`
- `CLIPTextEncode` ★核心
- `LTXVEmptyLatentAudio` ★核心
- `VHS_VideoCombine`
- `PrimitiveInt`
- `JWInteger`
- `LayerUtility: ImageScaleByAspectRatio V2`

## 关键参数

- `width` = `93`
- `height` = `20`
- `batch_size` = `1`
- `seed` = `937`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `lcm`
- `scheduler` = `sgm_uniform`
- `denoise` = `1`
- `checkpoint` = `ltx2-phr00tmerge-nsfw-v62.safetensors`

## 知识

覆盖率 **75%**（101/134）

**有卡**：`FL_IntToFloat`、`LTXVSeparateAVLatent`、`EmptyLTXVLatentVideo`、`LTXVEmptyLatentAudio`、`LTXVConcatAVLatent`、`CLIPTextEncode`、`LTXVConditioning`、`PathchSageAttentionKJ`、`LTXVCropGuides`、`KSampler`、`LTXVAudioVAEDecode`、`CheckpointLoaderSimple`、`AddLabel`、`LTXVAddGuideMulti`、`LoraLoaderModelOnly`、`KSamplerSelect`、`ManualSigmas`、`VAELoaderKJ`、`AudioConcat`、`VHS_SelectImages`、`VAEDecodeTiled`、`LTXVPreprocess`、`LTXVChunkFeedForward`、`CFGGuider`、`ImageScale`、`LTXVNormalizingSampler`、`Float to Int`、`ConditioningZeroOut`、`RandomNoise`、`DualCLIPLoader`、`LTXAVTextEncoderLoader`、`LTXVAudioVAELoader`、`LayerUtility: PurgeVRAM`、`FL_RIFE`、`VHS_VideoCombine`、`LoadImage`、`easy anythingIndexSwitch`、`RH_LLMAPI_Pro_Node`、`ImageConcatMulti`、`JWInteger`、`LayerUtility: ImageScaleByAspectRatio V2`

**用到的条目**：KSampler、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、ConditioningZeroOut、LoadImage、CFGGuider、KSamplerSelect

## 参数体检

发现 3 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换
