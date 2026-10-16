---
key: 视频生成/图生视频/Wan 2.1 FusionX VACE+Control_1949680224212000770.json
name: Wan 2.1 FusionX VACE+Control_1949680224212000770.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1949680224212000770.json
hash: 0be91f67a236a351
coverage: 0.759259
learned_at: 2026-10-15 22:30:49
nodes: [WanVideoBlockSwap, WanVideoVACEModelSelect, GetNode, VHS_LoadVideo, AIO_Preprocessor, GetNode, GetImageSizeAndCount, MaskPreview, WanVideoVACEStartToEndFrame, SetNode, ImageBlend, AIO_Preprocessor, SetNode, ImageResizeKJv2, ImageResizeKJv2, VHS_VideoCombine, ImageResizeKJv2, ImageResizeKJv2, ImageResizeKJv2, ImagePadKJ, ImageScale, Int, PreviewImage, WanVideoTextEncodeSingle, GetNode, LoadImage, WanVideoVACEEncode, WanVideoApplyNAG, WanVideoSLG, WanVideoExperimentalArgs, GetNode, WanVideoSampler, WanVideoVACEEncode, GetImageSizeAndCount, GetNode, WanVideoDecode, GetNode, ImageConcatMulti, EmptyImage, VHS_VideoCombine, VHS_VideoCombine, Int, SetNode, SetNode, SetNode, LoadWanVideoT5TextEncoder, WanVideoModelLoader, WanVideoVAELoader, Note Plus (mtb), LoadImageFromUrl, PreviewImage, WanVideoVACEStartToEndFrame, ImageConcatMulti, WanVideoTextEncodeSingle]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan 2.1 FusionX VACE+Control_1949680224212000770.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1949680224212000770.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（54 个）：
- `WanVideoBlockSwap`
- `WanVideoVACEModelSelect`
- `GetNode`
- `VHS_LoadVideo`
- `AIO_Preprocessor`
- `GetNode`
- `GetImageSizeAndCount`
- `MaskPreview`
- `WanVideoVACEStartToEndFrame`
- `SetNode`
- `ImageBlend`
- `AIO_Preprocessor`
- `SetNode`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `VHS_VideoCombine`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `ImagePadKJ`
- `ImageScale`
- `Int`
- `PreviewImage`
- `WanVideoTextEncodeSingle`
- `GetNode`
- `LoadImage`
- `WanVideoVACEEncode`
- `WanVideoApplyNAG`
- `WanVideoSLG`
- `WanVideoExperimentalArgs`
- `GetNode`
- `WanVideoSampler` ★核心
- `WanVideoVACEEncode`
- `GetImageSizeAndCount`
- `GetNode`
- `WanVideoDecode`
- `GetNode`
- `ImageConcatMulti`
- `EmptyImage`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `Int`
- `SetNode`
- `SetNode`
- `SetNode`
- `LoadWanVideoT5TextEncoder`
- `WanVideoModelLoader`
- `WanVideoVAELoader`
- `Note Plus (mtb)`
- `LoadImageFromUrl`
- `PreviewImage`
- `WanVideoVACEStartToEndFrame`
- `ImageConcatMulti`
- `WanVideoTextEncodeSingle`

## 知识

覆盖率 **76%**（41/54）

**有卡**：`WanVideoBlockSwap`、`WanVideoVACEModelSelect`、`VHS_LoadVideo`、`AIO_Preprocessor`、`GetImageSizeAndCount`、`MaskPreview`、`WanVideoVACEStartToEndFrame`、`ImageBlend`、`ImageResizeKJv2`、`VHS_VideoCombine`、`ImagePadKJ`、`ImageScale`、`Int`、`WanVideoTextEncodeSingle`、`LoadImage`、`WanVideoVACEEncode`、`WanVideoApplyNAG`、`WanVideoSLG`、`WanVideoExperimentalArgs`、`WanVideoSampler`、`WanVideoDecode`、`ImageConcatMulti`、`EmptyImage`、`LoadWanVideoT5TextEncoder`、`WanVideoModelLoader`、`WanVideoVAELoader`、`Note Plus (mtb)`、`LoadImageFromUrl`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoVAELoader、WanVideoTextEncodeSingle、WanVideoVACEEncode、GetImageSizeAndCount
