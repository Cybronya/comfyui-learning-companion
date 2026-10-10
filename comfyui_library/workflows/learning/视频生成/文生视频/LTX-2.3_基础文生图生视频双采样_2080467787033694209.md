---
key: 视频生成/文生视频/LTX-2.3_基础文生图生视频双采样_2080467787033694209.json
name: LTX-2.3_基础文生图生视频双采样_2080467787033694209
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX-2.3_基础文生图生视频双采样_2080467787033694209.json
hash: 0add3f26d3d7f4b9
coverage: 0.878049
learned_at: 2026-10-10 23:00:14
nodes: [LTXVEmptyLatentAudio, LTXVConcatAVLatent, LTXVImgToVideoConditionOnly, LTXVConditioning, KSamplerSelect, SamplerCustomAdvanced, CFGGuider, LTXVPreprocess, CLIPTextEncode, RandomNoise, CFGGuider, KSamplerSelect, SamplerCustomAdvanced, RandomNoise, ManualSigmas, ManualSigmas, LTXVConcatAVLatent, LTXVLatentUpsampler, LTXVSeparateAVLatent, LTXVSeparateAVLatent, LTXVAudioVAEDecode, CreateVideo, LTXVTiledVAEDecode, Note, LTXAVTextEncoderLoader, PrimitiveFloat, PrimitiveInt, LatentUpscaleModelLoader, LoraLoaderModelOnly, LTXVAudioVAELoader, CheckpointLoaderSimple, PrimitiveBoolean, Reroute, EmptyLTXVLatentVideo, LTXVImgToVideoConditionOnly, SaveVideo, LoadImage, CLIPTextEncode, LayerUtility: ImageScaleByAspectRatio V2, LTXFloatToInt, LoadImage]
patterns: []
missing: [LayerUtility: ImageScaleByAspectRatio V2]
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "height": 25, "width": 97}
discoveries: [次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/LTX-2.3_基础文生图生视频双采样_2080467787033694209.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX-2.3_基础文生图生视频双采样_2080467787033694209.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（41 个）：
- `LTXVEmptyLatentAudio` ★核心
- `LTXVConcatAVLatent`
- `LTXVImgToVideoConditionOnly`
- `LTXVConditioning`
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `CFGGuider`
- `LTXVPreprocess`
- `CLIPTextEncode` ★核心
- `RandomNoise`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `ManualSigmas`
- `ManualSigmas`
- `LTXVConcatAVLatent`
- `LTXVLatentUpsampler` ★核心
- `LTXVSeparateAVLatent`
- `LTXVSeparateAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `CreateVideo`
- `LTXVTiledVAEDecode` ★核心
- `Note`
- `LTXAVTextEncoderLoader`
- `PrimitiveFloat`
- `PrimitiveInt`
- `LatentUpscaleModelLoader`
- `LoraLoaderModelOnly` ★核心
- `LTXVAudioVAELoader`
- `CheckpointLoaderSimple` ★核心
- `PrimitiveBoolean`
- `Reroute`
- `EmptyLTXVLatentVideo`
- `LTXVImgToVideoConditionOnly`
- `SaveVideo`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LTXFloatToInt`
- `LoadImage`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-dev.safetensors`

## 知识

覆盖率 **88%**（36/41）

**有卡**：`LTXVEmptyLatentAudio`、`LTXVConcatAVLatent`、`LTXVImgToVideoConditionOnly`、`LTXVConditioning`、`KSamplerSelect`、`SamplerCustomAdvanced`、`CFGGuider`、`LTXVPreprocess`、`CLIPTextEncode`、`RandomNoise`、`ManualSigmas`、`LTXVLatentUpsampler`、`LTXVSeparateAVLatent`、`LTXVAudioVAEDecode`、`CreateVideo`、`LTXVTiledVAEDecode`、`LTXAVTextEncoderLoader`、`LatentUpscaleModelLoader`、`LoraLoaderModelOnly`、`LTXVAudioVAELoader`、`CheckpointLoaderSimple`、`PrimitiveBoolean`、`EmptyLTXVLatentVideo`、`SaveVideo`、`LoadImage`、`LTXFloatToInt`

**缺卡**（1）：`LayerUtility: ImageScaleByAspectRatio V2`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler

## 学习发现

- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
