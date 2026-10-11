---
key: 视频生成/文生视频/LTX2.3视频处理（视频高清修复）_2065411766766620674.json
name: LTX2.3视频处理（视频高清修复）_2065411766766620674
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.3视频处理（视频高清修复）_2065411766766620674.json
hash: 28a201465c2d47a7
coverage: 0.365591
learned_at: 2026-10-11 20:21:28
nodes: [DiffusionModelLoaderKJ, VAELoaderKJ, SamplerCustomAdvanced, SetNode, GetNode, GetNode, SetNode, SetNode, CR Text, VAELoaderKJ, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, RepeatImageBatch, LTXVPreprocess, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, LTXVConditioning, GetNode, VAEEncodeForInpaint, GetNode, GetNode, GetNode, GetNode, RandomNoise, CFGGuider, KSamplerSelect, ManualSigmas, GetNode, GetNode, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), CR Text, SetNode, SetNode, SetNode, SetNode, VHS_VideoInfoLoaded, SetNode, CLIPTextEncode, CLIPTextEncode, LTXAddVideoICLoRAGuide, LayerUtility: ImageScaleByAspectRatio V2, GetNode, ResizeImageMaskNode, easy imageSize, Image To Mask, LayerUtility: ColorImage, SetNode, SetNode, GetNode, VAEDecodeTiled, DualCLIPLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, SetNode, GetNode, CR Text, LTXVImgToVideoConditionOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, Fast Groups Bypasser (rgthree), Any Switch (rgthree), Any Switch (rgthree), GetNode, GetNode, GetNode, ResizeImageMaskNode, GetImageRangeFromBatch, SetNode, ImageConcatMulti, GetNode, VHS_VideoCombine, GetNode, GetImageRangeFromBatch, SetNode, GetNode, VHS_VideoCombine, FlashVSRNodeAdv, GetNode, FlashVSRInitPipe, GetNode, VHS_VideoCombine, VHS_LoadVideo]
patterns: []
missing: [CR Text, CR Text, CR Text, Image To Mask, LayerUtility: ColorImage, LayerUtility: ImageScaleByAspectRatio V2, easy imageSize]
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `Image To Mask` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ColorImage` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `easy imageSize` 仅有 Resolution 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/LTX2.3视频处理（视频高清修复）_2065411766766620674.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.3视频处理（视频高清修复）_2065411766766620674.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（93 个）：
- `DiffusionModelLoaderKJ`
- `VAELoaderKJ`
- `SamplerCustomAdvanced` ★核心
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `CR Text`
- `VAELoaderKJ`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `RepeatImageBatch`
- `LTXVPreprocess`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `LTXVConditioning`
- `GetNode`
- `VAEEncodeForInpaint` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `RandomNoise`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `GetNode`
- `GetNode`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `CR Text`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `VHS_VideoInfoLoaded`
- `SetNode`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LTXAddVideoICLoRAGuide`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetNode`
- `ResizeImageMaskNode`
- `easy imageSize`
- `Image To Mask`
- `LayerUtility: ColorImage`
- `SetNode`
- `SetNode`
- `GetNode`
- `VAEDecodeTiled` ★核心
- `DualCLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `GetNode`
- `CR Text`
- `LTXVImgToVideoConditionOnly`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `Fast Groups Bypasser (rgthree)`
- `Any Switch (rgthree)`
- `Any Switch (rgthree)`
- `GetNode`
- `GetNode`
- `GetNode`
- `ResizeImageMaskNode`
- `GetImageRangeFromBatch`
- `SetNode`
- `ImageConcatMulti`
- `GetNode`
- `VHS_VideoCombine`
- `GetNode`
- `GetImageRangeFromBatch`
- `SetNode`
- `GetNode`
- `VHS_VideoCombine`
- `FlashVSRNodeAdv`
- `GetNode`
- `FlashVSRInitPipe`
- `GetNode`
- `VHS_VideoCombine`
- `VHS_LoadVideo`

## 知识

覆盖率 **37%**（34/93）

**有卡**：`DiffusionModelLoaderKJ`、`VAELoaderKJ`、`SamplerCustomAdvanced`、`RepeatImageBatch`、`LTXVPreprocess`、`LTXVConditioning`、`VAEEncodeForInpaint`、`RandomNoise`、`CFGGuider`、`KSamplerSelect`、`ManualSigmas`、`VHS_VideoInfoLoaded`、`CLIPTextEncode`、`LTXAddVideoICLoRAGuide`、`ResizeImageMaskNode`、`VAEDecodeTiled`、`DualCLIPLoader`、`LoraLoaderModelOnly`、`LTXVImgToVideoConditionOnly`、`GetImageRangeFromBatch`、`ImageConcatMulti`、`VHS_VideoCombine`、`FlashVSRNodeAdv`、`FlashVSRInitPipe`、`VHS_LoadVideo`

**缺卡**（7）：`CR Text`、`CR Text`、`CR Text`、`Image To Mask`、`LayerUtility: ColorImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`easy imageSize`

**用到的条目**：LoraLoaderModelOnly、CLIPTextEncode、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、VAEDecodeTiled、VAELoaderKJ、VAEEncodeForInpaint

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `Image To Mask` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ColorImage` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `easy imageSize` 仅有 Resolution 的通用知识，没有该节点自己的说明
