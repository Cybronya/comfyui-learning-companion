---
key: 视频生成/图生视频/Ltx 2.3图生视频自动提示词一致性改进版V2（新版模型）_2043901634517929985.json
name: Ltx 2.3图生视频自动提示词一致性改进版V2（新版模型）_2043901634517929985.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2043901634517929985.json
hash: 22f6ae0998fec93a
coverage: 0.941176
learned_at: 2026-10-15 22:36:34
nodes: [KSamplerSelect, CFGGuider, RandomNoise, KSamplerSelect, SamplerCustomAdvanced, RandomNoise, LTXVConcatAVLatent, LTXVImgToVideoConditionOnly, LTXVLatentUpsampler, LTXVSeparateAVLatent, VAEDecodeTiled, LTXVAudioVAEDecode, SamplerCustomAdvanced, ManualSigmas, ModelPatchTorchSettings, CreateVideo, FlashVSR_SM_KSampler, JWInteger, FlashVSR_SM_Model, ImageFromBatch+, LayerUtility: ImageScaleByAspectRatio V2, JWInteger, VHS_VideoCombine, easy cleanGpuUsed, PrimitiveBoolean, JWInteger, JWInteger, Note, Note, Note, LoadImage, LTXVSeparateAVLatent, LTXVAudioVAEDecode, VAEDecodeTiled, LTXVAudioVAELoader, LatentUpscaleModelLoader, CR Text, VAELoader, UNETLoader, JWInteger, Float, LTXVEmptyLatentAudio, CM_FloatToInt, PrimitiveFloat, ResizeImageMaskNode, LTXVPreprocess, LTX2AttentionTunerPatch, LTXVConcatAVLatent, LoraLoaderModelOnly, LoraLoaderModelOnly, PathchSageAttentionKJ, LTXVChunkFeedForward, LTXVImgToVideoConditionOnly, EmptyLTXVLatentVideo, CR Text, LTXVConditioning, LTXAVTextEncoderLoader, CR Prompt Text, ConcatTextOfUtils, CLIPTextEncode, RH_LLMAPI_Pro_Node, CFGGuider, LTX2_NAG, VHS_VideoCombine, SaveVideo, ManualSigmas, CLIPTextEncode, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": "randomize", "denoise": 11, "height": 25, "sampler_name": 2, "scheduler": 3.5, "seed": 1280, "steps": 1833816664, "width": 97}
---

# 视频生成/图生视频/Ltx 2.3图生视频自动提示词一致性改进版V2（新版模型）_2043901634517929985.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2043901634517929985.json`

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
- `JWInteger`
- `JWInteger`
- `Note`
- `Note`
- `Note`
- `LoadImage`
- `LTXVSeparateAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAELoader`
- `LatentUpscaleModelLoader`
- `CR Text`
- `VAELoader`
- `UNETLoader` ★核心
- `JWInteger`
- `Float`
- `LTXVEmptyLatentAudio` ★核心
- `CM_FloatToInt`
- `PrimitiveFloat`
- `ResizeImageMaskNode`
- `LTXVPreprocess`
- `LTX2AttentionTunerPatch`
- `LTXVConcatAVLatent`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
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
- `SaveVideo`
- `ManualSigmas`
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`

## 关键参数

- `seed` = `1280`
- `steps` = `1833816664`
- `cfg` = `randomize`
- `sampler_name` = `2`
- `scheduler` = `3.5`
- `denoise` = `11`
- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **94%**（64/68）

**有卡**：`KSamplerSelect`、`CFGGuider`、`RandomNoise`、`SamplerCustomAdvanced`、`LTXVConcatAVLatent`、`LTXVImgToVideoConditionOnly`、`LTXVLatentUpsampler`、`LTXVSeparateAVLatent`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`ManualSigmas`、`ModelPatchTorchSettings`、`CreateVideo`、`FlashVSR_SM_KSampler`、`JWInteger`、`FlashVSR_SM_Model`、`ImageFromBatch+`、`LayerUtility: ImageScaleByAspectRatio V2`、`VHS_VideoCombine`、`easy cleanGpuUsed`、`PrimitiveBoolean`、`LoadImage`、`LTXVAudioVAELoader`、`LatentUpscaleModelLoader`、`CR Text`、`VAELoader`、`UNETLoader`、`Float`、`LTXVEmptyLatentAudio`、`CM_FloatToInt`、`ResizeImageMaskNode`、`LTXVPreprocess`、`LTX2AttentionTunerPatch`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`LTXVChunkFeedForward`、`EmptyLTXVLatentVideo`、`LTXVConditioning`、`LTXAVTextEncoderLoader`、`CR Prompt Text`、`ConcatTextOfUtils`、`CLIPTextEncode`、`RH_LLMAPI_Pro_Node`、`LTX2_NAG`、`SaveVideo`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2、CFGGuider、KSamplerSelect
