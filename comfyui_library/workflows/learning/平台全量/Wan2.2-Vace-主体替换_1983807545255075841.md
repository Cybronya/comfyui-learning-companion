---
key: 平台全量/Wan2.2-Vace-主体替换_1983807545255075841.json
name: Wan2.2-Vace-主体替换_1983807545255075841
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.2-Vace-主体替换_1983807545255075841.json
hash: 05f803f9a5a3c26f
coverage: 0.941176
learned_at: 2026-11-14 01:06:06
nodes: [Reroute, SolidMask, VHS_DuplicateMasks, MaskToImage, MaskPreview, WanVideoSampler, WanVideoSampler, WanVideoScheduler, StringToFloatList, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoExtraModelSelect, WanVideoModelLoader, WanVideoExtraModelSelect, WanVideoModelLoader, LoadWanVideoT5TextEncoder, WanVideoTorchCompileSettings, WanVideoSetBlockSwap, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSetLoRAs, WanVideoScheduler, WanVideoSigmaToStep, Float, INTConstant, StringToFloatList, WanVideoVAELoader, WanVideoDecode, ImageConcatMulti, ImageConcatMulti, PDIMAGE_LongerSize, InvertMask, ImageRemoveBackground+, TransparentBGSession+, PreviewImage, WanVideoVACEEncode, VHS_VideoInfo, LoadImage, JWInteger, JWInteger, easy showAnything, CR Prompt Text, WanVideoTextEncode, RH_Captioner, VHS_LoadVideo, LayerUtility: ImageScaleByAspectRatio V2, ImageCompositeMasked, VHS_VideoCombine, VHS_VideoCombine]
patterns: []
missing: []
---

# 平台全量/Wan2.2-Vace-主体替换_1983807545255075841.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.2-Vace-主体替换_1983807545255075841.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（51 个）：
- `Reroute`
- `SolidMask`
- `VHS_DuplicateMasks`
- `MaskToImage`
- `MaskPreview`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `WanVideoScheduler`
- `StringToFloatList`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoExtraModelSelect`
- `WanVideoModelLoader`
- `WanVideoExtraModelSelect`
- `WanVideoModelLoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoTorchCompileSettings`
- `WanVideoSetBlockSwap`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSetLoRAs`
- `WanVideoScheduler`
- `WanVideoSigmaToStep`
- `Float`
- `INTConstant`
- `StringToFloatList`
- `WanVideoVAELoader`
- `WanVideoDecode`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `PDIMAGE_LongerSize`
- `InvertMask`
- `ImageRemoveBackground+`
- `TransparentBGSession+`
- `PreviewImage`
- `WanVideoVACEEncode`
- `VHS_VideoInfo`
- `LoadImage`
- `JWInteger`
- `JWInteger`
- `easy showAnything`
- `CR Prompt Text`
- `WanVideoTextEncode`
- `RH_Captioner`
- `VHS_LoadVideo`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageCompositeMasked`
- `VHS_VideoCombine`
- `VHS_VideoCombine`

## 知识

覆盖率 **94%**（48/51）

**有卡**：`SolidMask`、`VHS_DuplicateMasks`、`MaskToImage`、`MaskPreview`、`WanVideoSampler`、`WanVideoScheduler`、`StringToFloatList`、`WanVideoLoraSelect`、`WanVideoExtraModelSelect`、`WanVideoModelLoader`、`LoadWanVideoT5TextEncoder`、`WanVideoTorchCompileSettings`、`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`WanVideoSetLoRAs`、`WanVideoSigmaToStep`、`Float`、`INTConstant`、`WanVideoVAELoader`、`WanVideoDecode`、`ImageConcatMulti`、`PDIMAGE_LongerSize`、`InvertMask`、`ImageRemoveBackground+`、`TransparentBGSession+`、`WanVideoVACEEncode`、`VHS_VideoInfo`、`LoadImage`、`JWInteger`、`CR Prompt Text`、`WanVideoTextEncode`、`RH_Captioner`、`VHS_LoadVideo`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageCompositeMasked`、`VHS_VideoCombine`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVACEEncode、WanVideoVAELoader、WanVideoLoraSelect
