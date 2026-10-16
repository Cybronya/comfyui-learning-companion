---
key: 视频生成/图生视频/室内设计专用！Wan2.2首尾帧图生视频+自动提示词+放大插帧_1999771954989105154.json
name: 室内设计专用！Wan2.2首尾帧图生视频+自动提示词+放大插帧_1999771954989105154.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1999771954989105154.json
hash: 309ab1429046e8eb
coverage: 0.906977
learned_at: 2026-10-15 22:33:38
nodes: [WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSetLoRAs, ImageUpscaleWithModel, DownloadAndLoadGIMMVFIModel, WanVideoSampler, WanVideoDecode, CreateCFGScheduleFloatList, INTConstant, INTConstant, WanVideoTorchCompileSettings, WanVideoBlockSwap, WanVideoSetBlockSwap, GetImageSizeAndCount, LoadWanVideoT5TextEncoder, WanVideoVAELoader, UpscaleModelLoader, GIMMVFI_interpolate, WanVideoImageToVideoEncode, WanVideoSampler, ImageResizeKJv2, VHS_VideoCombine, ImageResizeKJv2, TextSplitByDelimiter, TextSplitByDelimiter, SetNode, WanVideoTextEncode, VHS_VideoCombine, ttN text, easy showAnything, TextSplitByDelimiter, CR Combine Prompt, ImageBatch, SetNode, ttN text, ShowText|pysssss, LoadImage, LoadImage, AILab_QwenVL_Advanced, WanVideoModelLoader, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoModelLoader]
patterns: []
missing: []
---

# 视频生成/图生视频/室内设计专用！Wan2.2首尾帧图生视频+自动提示词+放大插帧_1999771954989105154.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1999771954989105154.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（43 个）：
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSetLoRAs`
- `ImageUpscaleWithModel`
- `DownloadAndLoadGIMMVFIModel`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `CreateCFGScheduleFloatList`
- `INTConstant`
- `INTConstant`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `GetImageSizeAndCount`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `UpscaleModelLoader`
- `GIMMVFI_interpolate`
- `WanVideoImageToVideoEncode`
- `WanVideoSampler` ★核心
- `ImageResizeKJv2`
- `VHS_VideoCombine`
- `ImageResizeKJv2`
- `TextSplitByDelimiter`
- `TextSplitByDelimiter`
- `SetNode`
- `WanVideoTextEncode`
- `VHS_VideoCombine`
- `ttN text`
- `easy showAnything`
- `TextSplitByDelimiter`
- `CR Combine Prompt`
- `ImageBatch`
- `SetNode`
- `ttN text`
- `ShowText|pysssss`
- `LoadImage`
- `LoadImage`
- `AILab_QwenVL_Advanced`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`

## 知识

覆盖率 **91%**（39/43）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`ImageUpscaleWithModel`、`DownloadAndLoadGIMMVFIModel`、`WanVideoSampler`、`WanVideoDecode`、`CreateCFGScheduleFloatList`、`INTConstant`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`GetImageSizeAndCount`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`UpscaleModelLoader`、`GIMMVFI_interpolate`、`WanVideoImageToVideoEncode`、`ImageResizeKJv2`、`VHS_VideoCombine`、`TextSplitByDelimiter`、`WanVideoTextEncode`、`ttN text`、`CR Combine Prompt`、`ImageBatch`、`LoadImage`、`AILab_QwenVL_Advanced`、`WanVideoModelLoader`、`WanVideoLoraSelect`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode
