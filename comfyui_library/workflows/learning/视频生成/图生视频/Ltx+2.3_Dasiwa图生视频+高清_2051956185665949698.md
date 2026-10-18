---
key: 视频生成/图生视频/Ltx+2.3_Dasiwa图生视频+高清_2051956185665949698.json
name: Ltx+2.3_Dasiwa图生视频+高清_2051956185665949698.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Ltx+2.3_Dasiwa图生视频+高清_2051956185665949698.json
hash: ab8f2d7843cc822b
coverage: 0.896552
learned_at: 2026-10-15 22:37:25
nodes: [KSamplerSelect, SamplerCustomAdvanced, Note, Float, LTXVEmptyLatentAudio, CFGGuider, JWInteger, VAELoader, LTXVAudioVAELoader, LatentUpscaleModelLoader, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LTX2AttentionTunerPatch, PathchSageAttentionKJ, ModelPatchTorchSettings, LTXVChunkFeedForward, ResizeImageMaskNode, PrimitiveBoolean, LTXVConditioning, LTXVImgToVideoConditionOnly, JWInteger, Note, JWInteger, PrimitiveFloat, Note, LTXVSeparateAVLatent, JWInteger, ImageFromBatch+, Note, FlashVSR_SM_Model, Note, VHS_VideoCombine, LTXVAudioVAEDecode, RandomNoise, LTXVConcatAVLatent, CM_FloatToInt, VAEDecodeTiled, LTX2_NAG, FlashVSR_SM_KSampler, CR Text, easy promptConcat, CLIPTextEncode, LoadImage, ManualSigmas, LTXAVTextEncoderLoader, Qwen3_VQA, CLIPTextEncode, TextListSplit, LTXVPreprocess, CR Text, EmptyLTXVLatentVideo, ShowAnything|Mie, JWInteger, LayerUtility: ImageScaleByAspectRatio V2, easy cleanGpuUsed, CreateVideo, SaveVideo]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": "randomize", "denoise": 11, "height": 25, "sampler_name": 2, "scheduler": 3.5, "seed": 1280, "steps": 1437645528, "width": 97}
---

# 视频生成/图生视频/Ltx+2.3_Dasiwa图生视频+高清_2051956185665949698.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2051956185665949698.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（58 个）：
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `Note`
- `Float`
- `LTXVEmptyLatentAudio` ★核心
- `CFGGuider`
- `JWInteger`
- `VAELoader`
- `LTXVAudioVAELoader`
- `LatentUpscaleModelLoader`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LTX2AttentionTunerPatch`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `LTXVChunkFeedForward`
- `ResizeImageMaskNode`
- `PrimitiveBoolean`
- `LTXVConditioning`
- `LTXVImgToVideoConditionOnly`
- `JWInteger`
- `Note`
- `JWInteger`
- `PrimitiveFloat`
- `Note`
- `LTXVSeparateAVLatent`
- `JWInteger`
- `ImageFromBatch+`
- `Note`
- `FlashVSR_SM_Model`
- `Note`
- `VHS_VideoCombine`
- `LTXVAudioVAEDecode` ★核心
- `RandomNoise`
- `LTXVConcatAVLatent`
- `CM_FloatToInt`
- `VAEDecodeTiled` ★核心
- `LTX2_NAG`
- `FlashVSR_SM_KSampler` ★核心
- `CR Text`
- `easy promptConcat`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `ManualSigmas`
- `LTXAVTextEncoderLoader`
- `Qwen3_VQA`
- `CLIPTextEncode` ★核心
- `TextListSplit`
- `LTXVPreprocess`
- `CR Text`
- `EmptyLTXVLatentVideo`
- `ShowAnything|Mie`
- `JWInteger`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `easy cleanGpuUsed`
- `CreateVideo`
- `SaveVideo`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `seed` = `1280`
- `steps` = `1437645528`
- `cfg` = `randomize`
- `sampler_name` = `2`
- `scheduler` = `3.5`
- `denoise` = `11`

## 知识

覆盖率 **90%**（52/58）

**有卡**：`KSamplerSelect`、`SamplerCustomAdvanced`、`Float`、`LTXVEmptyLatentAudio`、`CFGGuider`、`JWInteger`、`VAELoader`、`LTXVAudioVAELoader`、`LatentUpscaleModelLoader`、`UNETLoader`、`LoraLoaderModelOnly`、`LTX2AttentionTunerPatch`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`LTXVChunkFeedForward`、`ResizeImageMaskNode`、`PrimitiveBoolean`、`LTXVConditioning`、`LTXVImgToVideoConditionOnly`、`LTXVSeparateAVLatent`、`ImageFromBatch+`、`FlashVSR_SM_Model`、`VHS_VideoCombine`、`LTXVAudioVAEDecode`、`RandomNoise`、`LTXVConcatAVLatent`、`CM_FloatToInt`、`VAEDecodeTiled`、`LTX2_NAG`、`FlashVSR_SM_KSampler`、`CR Text`、`easy promptConcat`、`CLIPTextEncode`、`LoadImage`、`ManualSigmas`、`LTXAVTextEncoderLoader`、`Qwen3_VQA`、`TextListSplit`、`LTXVPreprocess`、`EmptyLTXVLatentVideo`、`ShowAnything|Mie`、`LayerUtility: ImageScaleByAspectRatio V2`、`easy cleanGpuUsed`、`CreateVideo`、`SaveVideo`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2、CFGGuider、KSamplerSelect
