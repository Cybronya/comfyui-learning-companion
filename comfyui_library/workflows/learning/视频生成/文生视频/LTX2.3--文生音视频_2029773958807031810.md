---
key: 视频生成/文生视频/LTX2.3--文生音视频_2029773958807031810.json
name: LTX2.3--文生音视频_2029773958807031810
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.3--文生音视频_2029773958807031810.json
hash: e4267483b8ffca91
coverage: 0.808511
learned_at: 2026-10-11 03:16:46
nodes: [LTXVEmptyLatentAudio, LTXVConditioning, CM_FloatToInt, RandomNoise, CFGGuider, KSamplerSelect, PrimitiveFloat, CheckpointLoaderSimple, LTXVAudioVAELoader, LTXAVTextEncoderLoader, CLIPTextEncode, CLIPTextEncode, LTXVConcatAVLatent, LatentUpscaleModelLoader, EmptyLTXVLatentVideo, LTXVSeparateAVLatent, JWInteger, ImageFromBatch+, LayerUtility: ImageScaleByAspectRatio V2, JWInteger, Float, LTXVPreprocess, PrimitiveBoolean, Note, LoraLoaderModelOnly, LTXVImgToVideoConditionOnly, PathchSageAttentionKJ, ModelPatchTorchSettings, LTXVChunkFeedForward, Note, CR Text, CR Text, RH_LLMAPI_Pro_Node, VHS_VideoCombine, LTXVAudioVAEDecode, FlashVSR_SM_Model, FlashVSR_SM_KSampler, CreateVideo, SaveVideo, SamplerCustomAdvanced, VAEDecodeTiled, easy cleanGpuUsed, ManualSigmas, JWInteger, JWInteger, JWInteger, Note]
patterns: []
missing: [CR Text, CR Text, ImageFromBatch+, LayerUtility: ImageScaleByAspectRatio V2, easy cleanGpuUsed]
parameters: {"batch_size": 1, "cfg": "randomize", "checkpoint": "ltx-2.3-22b-dev-fp8.safetensors", "denoise": 11, "height": 25, "sampler_name": 2, "scheduler": 3.5, "seed": 1280, "steps": 463552079, "width": 97}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `ImageFromBatch+` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/LTX2.3--文生音视频_2029773958807031810.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.3--文生音视频_2029773958807031810.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（47 个）：
- `LTXVEmptyLatentAudio` ★核心
- `LTXVConditioning`
- `CM_FloatToInt`
- `RandomNoise`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `PrimitiveFloat`
- `CheckpointLoaderSimple` ★核心
- `LTXVAudioVAELoader`
- `LTXAVTextEncoderLoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LTXVConcatAVLatent`
- `LatentUpscaleModelLoader`
- `EmptyLTXVLatentVideo`
- `LTXVSeparateAVLatent`
- `JWInteger`
- `ImageFromBatch+`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `JWInteger`
- `Float`
- `LTXVPreprocess`
- `PrimitiveBoolean`
- `Note`
- `LoraLoaderModelOnly` ★核心
- `LTXVImgToVideoConditionOnly`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `LTXVChunkFeedForward`
- `Note`
- `CR Text`
- `CR Text`
- `RH_LLMAPI_Pro_Node`
- `VHS_VideoCombine`
- `LTXVAudioVAEDecode` ★核心
- `FlashVSR_SM_Model`
- `FlashVSR_SM_KSampler` ★核心
- `CreateVideo`
- `SaveVideo`
- `SamplerCustomAdvanced` ★核心
- `VAEDecodeTiled` ★核心
- `easy cleanGpuUsed`
- `ManualSigmas`
- `JWInteger`
- `JWInteger`
- `JWInteger`
- `Note`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-dev-fp8.safetensors`
- `seed` = `1280`
- `steps` = `463552079`
- `cfg` = `randomize`
- `sampler_name` = `2`
- `scheduler` = `3.5`
- `denoise` = `11`

## 知识

覆盖率 **81%**（38/47）

**有卡**：`LTXVEmptyLatentAudio`、`LTXVConditioning`、`CM_FloatToInt`、`RandomNoise`、`CFGGuider`、`KSamplerSelect`、`CheckpointLoaderSimple`、`LTXVAudioVAELoader`、`LTXAVTextEncoderLoader`、`CLIPTextEncode`、`LTXVConcatAVLatent`、`LatentUpscaleModelLoader`、`EmptyLTXVLatentVideo`、`LTXVSeparateAVLatent`、`JWInteger`、`Float`、`LTXVPreprocess`、`PrimitiveBoolean`、`LoraLoaderModelOnly`、`LTXVImgToVideoConditionOnly`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`LTXVChunkFeedForward`、`RH_LLMAPI_Pro_Node`、`VHS_VideoCombine`、`LTXVAudioVAEDecode`、`FlashVSR_SM_Model`、`FlashVSR_SM_KSampler`、`CreateVideo`、`SaveVideo`、`SamplerCustomAdvanced`、`VAEDecodeTiled`、`ManualSigmas`

**缺卡**（5）：`CR Text`、`CR Text`、`ImageFromBatch+`、`LayerUtility: ImageScaleByAspectRatio V2`、`easy cleanGpuUsed`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、FlashVSR_SM_KSampler、LTXVConcatAVLatent

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `ImageFromBatch+` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
