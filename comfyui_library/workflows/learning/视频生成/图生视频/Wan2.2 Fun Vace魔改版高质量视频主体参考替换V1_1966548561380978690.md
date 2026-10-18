---
key: 视频生成/图生视频/Wan2.2 Fun Vace魔改版高质量视频主体参考替换V1_1966548561380978690.json
name: Wan2.2 Fun Vace魔改版高质量视频主体参考替换V1_1966548561380978690.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2 Fun Vace魔改版高质量视频主体参考替换V1_1966548561380978690.json
hash: 9dffa2ddef7cff35
coverage: 0.90566
learned_at: 2026-10-15 22:31:38
nodes: [WanVideoSetBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSetLoRAs, WanVideoBlockSwap, TransparentBGSession+, ImageRemoveBackground+, Reroute, SolidMask, PreviewImage, VHS_DuplicateMasks, MaskToImage, InvertMask, MaskPreview, WanVideoTorchCompileSettings, WanVideoLoraSelect, WanVideoExtraModelSelect, WanVideoExtraModelSelect, WanVideoModelLoader, WanVideoModelLoader, WanVideoLoraSelect, StringToFloatList, ImageCompositeMasked, WanVideoTextEncode, INTConstant, WanVideoSigmaToStep, Float, StringToFloatList, WanVideoLoraSelect, LoadWanVideoT5TextEncoder, RH_Captioner, CR Prompt Text, easy showAnything, LoadImage, PDIMAGE_LongerSize, ImageConcatMulti, ImageConcatMulti, VHS_VideoCombine, WanVideoSampler, WanVideoSampler, WanVideoScheduler, WanVideoScheduler, WanVideoVAELoader, LayerUtility: ImageScaleByAspectRatio V2, WanVideoDecode, VHS_VideoCombine, JWInteger, Note, WanVideoVACEEncode, JWInteger, Note, VHS_LoadVideo, VHS_VideoInfo]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2 Fun Vace魔改版高质量视频主体参考替换V1_1966548561380978690.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1966548561380978690.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（53 个）：
- `WanVideoSetBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSetLoRAs`
- `WanVideoBlockSwap`
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
- `WanVideoLoraSelect`
- `StringToFloatList`
- `ImageCompositeMasked`
- `WanVideoTextEncode`
- `INTConstant`
- `WanVideoSigmaToStep`
- `Float`
- `StringToFloatList`
- `WanVideoLoraSelect`
- `LoadWanVideoT5TextEncoder`
- `RH_Captioner`
- `CR Prompt Text`
- `easy showAnything`
- `LoadImage`
- `PDIMAGE_LongerSize`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `WanVideoScheduler`
- `WanVideoScheduler`
- `WanVideoVAELoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `JWInteger`
- `Note`
- `WanVideoVACEEncode`
- `JWInteger`
- `Note`
- `VHS_LoadVideo`
- `VHS_VideoInfo`

## 知识

覆盖率 **91%**（48/53）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoBlockSwap`、`TransparentBGSession+`、`ImageRemoveBackground+`、`SolidMask`、`VHS_DuplicateMasks`、`MaskToImage`、`InvertMask`、`MaskPreview`、`WanVideoTorchCompileSettings`、`WanVideoLoraSelect`、`WanVideoExtraModelSelect`、`WanVideoModelLoader`、`StringToFloatList`、`ImageCompositeMasked`、`WanVideoTextEncode`、`INTConstant`、`WanVideoSigmaToStep`、`Float`、`LoadWanVideoT5TextEncoder`、`RH_Captioner`、`CR Prompt Text`、`LoadImage`、`PDIMAGE_LongerSize`、`ImageConcatMulti`、`VHS_VideoCombine`、`WanVideoSampler`、`WanVideoScheduler`、`WanVideoVAELoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoDecode`、`JWInteger`、`WanVideoVACEEncode`、`VHS_LoadVideo`、`VHS_VideoInfo`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoVACEEncode、WanVideoLoraSelect
