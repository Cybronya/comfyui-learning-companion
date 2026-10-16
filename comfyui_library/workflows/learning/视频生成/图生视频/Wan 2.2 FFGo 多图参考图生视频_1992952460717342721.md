---
key: 视频生成/图生视频/Wan 2.2 FFGo 多图参考图生视频_1992952460717342721.json
name: Wan 2.2 FFGo 多图参考图生视频_1992952460717342721.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1992952460717342721.json
hash: cc550b3818bd098c
coverage: 0.82
learned_at: 2026-10-15 22:33:17
nodes: [PreviewImage, RMBG, PreviewImage, PreviewImage, CreateCFGScheduleFloatList, WanVideoSetBlockSwap, WanVideoSetLoRAs, SetNode, WanVideoSetBlockSwap, WanVideoSetLoRAs, SetNode, GetNode, GetNode, ImageStitch, WanVideoSampler, WanVideoSampler, WanVideoBlockSwap, WanVideoTorchCompileSettings, ImageResizeKJv2, WanVideoImageToVideoEncode, INTConstant, VHS_VideoCombine, ImageStitch, ImageResizeKJv2, ImageResizeKJv2, ImageStitch, ImageResizeKJv2, ImageBatchMulti, PreviewImage, PreviewImage, ImageConcatMulti, WanVideoDecode, INTConstant, INTConstant, INTConstant, INTConstant, GetImageRangeFromBatch, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoModelLoader, WanVideoModelLoader, LoadWanVideoT5TextEncoder, WanVideoVAELoader, VHS_VideoCombine, LoadImage, LoadImage, LoadImage, WanVideoTextEncode]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan 2.2 FFGo 多图参考图生视频_1992952460717342721.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1992952460717342721.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（50 个）：
- `PreviewImage`
- `RMBG`
- `PreviewImage`
- `PreviewImage`
- `CreateCFGScheduleFloatList`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `SetNode`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `SetNode`
- `GetNode`
- `GetNode`
- `ImageStitch`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `WanVideoBlockSwap`
- `WanVideoTorchCompileSettings`
- `ImageResizeKJv2`
- `WanVideoImageToVideoEncode`
- `INTConstant`
- `VHS_VideoCombine`
- `ImageStitch`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `ImageStitch`
- `ImageResizeKJv2`
- `ImageBatchMulti`
- `PreviewImage`
- `PreviewImage`
- `ImageConcatMulti`
- `WanVideoDecode`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `GetImageRangeFromBatch`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `VHS_VideoCombine`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `WanVideoTextEncode`

## 知识

覆盖率 **82%**（41/50）

**有卡**：`RMBG`、`CreateCFGScheduleFloatList`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`ImageStitch`、`WanVideoSampler`、`WanVideoBlockSwap`、`WanVideoTorchCompileSettings`、`ImageResizeKJv2`、`WanVideoImageToVideoEncode`、`INTConstant`、`VHS_VideoCombine`、`ImageBatchMulti`、`ImageConcatMulti`、`WanVideoDecode`、`GetImageRangeFromBatch`、`WanVideoLoraSelect`、`WanVideoModelLoader`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`LoadImage`、`WanVideoTextEncode`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode
