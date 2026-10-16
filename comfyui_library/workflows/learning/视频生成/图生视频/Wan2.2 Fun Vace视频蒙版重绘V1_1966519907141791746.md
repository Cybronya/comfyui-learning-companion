---
key: 视频生成/图生视频/Wan2.2 Fun Vace视频蒙版重绘V1_1966519907141791746.json
name: Wan2.2 Fun Vace视频蒙版重绘V1_1966519907141791746.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1966519907141791746.json
hash: 24448bbe41769de9
coverage: 0.916667
learned_at: 2026-10-15 22:31:38
nodes: [WanVideoSetBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSetLoRAs, LoadWanVideoT5TextEncoder, WanVideoDecode, ImageConcatMulti, WanVideoBlockSwap, WanVideoVACEEncode, TransparentBGSession+, ImageRemoveBackground+, Reroute, SolidMask, PreviewImage, VHS_DuplicateMasks, MaskToImage, InvertMask, MaskPreview, WanVideoTorchCompileSettings, WanVideoLoraSelect, WanVideoExtraModelSelect, WanVideoExtraModelSelect, WanVideoModelLoader, WanVideoModelLoader, WanVideoVAELoader, WanVideoLoraSelect, StringToFloatList, VHS_LoadVideo, ImageCompositeMasked, CR Prompt Text, WanVideoTextEncode, INTConstant, WanVideoSigmaToStep, Float, WanVideoScheduler, WanVideoScheduler, StringToFloatList, WanVideoLoraSelect, LayerUtility: ImageScaleByAspectRatio V2, WanVideoSampler, WanVideoSampler, VHS_VideoCombine, GetImageSizeAndCount, VHS_VideoCombine, JWInteger, JWInteger, Note, Note]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2 Fun Vace视频蒙版重绘V1_1966519907141791746.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1966519907141791746.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（48 个）：
- `WanVideoSetBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSetLoRAs`
- `LoadWanVideoT5TextEncoder`
- `WanVideoDecode`
- `ImageConcatMulti`
- `WanVideoBlockSwap`
- `WanVideoVACEEncode`
- `TransparentBGSession+`
- `ImageRemoveBackground+`
- `Reroute`
- `SolidMask`
- `PreviewImage`
- `VHS_DuplicateMasks`
- `MaskToImage`
- `InvertMask`
- `MaskPreview`
- `WanVideoTorchCompileSettings`
- `WanVideoLoraSelect`
- `WanVideoExtraModelSelect`
- `WanVideoExtraModelSelect`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoVAELoader`
- `WanVideoLoraSelect`
- `StringToFloatList`
- `VHS_LoadVideo`
- `ImageCompositeMasked`
- `CR Prompt Text`
- `WanVideoTextEncode`
- `INTConstant`
- `WanVideoSigmaToStep`
- `Float`
- `WanVideoScheduler`
- `WanVideoScheduler`
- `StringToFloatList`
- `WanVideoLoraSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `VHS_VideoCombine`
- `GetImageSizeAndCount`
- `VHS_VideoCombine`
- `JWInteger`
- `JWInteger`
- `Note`
- `Note`

## 知识

覆盖率 **92%**（44/48）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`LoadWanVideoT5TextEncoder`、`WanVideoDecode`、`ImageConcatMulti`、`WanVideoBlockSwap`、`WanVideoVACEEncode`、`TransparentBGSession+`、`ImageRemoveBackground+`、`SolidMask`、`VHS_DuplicateMasks`、`MaskToImage`、`InvertMask`、`MaskPreview`、`WanVideoTorchCompileSettings`、`WanVideoLoraSelect`、`WanVideoExtraModelSelect`、`WanVideoModelLoader`、`WanVideoVAELoader`、`StringToFloatList`、`VHS_LoadVideo`、`ImageCompositeMasked`、`CR Prompt Text`、`WanVideoTextEncode`、`INTConstant`、`WanVideoSigmaToStep`、`Float`、`WanVideoScheduler`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoSampler`、`VHS_VideoCombine`、`GetImageSizeAndCount`、`JWInteger`

**用到的条目**：WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoVACEEncode、WanVideoLoraSelect、WanVideoSetLoRAs
