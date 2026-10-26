---
name: unknown_workflow_video_lora_sampler_590
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.92225
common_nodes: [CreateCFGScheduleFloatList, GetImageSizeAndCount, INTConstant, ImageConcatMulti, ImageResizeKJv2, LoadImage, LoadWanVideoT5TextEncoder, SimpleMath+, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/wan2.2官方 VACE 视频人物替换电商版3.0_1968972312815026177.json, 视频生成/图生视频/极简——KJ版 wan2.2模型VACE 视频人物替换_1968955207906385921.json, 视频生成/文生视频/Wan2_2_Fun_VACE_画遮罩替换视频人物工作流_1968705709867192321.json, 视频生成/文生视频/【AI小兵哥】Wan2_2_Fun_VACE_参考人物进行姿势迁移工作流_1968471614218227713.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_590

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/wan2.2官方 VACE 视频人物替换电商版3.0_1968972312815026177.json、视频生成/图生视频/极简——KJ版 wan2.2模型VACE 视频人物替换_1968955207906385921.json、视频生成/文生视频/Wan2_2_Fun_VACE_画遮罩替换视频人物工作流_1968705709867192321.json、视频生成/文生视频/【AI小兵哥】Wan2_2_Fun_VACE_参考人物进行姿势迁移工作流_1968471614218227713.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 4 个 workflow 都包含：
- `CreateCFGScheduleFloatList`
- `GetImageSizeAndCount`
- `INTConstant`
- `ImageConcatMulti`
- `ImageResizeKJv2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `SimpleMath+`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoVACEEncode`
- `WanVideoVACEModelSelect`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `GrowMaskWithBlur` —— 3/4 个有
- `ImageCompositeMasked` —— 3/4 个有
- `LayerMask: SAM2VideoUltra` —— 3/4 个有
- `LayerMask: SegmentAnythingUltra V2` —— 3/4 个有
- `MaskToImage` —— 3/4 个有
- `SolidMask` —— 3/4 个有
- `VHS_VideoInfo` —— 3/4 个有
- `WanVideoTorchCompileSettings` —— 3/4 个有
- `easy imageRemBg` —— 3/4 个有
- `CM_FloatToInt` —— 2/4 个有
- `ImageFromBatch+` —— 2/4 个有
- `ImpactInt` —— 2/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/4 个有
- `LayerUtility: PurgeVRAM` —— 2/4 个有
- `PrimitiveFloat` —— 2/4 个有
- `PrimitiveStringMultiline` —— 2/4 个有
- `easy float` —— 2/4 个有
- `easy mathInt` —— 2/4 个有
- `easy showAnything` —— 2/4 个有
- `CR Text` —— 1/4 个有
- `DWPreprocessor` —— 1/4 个有
- `GetImageRangeFromBatch` —— 1/4 个有
- `PreviewImage` —— 1/4 个有
- `StringToFloatList` —— 1/4 个有
- `WanVideoImageResizeToClosest` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
