---
key: 视频生成/图生视频/Ltx2.3动作模仿+图片跳舞+动作迁移! B站艾橘溪_2048751560372523009.json
name: Ltx2.3动作模仿+图片跳舞+动作迁移! B站艾橘溪_2048751560372523009.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Ltx2.3动作模仿+图片跳舞+动作迁移! B站艾橘溪_2048751560372523009.json
hash: 668f421beaa1b0b2
coverage: 0.626263
learned_at: 2026-10-15 22:37:11
nodes: [LTXVEmptyLatentAudio, CFGGuider, KSamplerSelect, RandomNoise, LTXVImgToVideoConditionOnly, EmptyLTXVLatentVideo, KSamplerSelect, ManualSigmas, GetNode, GetNode, CFGGuider, RandomNoise, LTXVConcatAVLatent, GetNode, LTXVLatentUpsampler, SetNode, SetNode, LTXAddVideoICLoRAGuide, GetNode, SamplerCustomAdvanced, LTXVImgToVideoInplace, GetNode, PrimitiveBoolean, LTXVConditioning, ManualSigmas, ImageResizeKJv2, GetNode, GetNode, SimpleMath+, SimpleMath+, CLIPTextEncode, SetNode, SetNode, SetNode, SetNode, SetNode, LatentUpscaleModelLoader, LTXVSeparateAVLatent, LTXVImgToVideoInplace, GetNode, DWPreprocessor, ImageResizeKJv2, GetImageSize, SetNode, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, VHS_VideoCombine, VAEDecodeTiled, LTXVSeparateAVLatent, SamplerCustomAdvanced, RandomNoise, SetNode, SimpleMath+, INTConstant, INTConstant, GetNode, GetNode, CLIPTextEncode, UNETLoader, VAELoaderKJ, VAELoaderKJ, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, DualCLIPLoader, LTXICLoRALoaderModelOnly, SetNode, SetNode, VHS_VideoInfo, SetNode, ComfyMathExpression, Note, GetNode, GetNode, ImageResizeKJv2, GetNode, CFGGuider, KSamplerSelect, ManualSigmas, LTXVConcatAVLatent, RTXVideoSuperResolution, SetNode, SetNode, LTXVConcatAVLatent, LTXVSeparateAVLatent, LTXVCropGuides, SamplerCustomAdvanced, LTXVLatentUpsampler, GetNode, JjkText, LoadImage, VHS_LoadVideo, INTConstant, SimpleMath+, LTXVCropGuides, GetNode]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/图生视频/Ltx2.3动作模仿+图片跳舞+动作迁移! B站艾橘溪_2048751560372523009.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2048751560372523009.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（99 个）：
- `LTXVEmptyLatentAudio` ★核心
- `CFGGuider`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `LTXVImgToVideoConditionOnly`
- `EmptyLTXVLatentVideo`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `GetNode`
- `GetNode`
- `CFGGuider`
- `RandomNoise`
- `LTXVConcatAVLatent`
- `GetNode`
- `LTXVLatentUpsampler` ★核心
- `SetNode`
- `SetNode`
- `LTXAddVideoICLoRAGuide`
- `GetNode`
- `SamplerCustomAdvanced` ★核心
- `LTXVImgToVideoInplace`
- `GetNode`
- `PrimitiveBoolean`
- `LTXVConditioning`
- `ManualSigmas`
- `ImageResizeKJv2`
- `GetNode`
- `GetNode`
- `SimpleMath+`
- `SimpleMath+`
- `CLIPTextEncode` ★核心
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `LatentUpscaleModelLoader`
- `LTXVSeparateAVLatent`
- `LTXVImgToVideoInplace`
- `GetNode`
- `DWPreprocessor`
- `ImageResizeKJv2`
- `GetImageSize`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `VAEDecodeTiled` ★核心
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `SetNode`
- `SimpleMath+`
- `INTConstant`
- `INTConstant`
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `VAELoaderKJ`
- `VAELoaderKJ`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `DualCLIPLoader`
- `LTXICLoRALoaderModelOnly` ★核心
- `SetNode`
- `SetNode`
- `VHS_VideoInfo`
- `SetNode`
- `ComfyMathExpression`
- `Note`
- `GetNode`
- `GetNode`
- `ImageResizeKJv2`
- `GetNode`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `LTXVConcatAVLatent`
- `RTXVideoSuperResolution`
- `SetNode`
- `SetNode`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LTXVCropGuides`
- `SamplerCustomAdvanced` ★核心
- `LTXVLatentUpsampler` ★核心
- `GetNode`
- `JjkText`
- `LoadImage`
- `VHS_LoadVideo`
- `INTConstant`
- `SimpleMath+`
- `LTXVCropGuides`
- `GetNode`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **63%**（62/99）

**有卡**：`LTXVEmptyLatentAudio`、`CFGGuider`、`KSamplerSelect`、`RandomNoise`、`LTXVImgToVideoConditionOnly`、`EmptyLTXVLatentVideo`、`ManualSigmas`、`LTXVConcatAVLatent`、`LTXVLatentUpsampler`、`LTXAddVideoICLoRAGuide`、`SamplerCustomAdvanced`、`LTXVImgToVideoInplace`、`PrimitiveBoolean`、`LTXVConditioning`、`ImageResizeKJv2`、`SimpleMath+`、`CLIPTextEncode`、`LatentUpscaleModelLoader`、`LTXVSeparateAVLatent`、`DWPreprocessor`、`GetImageSize`、`VHS_VideoCombine`、`VAEDecodeTiled`、`INTConstant`、`UNETLoader`、`VAELoaderKJ`、`LayerUtility: PurgeVRAM`、`DualCLIPLoader`、`LTXICLoRALoaderModelOnly`、`VHS_VideoInfo`、`ComfyMathExpression`、`RTXVideoSuperResolution`、`LTXVCropGuides`、`LoadImage`、`VHS_LoadVideo`

**用到的条目**：CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler、LTXVConcatAVLatent
