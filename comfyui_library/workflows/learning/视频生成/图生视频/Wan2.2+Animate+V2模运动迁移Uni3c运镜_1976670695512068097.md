---
key: 视频生成/图生视频/Wan2.2+Animate+V2模运动迁移Uni3c运镜_1976670695512068097.json
name: Wan2.2+Animate+V2模运动迁移Uni3c运镜_1976670695512068097.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2+Animate+V2模运动迁移Uni3c运镜_1976670695512068097.json
hash: 07aaa7ba2f2d5e4a
coverage: 0.944444
learned_at: 2026-10-15 22:32:12
nodes: [WanVideoSetLoRAs, WanVideoSetBlockSwap, VHS_VideoCombine, WanVideoDecode, ImageResizeKJv2, Sam2Segmentation, GrowMask, DrawMaskOnImage, GetImageSize+, WanVideoClipVisionEncode, VHS_VideoCombine, ImageResizeKJv2, PoseAndFaceDetection, VHS_VideoCombine, SetNode, BlockifyMask, WanVideoBlockSwap, DownloadAndLoadSAM2Model, DrawViTPose, WanVideoVAELoader, OnnxDetectionModelLoader, WanVideoSampler, WanVideoAnimateEmbeds, SetNode, WanVideoTextEncodeCached, VHS_VideoCombine, WanVideoEncode, GetImageSizeAndCount, WanVideoUni3C_embeds, WanVideoUni3C_ControlnetLoader, VHS_LoadVideo, LoadImage, VHS_LoadVideo, WanVideoModelLoader, WanVideoLoraSelectMulti, CLIPVisionLoader]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2+Animate+V2模运动迁移Uni3c运镜_1976670695512068097.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1976670695512068097.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（36 个）：
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `ImageResizeKJv2`
- `Sam2Segmentation`
- `GrowMask`
- `DrawMaskOnImage`
- `GetImageSize+`
- `WanVideoClipVisionEncode`
- `VHS_VideoCombine`
- `ImageResizeKJv2`
- `PoseAndFaceDetection`
- `VHS_VideoCombine`
- `SetNode`
- `BlockifyMask`
- `WanVideoBlockSwap`
- `DownloadAndLoadSAM2Model`
- `DrawViTPose`
- `WanVideoVAELoader`
- `OnnxDetectionModelLoader`
- `WanVideoSampler` ★核心
- `WanVideoAnimateEmbeds`
- `SetNode`
- `WanVideoTextEncodeCached`
- `VHS_VideoCombine`
- `WanVideoEncode`
- `GetImageSizeAndCount`
- `WanVideoUni3C_embeds`
- `WanVideoUni3C_ControlnetLoader`
- `VHS_LoadVideo`
- `LoadImage`
- `VHS_LoadVideo`
- `WanVideoModelLoader`
- `WanVideoLoraSelectMulti`
- `CLIPVisionLoader`

## 知识

覆盖率 **94%**（34/36）

**有卡**：`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`VHS_VideoCombine`、`WanVideoDecode`、`ImageResizeKJv2`、`Sam2Segmentation`、`GrowMask`、`DrawMaskOnImage`、`GetImageSize+`、`WanVideoClipVisionEncode`、`PoseAndFaceDetection`、`BlockifyMask`、`WanVideoBlockSwap`、`DownloadAndLoadSAM2Model`、`DrawViTPose`、`WanVideoVAELoader`、`OnnxDetectionModelLoader`、`WanVideoSampler`、`WanVideoAnimateEmbeds`、`WanVideoTextEncodeCached`、`WanVideoEncode`、`GetImageSizeAndCount`、`WanVideoUni3C_embeds`、`WanVideoUni3C_ControlnetLoader`、`VHS_LoadVideo`、`LoadImage`、`WanVideoModelLoader`、`WanVideoLoraSelectMulti`、`CLIPVisionLoader`

**用到的条目**：LoadImage、WanVideoUni3C_ControlnetLoader、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoEncode
