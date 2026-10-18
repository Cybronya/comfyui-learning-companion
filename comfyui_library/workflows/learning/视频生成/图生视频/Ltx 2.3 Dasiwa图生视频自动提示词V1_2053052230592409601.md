---
key: 视频生成/图生视频/Ltx 2.3 Dasiwa图生视频自动提示词V1_2053052230592409601.json
name: Ltx 2.3 Dasiwa图生视频自动提示词V1_2053052230592409601.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Ltx 2.3 Dasiwa图生视频自动提示词V1_2053052230592409601.json
hash: ad3e330d54fb3ec7
coverage: 0.926471
learned_at: 2026-10-15 22:37:35
nodes: [KSamplerSelect, CFGGuider, RandomNoise, KSamplerSelect, SamplerCustomAdvanced, RandomNoise, LTXVConcatAVLatent, LTXVImgToVideoConditionOnly, LTXVLatentUpsampler, LTXVSeparateAVLatent, VAEDecodeTiled, LTXVAudioVAEDecode, SamplerCustomAdvanced, ManualSigmas, ModelPatchTorchSettings, CreateVideo, FlashVSR_SM_KSampler, JWInteger, FlashVSR_SM_Model, ImageFromBatch+, LayerUtility: ImageScaleByAspectRatio V2, JWInteger, VHS_VideoCombine, easy cleanGpuUsed, PrimitiveBoolean, LTXVSeparateAVLatent, LTXVAudioVAEDecode, VAEDecodeTiled, LTXVAudioVAELoader, LatentUpscaleModelLoader, VAELoader, Float, LTXVEmptyLatentAudio, CM_FloatToInt, ResizeImageMaskNode, LTXVPreprocess, LTXVConcatAVLatent, PathchSageAttentionKJ, LTXVChunkFeedForward, LTXVImgToVideoConditionOnly, EmptyLTXVLatentVideo, CR Text, LTXVConditioning, LTXAVTextEncoderLoader, CR Prompt Text, ConcatTextOfUtils, CLIPTextEncode, RH_LLMAPI_Pro_Node, CFGGuider, LTX2_NAG, VHS_VideoCombine, ManualSigmas, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, LTX2AttentionTunerPatch, UNETLoader, Reroute, JWInteger, JWInteger, Note, LayerUtility: ImageScaleByAspectRatio V2, CR Text, LoadImage, Note, Note, PrimitiveFloat, SaveVideo]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": "randomize", "denoise": 11, "height": 25, "sampler_name": 2, "scheduler": 3.5, "seed": 1280, "steps": 1742463012, "width": 97}
---

# 视频生成/图生视频/Ltx 2.3 Dasiwa图生视频自动提示词V1_2053052230592409601.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2053052230592409601.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（68 个）：
- `KSamplerSelect` ★核心
- `CFGGuider`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `LTXVConcatAVLatent`
- `LTXVImgToVideoConditionOnly`
- `LTXVLatentUpsampler` ★核心
- `LTXVSeparateAVLatent`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `SamplerCustomAdvanced` ★核心
- `ManualSigmas`
- `ModelPatchTorchSettings`
- `CreateVideo`
- `FlashVSR_SM_KSampler` ★核心
- `JWInteger`
- `FlashVSR_SM_Model`
- `ImageFromBatch+`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `JWInteger`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`
- `PrimitiveBoolean`
- `LTXVSeparateAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAELoader`
- `LatentUpscaleModelLoader`
- `VAELoader`
- `Float`
- `LTXVEmptyLatentAudio` ★核心
- `CM_FloatToInt`
- `ResizeImageMaskNode`
- `LTXVPreprocess`
- `LTXVConcatAVLatent`
- `PathchSageAttentionKJ`
- `LTXVChunkFeedForward`
- `LTXVImgToVideoConditionOnly`
- `EmptyLTXVLatentVideo`
- `CR Text`
- `LTXVConditioning`
- `LTXAVTextEncoderLoader`
- `CR Prompt Text`
- `ConcatTextOfUtils`
- `CLIPTextEncode` ★核心
- `RH_LLMAPI_Pro_Node`
- `CFGGuider`
- `LTX2_NAG`
- `VHS_VideoCombine`
- `ManualSigmas`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LTX2AttentionTunerPatch`
- `UNETLoader` ★核心
- `Reroute`
- `JWInteger`
- `JWInteger`
- `Note`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CR Text`
- `LoadImage`
- `Note`
- `Note`
- `PrimitiveFloat`
- `SaveVideo`

## 关键参数

- `seed` = `1280`
- `steps` = `1742463012`
- `cfg` = `randomize`
- `sampler_name` = `2`
- `scheduler` = `3.5`
- `denoise` = `11`
- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **93%**（63/68）

**有卡**：`KSamplerSelect`、`CFGGuider`、`RandomNoise`、`SamplerCustomAdvanced`、`LTXVConcatAVLatent`、`LTXVImgToVideoConditionOnly`、`LTXVLatentUpsampler`、`LTXVSeparateAVLatent`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`ManualSigmas`、`ModelPatchTorchSettings`、`CreateVideo`、`FlashVSR_SM_KSampler`、`JWInteger`、`FlashVSR_SM_Model`、`ImageFromBatch+`、`LayerUtility: ImageScaleByAspectRatio V2`、`VHS_VideoCombine`、`easy cleanGpuUsed`、`PrimitiveBoolean`、`LTXVAudioVAELoader`、`LatentUpscaleModelLoader`、`VAELoader`、`Float`、`LTXVEmptyLatentAudio`、`CM_FloatToInt`、`ResizeImageMaskNode`、`LTXVPreprocess`、`PathchSageAttentionKJ`、`LTXVChunkFeedForward`、`EmptyLTXVLatentVideo`、`CR Text`、`LTXVConditioning`、`LTXAVTextEncoderLoader`、`CR Prompt Text`、`ConcatTextOfUtils`、`CLIPTextEncode`、`RH_LLMAPI_Pro_Node`、`LTX2_NAG`、`LoraLoaderModelOnly`、`LTX2AttentionTunerPatch`、`UNETLoader`、`LoadImage`、`SaveVideo`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2、CFGGuider、KSamplerSelect
