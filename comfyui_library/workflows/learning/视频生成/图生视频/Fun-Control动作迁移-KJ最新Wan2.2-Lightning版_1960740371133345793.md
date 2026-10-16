---
key: 视频生成/图生视频/Fun-Control动作迁移-KJ最新Wan2.2-Lightning版_1960740371133345793.json
name: Fun-Control动作迁移-KJ最新Wan2.2-Lightning版_1960740371133345793.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1960740371133345793.json
hash: 41834292a6c681d8
coverage: 0.676923
learned_at: 2026-10-15 22:31:26
nodes: [WanVideoTextEmbedBridge, CLIPTextEncode, CLIPLoader, Note, GetNode, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoSetLoRAs, Note, WanVideoTorchCompileSettings, Note, Note, WanVideoSampler, WanVideoBlockSwap, CLIPTextEncode, SetNode, GetNode, GetNode, SetNode, INTConstant, WanVideoSampler, Reroute, GetNode, Reroute, VHS_VideoCombine, GetMaskSizeAndCount, VHS_VideoCombine, ImageResizeKJv2, INTConstant, INTConstant, GetImageSizeAndCount, CreateShapeImageOnPath, WanVideoEncode, WanVideoImageToVideoEncode, Note, WanVideoAddControlEmbeds, Reroute, MarkdownNote, SplineEditor, PrimitiveNode, LoadImage, SetNode, DWPreprocessor, Zoe-DepthMapPreprocessor, ImageBlend, PrimitiveNode, WanVideoModelLoader, WanVideoModelLoader, WanVideoLoraSelectMulti, WanVideoLoraSelectMulti, INTConstant, SetNode, WanVideoScheduler, SetNode, WanVideoEncode, ImageResizeKJv2, WanVideoTextEncodeCached, WanVideoVAELoader, GetNode, VHS_VideoCombine, VHS_VideoCombine, VHS_LoadVideo, ImageConcatMulti, WanVideoDecode]
patterns: []
missing: []
---

# 视频生成/图生视频/Fun-Control动作迁移-KJ最新Wan2.2-Lightning版_1960740371133345793.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1960740371133345793.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（65 个）：
- `WanVideoTextEmbedBridge`
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `Note`
- `GetNode`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `Note`
- `WanVideoTorchCompileSettings`
- `Note`
- `Note`
- `WanVideoSampler` ★核心
- `WanVideoBlockSwap`
- `CLIPTextEncode` ★核心
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `INTConstant`
- `WanVideoSampler` ★核心
- `Reroute`
- `GetNode`
- `Reroute`
- `VHS_VideoCombine`
- `GetMaskSizeAndCount`
- `VHS_VideoCombine`
- `ImageResizeKJv2`
- `INTConstant`
- `INTConstant`
- `GetImageSizeAndCount`
- `CreateShapeImageOnPath`
- `WanVideoEncode`
- `WanVideoImageToVideoEncode`
- `Note`
- `WanVideoAddControlEmbeds`
- `Reroute`
- `MarkdownNote`
- `SplineEditor`
- `PrimitiveNode`
- `LoadImage`
- `SetNode`
- `DWPreprocessor`
- `Zoe-DepthMapPreprocessor`
- `ImageBlend`
- `PrimitiveNode`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoLoraSelectMulti`
- `WanVideoLoraSelectMulti`
- `INTConstant`
- `SetNode`
- `WanVideoScheduler`
- `SetNode`
- `WanVideoEncode`
- `ImageResizeKJv2`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`
- `GetNode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `ImageConcatMulti`
- `WanVideoDecode`

## 知识

覆盖率 **68%**（44/65）

**有卡**：`WanVideoTextEmbedBridge`、`CLIPTextEncode`、`CLIPLoader`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoTorchCompileSettings`、`WanVideoSampler`、`WanVideoBlockSwap`、`INTConstant`、`VHS_VideoCombine`、`GetMaskSizeAndCount`、`ImageResizeKJv2`、`GetImageSizeAndCount`、`CreateShapeImageOnPath`、`WanVideoEncode`、`WanVideoImageToVideoEncode`、`WanVideoAddControlEmbeds`、`SplineEditor`、`LoadImage`、`DWPreprocessor`、`Zoe-DepthMapPreprocessor`、`ImageBlend`、`WanVideoModelLoader`、`WanVideoLoraSelectMulti`、`WanVideoScheduler`、`WanVideoTextEncodeCached`、`WanVideoVAELoader`、`VHS_LoadVideo`、`ImageConcatMulti`、`WanVideoDecode`

**用到的条目**：CLIPTextEncode、CLIPLoader、LoadImage、Zoe-DepthMapPreprocessor、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoImageToVideoEncode
