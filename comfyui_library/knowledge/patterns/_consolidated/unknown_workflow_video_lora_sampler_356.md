---
name: unknown_workflow_video_lora_sampler_356
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.572875
common_nodes: [CLIPVisionLoader, DrawViTPose, GetNode, ImageConcatMulti, ImageResizeKJv2, LoadImage, OnnxDetectionModelLoader, PoseAndFaceDetection, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetLoRAs, WanVideoVAELoader]
problems: []
missing: []
members: [平台全量/SeC整合版：2.WanAnimate+Sec 一键换主体_1985858678060457986.json, 平台全量/SeC整合版：4.WanAnimate 主体替换(自动)2.0_1986448672231718914.json, 平台全量/SeC整合版：5.WanAnimate 姿势参考2.0_1986448792906039298.json, 平台全量/（KJ版）姿势参考WanAnimate V2_1974868952310484993.json, 数字人/数字人/SeC整合版：1.WanAnimate+Sec 一键换头_1985857562799218689.json, 数字人/数字人/姿势迁移V2_2002454631311634433.json, 视频生成/图生视频/24号特工：快速版舞蹈视频人物替换+节约RH币+节约时间+性价比拉满_2030543201047678977.json, 视频生成/图生视频/Wan-Animate_V2-动作迁移自动版_1975030930718986242.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_356

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（平台全量/SeC整合版：2.WanAnimate+Sec 一键换主体_1985858678060457986.json、平台全量/SeC整合版：4.WanAnimate 主体替换(自动)2.0_1986448672231718914.json、平台全量/SeC整合版：5.WanAnimate 姿势参考2.0_1986448792906039298.json、平台全量/（KJ版）姿势参考WanAnimate V2_1974868952310484993.json、数字人/数字人/SeC整合版：1.WanAnimate+Sec 一键换头_1985857562799218689.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：57%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPVisionLoader`
- `DrawViTPose`
- `GetNode`
- `ImageConcatMulti`
- `ImageResizeKJv2`
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
- `WanVideoSetLoRAs`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageFromBatch` —— 7/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 7/8 个有
- `WanVideoTorchCompileSettings` —— 7/8 个有
- `ImpactInt` —— 6/8 个有
- `Int` —— 6/8 个有
- `PreviewImage` —— 6/8 个有
- `WanVideoSetBlockSwap` —— 6/8 个有
- `BlockifyMask` —— 5/8 个有
- `DrawMaskOnImage` —— 5/8 个有
- `CLIPLoader` —— 4/8 个有
- `CLIPTextEncode` —— 4/8 个有
- `GrowMaskWithBlur` —— 4/8 个有
- `MathExpression|pysssss` —— 4/8 个有
- `Textbox` —— 4/8 个有
- `WanVideoTextEmbedBridge` —— 4/8 个有
- `WanVideoTextEncodeCached` —— 4/8 个有
- `DownloadAndLoadSAM2Model` —— 3/8 个有
- `GetImageSizeAndCount` —— 3/8 个有
- `Sam2Segmentation` —— 3/8 个有
- `GrowMask` —— 2/8 个有
- `INTConstant` —— 2/8 个有
- `LayerMask: LoadSegmentAnythingModels` —— 2/8 个有
- `LayerMask: SegmentAnythingUltra V3` —— 2/8 个有
- `MaskToImage` —— 2/8 个有
- `SeCModelLoader` —— 2/8 个有
- `SeCVideoSegmentation` —— 2/8 个有
- `Text` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
