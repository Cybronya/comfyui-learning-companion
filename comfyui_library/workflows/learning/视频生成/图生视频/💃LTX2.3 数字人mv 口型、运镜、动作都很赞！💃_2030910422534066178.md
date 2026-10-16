---
key: 视频生成/图生视频/💃LTX2.3 数字人mv 口型、运镜、动作都很赞！💃_2030910422534066178.json
name: 💃LTX2.3 数字人mv 口型、运镜、动作都很赞！💃_2030910422534066178.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2030910422534066178.json
hash: 170cdaeb968b9529
coverage: 0.960784
learned_at: 2026-10-15 22:35:28
nodes: [CheckpointLoaderSimple, LoraLoaderModelOnly, PathchSageAttentionKJ, LoraLoaderModelOnly, LTXAVTextEncoderLoader, SimpleMath+, ModelPatchTorchSettings, LTXVPreprocess, PrimitiveBoolean, LTXVAudioVAELoader, LTXVImgToVideoConditionOnly, LTXVChunkFeedForward, CM_FloatToInt, DapaoImageAspectRatioResizeNode, EmptyLTXVLatentVideo, CLIPTextEncode, RH_LLMAPI_Pro_Node, CLIPTextEncode, PreviewAny, easy int, easy int, easy int, Seed (rgthree), LoadImage, LTXVConditioning, LTXVConcatAVLatent, MelBandRoFormerModelLoader, MelBandRoFormerSampler, LoadAudio, SoundFlow_GetLength, SolidMask, CR Text, TrimAudioDuration, LTXVImgToVideoConditionOnly, LTXVChunkFeedForward, PrimitiveFloat, CM_FloatToInt, SetLatentNoiseMask, LTXVAudioVAEEncode, CFGGuider, LTXVEmptyLatentAudio, VAEDecodeTiled, easy cleanGpuUsed, VHS_VideoCombine, LTXVAudioVAEDecode, KSamplerSelect, ManualSigmas, RandomNoise, CR Text, SamplerCustomAdvanced, LTXVSeparateAVLatent]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "height": 25, "width": 97}
---

# 视频生成/图生视频/💃LTX2.3 数字人mv 口型、运镜、动作都很赞！💃_2030910422534066178.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2030910422534066178.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Other

**节点**（51 个）：
- `CheckpointLoaderSimple` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `LTXAVTextEncoderLoader`
- `SimpleMath+`
- `ModelPatchTorchSettings`
- `LTXVPreprocess`
- `PrimitiveBoolean`
- `LTXVAudioVAELoader`
- `LTXVImgToVideoConditionOnly`
- `LTXVChunkFeedForward`
- `CM_FloatToInt`
- `DapaoImageAspectRatioResizeNode`
- `EmptyLTXVLatentVideo`
- `CLIPTextEncode` ★核心
- `RH_LLMAPI_Pro_Node`
- `CLIPTextEncode` ★核心
- `PreviewAny`
- `easy int`
- `easy int`
- `easy int`
- `Seed (rgthree)`
- `LoadImage`
- `LTXVConditioning`
- `LTXVConcatAVLatent`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler` ★核心
- `LoadAudio`
- `SoundFlow_GetLength`
- `SolidMask`
- `CR Text`
- `TrimAudioDuration`
- `LTXVImgToVideoConditionOnly`
- `LTXVChunkFeedForward`
- `PrimitiveFloat`
- `CM_FloatToInt`
- `SetLatentNoiseMask`
- `LTXVAudioVAEEncode` ★核心
- `CFGGuider`
- `LTXVEmptyLatentAudio` ★核心
- `VAEDecodeTiled` ★核心
- `easy cleanGpuUsed`
- `VHS_VideoCombine`
- `LTXVAudioVAEDecode` ★核心
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `RandomNoise`
- `CR Text`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev.safetensors`
- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **96%**（49/51）

**有卡**：`CheckpointLoaderSimple`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`LTXAVTextEncoderLoader`、`SimpleMath+`、`ModelPatchTorchSettings`、`LTXVPreprocess`、`PrimitiveBoolean`、`LTXVAudioVAELoader`、`LTXVImgToVideoConditionOnly`、`LTXVChunkFeedForward`、`CM_FloatToInt`、`DapaoImageAspectRatioResizeNode`、`EmptyLTXVLatentVideo`、`CLIPTextEncode`、`RH_LLMAPI_Pro_Node`、`easy int`、`Seed (rgthree)`、`LoadImage`、`LTXVConditioning`、`LTXVConcatAVLatent`、`MelBandRoFormerModelLoader`、`MelBandRoFormerSampler`、`LoadAudio`、`SoundFlow_GetLength`、`SolidMask`、`CR Text`、`TrimAudioDuration`、`SetLatentNoiseMask`、`LTXVAudioVAEEncode`、`CFGGuider`、`LTXVEmptyLatentAudio`、`VAEDecodeTiled`、`easy cleanGpuUsed`、`VHS_VideoCombine`、`LTXVAudioVAEDecode`、`KSamplerSelect`、`ManualSigmas`、`RandomNoise`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、MelBandRoFormerSampler
