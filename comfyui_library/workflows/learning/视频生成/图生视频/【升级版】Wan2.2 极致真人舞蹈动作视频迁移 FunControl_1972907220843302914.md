---
key: 视频生成/图生视频/【升级版】Wan2.2 极致真人舞蹈动作视频迁移 FunControl_1972907220843302914.json
name: 【升级版】Wan2.2 极致真人舞蹈动作视频迁移 FunControl_1972907220843302914.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1972907220843302914.json
hash: 76ab6a470c20eccd
coverage: 0.68
learned_at: 2026-10-15 22:32:01
nodes: [LoadWanVideoT5TextEncoder, WanVideoSampler, GetNode, WanVideoSampler, WanVideoImageToVideoEncode, Reroute, Reroute, SetNode, GetNode, WanVideoSetBlockSwap, GetNode, WanVideoModelLoader, WanVideoVAELoader, WanVideoBlockSwap, WanVideoLoraSelectMulti, WanVideoSetLoRAs, PrimitiveNode, PrimitiveNode, PrimitiveNode, PrimitiveNode, WanVideoModelLoader, WanVideoLoraSelectMulti, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoEmptyEmbeds, WanVideoControlEmbeds, WanVideoEncode, GetImageSizeAndCount, PrimitiveInt, PrimitiveInt, ImageResizeKJv2, Note, SetNode, VHS_VideoCombine, Zoe-DepthMapPreprocessor, DownloadAndLoadDepthAnythingV2Model, DepthAnything_V2, ImageResizeKJv2, GetNode, WanVideoDecode, VHS_VideoCombine, ImageBlend, ImageConcatMulti, DWPreprocessor, VHS_LoadVideo, WanVideoTorchCompileSettings, WanVideoTextEncode, Reroute, VHS_VideoCombine, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/【升级版】Wan2.2 极致真人舞蹈动作视频迁移 FunControl_1972907220843302914.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1972907220843302914.json`

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
- `WanVideoTextEncode`
- `Reroute`
- `VHS_VideoCombine`
- `LoadImage`

## 知识

覆盖率 **68%**（34/50）

**有卡**：`LoadWanVideoT5TextEncoder`、`WanVideoSampler`、`WanVideoImageToVideoEncode`、`WanVideoSetBlockSwap`、`WanVideoModelLoader`、`WanVideoVAELoader`、`WanVideoBlockSwap`、`WanVideoLoraSelectMulti`、`WanVideoSetLoRAs`、`WanVideoEmptyEmbeds`、`WanVideoControlEmbeds`、`WanVideoEncode`、`GetImageSizeAndCount`、`ImageResizeKJv2`、`VHS_VideoCombine`、`Zoe-DepthMapPreprocessor`、`DownloadAndLoadDepthAnythingV2Model`、`DepthAnything_V2`、`WanVideoDecode`、`ImageBlend`、`ImageConcatMulti`、`DWPreprocessor`、`VHS_LoadVideo`、`WanVideoTorchCompileSettings`、`WanVideoTextEncode`、`LoadImage`

**用到的条目**：LoadImage、DepthAnything_V2、DownloadAndLoadDepthAnythingV2Model、Zoe-DepthMapPreprocessor、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode
