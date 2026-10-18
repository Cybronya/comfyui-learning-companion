---
key: 视频生成/图生视频/人物替换   角色替换   二创首选  Wan2.2 wan22_2045436584266309633.json
name: 人物替换   角色替换   二创首选  Wan2.2 wan22_2045436584266309633.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/人物替换   角色替换   二创首选  Wan2.2 wan22_2045436584266309633.json
hash: 8c6b455bd71bd329
coverage: 0.560976
learned_at: 2026-10-15 22:36:48
nodes: [WanVideoModelLoader, WanVideoLoraSelectMulti, OnnxDetectionModelLoader, GetNode, GetNode, WanVideoSetLoRAs, WanVideoVAELoader, INTConstant, INTConstant, GetNode, easy cleanGpuUsed, SetNode, PoseAndFaceDetection, DrawViTPose, SetNode, easy cleanGpuUsed, SetNode, BlockifyMask, VHS_VideoCombine, SeCModelLoader, GrowMask, InvertMask, MaskToImage, SetNode, GetImageSizeAndCount, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, SetNode, SetNode, INTConstant, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, WanVideoTextEncodeCached, WanVideoClipVisionEncode, easy cleanGpuUsed, WanVideoAnimateEmbeds, WanVideoSampler, WanVideoDecode, GetImageSizeAndCount, ImageConcanate, easy cleanGpuUsed, SetNode, CLIPVisionLoader, VHS_VideoCombine, VHS_VideoCombine, SetNode, SetNode, WanVideoSetBlockSwap, WanVideoBlockSwap, VHS_LoadVideo, ImageResizeKJv2, GetNode, GetNode, SetNode, PreviewImage, ImageFromBatch+, SeCVideoSegmentation, LayerUtility: ImageBlend, JWInteger, GetNode, PointsEditor, VHS_VideoCombine, VHS_VideoInfo, CR Text, GetNode, LoadImage, VHS_VideoCombine, PreviewImage, Note, DrawMaskOnImage]
patterns: []
missing: []
---

# 视频生成/图生视频/人物替换   角色替换   二创首选  Wan2.2 wan22_2045436584266309633.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2045436584266309633.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（82 个）：
- `WanVideoModelLoader`
- `WanVideoLoraSelectMulti`
- `OnnxDetectionModelLoader`
- `GetNode`
- `GetNode`
- `WanVideoSetLoRAs`
- `WanVideoVAELoader`
- `INTConstant`
- `INTConstant`
- `GetNode`
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
- `GrowMask`
- `InvertMask`
- `MaskToImage`
- `SetNode`
- `GetImageSizeAndCount`
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
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `SetNode`
- `SetNode`
- `WanVideoSetBlockSwap`
- `WanVideoBlockSwap`
- `VHS_LoadVideo`
- `ImageResizeKJv2`
- `GetNode`
- `GetNode`
- `SetNode`
- `PreviewImage`
- `ImageFromBatch+`
- `SeCVideoSegmentation`
- `LayerUtility: ImageBlend`
- `JWInteger`
- `GetNode`
- `PointsEditor`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `CR Text`
- `GetNode`
- `LoadImage`
- `VHS_VideoCombine`
- `PreviewImage`
- `Note`
- `DrawMaskOnImage`

## 知识

覆盖率 **56%**（46/82）

**有卡**：`WanVideoModelLoader`、`WanVideoLoraSelectMulti`、`OnnxDetectionModelLoader`、`WanVideoSetLoRAs`、`WanVideoVAELoader`、`INTConstant`、`easy cleanGpuUsed`、`PoseAndFaceDetection`、`DrawViTPose`、`BlockifyMask`、`VHS_VideoCombine`、`SeCModelLoader`、`GrowMask`、`InvertMask`、`MaskToImage`、`GetImageSizeAndCount`、`WanVideoTextEncodeCached`、`WanVideoClipVisionEncode`、`WanVideoAnimateEmbeds`、`WanVideoSampler`、`WanVideoDecode`、`ImageConcanate`、`CLIPVisionLoader`、`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`VHS_LoadVideo`、`ImageResizeKJv2`、`ImageFromBatch+`、`SeCVideoSegmentation`、`LayerUtility: ImageBlend`、`JWInteger`、`PointsEditor`、`VHS_VideoInfo`、`CR Text`、`LoadImage`、`DrawMaskOnImage`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
