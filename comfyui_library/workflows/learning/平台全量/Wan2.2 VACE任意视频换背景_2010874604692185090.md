---
key: 平台全量/Wan2.2 VACE任意视频换背景_2010874604692185090.json
name: Wan2.2 VACE任意视频换背景_2010874604692185090
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.2 VACE任意视频换背景_2010874604692185090.json
hash: 776349571f7a0caa
coverage: 0.875
learned_at: 2026-11-14 01:05:34
nodes: [LayerUtility: PurgeVRAM V2, RIFE VFI, GetNode, VHS_VideoCombine, LayerUtility: PurgeVRAM V2, WanVideoDecode, ImageFromBatch+, GetNode, GetNode, GetImageSizeAndCount, ImageUpscaleWithModelBatched, WanVideoSampler, WanVideoSampler, INTConstant, UpscaleModelLoader, GetImageSizeAndCount, WanVideoVAELoader, INTConstant, Fast Groups Muter (rgthree), VHS_VideoCombine, LoadImage, VHS_VideoInfo, TTP_text_mix, VHS_LoadVideo, SetNode, SetNode, easy cleanGpuUsed, WanVideoBlockSwap, VHS_VideoCombine, LoadWanVideoT5TextEncoder, easy cleanGpuUsed, WanVideoTextEncode, LayerMask: ObjectDetectorFL2, RH_Translator, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoLoraSelect, LayerMask: SAM2Ultra, LayerMask: LoadFlorence2Model, LayerMask: SAM2VideoUltra, WanVideoVACEEncode, InvertMask, GrowMaskWithBlur, SeCModelLoader, MaskPreview, easy cleanGpuUsed, SeCVideoSegmentation, LayerMask: ObjectDetectorFL2, ImageFromBatch, Reroute, Reroute, GrowMask, INPAINT_MaskedFill, VHS_VideoCombine, MaskToImage, WanVideoBlockSwap, WanVideoVACEModelSelect, WanVideoModelLoader, WanVideoSetBlockSwap, CreateCFGScheduleFloatList, LayerUtility: ImageScaleByAspectRatio V2, INPAINT_MaskedFill, VHS_VideoCombine, GetImageRangeFromBatch, Sa2VANodeTpl, PreviewAny, LayerUtility: ImageScaleByAspectRatio V2, AILab_QwenVL, easy cleanGpuUsed]
patterns: []
missing: []
---

# 平台全量/Wan2.2 VACE任意视频换背景_2010874604692185090.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.2 VACE任意视频换背景_2010874604692185090.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（72 个）：
- `LayerUtility: PurgeVRAM V2`
- `RIFE VFI`
- `GetNode`
- `VHS_VideoCombine`
- `LayerUtility: PurgeVRAM V2`
- `WanVideoDecode`
- `ImageFromBatch+`
- `GetNode`
- `GetNode`
- `GetImageSizeAndCount`
- `ImageUpscaleWithModelBatched`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `INTConstant`
- `UpscaleModelLoader`
- `GetImageSizeAndCount`
- `WanVideoVAELoader`
- `INTConstant`
- `Fast Groups Muter (rgthree)`
- `VHS_VideoCombine`
- `LoadImage`
- `VHS_VideoInfo`
- `TTP_text_mix`
- `VHS_LoadVideo`
- `SetNode`
- `SetNode`
- `easy cleanGpuUsed`
- `WanVideoBlockSwap`
- `VHS_VideoCombine`
- `LoadWanVideoT5TextEncoder`
- `easy cleanGpuUsed`
- `WanVideoTextEncode`
- `LayerMask: ObjectDetectorFL2`
- `RH_Translator`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoLoraSelect`
- `LayerMask: SAM2Ultra`
- `LayerMask: LoadFlorence2Model`
- `LayerMask: SAM2VideoUltra`
- `WanVideoVACEEncode`
- `InvertMask`
- `GrowMaskWithBlur`
- `SeCModelLoader`
- `MaskPreview`
- `easy cleanGpuUsed`
- `SeCVideoSegmentation`
- `LayerMask: ObjectDetectorFL2`
- `ImageFromBatch`
- `Reroute`
- `Reroute`
- `GrowMask`
- `INPAINT_MaskedFill`
- `VHS_VideoCombine`
- `MaskToImage`
- `WanVideoBlockSwap`
- `WanVideoVACEModelSelect`
- `WanVideoModelLoader`
- `WanVideoSetBlockSwap`
- `CreateCFGScheduleFloatList`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `INPAINT_MaskedFill`
- `VHS_VideoCombine`
- `GetImageRangeFromBatch`
- `Sa2VANodeTpl`
- `PreviewAny`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `AILab_QwenVL`
- `easy cleanGpuUsed`

## 知识

覆盖率 **88%**（63/72）

**有卡**：`LayerUtility: PurgeVRAM V2`、`RIFE VFI`、`VHS_VideoCombine`、`WanVideoDecode`、`ImageFromBatch+`、`GetImageSizeAndCount`、`ImageUpscaleWithModelBatched`、`WanVideoSampler`、`INTConstant`、`UpscaleModelLoader`、`WanVideoVAELoader`、`LoadImage`、`VHS_VideoInfo`、`TTP_text_mix`、`VHS_LoadVideo`、`easy cleanGpuUsed`、`WanVideoBlockSwap`、`LoadWanVideoT5TextEncoder`、`WanVideoTextEncode`、`LayerMask: ObjectDetectorFL2`、`RH_Translator`、`WanVideoLoraSelect`、`WanVideoModelLoader`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`LayerMask: SAM2Ultra`、`LayerMask: LoadFlorence2Model`、`LayerMask: SAM2VideoUltra`、`WanVideoVACEEncode`、`InvertMask`、`GrowMaskWithBlur`、`SeCModelLoader`、`MaskPreview`、`SeCVideoSegmentation`、`ImageFromBatch`、`GrowMask`、`INPAINT_MaskedFill`、`MaskToImage`、`WanVideoVACEModelSelect`、`CreateCFGScheduleFloatList`、`LayerUtility: ImageScaleByAspectRatio V2`、`GetImageRangeFromBatch`、`Sa2VANodeTpl`、`AILab_QwenVL`

**用到的条目**：LoadImage、CreateCFGScheduleFloatList、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVACEEncode、WanVideoVAELoader
