---
key: 视频生成/图生视频/LTX2.3-22b-fp8低显存首尾帧快速生成ai视频保持人物一致性性价比LTX2.3-首尾帧视频_2030519163785060353.json
name: LTX2.3-22b-fp8低显存首尾帧快速生成ai视频保持人物一致性性价比LTX2.3-首尾帧视频_2030519163785060353.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3-22b-fp8低显存首尾帧快速生成ai视频保持人物一致性性价比LTX2.3-首尾帧视频_2030519163785060353.json
hash: 82ce57bed2c6c065
coverage: 0.907407
learned_at: 2026-10-15 22:35:26
nodes: [LTXVConcatAVLatent, KSamplerSelect, CFGGuider, CFGGuider, KSamplerSelect, SamplerCustomAdvanced, ManualSigmas, LTXVConcatAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, VAEDecodeTiled, LTXVAudioVAEDecode, CLIPTextEncode, LTXVConditioning, CLIPTextEncode, LTXVChunkFeedForward, PathchSageAttentionKJ, ModelPatchTorchSettings, PrimitiveFloat, PrimitiveInt, VHS_VideoCombine, LTXVLatentUpsampler, RandomNoise, RandomNoise, LTXVImgToVideoConditionOnly, LatentUpscaleModelLoader, LTXVSeparateAVLatent, ManualSigmas, INTConstant, ManualSigmas, VAEDecodeTiled, LTXVAudioVAEDecode, CheckpointLoaderSimple, LTXVAudioVAELoader, LTXAVTextEncoderLoader, CM_FloatToInt, EmptyLTXVLatentVideo, LTXVPreprocess, LTXVPreprocess, LTXVFirstLastFrameControl_TTP, LTXVEmptyLatentAudio, Fast Groups Bypasser (rgthree), MarkdownNote, MarkdownNote, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, PrimitiveBoolean, VHS_VideoCombine, INTConstant, INTConstant, LoadImage, LoadImage, LoraLoaderModelOnly, CR Text]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev-fp8.safetensors", "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX2.3-22b-fp8低显存首尾帧快速生成ai视频保持人物一致性性价比LTX2.3-首尾帧视频_2030519163785060353.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2030519163785060353.json`

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
- `LTXAVTextEncoderLoader`
- `CM_FloatToInt`
- `EmptyLTXVLatentVideo`
- `LTXVPreprocess`
- `LTXVPreprocess`
- `LTXVFirstLastFrameControl_TTP`
- `LTXVEmptyLatentAudio` ★核心
- `Fast Groups Bypasser (rgthree)`
- `MarkdownNote`
- `MarkdownNote`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PrimitiveBoolean`
- `VHS_VideoCombine`
- `INTConstant`
- `INTConstant`
- `LoadImage`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `CR Text`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev-fp8.safetensors`
- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **91%**（49/54）

**有卡**：`LTXVConcatAVLatent`、`KSamplerSelect`、`CFGGuider`、`SamplerCustomAdvanced`、`ManualSigmas`、`LTXVSeparateAVLatent`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`CLIPTextEncode`、`LTXVConditioning`、`LTXVChunkFeedForward`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`VHS_VideoCombine`、`LTXVLatentUpsampler`、`RandomNoise`、`LTXVImgToVideoConditionOnly`、`LatentUpscaleModelLoader`、`INTConstant`、`CheckpointLoaderSimple`、`LTXVAudioVAELoader`、`LTXAVTextEncoderLoader`、`CM_FloatToInt`、`EmptyLTXVLatentVideo`、`LTXVPreprocess`、`LTXVFirstLastFrameControl_TTP`、`LTXVEmptyLatentAudio`、`LayerUtility: ImageScaleByAspectRatio V2`、`PrimitiveBoolean`、`LoadImage`、`LoraLoaderModelOnly`、`CR Text`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler
