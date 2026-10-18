---
key: 视频生成/图生视频/人物替换    角色替换   二创首选  Wan2.2 wan22_2061714173691785218.json
name: 人物替换    角色替换   二创首选  Wan2.2 wan22_2061714173691785218.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/人物替换    角色替换   二创首选  Wan2.2 wan22_2061714173691785218.json
hash: 55a185afda3e287a
coverage: 0.560976
learned_at: 2026-10-15 22:38:55
nodes: [WanVideoLoraSelectMulti, GetNode, GetNode, VHS_VideoCombine, WanVideoSetLoRAs, WanVideoVAELoader, INTConstant, INTConstant, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, INTConstant, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, WanVideoTextEncodeCached, CR Text, WanVideoClipVisionEncode, easy cleanGpuUsed, WanVideoAnimateEmbeds, WanVideoSampler, WanVideoDecode, GetImageSizeAndCount, ImageConcanate, easy cleanGpuUsed, SetNode, CLIPVisionLoader, GetNode, WanVideoSetBlockSwap, WanVideoBlockSwap, VHS_LoadVideo, ImageResizeKJv2, GetNode, GetNode, PreviewImage, LoadImage, GetNode, GetNode, SetNode, PreviewImage, Note, PointsEditor, JWInteger, ImageFromBatch+, WanVideoModelLoader, SetNode, SetNode, SeCVideoSegmentation, OnnxDetectionModelLoader, SeCModelLoader, GrowMask, BlockifyMask, SetNode, DrawMaskOnImage, GetNode, GetNode, VHS_VideoInfo, SetNode, InvertMask, MaskToImage, LayerUtility: ImageBlend, SetNode, GetImageSizeAndCount, VHS_VideoCombine, SetNode, easy cleanGpuUsed, VHS_VideoCombine, PoseAndFaceDetection, DrawViTPose, easy cleanGpuUsed, SetNode, SetNode, VHS_VideoCombine, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/人物替换    角色替换   二创首选  Wan2.2 wan22_2061714173691785218.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2061714173691785218.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（82 个）：
- `WanVideoLoraSelectMulti`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `WanVideoSetLoRAs`
- `WanVideoVAELoader`
- `INTConstant`
- `INTConstant`
- `GetNode`
- `GetNode`
- `GetNode`
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
- `WanVideoSetBlockSwap`
- `WanVideoBlockSwap`
- `VHS_LoadVideo`
- `ImageResizeKJv2`
- `GetNode`
- `GetNode`
- `PreviewImage`
- `LoadImage`
- `GetNode`
- `GetNode`
- `SetNode`
- `PreviewImage`
- `Note`
- `PointsEditor`
- `JWInteger`
- `ImageFromBatch+`
- `WanVideoModelLoader`
- `SetNode`
- `SetNode`
- `SeCVideoSegmentation`
- `OnnxDetectionModelLoader`
- `SeCModelLoader`
- `GrowMask`
- `BlockifyMask`
- `SetNode`
- `DrawMaskOnImage`
- `GetNode`
- `GetNode`
- `VHS_VideoInfo`
- `SetNode`
- `InvertMask`
- `MaskToImage`
- `LayerUtility: ImageBlend`
- `SetNode`
- `GetImageSizeAndCount`
- `VHS_VideoCombine`
- `SetNode`
- `easy cleanGpuUsed`
- `VHS_VideoCombine`
- `PoseAndFaceDetection`
- `DrawViTPose`
- `easy cleanGpuUsed`
- `SetNode`
- `SetNode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`

## 知识

覆盖率 **56%**（46/82）

**有卡**：`WanVideoLoraSelectMulti`、`VHS_VideoCombine`、`WanVideoSetLoRAs`、`WanVideoVAELoader`、`INTConstant`、`WanVideoTextEncodeCached`、`CR Text`、`WanVideoClipVisionEncode`、`easy cleanGpuUsed`、`WanVideoAnimateEmbeds`、`WanVideoSampler`、`WanVideoDecode`、`GetImageSizeAndCount`、`ImageConcanate`、`CLIPVisionLoader`、`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`VHS_LoadVideo`、`ImageResizeKJv2`、`LoadImage`、`PointsEditor`、`JWInteger`、`ImageFromBatch+`、`WanVideoModelLoader`、`SeCVideoSegmentation`、`OnnxDetectionModelLoader`、`SeCModelLoader`、`GrowMask`、`BlockifyMask`、`DrawMaskOnImage`、`VHS_VideoInfo`、`InvertMask`、`MaskToImage`、`LayerUtility: ImageBlend`、`PoseAndFaceDetection`、`DrawViTPose`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
