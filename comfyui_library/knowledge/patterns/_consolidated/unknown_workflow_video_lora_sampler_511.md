---
name: unknown_workflow_video_lora_sampler_511
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.75475
common_nodes: [BBoxesToSAM2, CLIPVisionLoader, CM_IntToFloat, CR Text, DownloadAndLoadQwenModel, DrawViTPose, GetImageSizeAndCount, GetNode, ImageConcatMulti, ImageFromBatch, ImageResizeKJv2, Int, LayerMask: SAM2Ultra, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM V2, LoadImage, MaskPreview+, OnnxDetectionModelLoader, PoseAndFaceDetection, QwenVLDetection, RHHiddenNodes, SeCModelLoader, SeCVideoSegmentation, SetNode, SimpleMath+, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1989226857599995905.json, 视频生成/图生视频/2002723614807998465.json, 视频生成/图生视频/1988762483311652866.json, 视频生成/图生视频/2001920042348494850.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_511

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/1989226857599995905.json、视频生成/图生视频/2002723614807998465.json、视频生成/图生视频/1988762483311652866.json、视频生成/图生视频/2001920042348494850.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：75%

## 共有节点

全部 4 个 workflow 都包含：
- `BBoxesToSAM2`
- `CLIPVisionLoader`
- `CM_IntToFloat`
- `CR Text`
- `DownloadAndLoadQwenModel`
- `DrawViTPose`
- `GetImageSizeAndCount`
- `GetNode`
- `ImageConcatMulti`
- `ImageFromBatch`
- `ImageResizeKJv2`
- `Int`
- `LayerMask: SAM2Ultra`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `MaskPreview+`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `QwenVLDetection`
- `RHHiddenNodes`
- `SeCModelLoader`
- `SeCVideoSegmentation`
- `SetNode`
- `SimpleMath+`
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
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `BlockifyMask` —— 3/4 个有
- `DrawMaskOnImage` —— 3/4 个有
- `GrowMask` —— 3/4 个有
- `easy cleanGpuUsed` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
