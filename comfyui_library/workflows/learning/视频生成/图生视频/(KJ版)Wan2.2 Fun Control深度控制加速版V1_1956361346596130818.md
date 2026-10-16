---
key: 视频生成/图生视频/(KJ版)Wan2.2 Fun Control深度控制加速版V1_1956361346596130818.json
name: (KJ版)Wan2.2 Fun Control深度控制加速版V1_1956361346596130818.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1956361346596130818.json
hash: 83286126214f6aab
coverage: 0.630769
learned_at: 2026-10-15 22:31:13
nodes: [WanVideoDecode, GetNode, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoSetLoRAs, Note, Note, Note, GetNode, MarkdownNote, DownloadAndLoadDepthAnythingV2Model, Note, WanVideoBlockSwap, SetNode, GetNode, SetNode, SetNode, GetNode, GetNode, INTConstant, WanVideoScheduler, SetNode, INTConstant, WanVideoSampler, PrimitiveNode, Reroute, VHS_VideoCombine, SetNode, VHS_VideoCombine, Reroute, WanVideoEncode, GetNode, WanVideoImageToVideoEncode, Reroute, WanVideoModelLoader, WanVideoModelLoader, WanVideoVAELoader, WanVideoSampler, WanVideoTorchCompileSettings, WanVideoTextEncodeCached, ImageResizeKJv2, WanVideoAddControlEmbeds, GetImageSizeAndCount, WanVideoEncode, ImageConcatMulti, ImageConcanate, VHS_VideoCombine, PDIMAGE_LongerSize, DWPreprocessor, DepthAnything_V2, ImageResizeKJv2, WanVideoLoraSelectMulti, WanVideoLoraSelectMulti, VHS_LoadVideo, VHS_VideoCombine, LoadImage, Note, Note, Note, Note, JWInteger, JWInteger, JWInteger, CR Prompt Text]
patterns: []
missing: []
---

# 视频生成/图生视频/(KJ版)Wan2.2 Fun Control深度控制加速版V1_1956361346596130818.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1956361346596130818.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（65 个）：
- `WanVideoDecode`
- `GetNode`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `Note`
- `Note`
- `Note`
- `GetNode`
- `MarkdownNote`
- `DownloadAndLoadDepthAnythingV2Model`
- `Note`
- `WanVideoBlockSwap`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `INTConstant`
- `WanVideoScheduler`
- `SetNode`
- `INTConstant`
- `WanVideoSampler` ★核心
- `PrimitiveNode`
- `Reroute`
- `VHS_VideoCombine`
- `SetNode`
- `VHS_VideoCombine`
- `Reroute`
- `WanVideoEncode`
- `GetNode`
- `WanVideoImageToVideoEncode`
- `Reroute`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoVAELoader`
- `WanVideoSampler` ★核心
- `WanVideoTorchCompileSettings`
- `WanVideoTextEncodeCached`
- `ImageResizeKJv2`
- `WanVideoAddControlEmbeds`
- `GetImageSizeAndCount`
- `WanVideoEncode`
- `ImageConcatMulti`
- `ImageConcanate`
- `VHS_VideoCombine`
- `PDIMAGE_LongerSize`
- `DWPreprocessor`
- `DepthAnything_V2`
- `ImageResizeKJv2`
- `WanVideoLoraSelectMulti`
- `WanVideoLoraSelectMulti`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `LoadImage`
- `Note`
- `Note`
- `Note`
- `Note`
- `JWInteger`
- `JWInteger`
- `JWInteger`
- `CR Prompt Text`

## 知识

覆盖率 **63%**（41/65）

**有卡**：`WanVideoDecode`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`DownloadAndLoadDepthAnythingV2Model`、`WanVideoBlockSwap`、`INTConstant`、`WanVideoScheduler`、`WanVideoSampler`、`VHS_VideoCombine`、`WanVideoEncode`、`WanVideoImageToVideoEncode`、`WanVideoModelLoader`、`WanVideoVAELoader`、`WanVideoTorchCompileSettings`、`WanVideoTextEncodeCached`、`ImageResizeKJv2`、`WanVideoAddControlEmbeds`、`GetImageSizeAndCount`、`ImageConcatMulti`、`ImageConcanate`、`PDIMAGE_LongerSize`、`DWPreprocessor`、`DepthAnything_V2`、`WanVideoLoraSelectMulti`、`VHS_LoadVideo`、`LoadImage`、`JWInteger`、`CR Prompt Text`

**用到的条目**：LoadImage、DepthAnything_V2、DownloadAndLoadDepthAnythingV2Model、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoImageToVideoEncode、WanVideoTextEncodeCached
