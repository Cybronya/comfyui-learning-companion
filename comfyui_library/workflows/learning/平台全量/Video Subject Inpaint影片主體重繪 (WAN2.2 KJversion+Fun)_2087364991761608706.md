---
key: 平台全量/Video Subject Inpaint影片主體重繪 (WAN2.2 KJversion+Fun)_2087364991761608706.json
name: Video Subject Inpaint影片主體重繪 (WAN2.2 KJversion+Fun)_2087364991761608706
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Video Subject Inpaint影片主體重繪 (WAN2.2 KJversion+Fun)_2087364991761608706.json
hash: 8dd2d6caea23b7e9
coverage: 0.830189
learned_at: 2026-11-14 01:03:15
nodes: [WanVideoScheduler, WanVideoScheduler, WanVideoModelLoader, WanVideoModelLoader, StringToFloatList, WanVideoSetBlockSwap, WanVideoSetBlockSwap, WanVideoBlockSwap, WanVideoLoraSelect, WanVideoSetLoRAs, WanVideoSetLoRAs, WanVideoExtraModelSelect, WanVideoExtraModelSelect, WanVideoTorchCompileSettings, LoadWanVideoT5TextEncoder, WanVideoVAELoader, INTConstant, WanVideoSigmaToStep, Float, WanVideoLoraSelect, MaskToImage, SolidMask, VHS_DuplicateMasks, WanVideoLoraSelect, WanVideoSampler, BiRefNetRMBG, MaskPreview, InvertMask, ImageCompositeMasked, PreviewImage, WanVideoVACEEncode, StringToFloatList, WanVideoSampler, BiRefNetRMBG, PrimitiveInt, Note, Note, WanVideoDecode, PrimitiveInt, WanVideoTextEncode, VHS_VideoCombine, LayerUtility: ImageScaleByAspectRatio V2, VHS_LoadVideo, ImageFromBatch, SaveImage, Note, LayerUtility: PurgeVRAM, PreviewImage, Note, ImageResizeKJv2, Note, CR Prompt Text, LoadImage]
patterns: []
missing: []
---

# 平台全量/Video Subject Inpaint影片主體重繪 (WAN2.2 KJversion+Fun)_2087364991761608706.json

> 来源文件 `comfyui_library/workflows/平台全量/Video Subject Inpaint影片主體重繪 (WAN2.2 KJversion+Fun)_2087364991761608706.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（53 个）：
- `WanVideoScheduler`
- `WanVideoScheduler`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `StringToFloatList`
- `WanVideoSetBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoBlockSwap`
- `WanVideoLoraSelect`
- `WanVideoSetLoRAs`
- `WanVideoSetLoRAs`
- `WanVideoExtraModelSelect`
- `WanVideoExtraModelSelect`
- `WanVideoTorchCompileSettings`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `INTConstant`
- `WanVideoSigmaToStep`
- `Float`
- `WanVideoLoraSelect`
- `MaskToImage`
- `SolidMask`
- `VHS_DuplicateMasks`
- `WanVideoLoraSelect`
- `WanVideoSampler` ★核心
- `BiRefNetRMBG`
- `MaskPreview`
- `InvertMask`
- `ImageCompositeMasked`
- `PreviewImage`
- `WanVideoVACEEncode`
- `StringToFloatList`
- `WanVideoSampler` ★核心
- `BiRefNetRMBG`
- `PrimitiveInt`
- `Note`
- `Note`
- `WanVideoDecode`
- `PrimitiveInt`
- `WanVideoTextEncode`
- `VHS_VideoCombine`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VHS_LoadVideo`
- `ImageFromBatch`
- `SaveImage`
- `Note`
- `LayerUtility: PurgeVRAM`
- `PreviewImage`
- `Note`
- `ImageResizeKJv2`
- `Note`
- `CR Prompt Text`
- `LoadImage`

## 知识

覆盖率 **83%**（44/53）

**有卡**：`WanVideoScheduler`、`WanVideoModelLoader`、`StringToFloatList`、`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`WanVideoLoraSelect`、`WanVideoSetLoRAs`、`WanVideoExtraModelSelect`、`WanVideoTorchCompileSettings`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`INTConstant`、`WanVideoSigmaToStep`、`Float`、`MaskToImage`、`SolidMask`、`VHS_DuplicateMasks`、`WanVideoSampler`、`BiRefNetRMBG`、`MaskPreview`、`InvertMask`、`ImageCompositeMasked`、`WanVideoVACEEncode`、`WanVideoDecode`、`WanVideoTextEncode`、`VHS_VideoCombine`、`LayerUtility: ImageScaleByAspectRatio V2`、`VHS_LoadVideo`、`ImageFromBatch`、`SaveImage`、`LayerUtility: PurgeVRAM`、`ImageResizeKJv2`、`CR Prompt Text`、`LoadImage`

**用到的条目**：LayerUtility: ImageScaleByAspectRatio V2、LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVACEEncode、WanVideoVAELoader
