---
key: 视频生成/图生视频/LTX 2.3图生视频自动提示词版+FlashVSR放大_2036142607784484866.json
name: LTX 2.3图生视频自动提示词版+FlashVSR放大_2036142607784484866.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX 2.3图生视频自动提示词版+FlashVSR放大_2036142607784484866.json
hash: 7c3c2c7c20cbc2dd
coverage: 0.925926
learned_at: 2026-10-15 22:35:51
nodes: [LTXVEmptyLatentAudio, LTXVConditioning, LTXVPreprocess, CM_FloatToInt, RandomNoise, CFGGuider, KSamplerSelect, SamplerCustomAdvanced, ResizeImageMaskNode, PrimitiveFloat, CheckpointLoaderSimple, LTXVAudioVAELoader, LTXAVTextEncoderLoader, CLIPTextEncode, CLIPTextEncode, RH_LLMAPI_Pro_Node, LTXVConcatAVLatent, ModelPatchTorchSettings, PathchSageAttentionKJ, LTXVChunkFeedForward, LTXVImgToVideoConditionOnly, LatentUpscaleModelLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, EmptyLTXVLatentVideo, CreateVideo, FlashVSR_SM_KSampler, SaveVideo, JWInteger, FlashVSR_SM_Model, ImageFromBatch+, LayerUtility: ImageScaleByAspectRatio V2, JWInteger, LTXVSeparateAVLatent, LTXVAudioVAEDecode, Float, ManualSigmas, VAEDecodeTiled, easy cleanGpuUsed, PrimitiveBoolean, JWInteger, VHS_VideoCombine, Note, Note, CR Text, easy mathInt, JWInteger, easy mathInt, Note, ImageSizeInfo, LoadImage, CR Text, JWInteger, JWInteger]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": "randomize", "checkpoint": "ltx-2.3-22b-dev-fp8.safetensors", "denoise": 11, "height": 25, "sampler_name": 2, "scheduler": 3.5, "seed": 1280, "steps": 715871644, "width": 97}
---

# 视频生成/图生视频/LTX 2.3图生视频自动提示词版+FlashVSR放大_2036142607784484866.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2036142607784484866.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（54 个）：
- `LTXVEmptyLatentAudio` ★核心
- `LTXVConditioning`
- `LTXVPreprocess`
- `CM_FloatToInt`
- `RandomNoise`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `ResizeImageMaskNode`
- `PrimitiveFloat`
- `CheckpointLoaderSimple` ★核心
- `LTXVAudioVAELoader`
- `LTXAVTextEncoderLoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `RH_LLMAPI_Pro_Node`
- `LTXVConcatAVLatent`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `LTXVChunkFeedForward`
- `LTXVImgToVideoConditionOnly`
- `LatentUpscaleModelLoader`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `EmptyLTXVLatentVideo`
- `CreateVideo`
- `FlashVSR_SM_KSampler` ★核心
- `SaveVideo`
- `JWInteger`
- `FlashVSR_SM_Model`
- `ImageFromBatch+`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `JWInteger`
- `LTXVSeparateAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `Float`
- `ManualSigmas`
- `VAEDecodeTiled` ★核心
- `easy cleanGpuUsed`
- `PrimitiveBoolean`
- `JWInteger`
- `VHS_VideoCombine`
- `Note`
- `Note`
- `CR Text`
- `easy mathInt`
- `JWInteger`
- `easy mathInt`
- `Note`
- `ImageSizeInfo`
- `LoadImage`
- `CR Text`
- `JWInteger`
- `JWInteger`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-dev-fp8.safetensors`
- `seed` = `1280`
- `steps` = `715871644`
- `cfg` = `randomize`
- `sampler_name` = `2`
- `scheduler` = `3.5`
- `denoise` = `11`

## 知识

覆盖率 **93%**（50/54）

**有卡**：`LTXVEmptyLatentAudio`、`LTXVConditioning`、`LTXVPreprocess`、`CM_FloatToInt`、`RandomNoise`、`CFGGuider`、`KSamplerSelect`、`SamplerCustomAdvanced`、`ResizeImageMaskNode`、`CheckpointLoaderSimple`、`LTXVAudioVAELoader`、`LTXAVTextEncoderLoader`、`CLIPTextEncode`、`RH_LLMAPI_Pro_Node`、`LTXVConcatAVLatent`、`ModelPatchTorchSettings`、`PathchSageAttentionKJ`、`LTXVChunkFeedForward`、`LTXVImgToVideoConditionOnly`、`LatentUpscaleModelLoader`、`LoraLoaderModelOnly`、`EmptyLTXVLatentVideo`、`CreateVideo`、`FlashVSR_SM_KSampler`、`SaveVideo`、`JWInteger`、`FlashVSR_SM_Model`、`ImageFromBatch+`、`LayerUtility: ImageScaleByAspectRatio V2`、`LTXVSeparateAVLatent`、`LTXVAudioVAEDecode`、`Float`、`ManualSigmas`、`VAEDecodeTiled`、`easy cleanGpuUsed`、`PrimitiveBoolean`、`VHS_VideoCombine`、`CR Text`、`easy mathInt`、`ImageSizeInfo`、`LoadImage`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、LayerUtility: ImageScaleByAspectRatio V2、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
