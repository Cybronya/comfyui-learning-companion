---
key: 平台全量/Wan2.2-Vace-局部编辑_1983813532632424449.json
name: Wan2.2-Vace-局部编辑_1983813532632424449
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.2-Vace-局部编辑_1983813532632424449.json
hash: 932c76933138dcaf
coverage: 0.956522
learned_at: 2026-11-14 01:06:07
nodes: [TransparentBGSession+, VHS_DuplicateMasks, InvertMask, WanVideoSigmaToStep, Float, WanVideoSampler, StringToFloatList, JWInteger, CR Prompt Text, VHS_LoadVideo, ImageRemoveBackground+, LayerUtility: ImageScaleByAspectRatio V2, ImageCompositeMasked, MaskToImage, SolidMask, Reroute, PreviewImage, MaskPreview, WanVideoExtraModelSelect, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoExtraModelSelect, WanVideoModelLoader, WanVideoModelLoader, LoadWanVideoT5TextEncoder, WanVideoTorchCompileSettings, WanVideoTextEncode, WanVideoSetBlockSwap, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSetLoRAs, StringToFloatList, WanVideoScheduler, WanVideoScheduler, INTConstant, GetImageSizeAndCount, WanVideoDecode, ImageConcatMulti, WanVideoSampler, WanVideoVAELoader, WanVideoVACEEncode, JWInteger, VHS_VideoCombine, VHS_VideoCombine]
patterns: []
missing: []
---

# 平台全量/Wan2.2-Vace-局部编辑_1983813532632424449.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.2-Vace-局部编辑_1983813532632424449.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（46 个）：
- `TransparentBGSession+`
- `VHS_DuplicateMasks`
- `InvertMask`
- `WanVideoSigmaToStep`
- `Float`
- `WanVideoSampler` ★核心
- `StringToFloatList`
- `JWInteger`
- `CR Prompt Text`
- `VHS_LoadVideo`
- `ImageRemoveBackground+`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageCompositeMasked`
- `MaskToImage`
- `SolidMask`
- `Reroute`
- `PreviewImage`
- `MaskPreview`
- `WanVideoExtraModelSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoExtraModelSelect`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoTorchCompileSettings`
- `WanVideoTextEncode`
- `WanVideoSetBlockSwap`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSetLoRAs`
- `StringToFloatList`
- `WanVideoScheduler`
- `WanVideoScheduler`
- `INTConstant`
- `GetImageSizeAndCount`
- `WanVideoDecode`
- `ImageConcatMulti`
- `WanVideoSampler` ★核心
- `WanVideoVAELoader`
- `WanVideoVACEEncode`
- `JWInteger`
- `VHS_VideoCombine`
- `VHS_VideoCombine`

## 知识

覆盖率 **96%**（44/46）

**有卡**：`TransparentBGSession+`、`VHS_DuplicateMasks`、`InvertMask`、`WanVideoSigmaToStep`、`Float`、`WanVideoSampler`、`StringToFloatList`、`JWInteger`、`CR Prompt Text`、`VHS_LoadVideo`、`ImageRemoveBackground+`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageCompositeMasked`、`MaskToImage`、`SolidMask`、`MaskPreview`、`WanVideoExtraModelSelect`、`WanVideoLoraSelect`、`WanVideoModelLoader`、`LoadWanVideoT5TextEncoder`、`WanVideoTorchCompileSettings`、`WanVideoTextEncode`、`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`WanVideoSetLoRAs`、`WanVideoScheduler`、`INTConstant`、`GetImageSizeAndCount`、`WanVideoDecode`、`ImageConcatMulti`、`WanVideoVAELoader`、`WanVideoVACEEncode`、`VHS_VideoCombine`

**用到的条目**：WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVACEEncode、WanVideoVAELoader、WanVideoLoraSelect、WanVideoSetLoRAs
