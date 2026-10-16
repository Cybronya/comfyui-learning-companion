---
key: 视频生成/图生视频/Wan2.2  Wan22 角色替换   动作迁移  二创首选_2042132086164819970.json
name: Wan2.2  Wan22 角色替换   动作迁移  二创首选_2042132086164819970.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2042132086164819970.json
hash: e80d6f38512e05ca
coverage: 0.567901
learned_at: 2026-10-15 22:36:25
nodes: [GetNode, Reroute, INTConstant, INTConstant, INTConstant, SetNode, SetNode, WanVideoModelLoader, WanVideoLoraSelectMulti, GetNode, OnnxDetectionModelLoader, SeCVideoSegmentation, InvertMask, MaskToImage, Reroute, LayerUtility: ImageBlend, SetNode, GetNode, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, GrowMask, BlockifyMask, SetNode, GetNode, DrawMaskOnImage, easy cleanGpuUsed, SetNode, SetNode, Reroute, SeCModelLoader, SetNode, PoseAndFaceDetection, GetImageSizeAndCount, SetNode, ImageResizeKJv2, JWInteger, SetNode, GetNode, CLIPVisionLoader, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, WanVideoClipVisionEncode, CR Text, WanVideoAnimateEmbeds, WanVideoDecode, GetNode, GetNode, VHS_VideoCombine, GetImageSizeAndCount, WanVideoTextEncodeCached, easy cleanGpuUsed, ImageConcanate, easy cleanGpuUsed, WanVideoSampler, WanVideoVAELoader, SetNode, WanVideoBlockSwap, WanVideoSetLoRAs, WanVideoSetBlockSwap, SetNode, VHS_VideoInfo, Reroute, easy cleanGpuUsed, SetNode, DrawViTPose, ImageFromBatch+, PreviewImage, Note, LoadImage, VHS_LoadVideo, PointsEditor, SetNode, PreviewImage]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2  Wan22 角色替换   动作迁移  二创首选_2042132086164819970.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2042132086164819970.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（81 个）：
- `GetNode`
- `Reroute`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `SetNode`
- `SetNode`
- `WanVideoModelLoader`
- `WanVideoLoraSelectMulti`
- `GetNode`
- `OnnxDetectionModelLoader`
- `SeCVideoSegmentation`
- `InvertMask`
- `MaskToImage`
- `Reroute`
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
- `DrawMaskOnImage`
- `easy cleanGpuUsed`
- `SetNode`
- `SetNode`
- `Reroute`
- `SeCModelLoader`
- `SetNode`
- `PoseAndFaceDetection`
- `GetImageSizeAndCount`
- `SetNode`
- `ImageResizeKJv2`
- `JWInteger`
- `SetNode`
- `GetNode`
- `CLIPVisionLoader`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoClipVisionEncode`
- `CR Text`
- `WanVideoAnimateEmbeds`
- `WanVideoDecode`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `GetImageSizeAndCount`
- `WanVideoTextEncodeCached`
- `easy cleanGpuUsed`
- `ImageConcanate`
- `easy cleanGpuUsed`
- `WanVideoSampler` ★核心
- `WanVideoVAELoader`
- `SetNode`
- `WanVideoBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `SetNode`
- `VHS_VideoInfo`
- `Reroute`
- `easy cleanGpuUsed`
- `SetNode`
- `DrawViTPose`
- `ImageFromBatch+`
- `PreviewImage`
- `Note`
- `LoadImage`
- `VHS_LoadVideo`
- `PointsEditor`
- `SetNode`
- `PreviewImage`

## 知识

覆盖率 **57%**（46/81）

**有卡**：`INTConstant`、`WanVideoModelLoader`、`WanVideoLoraSelectMulti`、`OnnxDetectionModelLoader`、`SeCVideoSegmentation`、`InvertMask`、`MaskToImage`、`LayerUtility: ImageBlend`、`VHS_VideoCombine`、`GrowMask`、`BlockifyMask`、`DrawMaskOnImage`、`easy cleanGpuUsed`、`SeCModelLoader`、`PoseAndFaceDetection`、`GetImageSizeAndCount`、`ImageResizeKJv2`、`JWInteger`、`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`CR Text`、`WanVideoAnimateEmbeds`、`WanVideoDecode`、`WanVideoTextEncodeCached`、`ImageConcanate`、`WanVideoSampler`、`WanVideoVAELoader`、`WanVideoBlockSwap`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`VHS_VideoInfo`、`DrawViTPose`、`ImageFromBatch+`、`LoadImage`、`VHS_LoadVideo`、`PointsEditor`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
