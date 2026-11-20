---
key: 平台全量/JM最强去水印 浮云3.9_2030936851959259138.json
name: JM最强去水印 浮云3.9_2030936851959259138
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/JM最强去水印 浮云3.9_2030936851959259138.json
hash: 0bb428fe14197b68
coverage: 0.632653
learned_at: 2026-11-14 00:33:04
nodes: [SetNode, SetNode, SetNode, SetNode, PrimitiveString, GetNode, GetNode, SetNode, GetNode, SetNode, SetNode, SetNode, GetNode, SetNode, SetNode, WanVideoDecode, GetNode, StringConcatenate, StringConcatenate, VHS_VideoInfo, WanVideoExperimentalArgs, WanVideoSLG, SetNode, GetImageSize+, easy imageBatchToImageList, MaskToImage, easy imageListToImageBatch, ImageToMask, ImageFromBatch, VHS_DuplicateMasks, SetNode, UltralyticsDetectorProvider, ImageCompositeMasked, GetNode, easy compare, RepeatImageBatch, Label (rgthree), Label (rgthree), ImageToMask, SetNode, SetNode, BboxDetectorCombined_v2, easy int, ImageFromBatch, ImageFromBatch, easy int, easy seed, easy int, GetImageSize, GetImageSize, AddMask, AddMask, MaskToImage, VHS_DuplicateMasks, SaveImage, PrimitiveString, WanVideoMiniMaxRemoverEmbeds, GetNode, PrimitiveInt, WanVideoEncode, WanVideoEncode, WanVideoBlockSwap, WanVideoModelLoader, Mute / Bypass Repeater (rgthree), GetImageSize, MaskToImage, GetNode, GetNode, GetNode, easy int, GetImageSizeAndCount, Any Switch (rgthree), WanVideoVAELoader, GetNode, Fast Groups Muter (rgthree), PreviewBridge, PreviewBridge, PreviewBridge, ImageResizeKJ, WanVideoSampler, ResizeMask, INPAINT_MaskedFill, SetNode, Any Switch (rgthree), ImageFromBatch, PreviewBridge, GetNode, GetImageSize, WanVideoContextOptions, WanVideoEnhanceAVideo, PrimitiveString, Fast Groups Muter (rgthree), VHS_VideoCombine, VHS_VideoCombine, easy ifElse, LoadImage, LoadImage, VHS_LoadVideo]
patterns: []
missing: []
---

# 平台全量/JM最强去水印 浮云3.9_2030936851959259138.json

> 来源文件 `comfyui_library/workflows/平台全量/JM最强去水印 浮云3.9_2030936851959259138.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（98 个）：
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `PrimitiveString`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `WanVideoDecode`
- `GetNode`
- `StringConcatenate`
- `StringConcatenate`
- `VHS_VideoInfo`
- `WanVideoExperimentalArgs`
- `WanVideoSLG`
- `SetNode`
- `GetImageSize+`
- `easy imageBatchToImageList`
- `MaskToImage`
- `easy imageListToImageBatch`
- `ImageToMask`
- `ImageFromBatch`
- `VHS_DuplicateMasks`
- `SetNode`
- `UltralyticsDetectorProvider`
- `ImageCompositeMasked`
- `GetNode`
- `easy compare`
- `RepeatImageBatch`
- `Label (rgthree)`
- `Label (rgthree)`
- `ImageToMask`
- `SetNode`
- `SetNode`
- `BboxDetectorCombined_v2`
- `easy int`
- `ImageFromBatch`
- `ImageFromBatch`
- `easy int`
- `easy seed`
- `easy int`
- `GetImageSize`
- `GetImageSize`
- `AddMask`
- `AddMask`
- `MaskToImage`
- `VHS_DuplicateMasks`
- `SaveImage`
- `PrimitiveString`
- `WanVideoMiniMaxRemoverEmbeds`
- `GetNode`
- `PrimitiveInt`
- `WanVideoEncode`
- `WanVideoEncode`
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `Mute / Bypass Repeater (rgthree)`
- `GetImageSize`
- `MaskToImage`
- `GetNode`
- `GetNode`
- `GetNode`
- `easy int`
- `GetImageSizeAndCount`
- `Any Switch (rgthree)`
- `WanVideoVAELoader`
- `GetNode`
- `Fast Groups Muter (rgthree)`
- `PreviewBridge`
- `PreviewBridge`
- `PreviewBridge`
- `ImageResizeKJ`
- `WanVideoSampler` ★核心
- `ResizeMask`
- `INPAINT_MaskedFill`
- `SetNode`
- `Any Switch (rgthree)`
- `ImageFromBatch`
- `PreviewBridge`
- `GetNode`
- `GetImageSize`
- `WanVideoContextOptions`
- `WanVideoEnhanceAVideo`
- `PrimitiveString`
- `Fast Groups Muter (rgthree)`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `easy ifElse`
- `LoadImage`
- `LoadImage`
- `VHS_LoadVideo`

## 知识

覆盖率 **63%**（62/98）

**有卡**：`WanVideoDecode`、`StringConcatenate`、`VHS_VideoInfo`、`WanVideoExperimentalArgs`、`WanVideoSLG`、`GetImageSize+`、`easy imageBatchToImageList`、`MaskToImage`、`easy imageListToImageBatch`、`ImageToMask`、`ImageFromBatch`、`VHS_DuplicateMasks`、`UltralyticsDetectorProvider`、`ImageCompositeMasked`、`easy compare`、`RepeatImageBatch`、`Label (rgthree)`、`BboxDetectorCombined_v2`、`easy int`、`easy seed`、`GetImageSize`、`AddMask`、`SaveImage`、`WanVideoMiniMaxRemoverEmbeds`、`WanVideoEncode`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`Mute / Bypass Repeater (rgthree)`、`GetImageSizeAndCount`、`WanVideoVAELoader`、`PreviewBridge`、`ImageResizeKJ`、`WanVideoSampler`、`ResizeMask`、`INPAINT_MaskedFill`、`WanVideoContextOptions`、`WanVideoEnhanceAVideo`、`VHS_VideoCombine`、`LoadImage`、`VHS_LoadVideo`

**用到的条目**：LoadImage、easy seed、WanVideoSampler、WanVideoDecode、WanVideoEncode、WanVideoVAELoader、GetImageSize、GetImageSize+
