---
key: 平台全量/Wan2.1 Vace stand-in  视频换人（完全免费，无加密）_1957116752675135490.json
name: Wan2.1 Vace stand-in  视频换人（完全免费，无加密）_1957116752675135490
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.1 Vace stand-in  视频换人（完全免费，无加密）_1957116752675135490.json
hash: 92100fb0ce41372d
coverage: 0.393939
learned_at: 2026-11-14 01:04:27
nodes: [DownloadAndLoadSAM2Model, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, Sam2Segmentation, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, SetNode, SetNode, ImageResizeKJv2, SetNode, GetNode, LoadWanVideoT5TextEncoder, SetNode, SetNode, WanVideoEmptyEmbeds, GetNode, Reroute, GetNode, WanVideoEncode, GetNode, WanVideoDecode, SetNode, GetNode, GetNode, GetImageSizeAndCount, ImageResizeKJv2, SetNode, easy mathInt, GetNode, SetNode, GetNode, GetNode, ImageFromBatch, VHS_VideoCombine, VHS_VideoCombine, WanVideoSampler, WanVideoSampler, GetNode, GetNode, GetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, ImageResizeKJv2, GetNode, DepthAnythingV2Preprocessor, GetNode, SetNode, SetNode, WanVideoSetLoRAs, WanVideoTextEncodeSingle, GetNode, GetNode, SetNode, WanVideoAddStandInLatent, GetImageSizeAndCount, FaceProcessorLoader, GetNode, GetNode, SetNode, VideoInputPreprocessor, Florence2toCoordinates, SetNode, GetNode, LoadImage, GetNode, PreviewImage, SetNode, WanVideoApplyNAG, ApplyFaceProcessor, Florence2ModelLoader, LayerUtility: ImageRemoveAlpha, ImageResizeKJv2, WanVideoUniAnimateDWPoseDetector, DWPreprocessor, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, WanVideoAddStandInLatent, LayerUtility: ImageBlend V2, ImageResizeKJv2, ImageResizeKJv2, easy imageRemBg, InpaintPreprocessor, SetNode, GetNode, SetNode, GetNode, VHS_VideoCombine, LayerUtility: ImageRemoveAlpha, GetNode, PreviewImage, SetNode, GetNode, WanVideoEncode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, ImageFromBatch, WanVideoDecode, GetNode, WanVideoVACEStartToEndFrame, GetNode, WanVideoVACEStartToEndFrame, WanVideoVACEEncode, GetNode, SetNode, SetNode, GetNode, GetNode, SetNode, SetNode, LayerUtility: ImageBlend V2, GetNode, GetNode, GetNode, GetNode, GetNode, WanVideoTextEncodeSingle, GetNode, GetNode, Florence2Run, MaskToImage, InpaintPreprocessor, WanVideoVACEEncode, VHS_VideoCombine, GrowMaskWithBlur, String, WanVideoBlockSwap, Fast Groups Muter (rgthree), PreviewImage, INTConstant, INTConstant, INTConstant, INTConstant, WanVideoVAELoader, CR Upscale Image, GetNode, LoadImage, SetNode, SetNode, INTConstant, VHS_LoadVideo, WanVideoTorchCompileSettings, easy seed, SetNode, SetNode, WanVideoSetLoRAs, WanVideoVACEModelSelect, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoModelLoader, WanVideoModelLoader, SetNode, ColorMatch, DownloadAndLoadGIMMVFIModel, GIMMVFI_interpolate, VHS_VideoCombine, SDMatteApply]
patterns: []
missing: []
---

# 平台全量/Wan2.1 Vace stand-in  视频换人（完全免费，无加密）_1957116752675135490.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.1 Vace stand-in  视频换人（完全免费，无加密）_1957116752675135490.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（198 个）：
- `DownloadAndLoadSAM2Model`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `Sam2Segmentation`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `ImageResizeKJv2`
- `SetNode`
- `GetNode`
- `LoadWanVideoT5TextEncoder`
- `SetNode`
- `SetNode`
- `WanVideoEmptyEmbeds`
- `GetNode`
- `Reroute`
- `GetNode`
- `WanVideoEncode`
- `GetNode`
- `WanVideoDecode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetImageSizeAndCount`
- `ImageResizeKJv2`
- `SetNode`
- `easy mathInt`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `ImageFromBatch`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageResizeKJv2`
- `GetNode`
- `DepthAnythingV2Preprocessor`
- `GetNode`
- `SetNode`
- `SetNode`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeSingle`
- `GetNode`
- `GetNode`
- `SetNode`
- `WanVideoAddStandInLatent`
- `GetImageSizeAndCount`
- `FaceProcessorLoader`
- `GetNode`
- `GetNode`
- `SetNode`
- `VideoInputPreprocessor`
- `Florence2toCoordinates`
- `SetNode`
- `GetNode`
- `LoadImage`
- `GetNode`
- `PreviewImage`
- `SetNode`
- `WanVideoApplyNAG`
- `ApplyFaceProcessor`
- `Florence2ModelLoader`
- `LayerUtility: ImageRemoveAlpha`
- `ImageResizeKJv2`
- `WanVideoUniAnimateDWPoseDetector`
- `DWPreprocessor`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoAddStandInLatent`
- `LayerUtility: ImageBlend V2`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `easy imageRemBg`
- `InpaintPreprocessor`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `VHS_VideoCombine`
- `LayerUtility: ImageRemoveAlpha`
- `GetNode`
- `PreviewImage`
- `SetNode`
- `GetNode`
- `WanVideoEncode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `ImageFromBatch`
- `WanVideoDecode`
- `GetNode`
- `WanVideoVACEStartToEndFrame`
- `GetNode`
- `WanVideoVACEStartToEndFrame`
- `WanVideoVACEEncode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `LayerUtility: ImageBlend V2`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoTextEncodeSingle`
- `GetNode`
- `GetNode`
- `Florence2Run`
- `MaskToImage`
- `InpaintPreprocessor`
- `WanVideoVACEEncode`
- `VHS_VideoCombine`
- `GrowMaskWithBlur`
- `String`
- `WanVideoBlockSwap`
- `Fast Groups Muter (rgthree)`
- `PreviewImage`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `WanVideoVAELoader`
- `CR Upscale Image`
- `GetNode`
- `LoadImage`
- `SetNode`
- `SetNode`
- `INTConstant`
- `VHS_LoadVideo`
- `WanVideoTorchCompileSettings`
- `easy seed`
- `SetNode`
- `SetNode`
- `WanVideoSetLoRAs`
- `WanVideoVACEModelSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `SetNode`
- `ColorMatch`
- `DownloadAndLoadGIMMVFIModel`
- `GIMMVFI_interpolate`
- `VHS_VideoCombine`
- `SDMatteApply`

## 知识

覆盖率 **39%**（78/198）

**有卡**：`DownloadAndLoadSAM2Model`、`Sam2Segmentation`、`ImageResizeKJv2`、`LoadWanVideoT5TextEncoder`、`WanVideoEmptyEmbeds`、`WanVideoEncode`、`WanVideoDecode`、`GetImageSizeAndCount`、`easy mathInt`、`ImageFromBatch`、`VHS_VideoCombine`、`WanVideoSampler`、`DepthAnythingV2Preprocessor`、`WanVideoSetLoRAs`、`WanVideoTextEncodeSingle`、`WanVideoAddStandInLatent`、`FaceProcessorLoader`、`VideoInputPreprocessor`、`Florence2toCoordinates`、`LoadImage`、`WanVideoApplyNAG`、`ApplyFaceProcessor`、`Florence2ModelLoader`、`LayerUtility: ImageRemoveAlpha`、`WanVideoUniAnimateDWPoseDetector`、`DWPreprocessor`、`LayerUtility: ImageBlend V2`、`easy imageRemBg`、`InpaintPreprocessor`、`WanVideoVACEStartToEndFrame`、`WanVideoVACEEncode`、`Florence2Run`、`MaskToImage`、`GrowMaskWithBlur`、`String`、`WanVideoBlockSwap`、`INTConstant`、`WanVideoVAELoader`、`CR Upscale Image`、`VHS_LoadVideo`、`WanVideoTorchCompileSettings`、`easy seed`、`WanVideoVACEModelSelect`、`WanVideoLoraSelect`、`WanVideoModelLoader`、`ColorMatch`、`DownloadAndLoadGIMMVFIModel`、`GIMMVFI_interpolate`、`SDMatteApply`

**用到的条目**：LoadImage、DepthAnythingV2Preprocessor、easy seed、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoAddStandInLatent、WanVideoDecode、WanVideoEncode
