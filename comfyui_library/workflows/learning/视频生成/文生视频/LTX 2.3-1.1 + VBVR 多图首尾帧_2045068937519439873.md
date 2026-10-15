---
key: 视频生成/文生视频/LTX 2.3-1.1 + VBVR 多图首尾帧_2045068937519439873.json
name: LTX 2.3-1.1 + VBVR 多图首尾帧_2045068937519439873
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX 2.3-1.1 + VBVR 多图首尾帧_2045068937519439873.json
hash: 55832b2c99ad236b
coverage: 0.884615
learned_at: 2026-10-15 22:44:34
nodes: [PrimitiveInt, LoadImage, LoadImage, LayerUtility: PurgeVRAM V2, VRAMReserver, LoraLoaderModelOnly, LoadImage, LoadImage, PrimitiveFloat, image_scale_pixel_v2, CLIPTextEncode, CLIPTextEncode, LoraLoaderModelOnly, VHS_VideoCombine, KSamplerSelect, ManualSigmas, KSamplerSelect, ManualSigmas, RandomNoise, KSamplerSelect, ManualSigmas, RandomNoise, LTXVAudioVAELoader, PrimitiveBoolean, RandomNoise, LatentUpscaleModelLoader, LTXAVTextEncoderLoader, ResizeLongestToNode, CM_FloatToInt, EmptyLTXVLatentVideo, LTXVPreprocess, GetImageSize+, LTXVEmptyLatentAudio, LTXVConditioning, LTXVImgToVideoConditionOnly, ImageResizeKJv2, LTXVPreprocess, ImageResizeKJv2, LTX2_NAG, LTXVPreprocess, ImageResizeKJv2, LTXVPreprocess, LTXVAddGuideMulti, CFGGuider, LTXVConcatAVLatent, easy showAnything, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVLatentUpsampler, VAEDecodeTiled, PreviewImage, CFGGuider, LTXVConcatAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVLatentUpsampler, VAEDecodeTiled, LTXVImgToVideoConditionOnly, LTXVAddGuideMulti, PreviewImage, CFGGuider, LTXVConcatAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, VAEDecodeTiled, LTXVAudioVAEDecode, JWImageSequenceExtractFromBatch, CreateVideo, LTXVAddGuideMulti, Int, Int, Int, Int, PrimitiveFloat, PrimitiveFloat, PrimitiveFloat, PrimitiveFloat, CheckpointLoaderSimple]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-distilled-1.1.safetensors", "height": 25, "width": 97}
---

# 视频生成/文生视频/LTX 2.3-1.1 + VBVR 多图首尾帧_2045068937519439873.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX 2.3-1.1 + VBVR 多图首尾帧_2045068937519439873.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（78 个）：
- `PrimitiveInt`
- `LoadImage`
- `LoadImage`
- `LayerUtility: PurgeVRAM V2`
- `VRAMReserver`
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `LoadImage`
- `PrimitiveFloat`
- `image_scale_pixel_v2`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `VHS_VideoCombine`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `RandomNoise`
- `LTXVAudioVAELoader`
- `PrimitiveBoolean`
- `RandomNoise`
- `LatentUpscaleModelLoader`
- `LTXAVTextEncoderLoader`
- `ResizeLongestToNode`
- `CM_FloatToInt`
- `EmptyLTXVLatentVideo`
- `LTXVPreprocess`
- `GetImageSize+`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVConditioning`
- `LTXVImgToVideoConditionOnly`
- `ImageResizeKJv2`
- `LTXVPreprocess`
- `ImageResizeKJv2`
- `LTX2_NAG`
- `LTXVPreprocess`
- `ImageResizeKJv2`
- `LTXVPreprocess`
- `LTXVAddGuideMulti`
- `CFGGuider`
- `LTXVConcatAVLatent`
- `easy showAnything`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LTXVLatentUpsampler` ★核心
- `VAEDecodeTiled` ★核心
- `PreviewImage`
- `CFGGuider`
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LTXVLatentUpsampler` ★核心
- `VAEDecodeTiled` ★核心
- `LTXVImgToVideoConditionOnly`
- `LTXVAddGuideMulti`
- `PreviewImage`
- `CFGGuider`
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `JWImageSequenceExtractFromBatch`
- `CreateVideo`
- `LTXVAddGuideMulti`
- `Int`
- `Int`
- `Int`
- `Int`
- `PrimitiveFloat`
- `PrimitiveFloat`
- `PrimitiveFloat`
- `PrimitiveFloat`
- `CheckpointLoaderSimple` ★核心

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-distilled-1.1.safetensors`

## 知识

覆盖率 **88%**（69/78）

**有卡**：`LoadImage`、`LayerUtility: PurgeVRAM V2`、`VRAMReserver`、`LoraLoaderModelOnly`、`image_scale_pixel_v2`、`CLIPTextEncode`、`VHS_VideoCombine`、`KSamplerSelect`、`ManualSigmas`、`RandomNoise`、`LTXVAudioVAELoader`、`PrimitiveBoolean`、`LatentUpscaleModelLoader`、`LTXAVTextEncoderLoader`、`ResizeLongestToNode`、`CM_FloatToInt`、`EmptyLTXVLatentVideo`、`LTXVPreprocess`、`GetImageSize+`、`LTXVEmptyLatentAudio`、`LTXVConditioning`、`LTXVImgToVideoConditionOnly`、`ImageResizeKJv2`、`LTX2_NAG`、`LTXVAddGuideMulti`、`CFGGuider`、`LTXVConcatAVLatent`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`LTXVLatentUpsampler`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`JWImageSequenceExtractFromBatch`、`CreateVideo`、`Int`、`CheckpointLoaderSimple`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler
