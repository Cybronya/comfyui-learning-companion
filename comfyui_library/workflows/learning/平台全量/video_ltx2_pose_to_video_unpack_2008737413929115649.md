---
key: 平台全量/video_ltx2_pose_to_video_unpack_2008737413929115649.json
name: video_ltx2_pose_to_video_unpack_2008737413929115649
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/video_ltx2_pose_to_video_unpack_2008737413929115649.json
hash: 669e322edd79cc6f
coverage: 0.906977
learned_at: 2026-11-14 01:18:40
nodes: [GetVideoComponents, ImageFromBatch, ImageScaleBy, ImageScaleToMaxDimension, MarkdownNote, CFGGuider, KSamplerSelect, ManualSigmas, LatentUpscaleModelLoader, LTXVConcatAVLatent, CFGGuider, SamplerCustomAdvanced, LTXVConditioning, CLIPTextEncode, LTXVSeparateAVLatent, Reroute, KSamplerSelect, LoraLoaderModelOnly, LTXVCropGuides, LTXVScheduler, RandomNoise, SamplerCustomAdvanced, RandomNoise, GetImageSize, PrimitiveNode, CheckpointLoaderSimple, LoraLoaderModelOnly, LTXVAudioVAELoader, LTXAVTextEncoderLoader, VAEDecodeTiled, VHS_VideoCombine, LTXVAudioVAEDecode, LTXVLatentUpsampler, VHS_VideoCombine, CLIPTextEncode, LTXVAddGuide, MarkdownNote, EmptyLTXVLatentVideo, LTXVEmptyLatentAudio, LTXVConcatAVLatent, LTXVSeparateAVLatent, DWPreprocessor, LoadVideo]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2-19b-dev-fp8.safetensors", "height": 25, "width": 97}
---

# 平台全量/video_ltx2_pose_to_video_unpack_2008737413929115649.json

> 来源文件 `comfyui_library/workflows/平台全量/video_ltx2_pose_to_video_unpack_2008737413929115649.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（43 个）：
- `GetVideoComponents`
- `ImageFromBatch`
- `ImageScaleBy`
- `ImageScaleToMaxDimension`
- `MarkdownNote`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `LatentUpscaleModelLoader`
- `LTXVConcatAVLatent`
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `LTXVConditioning`
- `CLIPTextEncode` ★核心
- `LTXVSeparateAVLatent`
- `Reroute`
- `KSamplerSelect` ★核心
- `LoraLoaderModelOnly` ★核心
- `LTXVCropGuides`
- `LTXVScheduler`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `GetImageSize`
- `PrimitiveNode`
- `CheckpointLoaderSimple` ★核心
- `LoraLoaderModelOnly` ★核心
- `LTXVAudioVAELoader`
- `LTXAVTextEncoderLoader`
- `VAEDecodeTiled` ★核心
- `VHS_VideoCombine`
- `LTXVAudioVAEDecode` ★核心
- `LTXVLatentUpsampler` ★核心
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心
- `LTXVAddGuide`
- `MarkdownNote`
- `EmptyLTXVLatentVideo`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `DWPreprocessor`
- `LoadVideo`

## 关键参数

- `checkpoint` = `ltx-2-19b-dev-fp8.safetensors`
- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **91%**（39/43）

**有卡**：`GetVideoComponents`、`ImageFromBatch`、`ImageScaleBy`、`ImageScaleToMaxDimension`、`CFGGuider`、`KSamplerSelect`、`ManualSigmas`、`LatentUpscaleModelLoader`、`LTXVConcatAVLatent`、`SamplerCustomAdvanced`、`LTXVConditioning`、`CLIPTextEncode`、`LTXVSeparateAVLatent`、`LoraLoaderModelOnly`、`LTXVCropGuides`、`LTXVScheduler`、`RandomNoise`、`GetImageSize`、`CheckpointLoaderSimple`、`LTXVAudioVAELoader`、`LTXAVTextEncoderLoader`、`VAEDecodeTiled`、`VHS_VideoCombine`、`LTXVAudioVAEDecode`、`LTXVLatentUpsampler`、`LTXVAddGuide`、`EmptyLTXVLatentVideo`、`LTXVEmptyLatentAudio`、`DWPreprocessor`、`LoadVideo`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、CFGGuider、KSamplerSelect、LTXVLatentUpsampler、SamplerCustomAdvanced、EmptyLTXVLatentVideo
