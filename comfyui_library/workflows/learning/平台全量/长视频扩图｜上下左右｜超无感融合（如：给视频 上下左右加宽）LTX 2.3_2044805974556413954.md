---
key: 平台全量/长视频扩图｜上下左右｜超无感融合（如：给视频 上下左右加宽）LTX 2.3_2044805974556413954.json
name: 长视频扩图｜上下左右｜超无感融合（如：给视频 上下左右加宽）LTX 2.3_2044805974556413954
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/长视频扩图｜上下左右｜超无感融合（如：给视频 上下左右加宽）LTX 2.3_2044805974556413954.json
hash: 706c440aca733b5c
coverage: 0.867925
learned_at: 2026-11-14 02:49:26
nodes: [ResizeImageMaskNode, GetImageSize, CLIPTextEncode, LTXVCropGuides, LTXVEmptyLatentAudio, CM_FloatToInt, LTXVConcatAVLatent, Note, Note, Switch image [Crystools], LTXAddVideoICLoRAGuide, RandomNoise, CFGGuider, KSamplerSelect, CLIPTextEncode, EmptyLTXVLatentVideo, ManualSigmas, ImageConcanate, VAEDecodeTiled, Switch image [Crystools], LTXVSeparateAVLatent, SamplerCustomAdvanced, easy cleanGpuUsed, ImagePadKJ, LTXVAudioVAEDecode, VHS_VideoInfo, Note, LTXVImgToVideoConditionOnly, Note, ResizeImageMaskNode, ResizeImageMaskNode, PrimitiveBoolean, PrimitiveBoolean, LoadImage, Note, Color Correct (mtb), Note, LTXVConditioning, LoraLoaderModelOnly, VHS_VideoCombine, VHS_VideoCombine, VHS_LoadVideo, ModelPatchTorchSettings, LTXVChunkFeedForward, LoraLoaderModelOnly, CheckpointLoaderSimple, LTXVAudioVAELoader, LTXAVTextEncoderLoader, easy cleanGpuUsed, PathchSageAttentionKJ, LTXVPreprocess, Color Correct (mtb), Note]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev-fp8.safetensors", "height": 25, "width": 97}
---

# 平台全量/长视频扩图｜上下左右｜超无感融合（如：给视频 上下左右加宽）LTX 2.3_2044805974556413954.json

> 来源文件 `comfyui_library/workflows/平台全量/长视频扩图｜上下左右｜超无感融合（如：给视频 上下左右加宽）LTX 2.3_2044805974556413954.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（53 个）：
- `ResizeImageMaskNode`
- `GetImageSize`
- `CLIPTextEncode` ★核心
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio` ★核心
- `CM_FloatToInt`
- `LTXVConcatAVLatent`
- `Note`
- `Note`
- `Switch image [Crystools]`
- `LTXAddVideoICLoRAGuide`
- `RandomNoise`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `CLIPTextEncode` ★核心
- `EmptyLTXVLatentVideo`
- `ManualSigmas`
- `ImageConcanate`
- `VAEDecodeTiled` ★核心
- `Switch image [Crystools]`
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `easy cleanGpuUsed`
- `ImagePadKJ`
- `LTXVAudioVAEDecode` ★核心
- `VHS_VideoInfo`
- `Note`
- `LTXVImgToVideoConditionOnly`
- `Note`
- `ResizeImageMaskNode`
- `ResizeImageMaskNode`
- `PrimitiveBoolean`
- `PrimitiveBoolean`
- `LoadImage`
- `Note`
- `Color Correct (mtb)`
- `Note`
- `LTXVConditioning`
- `LoraLoaderModelOnly` ★核心
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `ModelPatchTorchSettings`
- `LTXVChunkFeedForward`
- `LoraLoaderModelOnly` ★核心
- `CheckpointLoaderSimple` ★核心
- `LTXVAudioVAELoader`
- `LTXAVTextEncoderLoader`
- `easy cleanGpuUsed`
- `PathchSageAttentionKJ`
- `LTXVPreprocess`
- `Color Correct (mtb)`
- `Note`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-dev-fp8.safetensors`

## 知识

覆盖率 **87%**（46/53）

**有卡**：`ResizeImageMaskNode`、`GetImageSize`、`CLIPTextEncode`、`LTXVCropGuides`、`LTXVEmptyLatentAudio`、`CM_FloatToInt`、`LTXVConcatAVLatent`、`Switch image [Crystools]`、`LTXAddVideoICLoRAGuide`、`RandomNoise`、`CFGGuider`、`KSamplerSelect`、`EmptyLTXVLatentVideo`、`ManualSigmas`、`ImageConcanate`、`VAEDecodeTiled`、`LTXVSeparateAVLatent`、`SamplerCustomAdvanced`、`easy cleanGpuUsed`、`ImagePadKJ`、`LTXVAudioVAEDecode`、`VHS_VideoInfo`、`LTXVImgToVideoConditionOnly`、`PrimitiveBoolean`、`LoadImage`、`Color Correct (mtb)`、`LTXVConditioning`、`LoraLoaderModelOnly`、`VHS_VideoCombine`、`VHS_LoadVideo`、`ModelPatchTorchSettings`、`LTXVChunkFeedForward`、`CheckpointLoaderSimple`、`LTXVAudioVAELoader`、`LTXAVTextEncoderLoader`、`PathchSageAttentionKJ`、`LTXVPreprocess`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、EmptyLTXVLatentVideo
