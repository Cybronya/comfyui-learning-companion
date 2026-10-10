---
key: 视频生成/文生视频/Ltx-2.3 IC LoRA Union 视频控制_2032312720623669250.json
name: Ltx-2.3 IC LoRA Union 视频控制_2032312720623669250
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Ltx-2.3 IC LoRA Union 视频控制_2032312720623669250.json
hash: 7b2fc89945758b9c
coverage: 0.886364
learned_at: 2026-10-11 03:16:48
nodes: [LTXVAudioVAEDecode, CreateVideo, VAEDecodeTiled, LTXVConditioning, LTXAddVideoICLoRAGuide, LTXVConcatAVLatent, LTXVEmptyLatentAudio, SamplerCustomAdvanced, LTXVCropGuides, LTXVSeparateAVLatent, CLIPTextEncode, LTXVPreprocess, RandomNoise, DownloadAndLoadDepthCrafterModel, easy showAnything, easy showAnything, VAELoaderKJ, VAELoader, DualCLIPLoader, UNETLoader, LTXICLoRALoaderModelOnly, CM_FloatToInt, VHS_VideoInfoLoaded, CannyEdgePreprocessor, DepthCrafter, EmptyLTXVLatentVideo, PreviewImage, LTXVImgToVideoConditionOnly, LoraLoaderModelOnly, KSamplerSelect, ManualSigmas, CFGGuider, GetImageSize, SimpleMath+, ImageResizeKJv2, ImageResizeKJv2, DWPreprocessor, CLIPTextEncode, ImageResizeKJv2, SaveVideo, PrimitiveBoolean, PreviewImage, LoadImage, VHS_LoadVideo]
patterns: []
missing: [SimpleMath+]
parameters: {"batch_size": 1, "height": 25, "width": 97}
discoveries: [次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/Ltx-2.3 IC LoRA Union 视频控制_2032312720623669250.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Ltx-2.3 IC LoRA Union 视频控制_2032312720623669250.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（44 个）：
- `LTXVAudioVAEDecode` ★核心
- `CreateVideo`
- `VAEDecodeTiled` ★核心
- `LTXVConditioning`
- `LTXAddVideoICLoRAGuide`
- `LTXVConcatAVLatent`
- `LTXVEmptyLatentAudio` ★核心
- `SamplerCustomAdvanced` ★核心
- `LTXVCropGuides`
- `LTXVSeparateAVLatent`
- `CLIPTextEncode` ★核心
- `LTXVPreprocess`
- `RandomNoise`
- `DownloadAndLoadDepthCrafterModel`
- `easy showAnything`
- `easy showAnything`
- `VAELoaderKJ`
- `VAELoader`
- `DualCLIPLoader`
- `UNETLoader` ★核心
- `LTXICLoRALoaderModelOnly` ★核心
- `CM_FloatToInt`
- `VHS_VideoInfoLoaded`
- `CannyEdgePreprocessor`
- `DepthCrafter`
- `EmptyLTXVLatentVideo`
- `PreviewImage`
- `LTXVImgToVideoConditionOnly`
- `LoraLoaderModelOnly` ★核心
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `CFGGuider`
- `GetImageSize`
- `SimpleMath+`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `DWPreprocessor`
- `CLIPTextEncode` ★核心
- `ImageResizeKJv2`
- `SaveVideo`
- `PrimitiveBoolean`
- `PreviewImage`
- `LoadImage`
- `VHS_LoadVideo`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **89%**（39/44）

**有卡**：`LTXVAudioVAEDecode`、`CreateVideo`、`VAEDecodeTiled`、`LTXVConditioning`、`LTXAddVideoICLoRAGuide`、`LTXVConcatAVLatent`、`LTXVEmptyLatentAudio`、`SamplerCustomAdvanced`、`LTXVCropGuides`、`LTXVSeparateAVLatent`、`CLIPTextEncode`、`LTXVPreprocess`、`RandomNoise`、`DownloadAndLoadDepthCrafterModel`、`VAELoaderKJ`、`VAELoader`、`DualCLIPLoader`、`UNETLoader`、`LTXICLoRALoaderModelOnly`、`CM_FloatToInt`、`VHS_VideoInfoLoaded`、`CannyEdgePreprocessor`、`DepthCrafter`、`EmptyLTXVLatentVideo`、`LTXVImgToVideoConditionOnly`、`LoraLoaderModelOnly`、`KSamplerSelect`、`ManualSigmas`、`CFGGuider`、`GetImageSize`、`ImageResizeKJv2`、`DWPreprocessor`、`SaveVideo`、`PrimitiveBoolean`、`LoadImage`、`VHS_LoadVideo`

**缺卡**（1）：`SimpleMath+`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CannyEdgePreprocessor、DepthCrafter、DownloadAndLoadDepthCrafterModel

## 学习发现

- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
