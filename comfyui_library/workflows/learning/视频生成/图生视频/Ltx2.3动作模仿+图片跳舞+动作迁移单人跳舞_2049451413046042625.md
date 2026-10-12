---
key: 视频生成/图生视频/Ltx2.3动作模仿+图片跳舞+动作迁移单人跳舞_2049451413046042625.json
name: Ltx2.3动作模仿+图片跳舞+动作迁移单人跳舞_2049451413046042625
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Ltx2.3动作模仿+图片跳舞+动作迁移单人跳舞_2049451413046042625.json
hash: d2df6f2a783e512b
coverage: 0.571429
learned_at: 2026-10-13 01:36:52
nodes: [LTXVEmptyLatentAudio, CFGGuider, KSamplerSelect, RandomNoise, LTXVImgToVideoConditionOnly, EmptyLTXVLatentVideo, KSamplerSelect, ManualSigmas, GetNode, GetNode, CFGGuider, RandomNoise, LTXVConcatAVLatent, GetNode, LTXVLatentUpsampler, SetNode, SetNode, LTXAddVideoICLoRAGuide, GetNode, SamplerCustomAdvanced, LTXVImgToVideoInplace, GetNode, PrimitiveBoolean, LTXVConditioning, ManualSigmas, ImageResizeKJv2, GetNode, GetNode, SimpleMath+, SimpleMath+, CLIPTextEncode, SetNode, SetNode, SetNode, SetNode, SetNode, LatentUpscaleModelLoader, LTXVSeparateAVLatent, LTXVImgToVideoInplace, GetNode, DWPreprocessor, ImageResizeKJv2, GetImageSize, SetNode, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, VHS_VideoCombine, VAEDecodeTiled, LTXVSeparateAVLatent, SamplerCustomAdvanced, RandomNoise, SetNode, SimpleMath+, INTConstant, INTConstant, GetNode, GetNode, CLIPTextEncode, UNETLoader, VAELoaderKJ, VAELoaderKJ, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, DualCLIPLoader, LTXICLoRALoaderModelOnly, SetNode, SetNode, VHS_VideoInfo, SetNode, ComfyMathExpression, GetNode, GetNode, ImageResizeKJv2, GetNode, CFGGuider, KSamplerSelect, ManualSigmas, LTXVConcatAVLatent, RTXVideoSuperResolution, SetNode, SetNode, LTXVConcatAVLatent, LTXVSeparateAVLatent, LTXVCropGuides, SamplerCustomAdvanced, LTXVLatentUpsampler, GetNode, JjkText, VHS_LoadVideo, INTConstant, SimpleMath+, LTXVCropGuides, GetNode, LoadImage]
patterns: []
missing: [LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, SimpleMath+, SimpleMath+, SimpleMath+, SimpleMath+]
parameters: {"batch_size": 1, "height": 25, "width": 97}
discoveries: [次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识]
---

# 视频生成/图生视频/Ltx2.3动作模仿+图片跳舞+动作迁移单人跳舞_2049451413046042625.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/Ltx2.3动作模仿+图片跳舞+动作迁移单人跳舞_2049451413046042625.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（98 个）：
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
- `VHS_LoadVideo`
- `INTConstant`
- `SimpleMath+`
- `LTXVCropGuides`
- `GetNode`
- `LoadImage`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **57%**（56/98）

**有卡**：`LTXVEmptyLatentAudio`、`CFGGuider`、`KSamplerSelect`、`RandomNoise`、`LTXVImgToVideoConditionOnly`、`EmptyLTXVLatentVideo`、`ManualSigmas`、`LTXVConcatAVLatent`、`LTXVLatentUpsampler`、`LTXAddVideoICLoRAGuide`、`SamplerCustomAdvanced`、`LTXVImgToVideoInplace`、`PrimitiveBoolean`、`LTXVConditioning`、`ImageResizeKJv2`、`CLIPTextEncode`、`LatentUpscaleModelLoader`、`LTXVSeparateAVLatent`、`DWPreprocessor`、`GetImageSize`、`VHS_VideoCombine`、`VAEDecodeTiled`、`INTConstant`、`UNETLoader`、`VAELoaderKJ`、`DualCLIPLoader`、`LTXICLoRALoaderModelOnly`、`VHS_VideoInfo`、`ComfyMathExpression`、`RTXVideoSuperResolution`、`LTXVCropGuides`、`VHS_LoadVideo`、`LoadImage`

**缺卡**（6）：`LayerUtility: PurgeVRAM`、`LayerUtility: PurgeVRAM`、`SimpleMath+`、`SimpleMath+`、`SimpleMath+`、`SimpleMath+`

**用到的条目**：CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler、LTXVConcatAVLatent

## 学习发现

- 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
