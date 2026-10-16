---
key: 视频生成/图生视频/【阿良绘】Ltx 2.3图生视频 _ 自动提示词 改进版V2（新版模型）_2047130634124005377.json
name: 【阿良绘】Ltx 2.3图生视频 _ 自动提示词 改进版V2（新版模型）_2047130634124005377.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2047130634124005377.json
hash: 1e32785ee5fb64d4
coverage: 0.75
learned_at: 2026-10-15 22:37:02
nodes: [UNETLoader, LoraLoaderModelOnly, LTX2AttentionTunerPatch, GetNode, RandomNoise, GetNode, GetNode, KSamplerSelect, ManualSigmas, GetNode, CFGGuider, LTXVConcatAVLatent, CLIPTextEncode, GetNode, GetNode, CM_FloatToInt, SetNode, LatentUpscaleModelLoader, LTXAVTextEncoderLoader, SetNode, SetNode, VAELoader, LTXVAudioVAELoader, ModelPatchTorchSettings, PrimitiveBoolean, LTXVChunkFeedForward, PathchSageAttentionKJ, SetNode, GetNode, LTXVEmptyLatentAudio, GetNode, KSamplerSelect, GetNode, CFGGuider, ManualSigmas, LTXVConcatAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVAudioVAEDecode, VAEDecodeTiled, RH_LLMAPI_Pro_Node, PrimitiveFloat, JWInteger, JWInteger, LayerUtility: ImageScaleByAspectRatio V2, GetNode, VHS_VideoCombine, CR Prompt Text, ConcatTextOfUtils, EmptyLTXVLatentVideo, SetNode, ImageScaleBy, SetNode, GetImageSize, easy cleanGpuUsed, GetNode, ImageFromBatch+, JWInteger, JWInteger, Float, FlashVSR_SM_Model, LayerUtility: ImageScaleByAspectRatio V2, FlashVSR_SM_KSampler, LoraLoaderModelOnly, CR Text, VHS_VideoCombine, CreateVideo, SaveVideo, LoadImage, CLIPTextEncode, LTX2_NAG, CR Text, ResizeImageMaskNode, LTXVConditioning, SetNode, GetNode, LTXVImgToVideoConditionOnly, LTXVPreprocess, RandomNoise, GetNode, GetNode, LTXVLatentUpsampler, LTXVImgToVideoConditionOnly, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVAudioVAEDecode, VAEDecodeTiled, LTX2_NAG]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": "randomize", "denoise": 11, "height": 25, "sampler_name": 2, "scheduler": 3.5, "seed": 1280, "steps": 1826187750, "width": 97}
---

# 视频生成/图生视频/【阿良绘】Ltx 2.3图生视频 _ 自动提示词 改进版V2（新版模型）_2047130634124005377.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2047130634124005377.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（88 个）：
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LTX2AttentionTunerPatch`
- `GetNode`
- `RandomNoise`
- `GetNode`
- `GetNode`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `GetNode`
- `CFGGuider`
- `LTXVConcatAVLatent`
- `CLIPTextEncode` ★核心
- `GetNode`
- `GetNode`
- `CM_FloatToInt`
- `SetNode`
- `LatentUpscaleModelLoader`
- `LTXAVTextEncoderLoader`
- `SetNode`
- `SetNode`
- `VAELoader`
- `LTXVAudioVAELoader`
- `ModelPatchTorchSettings`
- `PrimitiveBoolean`
- `LTXVChunkFeedForward`
- `PathchSageAttentionKJ`
- `SetNode`
- `GetNode`
- `LTXVEmptyLatentAudio` ★核心
- `GetNode`
- `KSamplerSelect` ★核心
- `GetNode`
- `CFGGuider`
- `ManualSigmas`
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `VAEDecodeTiled` ★核心
- `RH_LLMAPI_Pro_Node`
- `PrimitiveFloat`
- `JWInteger`
- `JWInteger`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetNode`
- `VHS_VideoCombine`
- `CR Prompt Text`
- `ConcatTextOfUtils`
- `EmptyLTXVLatentVideo`
- `SetNode`
- `ImageScaleBy`
- `SetNode`
- `GetImageSize`
- `easy cleanGpuUsed`
- `GetNode`
- `ImageFromBatch+`
- `JWInteger`
- `JWInteger`
- `Float`
- `FlashVSR_SM_Model`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `FlashVSR_SM_KSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `CR Text`
- `VHS_VideoCombine`
- `CreateVideo`
- `SaveVideo`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `LTX2_NAG`
- `CR Text`
- `ResizeImageMaskNode`
- `LTXVConditioning`
- `SetNode`
- `GetNode`
- `LTXVImgToVideoConditionOnly`
- `LTXVPreprocess`
- `RandomNoise`
- `GetNode`
- `GetNode`
- `LTXVLatentUpsampler` ★核心
- `LTXVImgToVideoConditionOnly`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `VAEDecodeTiled` ★核心
- `LTX2_NAG`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `seed` = `1280`
- `steps` = `1826187750`
- `cfg` = `randomize`
- `sampler_name` = `2`
- `scheduler` = `3.5`
- `denoise` = `11`

## 知识

覆盖率 **75%**（66/88）

**有卡**：`UNETLoader`、`LoraLoaderModelOnly`、`LTX2AttentionTunerPatch`、`RandomNoise`、`KSamplerSelect`、`ManualSigmas`、`CFGGuider`、`LTXVConcatAVLatent`、`CLIPTextEncode`、`CM_FloatToInt`、`LatentUpscaleModelLoader`、`LTXAVTextEncoderLoader`、`VAELoader`、`LTXVAudioVAELoader`、`ModelPatchTorchSettings`、`PrimitiveBoolean`、`LTXVChunkFeedForward`、`PathchSageAttentionKJ`、`LTXVEmptyLatentAudio`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`LTXVAudioVAEDecode`、`VAEDecodeTiled`、`RH_LLMAPI_Pro_Node`、`JWInteger`、`LayerUtility: ImageScaleByAspectRatio V2`、`VHS_VideoCombine`、`CR Prompt Text`、`ConcatTextOfUtils`、`EmptyLTXVLatentVideo`、`ImageScaleBy`、`GetImageSize`、`easy cleanGpuUsed`、`ImageFromBatch+`、`Float`、`FlashVSR_SM_Model`、`FlashVSR_SM_KSampler`、`CR Text`、`CreateVideo`、`SaveVideo`、`LoadImage`、`LTX2_NAG`、`ResizeImageMaskNode`、`LTXVConditioning`、`LTXVImgToVideoConditionOnly`、`LTXVPreprocess`、`LTXVLatentUpsampler`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2、CFGGuider、KSamplerSelect
