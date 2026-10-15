---
key: 视频生成/文生视频/最强优化  LTX2.3  图 _ 文 生视频合并版_2030179257439227905.json
name: 最强优化  LTX2.3  图 _ 文 生视频合并版_2030179257439227905
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/最强优化  LTX2.3  图 _ 文 生视频合并版_2030179257439227905.json
hash: e28e50a1b7433967
coverage: 0.916667
learned_at: 2026-10-15 22:48:47
nodes: [PathchSageAttentionKJ, INTConstant, INTConstant, INTConstant, LayerUtility: ImageScaleByAspectRatio V2, CLIPTextEncode, LTXAVTextEncoderLoader, LTXVPreprocess, LTXVConcatAVLatent, ModelPatchTorchSettings, CheckpointLoaderSimple, LTXVLatentUpsampler, SamplerCustomAdvanced, LTXVSeparateAVLatent, EmptyLTXVLatentVideo, LoraLoaderModelOnly, LatentUpscaleModelLoader, LTXVAudioVAELoader, LTXVEmptyLatentAudio, LTXVImgToVideoConditionOnly, ManualSigmas, KSamplerSelect, CFGGuider, RandomNoise, SamplerCustomAdvanced, LTXVImgToVideoConditionOnly, LTXVConcatAVLatent, RandomNoise, CFGGuider, KSamplerSelect, LTXVChunkFeedForward, LTXVConditioning, PrimitiveInt, PrimitiveBoolean, CLIPTextEncode, CR Text, LoadImage, MarkdownNote, MarkdownNote, VHS_VideoCombine, LTXVSeparateAVLatent, VAEDecodeTiled, LTXVAudioVAEDecode, ManualSigmas, CM_FloatToInt, PrimitiveFloat, CR Text, CR Text]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev-fp8.safetensors", "height": 25, "width": 97}
---

# 视频生成/文生视频/最强优化  LTX2.3  图 _ 文 生视频合并版_2030179257439227905.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/最强优化  LTX2.3  图 _ 文 生视频合并版_2030179257439227905.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（48 个）：
- `PathchSageAttentionKJ`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPTextEncode` ★核心
- `LTXAVTextEncoderLoader`
- `LTXVPreprocess`
- `LTXVConcatAVLatent`
- `ModelPatchTorchSettings`
- `CheckpointLoaderSimple` ★核心
- `LTXVLatentUpsampler` ★核心
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `EmptyLTXVLatentVideo`
- `LoraLoaderModelOnly` ★核心
- `LatentUpscaleModelLoader`
- `LTXVAudioVAELoader`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVImgToVideoConditionOnly`
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `CFGGuider`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `LTXVImgToVideoConditionOnly`
- `LTXVConcatAVLatent`
- `RandomNoise`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `LTXVChunkFeedForward`
- `LTXVConditioning`
- `PrimitiveInt`
- `PrimitiveBoolean`
- `CLIPTextEncode` ★核心
- `CR Text`
- `LoadImage`
- `MarkdownNote`
- `MarkdownNote`
- `VHS_VideoCombine`
- `LTXVSeparateAVLatent`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `ManualSigmas`
- `CM_FloatToInt`
- `PrimitiveFloat`
- `CR Text`
- `CR Text`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev-fp8.safetensors`
- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **92%**（44/48）

**有卡**：`PathchSageAttentionKJ`、`INTConstant`、`LayerUtility: ImageScaleByAspectRatio V2`、`CLIPTextEncode`、`LTXAVTextEncoderLoader`、`LTXVPreprocess`、`LTXVConcatAVLatent`、`ModelPatchTorchSettings`、`CheckpointLoaderSimple`、`LTXVLatentUpsampler`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`EmptyLTXVLatentVideo`、`LoraLoaderModelOnly`、`LatentUpscaleModelLoader`、`LTXVAudioVAELoader`、`LTXVEmptyLatentAudio`、`LTXVImgToVideoConditionOnly`、`ManualSigmas`、`KSamplerSelect`、`CFGGuider`、`RandomNoise`、`LTXVChunkFeedForward`、`LTXVConditioning`、`PrimitiveBoolean`、`CR Text`、`LoadImage`、`VHS_VideoCombine`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`CM_FloatToInt`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler
