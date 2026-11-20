---
name: unknown_workflow_video_lora_sampler_662
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.421
common_nodes: [BlockifyMask, CLIPVisionLoader, DrawMaskOnImage, Fast Groups Bypasser (rgthree), GetNode, GrowMaskWithBlur, INTConstant, LoadImage, OnnxDetectionModelLoader, PoseAndFaceDetection, PrimitiveStringMultiline, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVAELoader, easy cleanGpuUsed, easy clearCacheAll]
problems: []
missing: []
members: [数字人/数字人/啊不不2.0_1993514131133235201.json, 数字人/数字人/数字人抠图测试（请无视、别浪费大家的积分）_1993671742266818561.json, 视频生成/图生视频/自己玩_1995102886726184962.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_662

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（数字人/数字人/啊不不2.0_1993514131133235201.json、数字人/数字人/数字人抠图测试（请无视、别浪费大家的积分）_1993671742266818561.json、视频生成/图生视频/自己玩_1995102886726184962.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：42%

## 共有节点

全部 3 个 workflow 都包含：
- `BlockifyMask`
- `CLIPVisionLoader`
- `DrawMaskOnImage`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `GrowMaskWithBlur`
- `INTConstant`
- `LoadImage`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `PrimitiveStringMultiline`
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
- `easy cleanGpuUsed`
- `easy clearCacheAll`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 2/3 个有
- `DownloadAndLoadGIMMVFIModel` —— 2/3 个有
- `DrawViTPose` —— 2/3 个有
- `GIMMVFI_interpolate` —— 2/3 个有
- `GrowMask` —— 2/3 个有
- `ImageConcatMulti` —— 2/3 个有
- `ImageFromBatch` —— 2/3 个有
- `ImageRemoveBackground+` —— 2/3 个有
- `ImageScaleBy` —— 2/3 个有
- `PlaySound|pysssss` —— 2/3 个有
- `PointsEditor` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `PrimitiveInt` —— 2/3 个有
- `RemBGSession+` —— 2/3 个有
- `SeCModelLoader` —— 2/3 个有
- `SeCVideoSegmentation` —— 2/3 个有
- `SeedVR2` —— 2/3 个有
- `SeedVR2BlockSwap` —— 2/3 个有
- `SeedVR2ExtraArgs` —— 2/3 个有
- `easy seed` —— 2/3 个有
- `Any Switch (rgthree)` —— 1/3 个有
- `Bookmark (rgthree)` —— 1/3 个有
- `CR Image Input Switch (4 way)` —— 1/3 个有
- `DownloadAndLoadSAM2Model` —— 1/3 个有
- `Float` —— 1/3 个有
- `GroundingDinoModelLoader (segment anything)` —— 1/3 个有
- `ImpactSwitch` —— 1/3 个有
- `PrimitiveFloat` —— 1/3 个有
- `RMBG` —— 1/3 个有
- `ResizeMask` —— 1/3 个有
- `SDPoseOODLoader` —— 1/3 个有
- `SDPoseOODProcessor` —— 1/3 个有
- `Sam2Segmentation` —— 1/3 个有
- `YOLOModelLoader` —— 1/3 个有
- `easy sam3ModelLoader` —— 1/3 个有
- `easy sam3VideoSegmentation` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
