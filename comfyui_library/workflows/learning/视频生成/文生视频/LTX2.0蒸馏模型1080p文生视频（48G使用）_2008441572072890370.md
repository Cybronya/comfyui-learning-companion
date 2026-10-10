---
key: 视频生成/文生视频/LTX2.0蒸馏模型1080p文生视频（48G使用）_2008441572072890370.json
name: LTX2.0蒸馏模型1080p文生视频（48G使用）_2008441572072890370
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.0蒸馏模型1080p文生视频（48G使用）_2008441572072890370.json
hash: 0b39368c000e7560
coverage: 0.755556
learned_at: 2026-10-10 23:00:18
nodes: [MarkdownNote, SaveVideo, MarkdownNote, MarkdownNote, b7c2d337-c38d-4c04-922b-2d638449d13e, PrimitiveInt, PrimitiveFloat, LTXVEmptyLatentAudio, ImageScaleBy, ManualSigmas, LTXVConcatAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, RandomNoise, EmptyLTXVLatentVideo, CFGGuider, KSamplerSelect, MarkdownNote, MarkdownNote, GetImageSize, KSamplerSelect, ManualSigmas, LTXVConcatAVLatent, CFGGuider, LatentUpscaleModelLoader, LTXAVTextEncoderLoader, LTXVConditioning, CLIPTextEncode, MarkdownNote, PrimitiveInt, LTXVLatentUpsampler, SamplerCustomAdvanced, VAEDecodeTiled, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVAudioVAEDecode, VAEDecodeTiled, VHS_VideoCombine, LTXVSeparateAVLatent, VHS_VideoCombine, RandomNoise, CheckpointLoaderSimple, EmptyImage, PrimitiveStringMultiline, LoraLoaderModelOnly]
patterns: []
missing: [b7c2d337-c38d-4c04-922b-2d638449d13e]
parameters: {"batch_size": 1, "checkpoint": "ltx-2-19b-distilled-fp8.safetensors", "height": 25, "width": 121}
discoveries: [次要节点 `b7c2d337-c38d-4c04-922b-2d638449d13e` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/LTX2.0蒸馏模型1080p文生视频（48G使用）_2008441572072890370.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.0蒸馏模型1080p文生视频（48G使用）_2008441572072890370.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（45 个）：
- `MarkdownNote`
- `SaveVideo`
- `MarkdownNote`
- `MarkdownNote`
- `b7c2d337-c38d-4c04-922b-2d638449d13e`
- `PrimitiveInt`
- `PrimitiveFloat`
- `LTXVEmptyLatentAudio` ★核心
- `ImageScaleBy`
- `ManualSigmas`
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `RandomNoise`
- `EmptyLTXVLatentVideo`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `MarkdownNote`
- `MarkdownNote`
- `GetImageSize`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `LTXVConcatAVLatent`
- `CFGGuider`
- `LatentUpscaleModelLoader`
- `LTXAVTextEncoderLoader`
- `LTXVConditioning`
- `CLIPTextEncode` ★核心
- `MarkdownNote`
- `PrimitiveInt`
- `LTXVLatentUpsampler` ★核心
- `SamplerCustomAdvanced` ★核心
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `LTXVAudioVAELoader`
- `LTXVAudioVAEDecode` ★核心
- `VAEDecodeTiled` ★核心
- `VHS_VideoCombine`
- `LTXVSeparateAVLatent`
- `VHS_VideoCombine`
- `RandomNoise`
- `CheckpointLoaderSimple` ★核心
- `EmptyImage`
- `PrimitiveStringMultiline`
- `LoraLoaderModelOnly` ★核心

## 关键参数

- `width` = `121`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2-19b-distilled-fp8.safetensors`

## 知识

覆盖率 **76%**（34/45）

**有卡**：`SaveVideo`、`LTXVEmptyLatentAudio`、`ImageScaleBy`、`ManualSigmas`、`LTXVConcatAVLatent`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`RandomNoise`、`EmptyLTXVLatentVideo`、`CFGGuider`、`KSamplerSelect`、`GetImageSize`、`LatentUpscaleModelLoader`、`LTXAVTextEncoderLoader`、`LTXVConditioning`、`CLIPTextEncode`、`LTXVLatentUpsampler`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`LTXVAudioVAELoader`、`VHS_VideoCombine`、`CheckpointLoaderSimple`、`EmptyImage`、`LoraLoaderModelOnly`

**缺卡**（1）：`b7c2d337-c38d-4c04-922b-2d638449d13e`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler、LTXVConcatAVLatent

## 学习发现

- 次要节点 `b7c2d337-c38d-4c04-922b-2d638449d13e` 知识库中没有该节点类型的任何知识
