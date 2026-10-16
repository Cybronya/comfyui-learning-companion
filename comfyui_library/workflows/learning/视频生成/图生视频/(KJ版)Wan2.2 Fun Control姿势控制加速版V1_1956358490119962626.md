---
key: 视频生成/图生视频/(KJ版)Wan2.2 Fun Control姿势控制加速版V1_1956358490119962626.json
name: (KJ版)Wan2.2 Fun Control姿势控制加速版V1_1956358490119962626.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1956358490119962626.json
hash: af9bdfed9152e8f8
coverage: 0.637681
learned_at: 2026-10-15 22:31:13
nodes: [WanVideoTextEmbedBridge, CLIPTextEncode, CLIPLoader, Note, WanVideoDecode, GetNode, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoSetLoRAs, Note, Note, Note, GetNode, MarkdownNote, DownloadAndLoadDepthAnythingV2Model, Note, WanVideoBlockSwap, CLIPTextEncode, SetNode, GetNode, SetNode, SetNode, GetNode, GetNode, INTConstant, WanVideoScheduler, SetNode, INTConstant, WanVideoSampler, PrimitiveNode, Reroute, VHS_VideoCombine, SetNode, VHS_VideoCombine, Reroute, WanVideoEncode, GetNode, WanVideoImageToVideoEncode, Reroute, WanVideoModelLoader, WanVideoModelLoader, WanVideoVAELoader, WanVideoSampler, WanVideoTorchCompileSettings, WanVideoTextEncodeCached, ImageResizeKJv2, WanVideoAddControlEmbeds, GetImageSizeAndCount, WanVideoEncode, DWPreprocessor, ImageResizeKJv2, DepthAnything_V2, WanVideoLoraSelectMulti, WanVideoLoraSelectMulti, ImageConcatMulti, VHS_LoadVideo, ImageConcanate, VHS_VideoCombine, PDIMAGE_LongerSize, Note, Note, Note, JWInteger, JWInteger, JWInteger, Note, CR Prompt Text, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/(KJ版)Wan2.2 Fun Control姿势控制加速版V1_1956358490119962626.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1956358490119962626.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（69 个）：
- `WanVideoTextEmbedBridge`
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `Note`
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
- `CLIPTextEncode` ★核心
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
- `DWPreprocessor`
- `ImageResizeKJv2`
- `DepthAnything_V2`
- `WanVideoLoraSelectMulti`
- `WanVideoLoraSelectMulti`
- `ImageConcatMulti`
- `VHS_LoadVideo`
- `ImageConcanate`
- `VHS_VideoCombine`
- `PDIMAGE_LongerSize`
- `Note`
- `Note`
- `Note`
- `JWInteger`
- `JWInteger`
- `JWInteger`
- `Note`
- `CR Prompt Text`
- `LoadImage`

## 知识

覆盖率 **64%**（44/69）

**有卡**：`WanVideoTextEmbedBridge`、`CLIPTextEncode`、`CLIPLoader`、`WanVideoDecode`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`DownloadAndLoadDepthAnythingV2Model`、`WanVideoBlockSwap`、`INTConstant`、`WanVideoScheduler`、`WanVideoSampler`、`VHS_VideoCombine`、`WanVideoEncode`、`WanVideoImageToVideoEncode`、`WanVideoModelLoader`、`WanVideoVAELoader`、`WanVideoTorchCompileSettings`、`WanVideoTextEncodeCached`、`ImageResizeKJv2`、`WanVideoAddControlEmbeds`、`GetImageSizeAndCount`、`DWPreprocessor`、`DepthAnything_V2`、`WanVideoLoraSelectMulti`、`ImageConcatMulti`、`VHS_LoadVideo`、`ImageConcanate`、`PDIMAGE_LongerSize`、`JWInteger`、`CR Prompt Text`、`LoadImage`

**用到的条目**：CLIPTextEncode、CLIPLoader、LoadImage、DepthAnything_V2、DownloadAndLoadDepthAnythingV2Model、WanVideoSampler、WanVideoDecode、WanVideoVAELoader
