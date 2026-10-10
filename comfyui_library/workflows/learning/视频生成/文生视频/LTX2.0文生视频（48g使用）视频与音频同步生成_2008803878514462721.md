---
key: 视频生成/文生视频/LTX2.0文生视频（48g使用）视频与音频同步生成_2008803878514462721.json
name: LTX2.0文生视频（48g使用）视频与音频同步生成_2008803878514462721
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.0文生视频（48g使用）视频与音频同步生成_2008803878514462721.json
hash: aa4f2b6826e26621
coverage: 0.82
learned_at: 2026-10-11 03:07:10
nodes: [ManualSigmas, VAEDecode, CFGGuider, MarkdownNote, KSamplerSelect, KSamplerSelect, MarkdownNote, RandomNoise, LTXVConcatAVLatent, LoraLoaderModelOnly, Reroute, LTXVLatentUpsampler, LTXVCropGuides, GetImageSize, EmptyLTXVLatentVideo, LTXVEmptyLatentAudio, LatentUpscaleModelLoader, LTXVConditioning, CLIPTextEncode, SamplerCustomAdvanced, CheckpointLoaderSimple, LTXVConcatAVLatent, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVSeparateAVLatent, VAEDecodeTiled, PrimitiveInt, LTXAVTextEncoderLoader, CFGGuider, LTXVScheduler, RandomNoise, LoraLoaderModelOnly, LoraLoaderModelOnly, PrimitiveInt, PrimitiveFloat, LTXVSeparateAVLatent, VAEDecode, LTXVAudioVAEDecode, MarkdownNote, Int, MathExpression|pysssss, SamplerCustomAdvanced, VHS_VideoCombine, VHS_VideoCombine, LoraLoaderModelOnly, Int, ImageScaleBy, CLIPTextEncode, EmptyImage, CR Text]
patterns: []
missing: [CR Text, MathExpression|pysssss]
parameters: {"batch_size": 1, "checkpoint": "ltx-2-19b-dev-fp8.safetensors", "height": 25, "width": 97}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/LTX2.0文生视频（48g使用）视频与音频同步生成_2008803878514462721.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.0文生视频（48g使用）视频与音频同步生成_2008803878514462721.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（50 个）：
- `ManualSigmas`
- `VAEDecode` ★核心
- `CFGGuider`
- `MarkdownNote`
- `KSamplerSelect` ★核心
- `KSamplerSelect` ★核心
- `MarkdownNote`
- `RandomNoise`
- `LTXVConcatAVLatent`
- `LoraLoaderModelOnly` ★核心
- `Reroute`
- `LTXVLatentUpsampler` ★核心
- `LTXVCropGuides`
- `GetImageSize`
- `EmptyLTXVLatentVideo`
- `LTXVEmptyLatentAudio` ★核心
- `LatentUpscaleModelLoader`
- `LTXVConditioning`
- `CLIPTextEncode` ★核心
- `SamplerCustomAdvanced` ★核心
- `CheckpointLoaderSimple` ★核心
- `LTXVConcatAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `LTXVAudioVAELoader`
- `LTXVSeparateAVLatent`
- `VAEDecodeTiled` ★核心
- `PrimitiveInt`
- `LTXAVTextEncoderLoader`
- `CFGGuider`
- `LTXVScheduler`
- `RandomNoise`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `PrimitiveInt`
- `PrimitiveFloat`
- `LTXVSeparateAVLatent`
- `VAEDecode` ★核心
- `LTXVAudioVAEDecode` ★核心
- `MarkdownNote`
- `Int`
- `MathExpression|pysssss`
- `SamplerCustomAdvanced` ★核心
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `LoraLoaderModelOnly` ★核心
- `Int`
- `ImageScaleBy`
- `CLIPTextEncode` ★核心
- `EmptyImage`
- `CR Text`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2-19b-dev-fp8.safetensors`

## 知识

覆盖率 **82%**（41/50）

**有卡**：`ManualSigmas`、`VAEDecode`、`CFGGuider`、`KSamplerSelect`、`RandomNoise`、`LTXVConcatAVLatent`、`LoraLoaderModelOnly`、`LTXVLatentUpsampler`、`LTXVCropGuides`、`GetImageSize`、`EmptyLTXVLatentVideo`、`LTXVEmptyLatentAudio`、`LatentUpscaleModelLoader`、`LTXVConditioning`、`CLIPTextEncode`、`SamplerCustomAdvanced`、`CheckpointLoaderSimple`、`LTXVAudioVAEDecode`、`LTXVAudioVAELoader`、`LTXVSeparateAVLatent`、`VAEDecodeTiled`、`LTXAVTextEncoderLoader`、`LTXVScheduler`、`Int`、`VHS_VideoCombine`、`ImageScaleBy`、`EmptyImage`

**缺卡**（2）：`CR Text`、`MathExpression|pysssss`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
