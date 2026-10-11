---
key: 视频生成/文生视频/LTX2.3文生视频与图生视频-单_双人对话-唱歌_2033038147285688321.json
name: LTX2.3文生视频与图生视频-单_双人对话-唱歌_2033038147285688321
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.3文生视频与图生视频-单_双人对话-唱歌_2033038147285688321.json
hash: 0c6dc9c7ce69fe02
coverage: 0.829787
learned_at: 2026-10-11 03:48:36
nodes: [CFGGuider, KSamplerSelect, ManualSigmas, VAEDecodeTiled, RandomNoise, LTXVConcatAVLatent, RandomNoise, CFGGuider, LTXVConcatAVLatent, LTXVImgToVideoConditionOnly, LTXVEmptyLatentAudio, KSamplerSelect, LTXVLatentUpsampler, LTXVImgToVideoConditionOnly, LTXVSeparateAVLatent, SamplerCustomAdvanced, LTXVAudioVAEDecode, LatentUpscaleModelLoader, LTXVSeparateAVLatent, LTXVPreprocess, EmptyLTXVLatentVideo, CLIPTextEncode, CLIPTextEncode, PathchSageAttentionKJ, ModelPatchTorchSettings, LTXVChunkFeedForward, SamplerCustomAdvanced, CheckpointLoaderSimple, LTXAVTextEncoderLoader, LTXVAudioVAELoader, Note, CM_FloatToInt, PrimitiveFloat, SimpleMath+, ShowText|pysssss, ManualSigmas, LayerUtility: ImageScaleByAspectRatio V2, CR Text, LoraLoaderModelOnly, VHS_VideoCombine, RH_LLMAPI_Pro_Node, easy int, LoadImage, PrimitiveBoolean, INTConstant, INTConstant, CR Text]
patterns: []
missing: [CR Text, CR Text, LayerUtility: ImageScaleByAspectRatio V2, SimpleMath+, easy int]
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "height": 25, "width": 97}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/LTX2.3文生视频与图生视频-单_双人对话-唱歌_2033038147285688321.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.3文生视频与图生视频-单_双人对话-唱歌_2033038147285688321.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（47 个）：
- `CFGGuider`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `VAEDecodeTiled` ★核心
- `RandomNoise`
- `LTXVConcatAVLatent`
- `RandomNoise`
- `CFGGuider`
- `LTXVConcatAVLatent`
- `LTXVImgToVideoConditionOnly`
- `LTXVEmptyLatentAudio` ★核心
- `KSamplerSelect` ★核心
- `LTXVLatentUpsampler` ★核心
- `LTXVImgToVideoConditionOnly`
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVAudioVAEDecode` ★核心
- `LatentUpscaleModelLoader`
- `LTXVSeparateAVLatent`
- `LTXVPreprocess`
- `EmptyLTXVLatentVideo`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `LTXVChunkFeedForward`
- `SamplerCustomAdvanced` ★核心
- `CheckpointLoaderSimple` ★核心
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAELoader`
- `Note`
- `CM_FloatToInt`
- `PrimitiveFloat`
- `SimpleMath+`
- `ShowText|pysssss`
- `ManualSigmas`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CR Text`
- `LoraLoaderModelOnly` ★核心
- `VHS_VideoCombine`
- `RH_LLMAPI_Pro_Node`
- `easy int`
- `LoadImage`
- `PrimitiveBoolean`
- `INTConstant`
- `INTConstant`
- `CR Text`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-dev.safetensors`

## 知识

覆盖率 **83%**（39/47）

**有卡**：`CFGGuider`、`KSamplerSelect`、`ManualSigmas`、`VAEDecodeTiled`、`RandomNoise`、`LTXVConcatAVLatent`、`LTXVImgToVideoConditionOnly`、`LTXVEmptyLatentAudio`、`LTXVLatentUpsampler`、`LTXVSeparateAVLatent`、`SamplerCustomAdvanced`、`LTXVAudioVAEDecode`、`LatentUpscaleModelLoader`、`LTXVPreprocess`、`EmptyLTXVLatentVideo`、`CLIPTextEncode`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`LTXVChunkFeedForward`、`CheckpointLoaderSimple`、`LTXAVTextEncoderLoader`、`LTXVAudioVAELoader`、`CM_FloatToInt`、`LoraLoaderModelOnly`、`VHS_VideoCombine`、`RH_LLMAPI_Pro_Node`、`LoadImage`、`PrimitiveBoolean`、`INTConstant`

**缺卡**（5）：`CR Text`、`CR Text`、`LayerUtility: ImageScaleByAspectRatio V2`、`SimpleMath+`、`easy int`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `easy int` 知识库中没有该节点类型的任何知识
