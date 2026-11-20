---
key: 平台全量/AIROTO_Wan2.2-VACE-Fun-A14B_2511_v2_1990288109948596226.json
name: AIROTO_Wan2.2-VACE-Fun-A14B_2511_v2_1990288109948596226
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/AIROTO_Wan2.2-VACE-Fun-A14B_2511_v2_1990288109948596226.json
hash: d280f90df264038f
coverage: 0.875
learned_at: 2026-11-14 00:15:12
nodes: [WanVideoSetBlockSwap, Reroute, AIO_Preprocessor, ImageConcatMulti, VHS_VideoInfo, Reroute, WanVideoVAELoader, Pick From Batch (mtb), ImageScaleBy, WanVideoDecode, WanVideoSetBlockSwap, WanVideoSampler, WanVideoSampler, ImageConcatMulti, WanVideoModelLoader, WanVideoExtraModelSelect, INTConstant, ColorMatch, WanVideoTextEncodeCached, WanVideoScheduler, WanVideoContextOptions, WanVideoContextOptions, RIFE VFI, VHS_VideoCombine, VHS_VideoCombine, WanVideoModelLoader, Note, PixelPerfectResolution, WanVideoSetLoRAs, WanVideoLoraSelectMulti, WanVideoTorchCompileSettings, WanVideoSetLoRAs, WanVideoSigmaToStep, Florence2Run, GetImageSizeAndCount, WanVideoScheduler, WanVideoExperimentalArgs, WanVideoBlockSwap, INTConstant, INTConstant, VHS_VideoCombine, Note, PrimitiveInt, PrimitiveInt, SaveImage, YOLOModelLoader, WanVideoVACEEncode, SDPoseOODLoader, VHS_VideoCombine, ImageResizeKJv2, ImageResizeKJv2, ImageScaleBy, easy cleanGpuUsed, DWPreprocessor, PreviewImage, Florence2ModelLoader, SDPoseOODProcessor, PrimitiveInt, VHS_VideoCombine, Text, VHS_LoadVideo, LoadImage, WanVideoExtraModelSelect, WanVideoLoraSelectMulti]
patterns: []
missing: []
---

# 平台全量/AIROTO_Wan2.2-VACE-Fun-A14B_2511_v2_1990288109948596226.json

> 来源文件 `comfyui_library/workflows/平台全量/AIROTO_Wan2.2-VACE-Fun-A14B_2511_v2_1990288109948596226.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（64 个）：
- `WanVideoSetBlockSwap`
- `Reroute`
- `AIO_Preprocessor`
- `ImageConcatMulti`
- `VHS_VideoInfo`
- `Reroute`
- `WanVideoVAELoader`
- `Pick From Batch (mtb)`
- `ImageScaleBy`
- `WanVideoDecode`
- `WanVideoSetBlockSwap`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `ImageConcatMulti`
- `WanVideoModelLoader`
- `WanVideoExtraModelSelect`
- `INTConstant`
- `ColorMatch`
- `WanVideoTextEncodeCached`
- `WanVideoScheduler`
- `WanVideoContextOptions`
- `WanVideoContextOptions`
- `RIFE VFI`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `WanVideoModelLoader`
- `Note`
- `PixelPerfectResolution`
- `WanVideoSetLoRAs`
- `WanVideoLoraSelectMulti`
- `WanVideoTorchCompileSettings`
- `WanVideoSetLoRAs`
- `WanVideoSigmaToStep`
- `Florence2Run`
- `GetImageSizeAndCount`
- `WanVideoScheduler`
- `WanVideoExperimentalArgs`
- `WanVideoBlockSwap`
- `INTConstant`
- `INTConstant`
- `VHS_VideoCombine`
- `Note`
- `PrimitiveInt`
- `PrimitiveInt`
- `SaveImage`
- `YOLOModelLoader`
- `WanVideoVACEEncode`
- `SDPoseOODLoader`
- `VHS_VideoCombine`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `ImageScaleBy`
- `easy cleanGpuUsed`
- `DWPreprocessor`
- `PreviewImage`
- `Florence2ModelLoader`
- `SDPoseOODProcessor`
- `PrimitiveInt`
- `VHS_VideoCombine`
- `Text`
- `VHS_LoadVideo`
- `LoadImage`
- `WanVideoExtraModelSelect`
- `WanVideoLoraSelectMulti`

## 知识

覆盖率 **88%**（56/64）

**有卡**：`WanVideoSetBlockSwap`、`AIO_Preprocessor`、`ImageConcatMulti`、`VHS_VideoInfo`、`WanVideoVAELoader`、`Pick From Batch (mtb)`、`ImageScaleBy`、`WanVideoDecode`、`WanVideoSampler`、`WanVideoModelLoader`、`WanVideoExtraModelSelect`、`INTConstant`、`ColorMatch`、`WanVideoTextEncodeCached`、`WanVideoScheduler`、`WanVideoContextOptions`、`RIFE VFI`、`VHS_VideoCombine`、`PixelPerfectResolution`、`WanVideoSetLoRAs`、`WanVideoLoraSelectMulti`、`WanVideoTorchCompileSettings`、`WanVideoSigmaToStep`、`Florence2Run`、`GetImageSizeAndCount`、`WanVideoExperimentalArgs`、`WanVideoBlockSwap`、`SaveImage`、`YOLOModelLoader`、`WanVideoVACEEncode`、`SDPoseOODLoader`、`ImageResizeKJv2`、`easy cleanGpuUsed`、`DWPreprocessor`、`Florence2ModelLoader`、`SDPoseOODProcessor`、`Text`、`VHS_LoadVideo`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVACEEncode、WanVideoVAELoader、WanVideoLoraSelectMulti、WanVideoSetLoRAs
