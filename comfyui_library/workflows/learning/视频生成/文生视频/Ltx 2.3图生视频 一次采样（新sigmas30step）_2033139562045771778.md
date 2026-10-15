---
key: 视频生成/文生视频/Ltx 2.3图生视频 一次采样（新sigmas30step）_2033139562045771778.json
name: Ltx 2.3图生视频 一次采样（新sigmas30step）_2033139562045771778
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Ltx 2.3图生视频 一次采样（新sigmas30step）_2033139562045771778.json
hash: 9bcea08732566a33
coverage: 0.948718
learned_at: 2026-10-15 22:45:21
nodes: [KSamplerSelect, CFGGuider, KSamplerSelect, RandomNoise, LTXVLatentUpsampler, CheckpointLoaderSimple, LTXVSeparateAVLatent, VAEDecodeTiled, ManualSigmas, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, JWInteger, FlashVSR_SM_Model, ImageFromBatch+, LayerUtility: ImageScaleByAspectRatio V2, JWInteger, LTXVSeparateAVLatent, LTXVAudioVAEDecode, Float, VHS_VideoCombine, VHS_VideoCombine, VAEDecodeTiled, easy cleanGpuUsed, PrimitiveBoolean, JWInteger, Note, Note, Note, VHS_VideoCombine, VHS_VideoCombine, LTXVImgToVideoConditionOnly, LTXVConcatAVLatent, TextPreview, LTXVAudioVAEDecode, JWInteger, SamplerCustomAdvanced, DuckHideNode, SaveImage, LTXAVTextEncoderLoader, RH_LLMAPI_Pro_Node, VideoInfoSource, CR Text, FlashVSR_SM_KSampler, DuckHideNode, CreateVideo, SaveVideo, SaveImage, LTXVConcatAVLatent, ManualSigmas, RandomNoise, LTXVAudioVAELoader, LatentUpscaleModelLoader, LoraLoaderModelOnly, LTXVEmptyLatentAudio, SamplerCustomAdvanced, SigmasPreview, CM_FloatToInt, LTXVImgToVideoConditionOnly, PrimitiveFloat, CLIPTextEncode, LTXVChunkFeedForward, CFGGuider, LTX2_NAG, LTXVConditioning, LTXVPreprocess, EmptyLTXVLatentVideo, VHS_VideoCombine, ResizeImageMaskNode, ModelPatchTorchSettings, CLIPTextEncode, CR Text, VHS_LoadVideo, LoadImage, JWInteger, PathchSageAttentionKJ, LoraLoaderModelOnly, LoraLoaderModelOnly]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": "fixed", "checkpoint": "ltx-2.3-22b-dev-fp8.safetensors", "denoise": 11, "height": 25, "sampler_name": 2, "scheduler": 3.5, "seed": 1280, "steps": 2102623004, "width": 97}
---

# 视频生成/文生视频/Ltx 2.3图生视频 一次采样（新sigmas30step）_2033139562045771778.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Ltx 2.3图生视频 一次采样（新sigmas30step）_2033139562045771778.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（78 个）：
- `KSamplerSelect` ★核心
- `CFGGuider`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `LTXVLatentUpsampler` ★核心
- `CheckpointLoaderSimple` ★核心
- `LTXVSeparateAVLatent`
- `VAEDecodeTiled` ★核心
- `ManualSigmas`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `JWInteger`
- `FlashVSR_SM_Model`
- `ImageFromBatch+`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `JWInteger`
- `LTXVSeparateAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `Float`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VAEDecodeTiled` ★核心
- `easy cleanGpuUsed`
- `PrimitiveBoolean`
- `JWInteger`
- `Note`
- `Note`
- `Note`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `LTXVImgToVideoConditionOnly`
- `LTXVConcatAVLatent`
- `TextPreview`
- `LTXVAudioVAEDecode` ★核心
- `JWInteger`
- `SamplerCustomAdvanced` ★核心
- `DuckHideNode`
- `SaveImage`
- `LTXAVTextEncoderLoader`
- `RH_LLMAPI_Pro_Node`
- `VideoInfoSource`
- `CR Text`
- `FlashVSR_SM_KSampler` ★核心
- `DuckHideNode`
- `CreateVideo`
- `SaveVideo`
- `SaveImage`
- `LTXVConcatAVLatent`
- `ManualSigmas`
- `RandomNoise`
- `LTXVAudioVAELoader`
- `LatentUpscaleModelLoader`
- `LoraLoaderModelOnly` ★核心
- `LTXVEmptyLatentAudio` ★核心
- `SamplerCustomAdvanced` ★核心
- `SigmasPreview`
- `CM_FloatToInt`
- `LTXVImgToVideoConditionOnly`
- `PrimitiveFloat`
- `CLIPTextEncode` ★核心
- `LTXVChunkFeedForward`
- `CFGGuider`
- `LTX2_NAG`
- `LTXVConditioning`
- `LTXVPreprocess`
- `EmptyLTXVLatentVideo`
- `VHS_VideoCombine`
- `ResizeImageMaskNode`
- `ModelPatchTorchSettings`
- `CLIPTextEncode` ★核心
- `CR Text`
- `VHS_LoadVideo`
- `LoadImage`
- `JWInteger`
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev-fp8.safetensors`
- `seed` = `1280`
- `steps` = `2102623004`
- `cfg` = `fixed`
- `sampler_name` = `2`
- `scheduler` = `3.5`
- `denoise` = `11`
- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **95%**（74/78）

**有卡**：`KSamplerSelect`、`CFGGuider`、`RandomNoise`、`LTXVLatentUpsampler`、`CheckpointLoaderSimple`、`LTXVSeparateAVLatent`、`VAEDecodeTiled`、`ManualSigmas`、`VHS_VideoCombine`、`JWInteger`、`FlashVSR_SM_Model`、`ImageFromBatch+`、`LayerUtility: ImageScaleByAspectRatio V2`、`LTXVAudioVAEDecode`、`Float`、`easy cleanGpuUsed`、`PrimitiveBoolean`、`LTXVImgToVideoConditionOnly`、`LTXVConcatAVLatent`、`TextPreview`、`SamplerCustomAdvanced`、`DuckHideNode`、`SaveImage`、`LTXAVTextEncoderLoader`、`RH_LLMAPI_Pro_Node`、`VideoInfoSource`、`CR Text`、`FlashVSR_SM_KSampler`、`CreateVideo`、`SaveVideo`、`LTXVAudioVAELoader`、`LatentUpscaleModelLoader`、`LoraLoaderModelOnly`、`LTXVEmptyLatentAudio`、`SigmasPreview`、`CM_FloatToInt`、`CLIPTextEncode`、`LTXVChunkFeedForward`、`LTX2_NAG`、`LTXVConditioning`、`LTXVPreprocess`、`EmptyLTXVLatentVideo`、`ResizeImageMaskNode`、`ModelPatchTorchSettings`、`VHS_LoadVideo`、`LoadImage`、`PathchSageAttentionKJ`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、LayerUtility: ImageScaleByAspectRatio V2、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
