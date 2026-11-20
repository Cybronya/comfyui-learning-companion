---
name: unknown_workflow_video_lora_sampler_815
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.623333
common_nodes: [BlockifyMask, CLIPVisionLoader, DrawMaskOnImage, GetNode, GrowMask, ImageResizeKJv2, LoadImage, PreviewImage, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVAELoader, easy sam3GetObjectMask, easy sam3ModelLoader, easy sam3VideoSegmentation, easy sam3Visualization]
problems: []
missing: []
members: [平台全量/WanAnimateV2-恶搞角色替换_多人替换_2041138122003587074.json, 视频生成/图生视频/SAM3游戏人物替换二创_2034955430325129218.json, 视频生成/图生视频/WanAnimateV2-恶搞角色替换_单人_2040378422123307009.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_815

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/WanAnimateV2-恶搞角色替换_多人替换_2041138122003587074.json、视频生成/图生视频/SAM3游戏人物替换二创_2034955430325129218.json、视频生成/图生视频/WanAnimateV2-恶搞角色替换_单人_2040378422123307009.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：62%

## 共有节点

全部 3 个 workflow 都包含：
- `BlockifyMask`
- `CLIPVisionLoader`
- `DrawMaskOnImage`
- `GetNode`
- `GrowMask`
- `ImageResizeKJv2`
- `LoadImage`
- `PreviewImage`
- `SetNode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoAnimateEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `easy sam3GetObjectMask`
- `easy sam3ModelLoader`
- `easy sam3VideoSegmentation`
- `easy sam3Visualization`

**可变部分**（部分 workflow 才有）：
- `DWPreprocessor` —— 2/3 个有
- `FL_RIFE` —— 2/3 个有
- `FaceMaskFromPoseKeypoints` —— 2/3 个有
- `INTConstant` —— 2/3 个有
- `ImageBlend` —— 2/3 个有
- `ImageCropByMaskAndResize` —— 2/3 个有
- `ImageFromBatch` —— 2/3 个有
- `LayerMask: MaskPreview` —— 2/3 个有
- `PointsEditor` —— 2/3 个有
- `Primitive integer [Crystools]` —— 2/3 个有
- `SimpleMath+` —— 2/3 个有
- `TTResolutionSelector` —— 2/3 个有
- `easy int` —— 2/3 个有
- `CR Text` —— 1/3 个有
- `DownloadAndLoadSAM2Model` —— 1/3 个有
- `DrawViTPose` —— 1/3 个有
- `ImageConcatMulti` —— 1/3 个有
- `Int` —— 1/3 个有
- `MaskToImage` —— 1/3 个有
- `OnnxDetectionModelLoader` —— 1/3 个有
- `PoseAndFaceDetection` —— 1/3 个有
- `RHHiddenNodes` —— 1/3 个有
- `RH_Nano_Banana2_Gemini31Flash` —— 1/3 个有
- `Sam2Segmentation` —— 1/3 个有
- `SaveImage` —— 1/3 个有
- `Switch any [Crystools]` —— 1/3 个有
- `VHS_VideoInfoLoaded` —— 1/3 个有
- `easy cleanGpuUsed` —— 1/3 个有
- `easy imageSizeBySide` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
