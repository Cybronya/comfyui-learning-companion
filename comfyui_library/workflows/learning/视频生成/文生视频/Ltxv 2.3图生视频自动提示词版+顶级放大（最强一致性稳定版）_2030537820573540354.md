---
key: 视频生成/文生视频/Ltxv 2.3图生视频自动提示词版+顶级放大（最强一致性稳定版）_2030537820573540354.json
name: Ltxv 2.3图生视频自动提示词版+顶级放大（最强一致性稳定版）_2030537820573540354
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Ltxv 2.3图生视频自动提示词版+顶级放大（最强一致性稳定版）_2030537820573540354.json
hash: b73f60b0fdce04d4
coverage: 0.823529
learned_at: 2026-10-11 03:16:48
nodes: [JWInteger, MuyeSizeSelector, JWInteger, JWInteger, LayerUtility: ImageScaleByAspectRatio V2, ImageFromBatch+, Float, SaveVideo, CreateVideo, easy cleanGpuUsed, LTXVAudioVAEDecode, FlashVSR_SM_Model, Note, LTXVAudioVAELoader, RandomNoise, VHS_VideoCombine, FlashVSR_SM_KSampler, LTXAVTextEncoderLoader, ResizeImageMaskNode, LTXVImgToVideoConditionOnly, CFGGuider, LTXVSeparateAVLatent, SamplerCustomAdvanced, KSamplerSelect, ManualSigmas, LTXVEmptyLatentAudio, CR Text, CR Text, Note, Note, JWInteger, JWInteger, PrimitiveFloat, LoadImage, RH_LLMAPI_Pro_Node, LTXVPreprocess, CM_FloatToInt, EmptyLTXVLatentVideo, PrimitiveBoolean, CLIPTextEncode, CLIPTextEncode, LTXVConcatAVLatent, PathchSageAttentionKJ, LTXVChunkFeedForward, ModelPatchTorchSettings, LoraLoaderModelOnly, VAEDecodeTiled, LatentUpscaleModelLoader, CheckpointLoaderSimple, LoraLoaderModelOnly, LTXVConditioning]
patterns: []
missing: [CR Text, CR Text, ImageFromBatch+, LayerUtility: ImageScaleByAspectRatio V2, easy cleanGpuUsed]
parameters: {"batch_size": 1, "cfg": "randomize", "checkpoint": "ltx-2.3-22b-dev-fp8.safetensors", "denoise": 11, "height": 25, "sampler_name": 2, "scheduler": 3.5, "seed": 1280, "steps": 718880462, "width": 97}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `ImageFromBatch+` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/Ltxv 2.3图生视频自动提示词版+顶级放大（最强一致性稳定版）_2030537820573540354.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Ltxv 2.3图生视频自动提示词版+顶级放大（最强一致性稳定版）_2030537820573540354.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（51 个）：
- `JWInteger`
- `MuyeSizeSelector`
- `JWInteger`
- `JWInteger`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageFromBatch+`
- `Float`
- `SaveVideo`
- `CreateVideo`
- `easy cleanGpuUsed`
- `LTXVAudioVAEDecode` ★核心
- `FlashVSR_SM_Model`
- `Note`
- `LTXVAudioVAELoader`
- `RandomNoise`
- `VHS_VideoCombine`
- `FlashVSR_SM_KSampler` ★核心
- `LTXAVTextEncoderLoader`
- `ResizeImageMaskNode`
- `LTXVImgToVideoConditionOnly`
- `CFGGuider`
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `LTXVEmptyLatentAudio` ★核心
- `CR Text`
- `CR Text`
- `Note`
- `Note`
- `JWInteger`
- `JWInteger`
- `PrimitiveFloat`
- `LoadImage`
- `RH_LLMAPI_Pro_Node`
- `LTXVPreprocess`
- `CM_FloatToInt`
- `EmptyLTXVLatentVideo`
- `PrimitiveBoolean`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LTXVConcatAVLatent`
- `PathchSageAttentionKJ`
- `LTXVChunkFeedForward`
- `ModelPatchTorchSettings`
- `LoraLoaderModelOnly` ★核心
- `VAEDecodeTiled` ★核心
- `LatentUpscaleModelLoader`
- `CheckpointLoaderSimple` ★核心
- `LoraLoaderModelOnly` ★核心
- `LTXVConditioning`

## 关键参数

- `seed` = `1280`
- `steps` = `718880462`
- `cfg` = `randomize`
- `sampler_name` = `2`
- `scheduler` = `3.5`
- `denoise` = `11`
- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-dev-fp8.safetensors`

## 知识

覆盖率 **82%**（42/51）

**有卡**：`JWInteger`、`MuyeSizeSelector`、`Float`、`SaveVideo`、`CreateVideo`、`LTXVAudioVAEDecode`、`FlashVSR_SM_Model`、`LTXVAudioVAELoader`、`RandomNoise`、`VHS_VideoCombine`、`FlashVSR_SM_KSampler`、`LTXAVTextEncoderLoader`、`ResizeImageMaskNode`、`LTXVImgToVideoConditionOnly`、`CFGGuider`、`LTXVSeparateAVLatent`、`SamplerCustomAdvanced`、`KSamplerSelect`、`ManualSigmas`、`LTXVEmptyLatentAudio`、`LoadImage`、`RH_LLMAPI_Pro_Node`、`LTXVPreprocess`、`CM_FloatToInt`、`EmptyLTXVLatentVideo`、`PrimitiveBoolean`、`CLIPTextEncode`、`LTXVConcatAVLatent`、`PathchSageAttentionKJ`、`LTXVChunkFeedForward`、`ModelPatchTorchSettings`、`LoraLoaderModelOnly`、`VAEDecodeTiled`、`LatentUpscaleModelLoader`、`CheckpointLoaderSimple`、`LTXVConditioning`

**缺卡**（5）：`CR Text`、`CR Text`、`ImageFromBatch+`、`LayerUtility: ImageScaleByAspectRatio V2`、`easy cleanGpuUsed`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、FlashVSR_SM_KSampler

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `ImageFromBatch+` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
