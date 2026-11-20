---
key: 平台全量/wan2.2动作迁移-人物动作迁移v1_2061979901028298753.json
name: wan2.2动作迁移-人物动作迁移v1_2061979901028298753
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/wan2.2动作迁移-人物动作迁移v1_2061979901028298753.json
hash: 1d11ddae94b6890e
coverage: 0.546512
learned_at: 2026-11-14 01:19:44
nodes: [JWInteger, ImageFromBatch+, GetNode, DrawMaskOnImage, easy cleanGpuUsed, SetNode, PoseAndFaceDetection, DrawViTPose, SetNode, easy cleanGpuUsed, SetNode, BlockifyMask, VHS_VideoCombine, GrowMask, InvertMask, MaskToImage, SetNode, GetImageSizeAndCount, VHS_VideoCombine, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, WanVideoClipVisionEncode, easy cleanGpuUsed, WanVideoDecode, GetImageSizeAndCount, easy cleanGpuUsed, GetNode, VHS_VideoCombine, VHS_VideoCombine, SetNode, OnnxDetectionModelLoader, GetNode, GetNode, WanVideoSetLoRAs, SetNode, CLIPVisionLoader, WanVideoSetBlockSwap, VHS_VideoInfo, SetNode, Note, INTConstant, PreviewImage, SeCVideoSegmentation, WanVideoBlockSwap, SeCModelLoader, WanVideoModelLoader, WanVideoTextEncodeCached, CreateVideo, GetNode, SaveVideo, GetNode, WanVideoLoraSelectMulti, WanVideoVAELoader, LoadImage, VHS_LoadVideo, GetNode, ImageResizeKJv2, SetNode, GetNode, PreviewImage, Note, INTConstant, INTConstant, PointsEditor, GetNode, SetNode, ImageConcanate, WanVideoSampler, WanVideoAnimateEmbeds, CR Text, LayerUtility: ImageBlend, GetNode, SetNode]
patterns: []
missing: []
---

# 平台全量/wan2.2动作迁移-人物动作迁移v1_2061979901028298753.json

> 来源文件 `comfyui_library/workflows/平台全量/wan2.2动作迁移-人物动作迁移v1_2061979901028298753.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（86 个）：
- `JWInteger`
- `ImageFromBatch+`
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
- `GrowMask`
- `InvertMask`
- `MaskToImage`
- `SetNode`
- `GetImageSizeAndCount`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoClipVisionEncode`
- `easy cleanGpuUsed`
- `WanVideoDecode`
- `GetImageSizeAndCount`
- `easy cleanGpuUsed`
- `GetNode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `SetNode`
- `OnnxDetectionModelLoader`
- `GetNode`
- `GetNode`
- `WanVideoSetLoRAs`
- `SetNode`
- `CLIPVisionLoader`
- `WanVideoSetBlockSwap`
- `VHS_VideoInfo`
- `SetNode`
- `Note`
- `INTConstant`
- `PreviewImage`
- `SeCVideoSegmentation`
- `WanVideoBlockSwap`
- `SeCModelLoader`
- `WanVideoModelLoader`
- `WanVideoTextEncodeCached`
- `CreateVideo`
- `GetNode`
- `SaveVideo`
- `GetNode`
- `WanVideoLoraSelectMulti`
- `WanVideoVAELoader`
- `LoadImage`
- `VHS_LoadVideo`
- `GetNode`
- `ImageResizeKJv2`
- `SetNode`
- `GetNode`
- `PreviewImage`
- `Note`
- `INTConstant`
- `INTConstant`
- `PointsEditor`
- `GetNode`
- `SetNode`
- `ImageConcanate`
- `WanVideoSampler` ★核心
- `WanVideoAnimateEmbeds`
- `CR Text`
- `LayerUtility: ImageBlend`
- `GetNode`
- `SetNode`

## 知识

覆盖率 **55%**（47/86）

**有卡**：`JWInteger`、`ImageFromBatch+`、`DrawMaskOnImage`、`easy cleanGpuUsed`、`PoseAndFaceDetection`、`DrawViTPose`、`BlockifyMask`、`VHS_VideoCombine`、`GrowMask`、`InvertMask`、`MaskToImage`、`GetImageSizeAndCount`、`WanVideoClipVisionEncode`、`WanVideoDecode`、`OnnxDetectionModelLoader`、`WanVideoSetLoRAs`、`CLIPVisionLoader`、`WanVideoSetBlockSwap`、`VHS_VideoInfo`、`INTConstant`、`SeCVideoSegmentation`、`WanVideoBlockSwap`、`SeCModelLoader`、`WanVideoModelLoader`、`WanVideoTextEncodeCached`、`CreateVideo`、`SaveVideo`、`WanVideoLoraSelectMulti`、`WanVideoVAELoader`、`LoadImage`、`VHS_LoadVideo`、`ImageResizeKJv2`、`PointsEditor`、`ImageConcanate`、`WanVideoSampler`、`WanVideoAnimateEmbeds`、`CR Text`、`LayerUtility: ImageBlend`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVAELoader、WanVideoLoraSelectMulti、WanVideoSetLoRAs
