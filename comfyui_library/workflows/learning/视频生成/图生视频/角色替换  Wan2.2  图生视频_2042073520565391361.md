---
key: 视频生成/图生视频/角色替换  Wan2.2  图生视频_2042073520565391361.json
name: 角色替换  Wan2.2  图生视频_2042073520565391361.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/角色替换  Wan2.2  图生视频_2042073520565391361.json
hash: 02525d4986f88161
coverage: 0.567901
learned_at: 2026-10-15 22:36:24
nodes: [GetNode, Reroute, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, Reroute, Reroute, SetNode, GetNode, WanVideoAnimateEmbeds, GetNode, WanVideoSampler, easy cleanGpuUsed, GetNode, WanVideoDecode, GetImageSizeAndCount, ImageConcanate, LayerUtility: ImageBlend, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, SetNode, GetNode, WanVideoModelLoader, WanVideoLoraSelectMulti, WanVideoBlockSwap, WanVideoVAELoader, WanVideoSetLoRAs, WanVideoSetBlockSwap, SetNode, SetNode, easy cleanGpuUsed, WanVideoTextEncodeCached, CR Text, WanVideoClipVisionEncode, CLIPVisionLoader, GetNode, GetNode, GetNode, VHS_VideoCombine, SeCModelLoader, DrawViTPose, Reroute, PoseAndFaceDetection, easy cleanGpuUsed, ImageResizeKJv2, PreviewImage, SetNode, VHS_LoadVideo, PointsEditor, ImageFromBatch+, JWInteger, Note, PreviewImage, OnnxDetectionModelLoader, InvertMask, LoadImage, VHS_VideoInfo, GetImageSizeAndCount, SetNode, SetNode, SetNode, INTConstant, SetNode, INTConstant, INTConstant, SetNode, SetNode, SeCVideoSegmentation, SetNode, easy cleanGpuUsed, GetNode, GrowMask, BlockifyMask, VHS_VideoCombine, MaskToImage, DrawMaskOnImage, SetNode]
patterns: []
missing: []
---

# 视频生成/图生视频/角色替换  Wan2.2  图生视频_2042073520565391361.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2042073520565391361.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（81 个）：
- `GetNode`
- `Reroute`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `Reroute`
- `Reroute`
- `SetNode`
- `GetNode`
- `WanVideoAnimateEmbeds`
- `GetNode`
- `WanVideoSampler` ★核心
- `easy cleanGpuUsed`
- `GetNode`
- `WanVideoDecode`
- `GetImageSizeAndCount`
- `ImageConcanate`
- `LayerUtility: ImageBlend`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `SetNode`
- `GetNode`
- `WanVideoModelLoader`
- `WanVideoLoraSelectMulti`
- `WanVideoBlockSwap`
- `WanVideoVAELoader`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `SetNode`
- `SetNode`
- `easy cleanGpuUsed`
- `WanVideoTextEncodeCached`
- `CR Text`
- `WanVideoClipVisionEncode`
- `CLIPVisionLoader`
- `GetNode`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `SeCModelLoader`
- `DrawViTPose`
- `Reroute`
- `PoseAndFaceDetection`
- `easy cleanGpuUsed`
- `ImageResizeKJv2`
- `PreviewImage`
- `SetNode`
- `VHS_LoadVideo`
- `PointsEditor`
- `ImageFromBatch+`
- `JWInteger`
- `Note`
- `PreviewImage`
- `OnnxDetectionModelLoader`
- `InvertMask`
- `LoadImage`
- `VHS_VideoInfo`
- `GetImageSizeAndCount`
- `SetNode`
- `SetNode`
- `SetNode`
- `INTConstant`
- `SetNode`
- `INTConstant`
- `INTConstant`
- `SetNode`
- `SetNode`
- `SeCVideoSegmentation`
- `SetNode`
- `easy cleanGpuUsed`
- `GetNode`
- `GrowMask`
- `BlockifyMask`
- `VHS_VideoCombine`
- `MaskToImage`
- `DrawMaskOnImage`
- `SetNode`

## 知识

覆盖率 **57%**（46/81）

**有卡**：`WanVideoAnimateEmbeds`、`WanVideoSampler`、`easy cleanGpuUsed`、`WanVideoDecode`、`GetImageSizeAndCount`、`ImageConcanate`、`LayerUtility: ImageBlend`、`VHS_VideoCombine`、`WanVideoModelLoader`、`WanVideoLoraSelectMulti`、`WanVideoBlockSwap`、`WanVideoVAELoader`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`WanVideoTextEncodeCached`、`CR Text`、`WanVideoClipVisionEncode`、`CLIPVisionLoader`、`SeCModelLoader`、`DrawViTPose`、`PoseAndFaceDetection`、`ImageResizeKJv2`、`VHS_LoadVideo`、`PointsEditor`、`ImageFromBatch+`、`JWInteger`、`OnnxDetectionModelLoader`、`InvertMask`、`LoadImage`、`VHS_VideoInfo`、`INTConstant`、`SeCVideoSegmentation`、`GrowMask`、`BlockifyMask`、`MaskToImage`、`DrawMaskOnImage`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
