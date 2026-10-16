---
key: 视频生成/图生视频/LTX2.3动作迁移（人物二创）_2036397493621104642.json
name: LTX2.3动作迁移（人物二创）_2036397493621104642.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2036397493621104642.json
hash: df1aaa837e44bd28
coverage: 0.913043
learned_at: 2026-10-15 22:35:52
nodes: [KSamplerSelect, CLIPTextEncode, LTXVChunkFeedForward, PathchSageAttentionKJ, ModelPatchTorchSettings, CheckpointLoaderSimple, LTXVPreprocess, CFGGuider, RandomNoise, SamplerCustomAdvanced, LTXVPreprocess, LTXVSeparateAVLatent, LTXAddVideoICLoRAGuide, LTXVCropGuides, PrimitiveFloat, LatentUpscaleModelLoader, LTXVConditioning, EmptyLTXVLatentVideo, PrimitiveBoolean, ManualSigmas, LTXVConcatAVLatent, VAEDecodeTiled, PrimitiveInt, CM_FloatToInt, LTXVEmptyLatentAudio, CLIPTextEncode, ImageResizeKJv2, INTConstant, INTConstant, MarkdownNote, LTXVAudioVAELoader, LoraLoaderModelOnly, LTXICLoRALoaderModelOnly, LTXAVTextEncoderLoader, VHS_VideoCombine, LoadImage, DWPreprocessor, CR Text, VHS_VideoCombine, SDPoseOODLoader, PixelPerfectResolution, MarkdownNote, SDPoseOODProcessor, YOLOModelLoader, LTXVImgToVideoConditionOnly, VHS_LoadVideo]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev-fp8.safetensors", "height": 24, "width": 121}
---

# 视频生成/图生视频/LTX2.3动作迁移（人物二创）_2036397493621104642.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2036397493621104642.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（46 个）：
- `KSamplerSelect` ★核心
- `CLIPTextEncode` ★核心
- `LTXVChunkFeedForward`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `CheckpointLoaderSimple` ★核心
- `LTXVPreprocess`
- `CFGGuider`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LTXAddVideoICLoRAGuide`
- `LTXVCropGuides`
- `PrimitiveFloat`
- `LatentUpscaleModelLoader`
- `LTXVConditioning`
- `EmptyLTXVLatentVideo`
- `PrimitiveBoolean`
- `ManualSigmas`
- `LTXVConcatAVLatent`
- `VAEDecodeTiled` ★核心
- `PrimitiveInt`
- `CM_FloatToInt`
- `LTXVEmptyLatentAudio` ★核心
- `CLIPTextEncode` ★核心
- `ImageResizeKJv2`
- `INTConstant`
- `INTConstant`
- `MarkdownNote`
- `LTXVAudioVAELoader`
- `LoraLoaderModelOnly` ★核心
- `LTXICLoRALoaderModelOnly` ★核心
- `LTXAVTextEncoderLoader`
- `VHS_VideoCombine`
- `LoadImage`
- `DWPreprocessor`
- `CR Text`
- `VHS_VideoCombine`
- `SDPoseOODLoader`
- `PixelPerfectResolution`
- `MarkdownNote`
- `SDPoseOODProcessor`
- `YOLOModelLoader`
- `LTXVImgToVideoConditionOnly`
- `VHS_LoadVideo`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev-fp8.safetensors`
- `width` = `121`
- `height` = `24`
- `batch_size` = `1`

## 知识

覆盖率 **91%**（42/46）

**有卡**：`KSamplerSelect`、`CLIPTextEncode`、`LTXVChunkFeedForward`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`CheckpointLoaderSimple`、`LTXVPreprocess`、`CFGGuider`、`RandomNoise`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`LTXAddVideoICLoRAGuide`、`LTXVCropGuides`、`LatentUpscaleModelLoader`、`LTXVConditioning`、`EmptyLTXVLatentVideo`、`PrimitiveBoolean`、`ManualSigmas`、`LTXVConcatAVLatent`、`VAEDecodeTiled`、`CM_FloatToInt`、`LTXVEmptyLatentAudio`、`ImageResizeKJv2`、`INTConstant`、`LTXVAudioVAELoader`、`LoraLoaderModelOnly`、`LTXICLoRALoaderModelOnly`、`LTXAVTextEncoderLoader`、`VHS_VideoCombine`、`LoadImage`、`DWPreprocessor`、`CR Text`、`SDPoseOODLoader`、`PixelPerfectResolution`、`SDPoseOODProcessor`、`YOLOModelLoader`、`LTXVImgToVideoConditionOnly`、`VHS_LoadVideo`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVConcatAVLatent
