---
key: 视频生成/文生视频/LTX2.3_四宫格漫剧视频_2064675254458474498.json
name: LTX2.3_四宫格漫剧视频_2064675254458474498
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.3_四宫格漫剧视频_2064675254458474498.json
hash: da9af30493ed4014
coverage: 0.755556
learned_at: 2026-10-11 20:21:26
nodes: [LatentUpscaleModelLoader, KSamplerSelect, RandomNoise, DualCLIPLoader, VAELoader, VAELoaderKJ, ManualSigmas, UNETLoader, CLIPTextEncode, GuHaiAutoImageSplit, SimpleMath+, CR Float To Integer, PreviewImage, ImageFromBatch+, ImageFromBatch+, ImageFromBatch+, ImageFromBatch+, easy showAnything, easy cleanGpuUsed, CLIPTextEncode, ImageResizeKJv2, ImageResizeKJv2, ImageResizeKJv2, ImageResizeKJv2, LTXVConditioning, EmptyLTXVLatentVideo, LTXVAddGuideMulti, CFGGuider, LTXVConcatAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVAudioVAEDecode, LTXVCropGuides, VAEDecodeTiled, LoadImage, PrimitiveFloat, easy cleanGpuUsed, TTResolutionSelector, INTConstant, INTConstant, INTConstant, VHS_VideoCombine, LTXVEmptyLatentAudio, RH_LLMAPI_Pro_Node, Text]
patterns: []
missing: [CR Float To Integer, ImageFromBatch+, ImageFromBatch+, ImageFromBatch+, ImageFromBatch+, SimpleMath+, easy cleanGpuUsed, easy cleanGpuUsed]
parameters: {"batch_size": 401, "height": 25, "width": 97}
discoveries: [次要节点 `CR Float To Integer` 知识库中没有该节点类型的任何知识, 次要节点 `ImageFromBatch+` 知识库中没有该节点类型的任何知识, 次要节点 `ImageFromBatch+` 知识库中没有该节点类型的任何知识, 次要节点 `ImageFromBatch+` 知识库中没有该节点类型的任何知识, 次要节点 `ImageFromBatch+` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/LTX2.3_四宫格漫剧视频_2064675254458474498.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.3_四宫格漫剧视频_2064675254458474498.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（45 个）：
- `LatentUpscaleModelLoader`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `DualCLIPLoader`
- `VAELoader`
- `VAELoaderKJ`
- `ManualSigmas`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `GuHaiAutoImageSplit`
- `SimpleMath+`
- `CR Float To Integer`
- `PreviewImage`
- `ImageFromBatch+`
- `ImageFromBatch+`
- `ImageFromBatch+`
- `ImageFromBatch+`
- `easy showAnything`
- `easy cleanGpuUsed`
- `CLIPTextEncode` ★核心
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `LTXVConditioning`
- `EmptyLTXVLatentVideo`
- `LTXVAddGuideMulti`
- `CFGGuider`
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `LTXVCropGuides`
- `VAEDecodeTiled` ★核心
- `LoadImage`
- `PrimitiveFloat`
- `easy cleanGpuUsed`
- `TTResolutionSelector`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `VHS_VideoCombine`
- `LTXVEmptyLatentAudio` ★核心
- `RH_LLMAPI_Pro_Node`
- `Text`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `401`

## 知识

覆盖率 **76%**（34/45）

**有卡**：`LatentUpscaleModelLoader`、`KSamplerSelect`、`RandomNoise`、`DualCLIPLoader`、`VAELoader`、`VAELoaderKJ`、`ManualSigmas`、`UNETLoader`、`CLIPTextEncode`、`GuHaiAutoImageSplit`、`ImageResizeKJv2`、`LTXVConditioning`、`EmptyLTXVLatentVideo`、`LTXVAddGuideMulti`、`CFGGuider`、`LTXVConcatAVLatent`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`LTXVAudioVAEDecode`、`LTXVCropGuides`、`VAEDecodeTiled`、`LoadImage`、`TTResolutionSelector`、`INTConstant`、`VHS_VideoCombine`、`LTXVEmptyLatentAudio`、`RH_LLMAPI_Pro_Node`、`Text`

**缺卡**（8）：`CR Float To Integer`、`ImageFromBatch+`、`ImageFromBatch+`、`ImageFromBatch+`、`ImageFromBatch+`、`SimpleMath+`、`easy cleanGpuUsed`、`easy cleanGpuUsed`

**用到的条目**：VAELoader、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVConcatAVLatent

## 学习发现

- 次要节点 `CR Float To Integer` 知识库中没有该节点类型的任何知识
- 次要节点 `ImageFromBatch+` 知识库中没有该节点类型的任何知识
- 次要节点 `ImageFromBatch+` 知识库中没有该节点类型的任何知识
- 次要节点 `ImageFromBatch+` 知识库中没有该节点类型的任何知识
- 次要节点 `ImageFromBatch+` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
