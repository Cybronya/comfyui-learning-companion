---
key: 视频生成/图生视频/LTX 2.3  首尾帧高清工作流_2054364894450987010.json
name: LTX 2.3  首尾帧高清工作流_2054364894450987010.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX 2.3  首尾帧高清工作流_2054364894450987010.json
hash: 7db74e58161999a4
coverage: 0.495327
learned_at: 2026-10-15 22:37:46
nodes: [SetNode, SetNode, SetNode, SetNode, GetImageSize, SetNode, SetNode, ImageFlip, SetNode, GetNode, ImageResizeKJv2, GetNode, ImageFlip, ImageResizeKJv2, ResizeImageMaskNode, GetNode, SetNode, GetNode, GetNode, GetNode, EmptyLTXVLatentVideo, GetNode, LTXVConcatAVLatent, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, SetNode, SetNode, INTConstant, SimpleCalculatorKJ, GetNode, LTXVEmptyLatentAudio, LTXVSeparateAVLatent, GetNode, GetNode, GetNode, SimpleMath+, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, KSamplerSelect, LTXVLatentUpsampler, GetNode, LTXVConcatAVLatent, ManualSigmas, SetNode, GetNode, VAEDecodeTiled, KSamplerSelect, LTXVScheduler, VHS_VideoCombine, SamplerCustom, GetNode, GetNode, LTXVSeparateAVLatent, GetNode, SetNode, VAEDecodeTiled, GetNode, LTX2SamplingPreviewOverride, GetNode, SimpleMath+, ManualSigmas, VHS_VideoCombine, GetNode, Seed (rgthree), SamplerCustom, LTXVConditioning, SimpleMath+, SetNode, SetNode, VAELoaderKJ, VAELoaderKJ, SetNode, LatentUpscaleModelLoader, SetNode, DualCLIPLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, DiffusionModelLoaderKJ, GetNode, LTXVPreprocess, LTXVImgToVideoInplaceKJ, SetNode, GetNode, LTXVSeparateAVLatent, LTXVAudioVAEDecode, GetNode, LoadImage, LoadImage, MarkdownNote, INTConstant, INTConstant, LTXVImgToVideoInplaceKJ, CLIPTextEncode, INTConstant, LoraLoaderModelOnly, LoraLoaderModelOnly, PromptRelayEncode]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 24, "width": 121}
---

# 视频生成/图生视频/LTX 2.3  首尾帧高清工作流_2054364894450987010.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2054364894450987010.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（107 个）：
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetImageSize`
- `SetNode`
- `SetNode`
- `ImageFlip`
- `SetNode`
- `GetNode`
- `ImageResizeKJv2`
- `GetNode`
- `ImageFlip`
- `ImageResizeKJv2`
- `ResizeImageMaskNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `LTXVConcatAVLatent`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `INTConstant`
- `SimpleCalculatorKJ`
- `GetNode`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVSeparateAVLatent`
- `GetNode`
- `GetNode`
- `GetNode`
- `SimpleMath+`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `KSamplerSelect` ★核心
- `LTXVLatentUpsampler` ★核心
- `GetNode`
- `LTXVConcatAVLatent`
- `ManualSigmas`
- `SetNode`
- `GetNode`
- `VAEDecodeTiled` ★核心
- `KSamplerSelect` ★核心
- `LTXVScheduler`
- `VHS_VideoCombine`
- `SamplerCustom` ★核心
- `GetNode`
- `GetNode`
- `LTXVSeparateAVLatent`
- `GetNode`
- `SetNode`
- `VAEDecodeTiled` ★核心
- `GetNode`
- `LTX2SamplingPreviewOverride`
- `GetNode`
- `SimpleMath+`
- `ManualSigmas`
- `VHS_VideoCombine`
- `GetNode`
- `Seed (rgthree)`
- `SamplerCustom` ★核心
- `LTXVConditioning`
- `SimpleMath+`
- `SetNode`
- `SetNode`
- `VAELoaderKJ`
- `VAELoaderKJ`
- `SetNode`
- `LatentUpscaleModelLoader`
- `SetNode`
- `DualCLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `DiffusionModelLoaderKJ`
- `GetNode`
- `LTXVPreprocess`
- `LTXVImgToVideoInplaceKJ`
- `SetNode`
- `GetNode`
- `LTXVSeparateAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `GetNode`
- `LoadImage`
- `LoadImage`
- `MarkdownNote`
- `INTConstant`
- `INTConstant`
- `LTXVImgToVideoInplaceKJ`
- `CLIPTextEncode` ★核心
- `INTConstant`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `PromptRelayEncode`

## 关键参数

- `width` = `121`
- `height` = `24`
- `batch_size` = `1`

## 知识

覆盖率 **50%**（53/107）

**有卡**：`GetImageSize`、`ImageFlip`、`ImageResizeKJv2`、`ResizeImageMaskNode`、`EmptyLTXVLatentVideo`、`LTXVConcatAVLatent`、`INTConstant`、`SimpleCalculatorKJ`、`LTXVEmptyLatentAudio`、`LTXVSeparateAVLatent`、`SimpleMath+`、`KSamplerSelect`、`LTXVLatentUpsampler`、`ManualSigmas`、`VAEDecodeTiled`、`LTXVScheduler`、`VHS_VideoCombine`、`SamplerCustom`、`LTX2SamplingPreviewOverride`、`Seed (rgthree)`、`LTXVConditioning`、`VAELoaderKJ`、`LatentUpscaleModelLoader`、`DualCLIPLoader`、`LoraLoaderModelOnly`、`DiffusionModelLoaderKJ`、`LTXVPreprocess`、`LTXVImgToVideoInplaceKJ`、`LTXVAudioVAEDecode`、`LoadImage`、`CLIPTextEncode`、`PromptRelayEncode`

**用到的条目**：LoraLoaderModelOnly、CLIPTextEncode、LoadImage、KSamplerSelect、SamplerCustom、LTXVLatentUpsampler、Seed (rgthree)、LTXVConcatAVLatent
