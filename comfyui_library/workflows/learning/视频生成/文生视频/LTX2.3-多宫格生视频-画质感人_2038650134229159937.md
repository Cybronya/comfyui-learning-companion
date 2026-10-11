---
key: 视频生成/文生视频/LTX2.3-多宫格生视频-画质感人_2038650134229159937.json
name: LTX2.3-多宫格生视频-画质感人_2038650134229159937
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.3-多宫格生视频-画质感人_2038650134229159937.json
hash: d8e02ec44edc91e4
coverage: 0.85
learned_at: 2026-10-11 03:48:35
nodes: [ManualSigmas, CFGGuider, SamplerCustomAdvanced, SamplerCustomAdvanced, LatentUpscaleModelLoader, LTXVSeparateAVLatent, RandomNoise, KSamplerSelect, ManualSigmas, RandomNoise, UNETLoader, DualCLIPLoader, LTXVSeparateAVLatent, VAELoaderKJ, VAELoaderKJ, ImageFromBatch, ImageFromBatch, ImageFromBatch, ImageFromBatch, ImageResizeKJv2, ImageResizeKJv2, ImageResizeKJv2, ImageResizeKJv2, SimpleMath+, SimpleMath+, LTXVPreprocess, LTXVPreprocess, LTXVPreprocess, LTXVPreprocess, SimpleMath+, SimpleMath+, SimpleMath+, EmptyLTXVLatentVideo, VAEDecodeTiled, LTXVAudioVAEDecode, PrimitiveInt, SimpleMath+, Reroute, CFGGuider, KSamplerSelect, LTXVLatentUpsampler, LoadImage, QZ_ResolutionPreset, SaveImage, GuHaiAutoImageSplit, Int, LTXVConcatAVLatent, LTXVCropGuides, LTXVAddGuideMulti, CLIPTextEncode, ComfyMathExpression, LTXVEmptyLatentAudio, CreateVideo, CLIPTextEncode, LTXVConditioning, LTXVImgToVideoInplace, easy showAnything, SaveVideo, RH_LLMAPI_Pro_Node, LTXVConcatAVLatent]
patterns: []
missing: [SimpleMath+, SimpleMath+, SimpleMath+, SimpleMath+, SimpleMath+, SimpleMath+]
parameters: {"batch_size": 1, "height": 25, "width": 97}
discoveries: [次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/LTX2.3-多宫格生视频-画质感人_2038650134229159937.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.3-多宫格生视频-画质感人_2038650134229159937.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（60 个）：
- `ManualSigmas`
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `SamplerCustomAdvanced` ★核心
- `LatentUpscaleModelLoader`
- `LTXVSeparateAVLatent`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `RandomNoise`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `LTXVSeparateAVLatent`
- `VAELoaderKJ`
- `VAELoaderKJ`
- `ImageFromBatch`
- `ImageFromBatch`
- `ImageFromBatch`
- `ImageFromBatch`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `SimpleMath+`
- `SimpleMath+`
- `LTXVPreprocess`
- `LTXVPreprocess`
- `LTXVPreprocess`
- `LTXVPreprocess`
- `SimpleMath+`
- `SimpleMath+`
- `SimpleMath+`
- `EmptyLTXVLatentVideo`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `PrimitiveInt`
- `SimpleMath+`
- `Reroute`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `LTXVLatentUpsampler` ★核心
- `LoadImage`
- `QZ_ResolutionPreset`
- `SaveImage`
- `GuHaiAutoImageSplit`
- `Int`
- `LTXVConcatAVLatent`
- `LTXVCropGuides`
- `LTXVAddGuideMulti`
- `CLIPTextEncode` ★核心
- `ComfyMathExpression`
- `LTXVEmptyLatentAudio` ★核心
- `CreateVideo`
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `LTXVImgToVideoInplace`
- `easy showAnything`
- `SaveVideo`
- `RH_LLMAPI_Pro_Node`
- `LTXVConcatAVLatent`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **85%**（51/60）

**有卡**：`ManualSigmas`、`CFGGuider`、`SamplerCustomAdvanced`、`LatentUpscaleModelLoader`、`LTXVSeparateAVLatent`、`RandomNoise`、`KSamplerSelect`、`UNETLoader`、`DualCLIPLoader`、`VAELoaderKJ`、`ImageFromBatch`、`ImageResizeKJv2`、`LTXVPreprocess`、`EmptyLTXVLatentVideo`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`LTXVLatentUpsampler`、`LoadImage`、`QZ_ResolutionPreset`、`SaveImage`、`GuHaiAutoImageSplit`、`Int`、`LTXVConcatAVLatent`、`LTXVCropGuides`、`LTXVAddGuideMulti`、`CLIPTextEncode`、`ComfyMathExpression`、`LTXVEmptyLatentAudio`、`CreateVideo`、`LTXVConditioning`、`LTXVImgToVideoInplace`、`SaveVideo`、`RH_LLMAPI_Pro_Node`

**缺卡**（6）：`SimpleMath+`、`SimpleMath+`、`SimpleMath+`、`SimpleMath+`、`SimpleMath+`、`SimpleMath+`

**用到的条目**：CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler、LTXVConcatAVLatent

## 学习发现

- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
