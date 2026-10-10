---
key: 视频生成/文生视频/AA--音画同步视频-LTX2.0文生视频+放大+插帧_2008918263912206338.json
name: AA--音画同步视频-LTX2.0文生视频+放大+插帧_2008918263912206338
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/AA--音画同步视频-LTX2.0文生视频+放大+插帧_2008918263912206338.json
hash: c3d467c8eb8c3180
coverage: 0.714286
learned_at: 2026-10-11 03:07:08
nodes: [LTXVCropGuides, LTXVSeparateAVLatent, KSamplerSelect, CheckpointLoaderSimple, LTXVAudioVAELoader, LTXAVTextEncoderLoader, LTXVConcatAVLatent, SamplerCustomAdvanced, ManualSigmas, KSamplerSelect, LTXVConcatAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, RandomNoise, PrimitiveNode, EmptyLTXVLatentVideo, LoraLoaderModelOnly, LTXVAudioVAEDecode, VAEDecodeTiled, PrimitiveInt, GetImageSize, ImageScaleBy, CLIPTextEncode, LTXVConditioning, RandomNoise, LatentUpscaleModelLoader, LTXVLatentUpsampler, CFGGuider, LTXVScheduler, CreateVideo, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, SaveVideo, VAEDecode, MarkdownNote, Note, MarkdownNote, Note, RIFE VFI, JWInteger, JWInteger, VHS_VideoInfo, FlashVSRNode, easy showAnything, easy showAnything, easy showAnything, easy showAnything, CM_IntToFloat, CM_FloatBinaryOperation, VHS_LoadVideo, VHS_VideoCombine, MarkdownNote, Note, EmptyImage, LTXVEmptyLatentAudio, PrimitiveFloat, PrimitiveInt, Fast Groups Bypasser (rgthree), CFGGuider, Note, Note, CLIPTextEncode]
patterns: []
missing: [RIFE VFI]
parameters: {"batch_size": 1, "checkpoint": "ltx-2-19b-dev-fp8.safetensors", "height": 25, "width": 97}
discoveries: [次要节点 `RIFE VFI` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/AA--音画同步视频-LTX2.0文生视频+放大+插帧_2008918263912206338.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/AA--音画同步视频-LTX2.0文生视频+放大+插帧_2008918263912206338.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（63 个）：
- `LTXVCropGuides`
- `LTXVSeparateAVLatent`
- `KSamplerSelect` ★核心
- `CheckpointLoaderSimple` ★核心
- `LTXVAudioVAELoader`
- `LTXAVTextEncoderLoader`
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `RandomNoise`
- `PrimitiveNode`
- `EmptyLTXVLatentVideo`
- `LoraLoaderModelOnly` ★核心
- `LTXVAudioVAEDecode` ★核心
- `VAEDecodeTiled` ★核心
- `PrimitiveInt`
- `GetImageSize`
- `ImageScaleBy`
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `RandomNoise`
- `LatentUpscaleModelLoader`
- `LTXVLatentUpsampler` ★核心
- `CFGGuider`
- `LTXVScheduler`
- `CreateVideo`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `SaveVideo`
- `VAEDecode` ★核心
- `MarkdownNote`
- `Note`
- `MarkdownNote`
- `Note`
- `RIFE VFI`
- `JWInteger`
- `JWInteger`
- `VHS_VideoInfo`
- `FlashVSRNode`
- `easy showAnything`
- `easy showAnything`
- `easy showAnything`
- `easy showAnything`
- `CM_IntToFloat`
- `CM_FloatBinaryOperation`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `MarkdownNote`
- `Note`
- `EmptyImage`
- `LTXVEmptyLatentAudio` ★核心
- `PrimitiveFloat`
- `PrimitiveInt`
- `Fast Groups Bypasser (rgthree)`
- `CFGGuider`
- `Note`
- `Note`
- `CLIPTextEncode` ★核心

## 关键参数

- `checkpoint` = `ltx-2-19b-dev-fp8.safetensors`
- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **71%**（45/63）

**有卡**：`LTXVCropGuides`、`LTXVSeparateAVLatent`、`KSamplerSelect`、`CheckpointLoaderSimple`、`LTXVAudioVAELoader`、`LTXAVTextEncoderLoader`、`LTXVConcatAVLatent`、`SamplerCustomAdvanced`、`ManualSigmas`、`RandomNoise`、`EmptyLTXVLatentVideo`、`LoraLoaderModelOnly`、`LTXVAudioVAEDecode`、`VAEDecodeTiled`、`GetImageSize`、`ImageScaleBy`、`CLIPTextEncode`、`LTXVConditioning`、`LatentUpscaleModelLoader`、`LTXVLatentUpsampler`、`CFGGuider`、`LTXVScheduler`、`CreateVideo`、`SaveVideo`、`VAEDecode`、`JWInteger`、`VHS_VideoInfo`、`FlashVSRNode`、`CM_IntToFloat`、`CM_FloatBinaryOperation`、`VHS_LoadVideo`、`VHS_VideoCombine`、`EmptyImage`、`LTXVEmptyLatentAudio`

**缺卡**（1）：`RIFE VFI`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler

## 学习发现

- 次要节点 `RIFE VFI` 知识库中没有该节点类型的任何知识
