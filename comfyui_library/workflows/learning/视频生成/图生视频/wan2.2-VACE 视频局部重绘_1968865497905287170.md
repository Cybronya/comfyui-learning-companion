---
key: 视频生成/图生视频/wan2.2-VACE 视频局部重绘_1968865497905287170.json
name: wan2.2-VACE 视频局部重绘_1968865497905287170.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1968865497905287170.json
hash: ffa79cf348ec8521
coverage: 0.952381
learned_at: 2026-10-15 22:31:46
nodes: [WanVideoTorchCompileSettings, WanVideoTorchCompileSettings, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoSetBlockSwap, WanVideoLoraSelect, WanVideoVACEModelSelect, WanVideoVACEModelSelect, WanVideoLoraSelect, WanVideoVAELoader, GrowMask, INPAINT_MaskedFill, ImageConcatMulti, EmptyImage, GetImageSizeAndCount, Mute / Bypass Repeater (rgthree), WanVideoSampler, WanVideoSampler, CreateCFGScheduleFloatList, MathExpression|pysssss, WanVideoModelLoader, easy int, Int, Int, LoadImage, WanVideoModelLoader, WanVideoDecode, VHS_VideoCombine, AddLabel, Fast Bypasser (rgthree), LoadWanVideoT5TextEncoder, Fast Bypasser (rgthree), VHS_LoadVideo, MathExpression|pysssss, WanVideoVACEEncode, GetImageSizeAndCount, PreviewImage, PreviewImage, LayerUtility: ImageScaleByAspectRatio V2, LayerMask: SegmentAnythingUltra V2, VHS_VideoCombine, WanVideoTextEncode]
patterns: []
missing: []
---

# 视频生成/图生视频/wan2.2-VACE 视频局部重绘_1968865497905287170.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1968865497905287170.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（42 个）：
- `WanVideoTorchCompileSettings`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoLoraSelect`
- `WanVideoVACEModelSelect`
- `WanVideoVACEModelSelect`
- `WanVideoLoraSelect`
- `WanVideoVAELoader`
- `GrowMask`
- `INPAINT_MaskedFill`
- `ImageConcatMulti`
- `EmptyImage`
- `GetImageSizeAndCount`
- `Mute / Bypass Repeater (rgthree)`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `CreateCFGScheduleFloatList`
- `MathExpression|pysssss`
- `WanVideoModelLoader`
- `easy int`
- `Int`
- `Int`
- `LoadImage`
- `WanVideoModelLoader`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `AddLabel`
- `Fast Bypasser (rgthree)`
- `LoadWanVideoT5TextEncoder`
- `Fast Bypasser (rgthree)`
- `VHS_LoadVideo`
- `MathExpression|pysssss`
- `WanVideoVACEEncode`
- `GetImageSizeAndCount`
- `PreviewImage`
- `PreviewImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerMask: SegmentAnythingUltra V2`
- `VHS_VideoCombine`
- `WanVideoTextEncode`

## 知识

覆盖率 **95%**（40/42）

**有卡**：`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`WanVideoLoraSelect`、`WanVideoVACEModelSelect`、`WanVideoVAELoader`、`GrowMask`、`INPAINT_MaskedFill`、`ImageConcatMulti`、`EmptyImage`、`GetImageSizeAndCount`、`Mute / Bypass Repeater (rgthree)`、`WanVideoSampler`、`CreateCFGScheduleFloatList`、`MathExpression|pysssss`、`WanVideoModelLoader`、`easy int`、`Int`、`LoadImage`、`WanVideoDecode`、`VHS_VideoCombine`、`AddLabel`、`Fast Bypasser (rgthree)`、`LoadWanVideoT5TextEncoder`、`VHS_LoadVideo`、`WanVideoVACEEncode`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerMask: SegmentAnythingUltra V2`、`WanVideoTextEncode`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoVACEEncode
