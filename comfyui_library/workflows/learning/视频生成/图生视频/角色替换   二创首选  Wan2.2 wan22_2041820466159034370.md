---
key: 视频生成/图生视频/角色替换   二创首选  Wan2.2 wan22_2041820466159034370.json
name: 角色替换   二创首选  Wan2.2 wan22_2041820466159034370.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/角色替换   二创首选  Wan2.2 wan22_2041820466159034370.json
hash: d9a58df4bfca1972
coverage: 0.560976
learned_at: 2026-10-15 22:36:23
nodes: [WanVideoModelLoader, WanVideoLoraSelectMulti, OnnxDetectionModelLoader, GetNode, GetNode, VHS_VideoCombine, WanVideoSetLoRAs, WanVideoVAELoader, JWInteger, ImageFromBatch+, PreviewImage, INTConstant, INTConstant, GetNode, GetNode, ImageResizeKJv2, SetNode, GetNode, DrawMaskOnImage, easy cleanGpuUsed, SetNode, PoseAndFaceDetection, DrawViTPose, SetNode, easy cleanGpuUsed, SetNode, BlockifyMask, VHS_VideoCombine, SeCModelLoader, SeCVideoSegmentation, GrowMask, InvertMask, MaskToImage, SetNode, GetImageSizeAndCount, VHS_VideoCombine, LayerUtility: ImageBlend, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, SetNode, SetNode, INTConstant, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, WanVideoTextEncodeCached, CR Text, WanVideoClipVisionEncode, easy cleanGpuUsed, WanVideoAnimateEmbeds, WanVideoSampler, WanVideoDecode, GetImageSizeAndCount, ImageConcanate, easy cleanGpuUsed, SetNode, CLIPVisionLoader, GetNode, VHS_VideoInfo, PreviewImage, VHS_VideoCombine, VHS_VideoCombine, SetNode, VHS_LoadVideo, Note, PointsEditor, LoadImage, SetNode, WanVideoSetBlockSwap, WanVideoBlockSwap]
patterns: []
missing: []
---

# 视频生成/图生视频/角色替换   二创首选  Wan2.2 wan22_2041820466159034370.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2041820466159034370.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（82 个）：
- `WanVideoModelLoader`
- `WanVideoLoraSelectMulti`
- `OnnxDetectionModelLoader`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `WanVideoSetLoRAs`
- `WanVideoVAELoader`
- `JWInteger`
- `ImageFromBatch+`
- `PreviewImage`
- `INTConstant`
- `INTConstant`
- `GetNode`
- `GetNode`
- `ImageResizeKJv2`
- `SetNode`
- `GetNode`
- `DrawMaskOnImage`
- `easy cleanGpuUsed`
- `SetNode`
- `PoseAndFaceDetection`
- `DrawViTPose`
- `SetNode`
- `easy cleanGpuUsed`
- `SetNode`
- `BlockifyMask`
- `VHS_VideoCombine`
- `SeCModelLoader`
- `SeCVideoSegmentation`
- `GrowMask`
- `InvertMask`
- `MaskToImage`
- `SetNode`
- `GetImageSizeAndCount`
- `VHS_VideoCombine`
- `LayerUtility: ImageBlend`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `INTConstant`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoTextEncodeCached`
- `CR Text`
- `WanVideoClipVisionEncode`
- `easy cleanGpuUsed`
- `WanVideoAnimateEmbeds`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `GetImageSizeAndCount`
- `ImageConcanate`
- `easy cleanGpuUsed`
- `SetNode`
- `CLIPVisionLoader`
- `GetNode`
- `VHS_VideoInfo`
- `PreviewImage`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `SetNode`
- `VHS_LoadVideo`
- `Note`
- `PointsEditor`
- `LoadImage`
- `SetNode`
- `WanVideoSetBlockSwap`
- `WanVideoBlockSwap`

## 知识

覆盖率 **56%**（46/82）

**有卡**：`WanVideoModelLoader`、`WanVideoLoraSelectMulti`、`OnnxDetectionModelLoader`、`VHS_VideoCombine`、`WanVideoSetLoRAs`、`WanVideoVAELoader`、`JWInteger`、`ImageFromBatch+`、`INTConstant`、`ImageResizeKJv2`、`DrawMaskOnImage`、`easy cleanGpuUsed`、`PoseAndFaceDetection`、`DrawViTPose`、`BlockifyMask`、`SeCModelLoader`、`SeCVideoSegmentation`、`GrowMask`、`InvertMask`、`MaskToImage`、`GetImageSizeAndCount`、`LayerUtility: ImageBlend`、`WanVideoTextEncodeCached`、`CR Text`、`WanVideoClipVisionEncode`、`WanVideoAnimateEmbeds`、`WanVideoSampler`、`WanVideoDecode`、`ImageConcanate`、`CLIPVisionLoader`、`VHS_VideoInfo`、`VHS_LoadVideo`、`PointsEditor`、`LoadImage`、`WanVideoSetBlockSwap`、`WanVideoBlockSwap`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
