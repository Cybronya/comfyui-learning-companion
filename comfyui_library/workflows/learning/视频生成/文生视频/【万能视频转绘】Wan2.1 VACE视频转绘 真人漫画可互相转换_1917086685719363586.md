---
key: 视频生成/文生视频/【万能视频转绘】Wan2.1 VACE视频转绘 真人漫画可互相转换_1917086685719363586.json
name: 【万能视频转绘】Wan2.1 VACE视频转绘 真人漫画可互相转换_1917086685719363586.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/【万能视频转绘】Wan2.1 VACE视频转绘 真人漫画可互相转换_1917086685719363586.json
hash: 61303a280cda13bf
coverage: 0.561798
learned_at: 2026-10-15 22:43:22
nodes: [JoinStrings, SetNode, String Literal, GetNode, SetNode, String Literal, GetNode, JoinStrings, GetNode, String Literal, Fast Groups Muter (rgthree), Fast Groups Muter (rgthree), String Literal, easy int, GetNode, Any Switch (rgthree), SetNode, SetNode, WanVideoTorchCompileSettings, WanVideoVRAMManagement, WanVideoBlockSwap, Florence2ModelLoader, Florence2Run, GetNode, GetNode, WanVideoTextEncode, GetNode, ImageResize+, GetNode, WanVideoVACEStartToEndFrame, SetNode, ImageResize+, GetNode, WanVideoTeaCache, GetNode, WanVideoSLG, WanVideoExperimentalArgs, WanVideoEnhanceAVideo, GetNode, AddLabel, GetNode, GetNode, ImageConcatMulti, AddLabel, WanVideoDecode, GetImageSizeAndCount, SetNode, ImageConcatMulti, GetNode, SetNode, SetNode, VHS_VideoInfo, easy int, easy seed, easy positive, LoadImage, SetNode, GetNode, GetNode, VHS_LoadVideo, easy int, ImageFromBatch, PreviewImage, GetNode, LoadWanVideoT5TextEncoder, WanVideoVAELoader, WanVideoModelLoader, DWPreprocessor, ImageResize+, VHS_VideoCombine, DepthAnything_V2, DownloadAndLoadDepthAnythingV2Model, GetImageSizeAndCount, Any Switch (rgthree), SetNode, SetNode, SetNode, WanVideoVACEModelSelect, SetNode, SetNode, JoinStrings, GetNode, VHS_VideoCombine, SetNode, PreviewImage, WanVideoVACEEncode, WanVideoSampler, EmptyImage, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/文生视频/【万能视频转绘】Wan2.1 VACE视频转绘 真人漫画可互相转换_1917086685719363586.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1917086685719363586.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（89 个）：
- `JoinStrings`
- `SetNode`
- `String Literal`
- `GetNode`
- `SetNode`
- `String Literal`
- `GetNode`
- `JoinStrings`
- `GetNode`
- `String Literal`
- `Fast Groups Muter (rgthree)`
- `Fast Groups Muter (rgthree)`
- `String Literal`
- `easy int`
- `GetNode`
- `Any Switch (rgthree)`
- `SetNode`
- `SetNode`
- `WanVideoTorchCompileSettings`
- `WanVideoVRAMManagement`
- `WanVideoBlockSwap`
- `Florence2ModelLoader`
- `Florence2Run`
- `GetNode`
- `GetNode`
- `WanVideoTextEncode`
- `GetNode`
- `ImageResize+`
- `GetNode`
- `WanVideoVACEStartToEndFrame`
- `SetNode`
- `ImageResize+`
- `GetNode`
- `WanVideoTeaCache`
- `GetNode`
- `WanVideoSLG`
- `WanVideoExperimentalArgs`
- `WanVideoEnhanceAVideo`
- `GetNode`
- `AddLabel`
- `GetNode`
- `GetNode`
- `ImageConcatMulti`
- `AddLabel`
- `WanVideoDecode`
- `GetImageSizeAndCount`
- `SetNode`
- `ImageConcatMulti`
- `GetNode`
- `SetNode`
- `SetNode`
- `VHS_VideoInfo`
- `easy int`
- `easy seed`
- `easy positive`
- `LoadImage`
- `SetNode`
- `GetNode`
- `GetNode`
- `VHS_LoadVideo`
- `easy int`
- `ImageFromBatch`
- `PreviewImage`
- `GetNode`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `WanVideoModelLoader`
- `DWPreprocessor`
- `ImageResize+`
- `VHS_VideoCombine`
- `DepthAnything_V2`
- `DownloadAndLoadDepthAnythingV2Model`
- `GetImageSizeAndCount`
- `Any Switch (rgthree)`
- `SetNode`
- `SetNode`
- `SetNode`
- `WanVideoVACEModelSelect`
- `SetNode`
- `SetNode`
- `JoinStrings`
- `GetNode`
- `VHS_VideoCombine`
- `SetNode`
- `PreviewImage`
- `WanVideoVACEEncode`
- `WanVideoSampler` ★核心
- `EmptyImage`
- `VHS_VideoCombine`

## 知识

覆盖率 **56%**（50/89）

**有卡**：`JoinStrings`、`String Literal`、`easy int`、`WanVideoTorchCompileSettings`、`WanVideoVRAMManagement`、`WanVideoBlockSwap`、`Florence2ModelLoader`、`Florence2Run`、`WanVideoTextEncode`、`ImageResize+`、`WanVideoVACEStartToEndFrame`、`WanVideoTeaCache`、`WanVideoSLG`、`WanVideoExperimentalArgs`、`WanVideoEnhanceAVideo`、`AddLabel`、`ImageConcatMulti`、`WanVideoDecode`、`GetImageSizeAndCount`、`VHS_VideoInfo`、`easy seed`、`easy positive`、`LoadImage`、`VHS_LoadVideo`、`ImageFromBatch`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoModelLoader`、`DWPreprocessor`、`VHS_VideoCombine`、`DepthAnything_V2`、`DownloadAndLoadDepthAnythingV2Model`、`WanVideoVACEModelSelect`、`WanVideoVACEEncode`、`WanVideoSampler`、`EmptyImage`

**用到的条目**：LoadImage、DepthAnything_V2、DownloadAndLoadDepthAnythingV2Model、WanVideoSampler、easy seed、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode
