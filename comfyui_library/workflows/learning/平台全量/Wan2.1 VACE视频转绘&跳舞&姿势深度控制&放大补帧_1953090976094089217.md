---
key: 平台全量/Wan2.1 VACE视频转绘&跳舞&姿势深度控制&放大补帧_1953090976094089217.json
name: Wan2.1 VACE视频转绘&跳舞&姿势深度控制&放大补帧_1953090976094089217
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.1 VACE视频转绘&跳舞&姿势深度控制&放大补帧_1953090976094089217.json
hash: 6e81425acc98f3ac
coverage: 0.529915
learned_at: 2026-11-14 01:04:26
nodes: [SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, AddLabel, EmptyImage, AddLabel, WanVideoDecode, ImageConcatMulti, WanVideoExperimentalArgs, ImageResize+, ImageResize+, ImageResizeKJ, VHS_VideoInfo, Florence2Run, ImageUpscaleWithModel, JoinStrings, DepthAnything_V2, Any Switch (rgthree), VHS_VideoCombine, Any Switch (rgthree), PreviewImage, GetImageSize, EmptyImage, ImageComposite+, ImageResize+, WanVideoVACEEncode, GetImageSizeAndCount, WanVideoVACEStartToEndFrame, JoinStrings, String Literal, String Literal, JoinStrings, VHS_VideoCombine, WanVideoTextEncode, WanVideoTorchCompileSettings, String Literal, JoinStrings, Any Switch (rgthree), VHS_VideoCombine, GetImageSizeAndCount, ImageConcatMulti, ImageBlend, WanVideoBlockSwap, WanVideoSLG, WanVideoSampler, WanVideoEnhanceAVideo, WanVideoTeaCache, WanVideoLoraSelect, WanVideoModelLoader, WanVideoVAELoader, easy positive, easy int, easy int, easy int, easy int, String Literal, SetNode, Fast Groups Muter (rgthree), Fast Groups Muter (rgthree), Fast Groups Muter (rgthree), MarkdownNote, LoadImage, DownloadAndLoadDepthAnythingV2Model, AIO_Preprocessor, AIO_Preprocessor, LoadWanVideoT5TextEncoder, Florence2ModelLoader, VHS_VideoCombine, DWPreprocessor, GetNode, InspyrenetRembg, SetNode, GetNode, String Literal, FILM VFI, GetNode, UpscaleModelLoader, VHS_LoadVideo]
patterns: []
missing: []
---

# 平台全量/Wan2.1 VACE视频转绘&跳舞&姿势深度控制&放大补帧_1953090976094089217.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.1 VACE视频转绘&跳舞&姿势深度控制&放大补帧_1953090976094089217.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（117 个）：
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
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
- `GetNode`
- `GetNode`
- `AddLabel`
- `EmptyImage`
- `AddLabel`
- `WanVideoDecode`
- `ImageConcatMulti`
- `WanVideoExperimentalArgs`
- `ImageResize+`
- `ImageResize+`
- `ImageResizeKJ`
- `VHS_VideoInfo`
- `Florence2Run`
- `ImageUpscaleWithModel`
- `JoinStrings`
- `DepthAnything_V2`
- `Any Switch (rgthree)`
- `VHS_VideoCombine`
- `Any Switch (rgthree)`
- `PreviewImage`
- `GetImageSize`
- `EmptyImage`
- `ImageComposite+`
- `ImageResize+`
- `WanVideoVACEEncode`
- `GetImageSizeAndCount`
- `WanVideoVACEStartToEndFrame`
- `JoinStrings`
- `String Literal`
- `String Literal`
- `JoinStrings`
- `VHS_VideoCombine`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `String Literal`
- `JoinStrings`
- `Any Switch (rgthree)`
- `VHS_VideoCombine`
- `GetImageSizeAndCount`
- `ImageConcatMulti`
- `ImageBlend`
- `WanVideoBlockSwap`
- `WanVideoSLG`
- `WanVideoSampler` ★核心
- `WanVideoEnhanceAVideo`
- `WanVideoTeaCache`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoVAELoader`
- `easy positive`
- `easy int`
- `easy int`
- `easy int`
- `easy int`
- `String Literal`
- `SetNode`
- `Fast Groups Muter (rgthree)`
- `Fast Groups Muter (rgthree)`
- `Fast Groups Muter (rgthree)`
- `MarkdownNote`
- `LoadImage`
- `DownloadAndLoadDepthAnythingV2Model`
- `AIO_Preprocessor`
- `AIO_Preprocessor`
- `LoadWanVideoT5TextEncoder`
- `Florence2ModelLoader`
- `VHS_VideoCombine`
- `DWPreprocessor`
- `GetNode`
- `InspyrenetRembg`
- `SetNode`
- `GetNode`
- `String Literal`
- `FILM VFI`
- `GetNode`
- `UpscaleModelLoader`
- `VHS_LoadVideo`

## 知识

覆盖率 **53%**（62/117）

**有卡**：`AddLabel`、`EmptyImage`、`WanVideoDecode`、`ImageConcatMulti`、`WanVideoExperimentalArgs`、`ImageResize+`、`ImageResizeKJ`、`VHS_VideoInfo`、`Florence2Run`、`ImageUpscaleWithModel`、`JoinStrings`、`DepthAnything_V2`、`VHS_VideoCombine`、`GetImageSize`、`ImageComposite+`、`WanVideoVACEEncode`、`GetImageSizeAndCount`、`WanVideoVACEStartToEndFrame`、`String Literal`、`WanVideoTextEncode`、`WanVideoTorchCompileSettings`、`ImageBlend`、`WanVideoBlockSwap`、`WanVideoSLG`、`WanVideoSampler`、`WanVideoEnhanceAVideo`、`WanVideoTeaCache`、`WanVideoLoraSelect`、`WanVideoModelLoader`、`WanVideoVAELoader`、`easy positive`、`easy int`、`LoadImage`、`DownloadAndLoadDepthAnythingV2Model`、`AIO_Preprocessor`、`LoadWanVideoT5TextEncoder`、`Florence2ModelLoader`、`DWPreprocessor`、`InspyrenetRembg`、`FILM VFI`、`UpscaleModelLoader`、`VHS_LoadVideo`

**用到的条目**：LoadImage、DepthAnything_V2、DownloadAndLoadDepthAnythingV2Model、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVACEEncode
