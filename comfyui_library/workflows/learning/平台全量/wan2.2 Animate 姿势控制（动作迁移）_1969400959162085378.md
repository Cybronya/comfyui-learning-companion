---
key: 平台全量/wan2.2 Animate 姿势控制（动作迁移）_1969400959162085378.json
name: wan2.2 Animate 姿势控制（动作迁移）_1969400959162085378
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/wan2.2 Animate 姿势控制（动作迁移）_1969400959162085378.json
hash: 8eeb6d9a86e1ca61
coverage: 0.888889
learned_at: 2026-11-14 01:19:16
nodes: [WanVideoBlockSwap, Reroute, WanVideoDecode, WanVideoClipVisionEncode, WanVideoSetBlockSwap, PixelPerfectResolution, WanVideoSetLoRAs, CLIPVisionLoader, DWPreprocessor, WanVideoModelLoader, WanVideoLoraSelectMulti, VHS_VideoCombine, FaceMaskFromPoseKeypoints, WanVideoTextEncodeCached, WanVideoVAELoader, CR Text, PreviewImage, LoadImage, ImageCropByMaskAndResize, WanVideoSampler, JWInteger, VHS_LoadVideo, Reroute, WanVideoAnimateEmbeds, VHS_VideoCombine, JWInteger, ImageResizeKJv2]
patterns: []
missing: []
---

# 平台全量/wan2.2 Animate 姿势控制（动作迁移）_1969400959162085378.json

> 来源文件 `comfyui_library/workflows/平台全量/wan2.2 Animate 姿势控制（动作迁移）_1969400959162085378.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（27 个）：
- `WanVideoBlockSwap`
- `Reroute`
- `WanVideoDecode`
- `WanVideoClipVisionEncode`
- `WanVideoSetBlockSwap`
- `PixelPerfectResolution`
- `WanVideoSetLoRAs`
- `CLIPVisionLoader`
- `DWPreprocessor`
- `WanVideoModelLoader`
- `WanVideoLoraSelectMulti`
- `VHS_VideoCombine`
- `FaceMaskFromPoseKeypoints`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`
- `CR Text`
- `PreviewImage`
- `LoadImage`
- `ImageCropByMaskAndResize`
- `WanVideoSampler` ★核心
- `JWInteger`
- `VHS_LoadVideo`
- `Reroute`
- `WanVideoAnimateEmbeds`
- `VHS_VideoCombine`
- `JWInteger`
- `ImageResizeKJv2`

## 知识

覆盖率 **89%**（24/27）

**有卡**：`WanVideoBlockSwap`、`WanVideoDecode`、`WanVideoClipVisionEncode`、`WanVideoSetBlockSwap`、`PixelPerfectResolution`、`WanVideoSetLoRAs`、`CLIPVisionLoader`、`DWPreprocessor`、`WanVideoModelLoader`、`WanVideoLoraSelectMulti`、`VHS_VideoCombine`、`FaceMaskFromPoseKeypoints`、`WanVideoTextEncodeCached`、`WanVideoVAELoader`、`CR Text`、`LoadImage`、`ImageCropByMaskAndResize`、`WanVideoSampler`、`JWInteger`、`VHS_LoadVideo`、`WanVideoAnimateEmbeds`、`ImageResizeKJv2`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVAELoader、WanVideoLoraSelectMulti、WanVideoSetLoRAs
