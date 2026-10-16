---
key: 视频生成/图生视频/Ltx 2.3 Dasiwa V3模型最强人脸一致性图生视频自动提示词V1_2070799952854474753.json
name: Ltx 2.3 Dasiwa V3模型最强人脸一致性图生视频自动提示词V1_2070799952854474753.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2070799952854474753.json
hash: e7ebed69f3165526
coverage: 0.940299
learned_at: 2026-10-15 22:40:42
nodes: [KSamplerSelect, CFGGuider, RandomNoise, KSamplerSelect, SamplerCustomAdvanced, RandomNoise, LTXVConcatAVLatent, LTXVImgToVideoConditionOnly, LTXVLatentUpsampler, LTXVSeparateAVLatent, VAEDecodeTiled, LTXVAudioVAEDecode, SamplerCustomAdvanced, ManualSigmas, ModelPatchTorchSettings, CreateVideo, FlashVSR_SM_KSampler, JWInteger, FlashVSR_SM_Model, ImageFromBatch+, LayerUtility: ImageScaleByAspectRatio V2, JWInteger, VHS_VideoCombine, easy cleanGpuUsed, PrimitiveBoolean, LTXVSeparateAVLatent, LTXVAudioVAEDecode, VAEDecodeTiled, LTXVAudioVAELoader, CR Text, VAELoader, Float, LTXVEmptyLatentAudio, CM_FloatToInt, ResizeImageMaskNode, LTXVPreprocess, LTXVConcatAVLatent, PathchSageAttentionKJ, LTXVChunkFeedForward, LTXVImgToVideoConditionOnly, EmptyLTXVLatentVideo, CR Text, LTXVConditioning, LTXAVTextEncoderLoader, CR Prompt Text, ConcatTextOfUtils, CLIPTextEncode, RH_LLMAPI_Pro_Node, CFGGuider, LTX2_NAG, ManualSigmas, CLIPTextEncode, LoraLoaderModelOnly, LTX2AttentionTunerPatch, LatentUpscaleModelLoader, UNETLoader, LoraLoaderModelOnly, JWInteger, Note, Note, Note, JWInteger, JWInteger, PrimitiveFloat, LoadImage, VHS_VideoCombine, SaveVideo]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": "randomize", "denoise": 11, "height": 25, "sampler_name": 2, "scheduler": 3.5, "seed": 1280, "steps": 235078828, "width": 97}
---

# 视频生成/图生视频/Ltx 2.3 Dasiwa V3模型最强人脸一致性图生视频自动提示词V1_2070799952854474753.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2070799952854474753.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（67 个）：
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
- `CR Text`
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
- `ManualSigmas`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LTX2AttentionTunerPatch`
- `LatentUpscaleModelLoader`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `JWInteger`
- `Note`
- `Note`
- `Note`
- `JWInteger`
- `JWInteger`
- `PrimitiveFloat`
- `LoadImage`
- `VHS_VideoCombine`
- `SaveVideo`

## 关键参数

- `seed` = `1280`
- `steps` = `235078828`
- `cfg` = `randomize`
- `sampler_name` = `2`
- `scheduler` = `3.5`
- `denoise` = `11`
- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **94%**（63/67）

**有卡**：`KSamplerSelect`、`CFGGuider`、`RandomNoise`、`SamplerCustomAdvanced`、`LTXVConcatAVLatent`、`LTXVImgToVideoConditionOnly`、`LTXVLatentUpsampler`、`LTXVSeparateAVLatent`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`ManualSigmas`、`ModelPatchTorchSettings`、`CreateVideo`、`FlashVSR_SM_KSampler`、`JWInteger`、`FlashVSR_SM_Model`、`ImageFromBatch+`、`LayerUtility: ImageScaleByAspectRatio V2`、`VHS_VideoCombine`、`easy cleanGpuUsed`、`PrimitiveBoolean`、`LTXVAudioVAELoader`、`CR Text`、`VAELoader`、`Float`、`LTXVEmptyLatentAudio`、`CM_FloatToInt`、`ResizeImageMaskNode`、`LTXVPreprocess`、`PathchSageAttentionKJ`、`LTXVChunkFeedForward`、`EmptyLTXVLatentVideo`、`LTXVConditioning`、`LTXAVTextEncoderLoader`、`CR Prompt Text`、`ConcatTextOfUtils`、`CLIPTextEncode`、`RH_LLMAPI_Pro_Node`、`LTX2_NAG`、`LoraLoaderModelOnly`、`LTX2AttentionTunerPatch`、`LatentUpscaleModelLoader`、`UNETLoader`、`LoadImage`、`SaveVideo`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2、CFGGuider、KSamplerSelect
