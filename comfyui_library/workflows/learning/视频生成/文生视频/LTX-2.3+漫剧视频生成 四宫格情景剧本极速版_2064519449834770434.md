---
key: 视频生成/文生视频/LTX-2.3+漫剧视频生成 四宫格情景剧本极速版_2064519449834770434.json
name: LTX-2.3+漫剧视频生成 四宫格情景剧本极速版_2064519449834770434
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX-2.3+漫剧视频生成 四宫格情景剧本极速版_2064519449834770434.json
hash: c77e3003a5f4f4e7
coverage: 0.452055
learned_at: 2026-10-11 20:21:25
nodes: [SetNode, SetNode, SimpleMath+, SetNode, GetNode, PrimitiveFloat, SetNode, LTXVAudioVAEDecode, GetNode, GetNode, GetNode, GetNode, ImageResizeKJv2, ImageResizeKJv2, ImageResizeKJv2, SetNode, GuHaiAutoImageSplit, ImageFromBatch+, ImageFromBatch+, ImageFromBatch+, ImageFromBatch+, SetNode, SetNode, ImageResizeKJv2, SetNode, CR Float To Integer, EmptyLTXVLatentVideo, LTXVEmptyLatentAudio, VAELoader, LatentUpscaleModelLoader, SetNode, VAELoaderKJ, SetNode, DualCLIPLoader, SetNode, SetNode, SetNode, CFGGuider, RandomNoise, KSamplerSelect, ManualSigmas, LTXVConcatAVLatent, GetNode, GetNode, GetNode, CLIPTextEncode, GetNode, GetNode, GetNode, LTXVCropGuides, SamplerCustomAdvanced, LTXVSeparateAVLatent, CLIPTextEncode, LTXVConditioning, GetNode, easy showAnything, RH_LLMAPI_Pro_Node, easy cleanGpuUsed, easy cleanGpuUsed, VAEDecodeTiled, UNETLoader, RHHiddenNodes, GetNode, GetNode, GetNode, GetNode, LTXVAddGuideMulti, INTConstant, TTResolutionSelector, LoadImage, VHS_VideoCombine, PreviewImage, Text]
patterns: []
missing: [CR Float To Integer, ImageFromBatch+, ImageFromBatch+, ImageFromBatch+, ImageFromBatch+, SimpleMath+, easy cleanGpuUsed, easy cleanGpuUsed]
parameters: {"batch_size": 1, "height": 25, "width": 97}
discoveries: [次要节点 `CR Float To Integer` 知识库中没有该节点类型的任何知识, 次要节点 `ImageFromBatch+` 知识库中没有该节点类型的任何知识, 次要节点 `ImageFromBatch+` 知识库中没有该节点类型的任何知识, 次要节点 `ImageFromBatch+` 知识库中没有该节点类型的任何知识, 次要节点 `ImageFromBatch+` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/LTX-2.3+漫剧视频生成 四宫格情景剧本极速版_2064519449834770434.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX-2.3+漫剧视频生成 四宫格情景剧本极速版_2064519449834770434.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（73 个）：
- `SetNode`
- `SetNode`
- `SimpleMath+`
- `SetNode`
- `GetNode`
- `PrimitiveFloat`
- `SetNode`
- `LTXVAudioVAEDecode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `SetNode`
- `GuHaiAutoImageSplit`
- `ImageFromBatch+`
- `ImageFromBatch+`
- `ImageFromBatch+`
- `ImageFromBatch+`
- `SetNode`
- `SetNode`
- `ImageResizeKJv2`
- `SetNode`
- `CR Float To Integer`
- `EmptyLTXVLatentVideo`
- `LTXVEmptyLatentAudio` ★核心
- `VAELoader`
- `LatentUpscaleModelLoader`
- `SetNode`
- `VAELoaderKJ`
- `SetNode`
- `DualCLIPLoader`
- `SetNode`
- `SetNode`
- `SetNode`
- `CFGGuider`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `LTXVConcatAVLatent`
- `GetNode`
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVCropGuides`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `GetNode`
- `easy showAnything`
- `RH_LLMAPI_Pro_Node`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `VAEDecodeTiled` ★核心
- `UNETLoader` ★核心
- `RHHiddenNodes`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVAddGuideMulti`
- `INTConstant`
- `TTResolutionSelector`
- `LoadImage`
- `VHS_VideoCombine`
- `PreviewImage`
- `Text`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **45%**（33/73）

**有卡**：`LTXVAudioVAEDecode`、`ImageResizeKJv2`、`GuHaiAutoImageSplit`、`EmptyLTXVLatentVideo`、`LTXVEmptyLatentAudio`、`VAELoader`、`LatentUpscaleModelLoader`、`VAELoaderKJ`、`DualCLIPLoader`、`CFGGuider`、`RandomNoise`、`KSamplerSelect`、`ManualSigmas`、`LTXVConcatAVLatent`、`CLIPTextEncode`、`LTXVCropGuides`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`LTXVConditioning`、`RH_LLMAPI_Pro_Node`、`VAEDecodeTiled`、`UNETLoader`、`RHHiddenNodes`、`LTXVAddGuideMulti`、`INTConstant`、`TTResolutionSelector`、`LoadImage`、`VHS_VideoCombine`、`Text`

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
