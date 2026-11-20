---
name: unknown_workflow_video_lora_sampler_593
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.4358
common_nodes: [BlockifyMask, CLIPVisionLoader, DrawMaskOnImage, GetNode, INTConstant, LoadImage, OnnxDetectionModelLoader, PoseAndFaceDetection, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [数字人/数字人/Wan2.2-Animate【换人迁移】kj遮罩-高质+快速+细节_1990762965668405249.json, 数字人/数字人/WanAnimate-KJ流遮罩自动获取版_1970211323026022401.json, 数字人/数字人/啊不不2.0_1993514131133235201.json, 数字人/数字人/数字人抠图测试（请无视、别浪费大家的积分）_1993671742266818561.json, 视频生成/图生视频/自己玩_1995102886726184962.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_593

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（数字人/数字人/Wan2.2-Animate【换人迁移】kj遮罩-高质+快速+细节_1990762965668405249.json、数字人/数字人/WanAnimate-KJ流遮罩自动获取版_1970211323026022401.json、数字人/数字人/啊不不2.0_1993514131133235201.json、数字人/数字人/数字人抠图测试（请无视、别浪费大家的积分）_1993671742266818561.json、视频生成/图生视频/自己玩_1995102886726184962.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：44%

## 共有节点

全部 5 个 workflow 都包含：
- `BlockifyMask`
- `CLIPVisionLoader`
- `DrawMaskOnImage`
- `GetNode`
- `INTConstant`
- `LoadImage`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
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

**可变部分**（部分 workflow 才有）：
- `DownloadAndLoadGIMMVFIModel` —— 4/5 个有
- `DrawViTPose` —— 4/5 个有
- `Fast Groups Bypasser (rgthree)` —— 4/5 个有
- `GIMMVFI_interpolate` —— 4/5 个有
- `GrowMask` —— 4/5 个有
- `ImageConcatMulti` —— 4/5 个有
- `PreviewImage` —— 4/5 个有
- `PrimitiveStringMultiline` —— 4/5 个有
- `GrowMaskWithBlur` —— 3/5 个有
- `ImageRemoveBackground+` —— 3/5 个有
- `PrimitiveInt` —— 3/5 个有
- `RemBGSession+` —— 3/5 个有
- `easy cleanGpuUsed` —— 3/5 个有
- `easy clearCacheAll` —— 3/5 个有
- `CLIPLoader` —— 2/5 个有
- `DownloadAndLoadSAM2Model` —— 2/5 个有
- `GetImageSizeAndCount` —— 2/5 个有
- `ImageBlend` —— 2/5 个有
- `ImageFromBatch` —— 2/5 个有
- `ImageResizeKJv2` —— 2/5 个有
- `ImageScaleBy` —— 2/5 个有
- `PlaySound|pysssss` —— 2/5 个有
- `PointsEditor` —— 2/5 个有
- `PrimitiveFloat` —— 2/5 个有
- `Sam2Segmentation` —— 2/5 个有
- `SeCModelLoader` —— 2/5 个有
- `SeCVideoSegmentation` —— 2/5 个有
- `SeedVR2` —— 2/5 个有
- `SeedVR2BlockSwap` —— 2/5 个有
- `SeedVR2ExtraArgs` —— 2/5 个有
- `easy seed` —— 2/5 个有
- `Any Switch (rgthree)` —— 1/5 个有
- `Bookmark (rgthree)` —— 1/5 个有
- `CR Image Input Switch (4 way)` —— 1/5 个有
- `Float` —— 1/5 个有
- `GroundingDinoModelLoader (segment anything)` —— 1/5 个有
- `ImpactSwitch` —— 1/5 个有
- `PreviewAny` —— 1/5 个有
- `RMBG` —— 1/5 个有
- `ResizeMask` —— 1/5 个有
- `SDPoseOODLoader` —— 1/5 个有
- `SDPoseOODProcessor` —— 1/5 个有
- `Seed (rgthree)` —— 1/5 个有
- `YOLOModelLoader` —— 1/5 个有
- `easy sam3ModelLoader` —— 1/5 个有
- `easy sam3VideoSegmentation` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
