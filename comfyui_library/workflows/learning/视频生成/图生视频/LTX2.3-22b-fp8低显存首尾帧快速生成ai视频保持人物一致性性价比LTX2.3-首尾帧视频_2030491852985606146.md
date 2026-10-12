---
key: 视频生成/图生视频/LTX2.3-22b-fp8低显存首尾帧快速生成ai视频保持人物一致性性价比LTX2.3-首尾帧视频_2030491852985606146.json
name: LTX2.3-22b-fp8低显存首尾帧快速生成ai视频保持人物一致性性价比LTX2.3-首尾帧视频_2030491852985606146
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3-22b-fp8低显存首尾帧快速生成ai视频保持人物一致性性价比LTX2.3-首尾帧视频_2030491852985606146.json
hash: 806c2459c18964b3
coverage: 0.851852
learned_at: 2026-10-13 01:36:51
nodes: [LTXVConcatAVLatent, KSamplerSelect, CFGGuider, CFGGuider, KSamplerSelect, SamplerCustomAdvanced, ManualSigmas, LTXVConcatAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, VAEDecodeTiled, LTXVAudioVAEDecode, CLIPTextEncode, LTXVConditioning, CLIPTextEncode, LTXVChunkFeedForward, PathchSageAttentionKJ, ModelPatchTorchSettings, PrimitiveFloat, PrimitiveInt, VHS_VideoCombine, LTXVLatentUpsampler, RandomNoise, RandomNoise, LTXVImgToVideoConditionOnly, LatentUpscaleModelLoader, LTXVSeparateAVLatent, ManualSigmas, INTConstant, ManualSigmas, VAEDecodeTiled, LTXVAudioVAEDecode, CheckpointLoaderSimple, LTXVAudioVAELoader, LoraLoaderModelOnly, LTXAVTextEncoderLoader, CM_FloatToInt, EmptyLTXVLatentVideo, LTXVPreprocess, LTXVPreprocess, LTXVFirstLastFrameControl_TTP, LTXVEmptyLatentAudio, Fast Groups Bypasser (rgthree), LoadImage, LoadImage, MarkdownNote, MarkdownNote, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, PrimitiveBoolean, VHS_VideoCombine, CR Text, INTConstant, INTConstant]
patterns: []
missing: [CR Text, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2]
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev-fp8.safetensors", "height": 25, "width": 97}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识]
---

# 视频生成/图生视频/LTX2.3-22b-fp8低显存首尾帧快速生成ai视频保持人物一致性性价比LTX2.3-首尾帧视频_2030491852985606146.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/LTX2.3-22b-fp8低显存首尾帧快速生成ai视频保持人物一致性性价比LTX2.3-首尾帧视频_2030491852985606146.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（54 个）：
- `LTXVConcatAVLatent`
- `KSamplerSelect` ★核心
- `CFGGuider`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `ManualSigmas`
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `CLIPTextEncode` ★核心
- `LTXVChunkFeedForward`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `PrimitiveFloat`
- `PrimitiveInt`
- `VHS_VideoCombine`
- `LTXVLatentUpsampler` ★核心
- `RandomNoise`
- `RandomNoise`
- `LTXVImgToVideoConditionOnly`
- `LatentUpscaleModelLoader`
- `LTXVSeparateAVLatent`
- `ManualSigmas`
- `INTConstant`
- `ManualSigmas`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `CheckpointLoaderSimple` ★核心
- `LTXVAudioVAELoader`
- `LoraLoaderModelOnly` ★核心
- `LTXAVTextEncoderLoader`
- `CM_FloatToInt`
- `EmptyLTXVLatentVideo`
- `LTXVPreprocess`
- `LTXVPreprocess`
- `LTXVFirstLastFrameControl_TTP`
- `LTXVEmptyLatentAudio` ★核心
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `LoadImage`
- `MarkdownNote`
- `MarkdownNote`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PrimitiveBoolean`
- `VHS_VideoCombine`
- `CR Text`
- `INTConstant`
- `INTConstant`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev-fp8.safetensors`
- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **85%**（46/54）

**有卡**：`LTXVConcatAVLatent`、`KSamplerSelect`、`CFGGuider`、`SamplerCustomAdvanced`、`ManualSigmas`、`LTXVSeparateAVLatent`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`CLIPTextEncode`、`LTXVConditioning`、`LTXVChunkFeedForward`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`VHS_VideoCombine`、`LTXVLatentUpsampler`、`RandomNoise`、`LTXVImgToVideoConditionOnly`、`LatentUpscaleModelLoader`、`INTConstant`、`CheckpointLoaderSimple`、`LTXVAudioVAELoader`、`LoraLoaderModelOnly`、`LTXAVTextEncoderLoader`、`CM_FloatToInt`、`EmptyLTXVLatentVideo`、`LTXVPreprocess`、`LTXVFirstLastFrameControl_TTP`、`LTXVEmptyLatentAudio`、`LoadImage`、`PrimitiveBoolean`

**缺卡**（3）：`CR Text`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageScaleByAspectRatio V2`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
