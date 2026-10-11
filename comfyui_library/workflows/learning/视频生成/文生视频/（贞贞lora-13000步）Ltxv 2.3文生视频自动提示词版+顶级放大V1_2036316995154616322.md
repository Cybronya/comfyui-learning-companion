---
key: 视频生成/文生视频/（贞贞lora-13000步）Ltxv 2.3文生视频自动提示词版+顶级放大V1_2036316995154616322.json
name: （贞贞lora-13000步）Ltxv 2.3文生视频自动提示词版+顶级放大V1_2036316995154616322
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/（贞贞lora-13000步）Ltxv 2.3文生视频自动提示词版+顶级放大V1_2036316995154616322.json
hash: d61978bc3d07e47e
coverage: 0.803571
learned_at: 2026-10-11 03:48:41
nodes: [LTXVEmptyLatentAudio, LTXVConditioning, GemmaAPITextEncode, CM_FloatToInt, RandomNoise, CFGGuider, KSamplerSelect, SamplerCustomAdvanced, GemmaAPITextEncode, LTXAVTextEncoderLoader, CLIPTextEncode, CLIPTextEncode, LTXVConcatAVLatent, LTXVAudioVAEDecode, ModelPatchTorchSettings, PathchSageAttentionKJ, EmptyLTXVLatentVideo, LoraLoaderModelOnly, LTXVSeparateAVLatent, ManualSigmas, CreateVideo, FlashVSR_SM_KSampler, JWInteger, FlashVSR_SM_Model, ImageFromBatch+, LayerUtility: ImageScaleByAspectRatio V2, JWInteger, Float, CR Text, easy cleanGpuUsed, VAEDecodeTiled, LTXVPreprocess, ResizeImageMaskNode, LTXVChunkFeedForward, JWInteger, JWInteger, JWInteger, Note, Note, Note, LTXVImgToVideoConditionOnly, LoadImage, CR Text, CR Prompt Text, ConcatTextOfUtils, VHS_VideoCombine, SaveVideo, RH_LLMAPI_Pro_Node, PrimitiveFloat, PrimitiveBoolean, PrimitiveString, LoraLoaderModelOnly, LoraLoaderModelOnly, LatentUpscaleModelLoader, CheckpointLoaderSimple, LTXVAudioVAELoader]
patterns: []
missing: [CR Text, CR Text, ImageFromBatch+, LayerUtility: ImageScaleByAspectRatio V2, easy cleanGpuUsed, CR Prompt Text]
parameters: {"batch_size": 1, "cfg": "randomize", "checkpoint": "ltx-2.3-22b-dev-fp8.safetensors", "denoise": 11, "height": 25, "sampler_name": 2, "scheduler": 3.5, "seed": 1280, "steps": 830682222, "width": 97}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `ImageFromBatch+` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/（贞贞lora-13000步）Ltxv 2.3文生视频自动提示词版+顶级放大V1_2036316995154616322.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/（贞贞lora-13000步）Ltxv 2.3文生视频自动提示词版+顶级放大V1_2036316995154616322.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（56 个）：
- `LTXVEmptyLatentAudio` ★核心
- `LTXVConditioning`
- `GemmaAPITextEncode`
- `CM_FloatToInt`
- `RandomNoise`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `GemmaAPITextEncode`
- `LTXAVTextEncoderLoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LTXVConcatAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `EmptyLTXVLatentVideo`
- `LoraLoaderModelOnly` ★核心
- `LTXVSeparateAVLatent`
- `ManualSigmas`
- `CreateVideo`
- `FlashVSR_SM_KSampler` ★核心
- `JWInteger`
- `FlashVSR_SM_Model`
- `ImageFromBatch+`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `JWInteger`
- `Float`
- `CR Text`
- `easy cleanGpuUsed`
- `VAEDecodeTiled` ★核心
- `LTXVPreprocess`
- `ResizeImageMaskNode`
- `LTXVChunkFeedForward`
- `JWInteger`
- `JWInteger`
- `JWInteger`
- `Note`
- `Note`
- `Note`
- `LTXVImgToVideoConditionOnly`
- `LoadImage`
- `CR Text`
- `CR Prompt Text`
- `ConcatTextOfUtils`
- `VHS_VideoCombine`
- `SaveVideo`
- `RH_LLMAPI_Pro_Node`
- `PrimitiveFloat`
- `PrimitiveBoolean`
- `PrimitiveString`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LatentUpscaleModelLoader`
- `CheckpointLoaderSimple` ★核心
- `LTXVAudioVAELoader`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `seed` = `1280`
- `steps` = `830682222`
- `cfg` = `randomize`
- `sampler_name` = `2`
- `scheduler` = `3.5`
- `denoise` = `11`
- `checkpoint` = `ltx-2.3-22b-dev-fp8.safetensors`

## 知识

覆盖率 **80%**（45/56）

**有卡**：`LTXVEmptyLatentAudio`、`LTXVConditioning`、`GemmaAPITextEncode`、`CM_FloatToInt`、`RandomNoise`、`CFGGuider`、`KSamplerSelect`、`SamplerCustomAdvanced`、`LTXAVTextEncoderLoader`、`CLIPTextEncode`、`LTXVConcatAVLatent`、`LTXVAudioVAEDecode`、`ModelPatchTorchSettings`、`PathchSageAttentionKJ`、`EmptyLTXVLatentVideo`、`LoraLoaderModelOnly`、`LTXVSeparateAVLatent`、`ManualSigmas`、`CreateVideo`、`FlashVSR_SM_KSampler`、`JWInteger`、`FlashVSR_SM_Model`、`Float`、`VAEDecodeTiled`、`LTXVPreprocess`、`ResizeImageMaskNode`、`LTXVChunkFeedForward`、`LTXVImgToVideoConditionOnly`、`LoadImage`、`ConcatTextOfUtils`、`VHS_VideoCombine`、`SaveVideo`、`RH_LLMAPI_Pro_Node`、`PrimitiveBoolean`、`LatentUpscaleModelLoader`、`CheckpointLoaderSimple`、`LTXVAudioVAELoader`

**缺卡**（6）：`CR Text`、`CR Text`、`ImageFromBatch+`、`LayerUtility: ImageScaleByAspectRatio V2`、`easy cleanGpuUsed`、`CR Prompt Text`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、FlashVSR_SM_KSampler

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `ImageFromBatch+` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
