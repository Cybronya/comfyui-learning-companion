---
key: 视频生成/图生视频/Wan2.2_Fun-VACE_首尾帧+动作控制+视频角色替换_1967688435714711553.json
name: Wan2.2_Fun-VACE_首尾帧+动作控制+视频角色替换_1967688435714711553.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2_Fun-VACE_首尾帧+动作控制+视频角色替换_1967688435714711553.json
hash: 1abda9d91f42615b
coverage: 0.96
learned_at: 2026-10-15 22:31:42
nodes: [VHS_VideoInfo, SolidMask, MaskToImage, WanVideoTorchCompileSettings, VHS_VideoCombine, VHS_VideoCombine, PreviewImage, WanVideoSetBlockSwap, WanVideoBlockSwap, GrowMaskWithBlur, DownloadAndLoadSAM2Model, MaskToImage, Sam2Segmentation, INTConstant, WanVideoSetBlockSwap, VHS_VideoInfo, WanVideoSampler, INTConstant, CreateCFGScheduleFloatList, CreateCFGScheduleFloatList, INTConstant, VHS_VideoCombine, ImageResizeKJv2, ImageResizeKJv2, easy imageRemBg, ImageResizeKJv2, WanVideoDecode, VHS_VideoCombine, WanVideoSampler, INTConstant, WanVideoDecode, VHS_VideoCombine, INTConstant, INTConstant, CreateCFGScheduleFloatList, WanVideoVACEEncode, ImageResizeKJv2, WanVideoVACEEncode, WanVideoSampler, WanVideoSetLoRAs, WanVideoSetLoRAs, WanVideoVACEStartToEndFrame, ImageResizeKJv2, ImageResizeKJv2, WanVideoVAELoader, WanVideoSampler, WanVideoSampler, PrimitiveInt, WanVideoDecode, WanVideoSampler, GetImageSizeAndCount, MaskToImage, ImageCompositeMasked, LoadImage, VHS_LoadVideo, DWPreprocessor, WanVideoVACEEncode, VHS_LoadVideo, LoadImage, VHS_VideoCombine, PointsEditor, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoVACEModelSelect, WanVideoVACEModelSelect, WanVideoModelLoader, WanVideoModelLoader, LoadWanVideoT5TextEncoder, INTConstant, INTConstant, LoadImage, LoadImage, WanVideoTextEncode, Label (rgthree), Fast Groups Muter (rgthree)]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2_Fun-VACE_首尾帧+动作控制+视频角色替换_1967688435714711553.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1967688435714711553.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（75 个）：
- `VHS_VideoInfo`
- `SolidMask`
- `MaskToImage`
- `WanVideoTorchCompileSettings`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `PreviewImage`
- `WanVideoSetBlockSwap`
- `WanVideoBlockSwap`
- `GrowMaskWithBlur`
- `DownloadAndLoadSAM2Model`
- `MaskToImage`
- `Sam2Segmentation`
- `INTConstant`
- `WanVideoSetBlockSwap`
- `VHS_VideoInfo`
- `WanVideoSampler` ★核心
- `INTConstant`
- `CreateCFGScheduleFloatList`
- `CreateCFGScheduleFloatList`
- `INTConstant`
- `VHS_VideoCombine`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `easy imageRemBg`
- `ImageResizeKJv2`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `WanVideoSampler` ★核心
- `INTConstant`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `INTConstant`
- `INTConstant`
- `CreateCFGScheduleFloatList`
- `WanVideoVACEEncode`
- `ImageResizeKJv2`
- `WanVideoVACEEncode`
- `WanVideoSampler` ★核心
- `WanVideoSetLoRAs`
- `WanVideoSetLoRAs`
- `WanVideoVACEStartToEndFrame`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `WanVideoVAELoader`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `PrimitiveInt`
- `WanVideoDecode`
- `WanVideoSampler` ★核心
- `GetImageSizeAndCount`
- `MaskToImage`
- `ImageCompositeMasked`
- `LoadImage`
- `VHS_LoadVideo`
- `DWPreprocessor`
- `WanVideoVACEEncode`
- `VHS_LoadVideo`
- `LoadImage`
- `VHS_VideoCombine`
- `PointsEditor`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoVACEModelSelect`
- `WanVideoVACEModelSelect`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `LoadWanVideoT5TextEncoder`
- `INTConstant`
- `INTConstant`
- `LoadImage`
- `LoadImage`
- `WanVideoTextEncode`
- `Label (rgthree)`
- `Fast Groups Muter (rgthree)`

## 知识

覆盖率 **96%**（72/75）

**有卡**：`VHS_VideoInfo`、`SolidMask`、`MaskToImage`、`WanVideoTorchCompileSettings`、`VHS_VideoCombine`、`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`GrowMaskWithBlur`、`DownloadAndLoadSAM2Model`、`Sam2Segmentation`、`INTConstant`、`WanVideoSampler`、`CreateCFGScheduleFloatList`、`ImageResizeKJv2`、`easy imageRemBg`、`WanVideoDecode`、`WanVideoVACEEncode`、`WanVideoSetLoRAs`、`WanVideoVACEStartToEndFrame`、`WanVideoVAELoader`、`GetImageSizeAndCount`、`ImageCompositeMasked`、`LoadImage`、`VHS_LoadVideo`、`DWPreprocessor`、`PointsEditor`、`WanVideoLoraSelect`、`WanVideoVACEModelSelect`、`WanVideoModelLoader`、`LoadWanVideoT5TextEncoder`、`WanVideoTextEncode`、`Label (rgthree)`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoVACEEncode
