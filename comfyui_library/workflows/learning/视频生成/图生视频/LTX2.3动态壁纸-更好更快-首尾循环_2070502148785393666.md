---
key: 视频生成/图生视频/LTX2.3动态壁纸-更好更快-首尾循环_2070502148785393666.json
name: LTX2.3动态壁纸-更好更快-首尾循环_2070502148785393666.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3动态壁纸-更好更快-首尾循环_2070502148785393666.json
hash: 1c6eaf9cf5089887
coverage: 0.571429
learned_at: 2026-10-15 22:40:40
nodes: [SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, PrimitiveInt, PrimitiveInt, GetNode, SetNode, GetNode, GetNode, GetNode, GetNode, VHS_VideoCombine, GetNode, SetNode, GetNode, CLIPTextEncode, CLIPTextEncode, ComfyNumberConvert, SetNode, INTConstant, SimpleCalculatorKJ, SetNode, SimpleCalculatorKJ, ImageScaleBy, GetNode, GetNode, GetNode, GetNode, ImageResizeKJv2, GetNode, ImageScaleBy, PreviewAny, GetNode, GetNode, SetNode, GetNode, INTConstant, VAEDecode, GetImageSize, LTXVConcatAVLatent, SamplerCustomAdvanced, LTXVCropGuides, ComfyNumberConvert, LTXVEmptyLatentAudio, LTXVImgToVideo, BasicScheduler, CFGGuider, RandomNoise, LTXVCropGuides, GetNode, GetNode, KSamplerSelect, LTXVConcatAVLatent, VRAM_Debug, GetNode, BasicScheduler, CFGGuider, SamplerCustomAdvanced, LTXVSeparateAVLatent, CLIPTextEncode, CLIPTextEncode, GetNode, GetNode, VAEDecode, ColorTransfer, ImageResizeKJv2, RTXVideoSuperResolution, FrameInterpolationModelLoader, FrameInterpolate, Any Switch (rgthree), SimpleMath+, Fast Groups Muter (rgthree), GetNode, Any Switch (rgthree), VAELoaderKJ, VAELoaderKJ, UNETLoader, DualCLIPLoader, LoadImage, Note, TextGenerate, LoraLoaderModelOnly, VRAM_Debug, KSamplerSelect, LTXVSeparateAVLatent, Video_Fade, GetNode, RandomNoise, EmptyLTXVLatentVideo, ImageFromBatch, GetImageSize, LTXVAddGuideMulti, LTXVEmptyLatentAudio]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 50, "width": 81}
---

# 视频生成/图生视频/LTX2.3动态壁纸-更好更快-首尾循环_2070502148785393666.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2070502148785393666.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（98 个）：
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `PrimitiveInt`
- `PrimitiveInt`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `GetNode`
- `SetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ComfyNumberConvert`
- `SetNode`
- `INTConstant`
- `SimpleCalculatorKJ`
- `SetNode`
- `SimpleCalculatorKJ`
- `ImageScaleBy`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageResizeKJv2`
- `GetNode`
- `ImageScaleBy`
- `PreviewAny`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `INTConstant`
- `VAEDecode` ★核心
- `GetImageSize`
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVCropGuides`
- `ComfyNumberConvert`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVImgToVideo`
- `BasicScheduler`
- `CFGGuider`
- `RandomNoise`
- `LTXVCropGuides`
- `GetNode`
- `GetNode`
- `KSamplerSelect` ★核心
- `LTXVConcatAVLatent`
- `VRAM_Debug`
- `GetNode`
- `BasicScheduler`
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `GetNode`
- `GetNode`
- `VAEDecode` ★核心
- `ColorTransfer`
- `ImageResizeKJv2`
- `RTXVideoSuperResolution`
- `FrameInterpolationModelLoader`
- `FrameInterpolate`
- `Any Switch (rgthree)`
- `SimpleMath+`
- `Fast Groups Muter (rgthree)`
- `GetNode`
- `Any Switch (rgthree)`
- `VAELoaderKJ`
- `VAELoaderKJ`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `LoadImage`
- `Note`
- `TextGenerate`
- `LoraLoaderModelOnly` ★核心
- `VRAM_Debug`
- `KSamplerSelect` ★核心
- `LTXVSeparateAVLatent`
- `Video_Fade`
- `GetNode`
- `RandomNoise`
- `EmptyLTXVLatentVideo`
- `ImageFromBatch`
- `GetImageSize`
- `LTXVAddGuideMulti`
- `LTXVEmptyLatentAudio` ★核心

## 关键参数

- `width` = `81`
- `height` = `50`
- `batch_size` = `1`

## 知识

覆盖率 **57%**（56/98）

**有卡**：`VHS_VideoCombine`、`CLIPTextEncode`、`ComfyNumberConvert`、`INTConstant`、`SimpleCalculatorKJ`、`ImageScaleBy`、`ImageResizeKJv2`、`VAEDecode`、`GetImageSize`、`LTXVConcatAVLatent`、`SamplerCustomAdvanced`、`LTXVCropGuides`、`LTXVEmptyLatentAudio`、`LTXVImgToVideo`、`BasicScheduler`、`CFGGuider`、`RandomNoise`、`KSamplerSelect`、`VRAM_Debug`、`LTXVSeparateAVLatent`、`ColorTransfer`、`RTXVideoSuperResolution`、`FrameInterpolationModelLoader`、`FrameInterpolate`、`SimpleMath+`、`VAELoaderKJ`、`UNETLoader`、`DualCLIPLoader`、`LoadImage`、`TextGenerate`、`LoraLoaderModelOnly`、`Video_Fade`、`EmptyLTXVLatentVideo`、`ImageFromBatch`、`LTXVAddGuideMulti`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
