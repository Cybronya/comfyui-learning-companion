---
key: 视频生成/文生视频/Wan2.2 极致真人舞蹈动作视频迁移 FunControl_1956170101122891778.json
name: Wan2.2 极致真人舞蹈动作视频迁移 FunControl_1956170101122891778.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/1956170101122891778.json
hash: b9ba63be36586646
coverage: 0.68
learned_at: 2026-10-15 22:43:40
nodes: [LoadWanVideoT5TextEncoder, WanVideoSampler, GetNode, WanVideoSampler, WanVideoImageToVideoEncode, Reroute, Reroute, SetNode, GetNode, WanVideoSetBlockSwap, GetNode, WanVideoModelLoader, WanVideoVAELoader, WanVideoBlockSwap, WanVideoLoraSelectMulti, WanVideoSetLoRAs, PrimitiveNode, PrimitiveNode, PrimitiveNode, PrimitiveNode, WanVideoModelLoader, WanVideoLoraSelectMulti, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoEmptyEmbeds, WanVideoControlEmbeds, WanVideoEncode, GetImageSizeAndCount, PrimitiveInt, PrimitiveInt, ImageResizeKJv2, Note, SetNode, VHS_VideoCombine, Zoe-DepthMapPreprocessor, DownloadAndLoadDepthAnythingV2Model, DepthAnything_V2, ImageResizeKJv2, GetNode, WanVideoDecode, VHS_VideoCombine, ImageBlend, ImageConcatMulti, DWPreprocessor, VHS_LoadVideo, WanVideoTorchCompileSettings, LoadImage, WanVideoTextEncode, Reroute, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/文生视频/Wan2.2 极致真人舞蹈动作视频迁移 FunControl_1956170101122891778.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1956170101122891778.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（50 个）：
- `LoadWanVideoT5TextEncoder`
- `WanVideoSampler` ★核心
- `GetNode`
- `WanVideoSampler` ★核心
- `WanVideoImageToVideoEncode`
- `Reroute`
- `Reroute`
- `SetNode`
- `GetNode`
- `WanVideoSetBlockSwap`
- `GetNode`
- `WanVideoModelLoader`
- `WanVideoVAELoader`
- `WanVideoBlockSwap`
- `WanVideoLoraSelectMulti`
- `WanVideoSetLoRAs`
- `PrimitiveNode`
- `PrimitiveNode`
- `PrimitiveNode`
- `PrimitiveNode`
- `WanVideoModelLoader`
- `WanVideoLoraSelectMulti`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoEmptyEmbeds`
- `WanVideoControlEmbeds`
- `WanVideoEncode`
- `GetImageSizeAndCount`
- `PrimitiveInt`
- `PrimitiveInt`
- `ImageResizeKJv2`
- `Note`
- `SetNode`
- `VHS_VideoCombine`
- `Zoe-DepthMapPreprocessor`
- `DownloadAndLoadDepthAnythingV2Model`
- `DepthAnything_V2`
- `ImageResizeKJv2`
- `GetNode`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `ImageBlend`
- `ImageConcatMulti`
- `DWPreprocessor`
- `VHS_LoadVideo`
- `WanVideoTorchCompileSettings`
- `LoadImage`
- `WanVideoTextEncode`
- `Reroute`
- `VHS_VideoCombine`

## 知识

覆盖率 **68%**（34/50）

**有卡**：`LoadWanVideoT5TextEncoder`、`WanVideoSampler`、`WanVideoImageToVideoEncode`、`WanVideoSetBlockSwap`、`WanVideoModelLoader`、`WanVideoVAELoader`、`WanVideoBlockSwap`、`WanVideoLoraSelectMulti`、`WanVideoSetLoRAs`、`WanVideoEmptyEmbeds`、`WanVideoControlEmbeds`、`WanVideoEncode`、`GetImageSizeAndCount`、`ImageResizeKJv2`、`VHS_VideoCombine`、`Zoe-DepthMapPreprocessor`、`DownloadAndLoadDepthAnythingV2Model`、`DepthAnything_V2`、`WanVideoDecode`、`ImageBlend`、`ImageConcatMulti`、`DWPreprocessor`、`VHS_LoadVideo`、`WanVideoTorchCompileSettings`、`LoadImage`、`WanVideoTextEncode`

**用到的条目**：LoadImage、DepthAnything_V2、DownloadAndLoadDepthAnythingV2Model、Zoe-DepthMapPreprocessor、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode
