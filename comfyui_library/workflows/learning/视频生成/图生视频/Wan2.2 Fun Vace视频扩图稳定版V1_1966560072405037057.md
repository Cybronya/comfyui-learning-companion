---
key: 视频生成/图生视频/Wan2.2 Fun Vace视频扩图稳定版V1_1966560072405037057.json
name: Wan2.2 Fun Vace视频扩图稳定版V1_1966560072405037057.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2 Fun Vace视频扩图稳定版V1_1966560072405037057.json
hash: 6558669b40ef03bb
coverage: 0.844828
learned_at: 2026-10-15 22:31:38
nodes: [WanVideoSetBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSetLoRAs, LoadWanVideoT5TextEncoder, WanVideoBlockSwap, WanVideoTorchCompileSettings, WanVideoLoraSelect, WanVideoExtraModelSelect, WanVideoExtraModelSelect, WanVideoModelLoader, WanVideoModelLoader, WanVideoLoraSelect, StringToFloatList, WanVideoTextEncode, INTConstant, WanVideoSigmaToStep, Float, WanVideoScheduler, WanVideoScheduler, StringToFloatList, WanVideoLoraSelect, WanVideoSampler, JWInteger, Note, Note, GetImageSizeAndCount, VHS_LoadVideo, CR Prompt Text, WanVideoSampler, WanVideoVACEEncode, WanVideoVAELoader, MaskPreview+, VHS_VideoCombine, GetImageSizeAndCount, VHS_VideoInfo, GetImageRangeFromBatch, GetImageRangeFromBatch, GrowMaskWithBlur, ImagePadKJ, ImageAndMaskPreview, PreviewImage, WanVideoDecode, PreviewImage, JWInteger, LayerUtility: ImageScaleByAspectRatio V2, ImageConcatMulti, VHS_VideoCombine, JWInteger, JWInteger, Note, JWInteger, Note, Note, JWInteger, Note, JWInteger, Note]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2 Fun Vace视频扩图稳定版V1_1966560072405037057.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1966560072405037057.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（58 个）：
- `WanVideoSetBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSetLoRAs`
- `LoadWanVideoT5TextEncoder`
- `WanVideoBlockSwap`
- `WanVideoTorchCompileSettings`
- `WanVideoLoraSelect`
- `WanVideoExtraModelSelect`
- `WanVideoExtraModelSelect`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `StringToFloatList`
- `WanVideoTextEncode`
- `INTConstant`
- `WanVideoSigmaToStep`
- `Float`
- `WanVideoScheduler`
- `WanVideoScheduler`
- `StringToFloatList`
- `WanVideoLoraSelect`
- `WanVideoSampler` ★核心
- `JWInteger`
- `Note`
- `Note`
- `GetImageSizeAndCount`
- `VHS_LoadVideo`
- `CR Prompt Text`
- `WanVideoSampler` ★核心
- `WanVideoVACEEncode`
- `WanVideoVAELoader`
- `MaskPreview+`
- `VHS_VideoCombine`
- `GetImageSizeAndCount`
- `VHS_VideoInfo`
- `GetImageRangeFromBatch`
- `GetImageRangeFromBatch`
- `GrowMaskWithBlur`
- `ImagePadKJ`
- `ImageAndMaskPreview`
- `PreviewImage`
- `WanVideoDecode`
- `PreviewImage`
- `JWInteger`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `JWInteger`
- `JWInteger`
- `Note`
- `JWInteger`
- `Note`
- `Note`
- `JWInteger`
- `Note`
- `JWInteger`
- `Note`

## 知识

覆盖率 **84%**（49/58）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`LoadWanVideoT5TextEncoder`、`WanVideoBlockSwap`、`WanVideoTorchCompileSettings`、`WanVideoLoraSelect`、`WanVideoExtraModelSelect`、`WanVideoModelLoader`、`StringToFloatList`、`WanVideoTextEncode`、`INTConstant`、`WanVideoSigmaToStep`、`Float`、`WanVideoScheduler`、`WanVideoSampler`、`JWInteger`、`GetImageSizeAndCount`、`VHS_LoadVideo`、`CR Prompt Text`、`WanVideoVACEEncode`、`WanVideoVAELoader`、`MaskPreview+`、`VHS_VideoCombine`、`VHS_VideoInfo`、`GetImageRangeFromBatch`、`GrowMaskWithBlur`、`ImagePadKJ`、`ImageAndMaskPreview`、`WanVideoDecode`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageConcatMulti`

**用到的条目**：WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoVACEEncode、WanVideoLoraSelect、WanVideoSetLoRAs
