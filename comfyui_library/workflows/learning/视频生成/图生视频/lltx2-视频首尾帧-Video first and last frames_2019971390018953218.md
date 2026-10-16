---
key: 视频生成/图生视频/lltx2-视频首尾帧-Video first and last frames_2019971390018953218.json
name: lltx2-视频首尾帧-Video first and last frames_2019971390018953218.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2019971390018953218.json
hash: 28670e39d11e0db1
coverage: 0.930233
learned_at: 2026-10-15 22:35:05
nodes: [PathchSageAttentionKJ, LTXVChunkFeedForward, LoraLoaderModelOnly, PrimitiveInt, DualCLIPLoader, LTXVPreprocess, PrimitiveInt, LTXVPreprocess, LayerUtility: ImageScaleByAspectRatio V2, LTXVCropGuides, LTXVAudioVAEDecode, CLIPTextEncode, CLIPTextEncode, LTXVConditioning, FL_IntToFloat, AudioConcat, EmptyLTXVLatentVideo, MathExpression|pysssss, VAEDecodeTiled, LTXVSeparateAVLatent, RH_LLMAPI_NODE, VAELoaderKJ, JWInteger, ImageResizeKJv2, LoraLoaderModelOnly, PrimitiveInt, LTXVEmptyLatentAudio, CFGGuider, LTXVNormalizingSampler, KSamplerSelect, RandomNoise, LTXVConcatAVLatent, BasicScheduler, LoadImage, LoadImage, VHS_VideoCombine, LTXVAddGuideMulti, VAELoaderKJ, GetImageRangeFromBatch, CheckpointLoaderSimple, RH_LLMAPI_Pro_Node, ImageSharpen, ImageSharpen]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx2-phr00tmerge-sfw-v5.safetensors", "height": 20, "width": 93}
---

# 视频生成/图生视频/lltx2-视频首尾帧-Video first and last frames_2019971390018953218.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2019971390018953218.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（43 个）：
- `PathchSageAttentionKJ`
- `LTXVChunkFeedForward`
- `LoraLoaderModelOnly` ★核心
- `PrimitiveInt`
- `DualCLIPLoader`
- `LTXVPreprocess`
- `PrimitiveInt`
- `LTXVPreprocess`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LTXVCropGuides`
- `LTXVAudioVAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `FL_IntToFloat`
- `AudioConcat`
- `EmptyLTXVLatentVideo`
- `MathExpression|pysssss`
- `VAEDecodeTiled` ★核心
- `LTXVSeparateAVLatent`
- `RH_LLMAPI_NODE`
- `VAELoaderKJ`
- `JWInteger`
- `ImageResizeKJv2`
- `LoraLoaderModelOnly` ★核心
- `PrimitiveInt`
- `LTXVEmptyLatentAudio` ★核心
- `CFGGuider`
- `LTXVNormalizingSampler` ★核心
- `KSamplerSelect` ★核心
- `RandomNoise`
- `LTXVConcatAVLatent`
- `BasicScheduler`
- `LoadImage`
- `LoadImage`
- `VHS_VideoCombine`
- `LTXVAddGuideMulti`
- `VAELoaderKJ`
- `GetImageRangeFromBatch`
- `CheckpointLoaderSimple` ★核心
- `RH_LLMAPI_Pro_Node`
- `ImageSharpen`
- `ImageSharpen`

## 关键参数

- `width` = `93`
- `height` = `20`
- `batch_size` = `1`
- `checkpoint` = `ltx2-phr00tmerge-sfw-v5.safetensors`

## 知识

覆盖率 **93%**（40/43）

**有卡**：`PathchSageAttentionKJ`、`LTXVChunkFeedForward`、`LoraLoaderModelOnly`、`DualCLIPLoader`、`LTXVPreprocess`、`LayerUtility: ImageScaleByAspectRatio V2`、`LTXVCropGuides`、`LTXVAudioVAEDecode`、`CLIPTextEncode`、`LTXVConditioning`、`FL_IntToFloat`、`AudioConcat`、`EmptyLTXVLatentVideo`、`MathExpression|pysssss`、`VAEDecodeTiled`、`LTXVSeparateAVLatent`、`RH_LLMAPI_NODE`、`VAELoaderKJ`、`JWInteger`、`ImageResizeKJv2`、`LTXVEmptyLatentAudio`、`CFGGuider`、`LTXVNormalizingSampler`、`KSamplerSelect`、`RandomNoise`、`LTXVConcatAVLatent`、`BasicScheduler`、`LoadImage`、`VHS_VideoCombine`、`LTXVAddGuideMulti`、`GetImageRangeFromBatch`、`CheckpointLoaderSimple`、`RH_LLMAPI_Pro_Node`、`ImageSharpen`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、LayerUtility: ImageScaleByAspectRatio V2、CFGGuider、KSamplerSelect、LTXVNormalizingSampler
