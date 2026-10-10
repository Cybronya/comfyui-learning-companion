---
key: 视频生成/文生视频/LTX2.3-首尾帧_2031929637428793346.json
name: LTX2.3-首尾帧_2031929637428793346
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.3-首尾帧_2031929637428793346.json
hash: 42b1224e12ccab5c
coverage: 0.829787
learned_at: 2026-10-11 03:16:46
nodes: [RandomNoise, CFGGuider, KSamplerSelect, DualCLIPLoader, UNETLoader, VAELoaderKJ, LatentUpscaleModelLoader, CLIPTextEncode, VAELoaderKJ, LTXVConditioning, LTXVSeparateAVLatent, VAEDecodeTiled, RandomNoise, CFGGuider, KSamplerSelect, CreateVideo, LTXVAudioVAEDecode, ManualSigmas, ImageResizeKJv2, SimpleMath+, SimpleMath+, LTXVPreprocess, EmptyLTXVLatentVideo, LTXVEmptyLatentAudio, SamplerCustomAdvanced, LTXVLatentUpsampler, LTXVCropGuides, LTXVImgToVideoInplace, LTXVConcatAVLatent, ManualSigmas, ImageResizeKJv2, LTXVSeparateAVLatent, LTXVConcatAVLatent, LoadImage, LoadImage, CLIPTextEncode, SimpleMath+, Primitive float [Crystools], PrimitiveNode, PrimitiveNode, PrimitiveInt, SamplerCustomAdvanced, LTXVImgToVideoInplaceKJ, SimpleMath+, LTXVPreprocess, SaveImage, 1hew_SaveVideo]
patterns: []
missing: [Primitive float [Crystools], SimpleMath+, SimpleMath+, SimpleMath+, SimpleMath+]
parameters: {"batch_size": 1, "height": 25, "width": 121}
discoveries: [次要节点 `Primitive float [Crystools]` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/LTX2.3-首尾帧_2031929637428793346.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.3-首尾帧_2031929637428793346.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（47 个）：
- `RandomNoise`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `DualCLIPLoader`
- `UNETLoader` ★核心
- `VAELoaderKJ`
- `LatentUpscaleModelLoader`
- `CLIPTextEncode` ★核心
- `VAELoaderKJ`
- `LTXVConditioning`
- `LTXVSeparateAVLatent`
- `VAEDecodeTiled` ★核心
- `RandomNoise`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `CreateVideo`
- `LTXVAudioVAEDecode` ★核心
- `ManualSigmas`
- `ImageResizeKJv2`
- `SimpleMath+`
- `SimpleMath+`
- `LTXVPreprocess`
- `EmptyLTXVLatentVideo`
- `LTXVEmptyLatentAudio` ★核心
- `SamplerCustomAdvanced` ★核心
- `LTXVLatentUpsampler` ★核心
- `LTXVCropGuides`
- `LTXVImgToVideoInplace`
- `LTXVConcatAVLatent`
- `ManualSigmas`
- `ImageResizeKJv2`
- `LTXVSeparateAVLatent`
- `LTXVConcatAVLatent`
- `LoadImage`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `SimpleMath+`
- `Primitive float [Crystools]`
- `PrimitiveNode`
- `PrimitiveNode`
- `PrimitiveInt`
- `SamplerCustomAdvanced` ★核心
- `LTXVImgToVideoInplaceKJ`
- `SimpleMath+`
- `LTXVPreprocess`
- `SaveImage`
- `1hew_SaveVideo`

## 关键参数

- `width` = `121`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **83%**（39/47）

**有卡**：`RandomNoise`、`CFGGuider`、`KSamplerSelect`、`DualCLIPLoader`、`UNETLoader`、`VAELoaderKJ`、`LatentUpscaleModelLoader`、`CLIPTextEncode`、`LTXVConditioning`、`LTXVSeparateAVLatent`、`VAEDecodeTiled`、`CreateVideo`、`LTXVAudioVAEDecode`、`ManualSigmas`、`ImageResizeKJv2`、`LTXVPreprocess`、`EmptyLTXVLatentVideo`、`LTXVEmptyLatentAudio`、`SamplerCustomAdvanced`、`LTXVLatentUpsampler`、`LTXVCropGuides`、`LTXVImgToVideoInplace`、`LTXVConcatAVLatent`、`LoadImage`、`LTXVImgToVideoInplaceKJ`、`SaveImage`、`1hew_SaveVideo`

**缺卡**（5）：`Primitive float [Crystools]`、`SimpleMath+`、`SimpleMath+`、`SimpleMath+`、`SimpleMath+`

**用到的条目**：CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler、LTXVConcatAVLatent

## 学习发现

- 次要节点 `Primitive float [Crystools]` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
