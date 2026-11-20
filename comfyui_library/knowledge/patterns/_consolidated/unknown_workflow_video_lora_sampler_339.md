---
name: unknown_workflow_video_lora_sampler_339
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.577
common_nodes: [CLIPVisionLoader, GetNode, ImageConcatMulti, ImageFromBatch, ImageResizeKJv2, Int, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetLoRAs, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [数字人/数字人/SeC整合版：1.WanAnimate+Sec 一键换头_1985857562799218689.json, 数字人/数字人/姿势迁移V2_2002454631311634433.json, 视频生成/图生视频/24号特工：快速版舞蹈视频人物替换+节约RH币+节约时间+性价比拉满_2030543201047678977.json, 视频生成/图生视频/KJ版【 主体替换 + 姿势参考 】 Wan2.2+Animate_1970037279043579906.json, 视频生成/图生视频/Nuash版-Wan Animation 数字人+视频人物替换_1969961202665332737.json, 视频生成/图生视频/Wan-Animate 完美复刻官方效果-调参升级版_1969938728464621569.json, 视频生成/图生视频/主体替换调参版本_转身_1980181283542306818.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_339

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（数字人/数字人/SeC整合版：1.WanAnimate+Sec 一键换头_1985857562799218689.json、数字人/数字人/姿势迁移V2_2002454631311634433.json、视频生成/图生视频/24号特工：快速版舞蹈视频人物替换+节约RH币+节约时间+性价比拉满_2030543201047678977.json、视频生成/图生视频/KJ版【 主体替换 + 姿势参考 】 Wan2.2+Animate_1970037279043579906.json、视频生成/图生视频/Nuash版-Wan Animation 数字人+视频人物替换_1969961202665332737.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：58%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPVisionLoader`
- `GetNode`
- `ImageConcatMulti`
- `ImageFromBatch`
- `ImageResizeKJv2`
- `Int`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
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
- `WanVideoSetLoRAs`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `BlockifyMask` —— 6/7 个有
- `DrawMaskOnImage` —— 6/7 个有
- `ImpactInt` —— 6/7 个有
- `MathExpression|pysssss` —— 6/7 个有
- `PreviewImage` —— 6/7 个有
- `WanVideoSetBlockSwap` —— 6/7 个有
- `WanVideoTextEncodeCached` —— 6/7 个有
- `GrowMask` —— 5/7 个有
- `OnnxDetectionModelLoader` —— 5/7 个有
- `PoseAndFaceDetection` —— 5/7 个有
- `Textbox` —— 5/7 个有
- `DWPreprocessor` —— 4/7 个有
- `FaceMaskFromPoseKeypoints` —— 4/7 个有
- `ImageCropByMaskAndResize` —— 4/7 个有
- `DownloadAndLoadSAM2Model` —— 3/7 个有
- `DrawViTPose` —— 3/7 个有
- `LayerMask: LoadSegmentAnythingModels` —— 3/7 个有
- `LayerMask: SegmentAnythingUltra V3` —— 3/7 个有
- `Sam2Segmentation` —— 3/7 个有
- `VHS_VideoInfo` —— 3/7 个有
- `easy showAnything` —— 3/7 个有
- `BBoxesToSAM2` —— 2/7 个有
- `CR String To Number` —— 2/7 个有
- `DownloadAndLoadQwenModel` —— 2/7 个有
- `GetImagesFromBatchIndexed` —— 2/7 个有
- `ImpactSwitch` —— 2/7 个有
- `LayerMask: SAM2VideoUltra` —— 2/7 个有
- `QwenVLDetection` —— 2/7 个有
- `TextBoxNode_UTK` —— 2/7 个有
- `WanVideoLoraSelect` —— 2/7 个有
- `CLIPLoader` —— 1/7 个有
- `CLIPTextEncode` —— 1/7 个有
- `CR Prompt Text` —— 1/7 个有
- `Fast Groups Bypasser (rgthree)` —— 1/7 个有
- `GetImageSizeAndCount` —— 1/7 个有
- `GrowMaskWithBlur` —— 1/7 个有
- `INTConstant` —— 1/7 个有
- `Image Stitch` —— 1/7 个有
- `MaskToImage` —— 1/7 个有
- `SeCModelLoader` —— 1/7 个有
- `SeCVideoSegmentation` —— 1/7 个有
- `WanVideoTextEmbedBridge` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
