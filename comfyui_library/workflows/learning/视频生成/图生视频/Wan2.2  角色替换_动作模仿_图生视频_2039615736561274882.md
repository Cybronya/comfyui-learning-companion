---
key: 视频生成/图生视频/Wan2.2  角色替换_动作模仿_图生视频_2039615736561274882.json
name: Wan2.2  角色替换_动作模仿_图生视频_2039615736561274882.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2  角色替换_动作模仿_图生视频_2039615736561274882.json
hash: 4661e5acd4aabe16
coverage: 0.567901
learned_at: 2026-10-15 22:36:09
nodes: [GetNode, Reroute, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, ImageFromBatch+, Note, Reroute, Reroute, PreviewImage, INTConstant, INTConstant, SetNode, SetNode, PreviewImage, SetNode, JWInteger, GetNode, WanVideoAnimateEmbeds, GetNode, WanVideoSampler, easy cleanGpuUsed, GetNode, WanVideoDecode, GetImageSizeAndCount, ImageConcanate, SeCVideoSegmentation, LayerUtility: ImageBlend, SetNode, GetNode, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, GrowMask, BlockifyMask, SetNode, GetNode, SetNode, WanVideoModelLoader, WanVideoLoraSelectMulti, WanVideoBlockSwap, WanVideoVAELoader, WanVideoSetLoRAs, WanVideoSetBlockSwap, SetNode, SetNode, easy cleanGpuUsed, WanVideoTextEncodeCached, CR Text, WanVideoClipVisionEncode, CLIPVisionLoader, GetNode, GetNode, GetNode, VHS_VideoCombine, SeCModelLoader, OnnxDetectionModelLoader, DrawViTPose, Reroute, PoseAndFaceDetection, SetNode, easy cleanGpuUsed, easy cleanGpuUsed, DrawMaskOnImage, MaskToImage, InvertMask, SetNode, SetNode, SetNode, VHS_VideoInfo, GetImageSizeAndCount, INTConstant, SetNode, ImageResizeKJv2, VHS_LoadVideo, LoadImage, PointsEditor]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2  角色替换_动作模仿_图生视频_2039615736561274882.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2039615736561274882.json`

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
- `ImageFromBatch+`
- `Note`
- `Reroute`
- `Reroute`
- `PreviewImage`
- `INTConstant`
- `INTConstant`
- `SetNode`
- `SetNode`
- `PreviewImage`
- `SetNode`
- `JWInteger`
- `GetNode`
- `WanVideoAnimateEmbeds`
- `GetNode`
- `WanVideoSampler` ★核心
- `easy cleanGpuUsed`
- `GetNode`
- `WanVideoDecode`
- `GetImageSizeAndCount`
- `ImageConcanate`
- `SeCVideoSegmentation`
- `LayerUtility: ImageBlend`
- `SetNode`
- `GetNode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `GrowMask`
- `BlockifyMask`
- `SetNode`
- `GetNode`
- `SetNode`
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
- `OnnxDetectionModelLoader`
- `DrawViTPose`
- `Reroute`
- `PoseAndFaceDetection`
- `SetNode`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `DrawMaskOnImage`
- `MaskToImage`
- `InvertMask`
- `SetNode`
- `SetNode`
- `SetNode`
- `VHS_VideoInfo`
- `GetImageSizeAndCount`
- `INTConstant`
- `SetNode`
- `ImageResizeKJv2`
- `VHS_LoadVideo`
- `LoadImage`
- `PointsEditor`

## 知识

覆盖率 **57%**（46/81）

**有卡**：`ImageFromBatch+`、`INTConstant`、`JWInteger`、`WanVideoAnimateEmbeds`、`WanVideoSampler`、`easy cleanGpuUsed`、`WanVideoDecode`、`GetImageSizeAndCount`、`ImageConcanate`、`SeCVideoSegmentation`、`LayerUtility: ImageBlend`、`VHS_VideoCombine`、`GrowMask`、`BlockifyMask`、`WanVideoModelLoader`、`WanVideoLoraSelectMulti`、`WanVideoBlockSwap`、`WanVideoVAELoader`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`WanVideoTextEncodeCached`、`CR Text`、`WanVideoClipVisionEncode`、`CLIPVisionLoader`、`SeCModelLoader`、`OnnxDetectionModelLoader`、`DrawViTPose`、`PoseAndFaceDetection`、`DrawMaskOnImage`、`MaskToImage`、`InvertMask`、`VHS_VideoInfo`、`ImageResizeKJv2`、`VHS_LoadVideo`、`LoadImage`、`PointsEditor`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
