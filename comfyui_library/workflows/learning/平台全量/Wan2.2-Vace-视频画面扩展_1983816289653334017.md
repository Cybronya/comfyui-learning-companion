---
key: 平台全量/Wan2.2-Vace-视频画面扩展_1983816289653334017.json
name: Wan2.2-Vace-视频画面扩展_1983816289653334017
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.2-Vace-视频画面扩展_1983816289653334017.json
hash: 9778ed3976adaf15
coverage: 0.960784
learned_at: 2026-11-14 01:06:07
nodes: [WanVideoScheduler, WanVideoSampler, WanVideoVAELoader, JWInteger, JWInteger, JWInteger, JWInteger, ImagePadKJ, ImageAndMaskPreview, PreviewImage, PreviewImage, GetImageRangeFromBatch, GetImageRangeFromBatch, GrowMaskWithBlur, MaskPreview+, StringToFloatList, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoExtraModelSelect, WanVideoExtraModelSelect, WanVideoModelLoader, WanVideoModelLoader, WanVideoTorchCompileSettings, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoSetBlockSwap, WanVideoTextEncode, LoadWanVideoT5TextEncoder, WanVideoSetLoRAs, WanVideoSetLoRAs, StringToFloatList, GetImageSizeAndCount, INTConstant, WanVideoSigmaToStep, Float, WanVideoScheduler, WanVideoVACEEncode, ImageConcatMulti, GetImageSizeAndCount, VHS_VideoInfo, WanVideoSampler, LayerUtility: ImageScaleByAspectRatio V2, WanVideoDecode, JWInteger, JWInteger, CR Prompt Text, JWInteger, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoCombine]
patterns: []
missing: []
---

# 平台全量/Wan2.2-Vace-视频画面扩展_1983816289653334017.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.2-Vace-视频画面扩展_1983816289653334017.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（51 个）：
- `WanVideoScheduler`
- `WanVideoSampler` ★核心
- `WanVideoVAELoader`
- `JWInteger`
- `JWInteger`
- `JWInteger`
- `JWInteger`
- `ImagePadKJ`
- `ImageAndMaskPreview`
- `PreviewImage`
- `PreviewImage`
- `GetImageRangeFromBatch`
- `GetImageRangeFromBatch`
- `GrowMaskWithBlur`
- `MaskPreview+`
- `StringToFloatList`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoExtraModelSelect`
- `WanVideoExtraModelSelect`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoTextEncode`
- `LoadWanVideoT5TextEncoder`
- `WanVideoSetLoRAs`
- `WanVideoSetLoRAs`
- `StringToFloatList`
- `GetImageSizeAndCount`
- `INTConstant`
- `WanVideoSigmaToStep`
- `Float`
- `WanVideoScheduler`
- `WanVideoVACEEncode`
- `ImageConcatMulti`
- `GetImageSizeAndCount`
- `VHS_VideoInfo`
- `WanVideoSampler` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoDecode`
- `JWInteger`
- `JWInteger`
- `CR Prompt Text`
- `JWInteger`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoCombine`

## 知识

覆盖率 **96%**（49/51）

**有卡**：`WanVideoScheduler`、`WanVideoSampler`、`WanVideoVAELoader`、`JWInteger`、`ImagePadKJ`、`ImageAndMaskPreview`、`GetImageRangeFromBatch`、`GrowMaskWithBlur`、`MaskPreview+`、`StringToFloatList`、`WanVideoLoraSelect`、`WanVideoExtraModelSelect`、`WanVideoModelLoader`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`WanVideoTextEncode`、`LoadWanVideoT5TextEncoder`、`WanVideoSetLoRAs`、`GetImageSizeAndCount`、`INTConstant`、`WanVideoSigmaToStep`、`Float`、`WanVideoVACEEncode`、`ImageConcatMulti`、`VHS_VideoInfo`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoDecode`、`CR Prompt Text`、`VHS_LoadVideo`、`VHS_VideoCombine`

**用到的条目**：WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVACEEncode、WanVideoVAELoader、WanVideoLoraSelect、WanVideoSetLoRAs
