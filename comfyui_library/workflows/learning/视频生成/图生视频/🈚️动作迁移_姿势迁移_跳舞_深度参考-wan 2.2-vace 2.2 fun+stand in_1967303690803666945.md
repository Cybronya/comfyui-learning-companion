---
key: 视频生成/图生视频/🈚️动作迁移_姿势迁移_跳舞_深度参考-wan 2.2-vace 2.2 fun+stand in_1967303690803666945.json
name: 🈚️动作迁移_姿势迁移_跳舞_深度参考-wan 2.2-vace 2.2 fun+stand in_1967303690803666945.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1967303690803666945.json
hash: a378576cb40685c1
coverage: 0.434783
learned_at: 2026-10-15 22:31:41
nodes: [SetNode, SetNode, SetNode, GetNode, LoadImage, VHS_VideoCombine, GetNode, GetNode, SetNode, SetNode, SetNode, Int, GetNode, LoadWanVideoT5TextEncoder, GetNode, SetNode, GetImageSizeAndCount, WanVideoTextEncode, SetNode, WanVideoDecode, SetNode, GetNode, SetNode, GetNode, GetImageSizeAndCount, GetNode, GetNode, FaceProcessorLoader, GetNode, ApplyFaceProcessor, PreviewImage, WanVideoEncode, WanVideoAddStandInLatent, WanVideoVACEEncode, PreviewImage, SetNode, ImageResizeKJv2, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, ImageResizeKJv2, SetNode, ImageResizeKJv2, SetNode, easy cleanGpuUsed, AIO_Preprocessor, WanVideoModelLoader, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, Manual XY Entry Info, Int, Int, VHS_LoadVideo, VHS_VideoCombine, OnnxDetectionModelLoader, PoseDetectionOneToAllAnimation, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoContextOptions, CreateCFGScheduleFloatList, GetNode, WanVideoVAELoader, WanVideoVACEEncode, WanVideoBlockSwap, WanVideoSampler, GetNode, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoSampler, GetNode, ImpactSwitch, GetNode, ImpactSwitch, ImpactSwitch, WanVideoLoraSelect, SetNode, SetNode, WanVideoModelLoader, SetNode, GetNode, GetNode]
patterns: []
missing: []
---

# 视频生成/图生视频/🈚️动作迁移_姿势迁移_跳舞_深度参考-wan 2.2-vace 2.2 fun+stand in_1967303690803666945.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1967303690803666945.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（92 个）：
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `LoadImage`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `Int`
- `GetNode`
- `LoadWanVideoT5TextEncoder`
- `GetNode`
- `SetNode`
- `GetImageSizeAndCount`
- `WanVideoTextEncode`
- `SetNode`
- `WanVideoDecode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetImageSizeAndCount`
- `GetNode`
- `GetNode`
- `FaceProcessorLoader`
- `GetNode`
- `ApplyFaceProcessor`
- `PreviewImage`
- `WanVideoEncode`
- `WanVideoAddStandInLatent`
- `WanVideoVACEEncode`
- `PreviewImage`
- `SetNode`
- `ImageResizeKJv2`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageResizeKJv2`
- `SetNode`
- `ImageResizeKJv2`
- `SetNode`
- `easy cleanGpuUsed`
- `AIO_Preprocessor`
- `WanVideoModelLoader`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `Manual XY Entry Info`
- `Int`
- `Int`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `OnnxDetectionModelLoader`
- `PoseDetectionOneToAllAnimation`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoContextOptions`
- `CreateCFGScheduleFloatList`
- `GetNode`
- `WanVideoVAELoader`
- `WanVideoVACEEncode`
- `WanVideoBlockSwap`
- `WanVideoSampler` ★核心
- `GetNode`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoSampler` ★核心
- `GetNode`
- `ImpactSwitch`
- `GetNode`
- `ImpactSwitch`
- `ImpactSwitch`
- `WanVideoLoraSelect`
- `SetNode`
- `SetNode`
- `WanVideoModelLoader`
- `SetNode`
- `GetNode`
- `GetNode`

## 知识

覆盖率 **43%**（40/92）

**有卡**：`LoadImage`、`VHS_VideoCombine`、`Int`、`LoadWanVideoT5TextEncoder`、`GetImageSizeAndCount`、`WanVideoTextEncode`、`WanVideoDecode`、`FaceProcessorLoader`、`ApplyFaceProcessor`、`WanVideoEncode`、`WanVideoAddStandInLatent`、`WanVideoVACEEncode`、`ImageResizeKJv2`、`easy cleanGpuUsed`、`AIO_Preprocessor`、`WanVideoModelLoader`、`Manual XY Entry Info`、`VHS_LoadVideo`、`OnnxDetectionModelLoader`、`PoseDetectionOneToAllAnimation`、`WanVideoLoraSelect`、`WanVideoContextOptions`、`CreateCFGScheduleFloatList`、`WanVideoVAELoader`、`WanVideoBlockSwap`、`WanVideoSampler`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoVACEEncode
