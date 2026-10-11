---
key: 视频生成/文生视频/Ltx2.3反推提示词 文生音视频_2044962799889162242.json
name: Ltx2.3反推提示词 文生音视频_2044962799889162242
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Ltx2.3反推提示词 文生音视频_2044962799889162242.json
hash: 79f56a677ed0f9d8
coverage: 0.847826
learned_at: 2026-10-11 19:49:40
nodes: [LTXAVTextEncoderLoader, LTXVAudioVAELoader, EmptyImage, GetImageSize, PrimitiveInt, PrimitiveInt, PrimitiveFloat, RandomNoise, CFGGuider, KSamplerSelect, LTXVScheduler, LTXVSeparateAVLatent, LTXVCropGuides, SamplerCustomAdvanced, VAEDecodeTiled, LTXVAudioVAEDecode, ImageScaleBy, CheckpointLoaderSimple, EmptyLTXVLatentVideo, LTXVEmptyLatentAudio, LTXVConcatAVLatent, LTXVConditioning, CLIPTextEncode, DualCLIPLoader, MarkdownNote, MarkdownNote, LoadImage, TextGenerateLTX2Prompt, LoraLoaderModelOnly, CLIPTextEncode, PreviewAny, CR Text, VHS_VideoCombine, LoraLoaderModelOnly, LTXVLatentUpsampler, LatentUpscaleModelLoader, CFGGuider, LTXVConcatAVLatent, RandomNoise, ManualSigmas, KSamplerSelect, SamplerCustomAdvanced, LTXVSeparateAVLatent, VAEDecodeTiled, LTXVAudioVAEDecode, VHS_VideoCombine]
patterns: []
missing: [CR Text]
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev-fp8.safetensors", "height": 25, "width": 97}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/Ltx2.3反推提示词 文生音视频_2044962799889162242.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Ltx2.3反推提示词 文生音视频_2044962799889162242.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（46 个）：
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAELoader`
- `EmptyImage`
- `GetImageSize`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveFloat`
- `RandomNoise`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `LTXVScheduler`
- `LTXVSeparateAVLatent`
- `LTXVCropGuides`
- `SamplerCustomAdvanced` ★核心
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `ImageScaleBy`
- `CheckpointLoaderSimple` ★核心
- `EmptyLTXVLatentVideo`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `CLIPTextEncode` ★核心
- `DualCLIPLoader`
- `MarkdownNote`
- `MarkdownNote`
- `LoadImage`
- `TextGenerateLTX2Prompt`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `PreviewAny`
- `CR Text`
- `VHS_VideoCombine`
- `LoraLoaderModelOnly` ★核心
- `LTXVLatentUpsampler` ★核心
- `LatentUpscaleModelLoader`
- `CFGGuider`
- `LTXVConcatAVLatent`
- `RandomNoise`
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `VHS_VideoCombine`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev-fp8.safetensors`
- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **85%**（39/46）

**有卡**：`LTXAVTextEncoderLoader`、`LTXVAudioVAELoader`、`EmptyImage`、`GetImageSize`、`RandomNoise`、`CFGGuider`、`KSamplerSelect`、`LTXVScheduler`、`LTXVSeparateAVLatent`、`LTXVCropGuides`、`SamplerCustomAdvanced`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`ImageScaleBy`、`CheckpointLoaderSimple`、`EmptyLTXVLatentVideo`、`LTXVEmptyLatentAudio`、`LTXVConcatAVLatent`、`LTXVConditioning`、`CLIPTextEncode`、`DualCLIPLoader`、`LoadImage`、`TextGenerateLTX2Prompt`、`LoraLoaderModelOnly`、`VHS_VideoCombine`、`LTXVLatentUpsampler`、`LatentUpscaleModelLoader`、`ManualSigmas`

**缺卡**（1）：`CR Text`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
