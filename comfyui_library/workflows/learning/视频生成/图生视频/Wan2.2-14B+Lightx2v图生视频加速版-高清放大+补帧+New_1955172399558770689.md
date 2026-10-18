---
key: 视频生成/图生视频/Wan2.2-14B+Lightx2v图生视频加速版-高清放大+补帧+New_1955172399558770689.json
name: Wan2.2-14B+Lightx2v图生视频加速版-高清放大+补帧+New_1955172399558770689.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2-14B+Lightx2v图生视频加速版-高清放大+补帧+New_1955172399558770689.json
hash: cd769b07fabbafae
coverage: 0.902439
learned_at: 2026-10-15 22:31:07
nodes: [WanVideoSetBlockSwap, WanVideoBlockSwap, WanVideoModelLoader, WanVideoSetBlockSwap, WanVideoModelLoader, WanVideoTorchCompileSettings, LoadWanVideoT5TextEncoder, WanVideoTextEncode, WanVideoSampler, JWInteger, JWInteger, ImageResizeKJv2, CreateCFGScheduleFloatList, WanVideoVAELoader, JWInteger, WanVideoSampler, WanVideoDecode, WanVideoSetLoRAs, WanVideoSetLoRAs, PrimitiveNode, JWInteger, ImageResize+, WanVideoImageToVideoEncode, Primitive integer [Crystools], UpscaleModelLoader, ImageUpscaleWithModel, Primitive integer [Crystools], Primitive integer [Crystools], WanVideoLoraSelect, WanVideoLoraSelect, PreviewImage, easy cleanGpuUsed, ShowText|pysssss, RIFE VFI, VHS_VideoCombine, JWInteger, SimpleMath+, PreviewImage, RH_Captioner, LoadImage, LayerUtility: ImageScaleByAspectRatio V2]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2-14B+Lightx2v图生视频加速版-高清放大+补帧+New_1955172399558770689.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1955172399558770689.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（41 个）：
- `WanVideoSetBlockSwap`
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `WanVideoSetBlockSwap`
- `WanVideoModelLoader`
- `WanVideoTorchCompileSettings`
- `LoadWanVideoT5TextEncoder`
- `WanVideoTextEncode`
- `WanVideoSampler` ★核心
- `JWInteger`
- `JWInteger`
- `ImageResizeKJv2`
- `CreateCFGScheduleFloatList`
- `WanVideoVAELoader`
- `JWInteger`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `WanVideoSetLoRAs`
- `WanVideoSetLoRAs`
- `PrimitiveNode`
- `JWInteger`
- `ImageResize+`
- `WanVideoImageToVideoEncode`
- `Primitive integer [Crystools]`
- `UpscaleModelLoader`
- `ImageUpscaleWithModel`
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `PreviewImage`
- `easy cleanGpuUsed`
- `ShowText|pysssss`
- `RIFE VFI`
- `VHS_VideoCombine`
- `JWInteger`
- `SimpleMath+`
- `PreviewImage`
- `RH_Captioner`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`

## 知识

覆盖率 **90%**（37/41）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`WanVideoTorchCompileSettings`、`LoadWanVideoT5TextEncoder`、`WanVideoTextEncode`、`WanVideoSampler`、`JWInteger`、`ImageResizeKJv2`、`CreateCFGScheduleFloatList`、`WanVideoVAELoader`、`WanVideoDecode`、`WanVideoSetLoRAs`、`ImageResize+`、`WanVideoImageToVideoEncode`、`Primitive integer [Crystools]`、`UpscaleModelLoader`、`ImageUpscaleWithModel`、`WanVideoLoraSelect`、`easy cleanGpuUsed`、`RIFE VFI`、`VHS_VideoCombine`、`SimpleMath+`、`RH_Captioner`、`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`

**用到的条目**：LoadImage、LayerUtility: ImageScaleByAspectRatio V2、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader
