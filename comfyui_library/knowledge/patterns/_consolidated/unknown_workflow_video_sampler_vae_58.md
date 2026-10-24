---
name: unknown_workflow_video_sampler_vae_58
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.95425
common_nodes: [INTConstant, ImageResizeKJv2, LoadImage, LoadWanVideoT5TextEncoder, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/All-in-one 视频驱动图片_1965428165915103234.json, 视频生成/图生视频/Wan2.2 Fun Vace视频驱动图片——动作迁移_1966850900927057922.json, 视频生成/图生视频/wan2.2Fun-VACE 动作迁移_1966739330226139137.json, 视频生成/图生视频/wan2.2官方 VACE 人物姿态迁移 KJ流【推荐】_1967834051866406914.json, 视频生成/图生视频/wan2.2官方 VACE 视频人物替换电商版3.0_1968972312815026177.json, 视频生成/图生视频/极简——KJ版 wan2.2模型VACE 视频人物替换_1968955207906385921.json, 视频生成/文生视频/Wan2_2_Fun_VACE_画遮罩替换视频人物工作流_1968705709867192321.json, 视频生成/文生视频/【AI小兵哥】Wan2_2_Fun_VACE_参考人物进行姿势迁移工作流_1968471614218227713.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_58

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/All-in-one 视频驱动图片_1965428165915103234.json、视频生成/图生视频/Wan2.2 Fun Vace视频驱动图片——动作迁移_1966850900927057922.json、视频生成/图生视频/wan2.2Fun-VACE 动作迁移_1966739330226139137.json、视频生成/图生视频/wan2.2官方 VACE 人物姿态迁移 KJ流【推荐】_1967834051866406914.json、视频生成/图生视频/wan2.2官方 VACE 视频人物替换电商版3.0_1968972312815026177.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 8 个 workflow 都包含：
- `INTConstant`
- `ImageResizeKJv2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVACEEncode`
- `WanVideoVACEModelSelect`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `CreateCFGScheduleFloatList` —— 7/8 个有
- `WanVideoLoraSelect` —— 7/8 个有
- `WanVideoSetBlockSwap` —— 7/8 个有
- `WanVideoSetLoRAs` —— 7/8 个有
- `WanVideoTorchCompileSettings` —— 7/8 个有
- `ImageConcatMulti` —— 6/8 个有
- `VHS_VideoInfo` —— 6/8 个有
- `GetImageSizeAndCount` —— 5/8 个有
- `SimpleMath+` —— 5/8 个有
- `DWPreprocessor` —— 4/8 个有
- `GrowMaskWithBlur` —— 3/8 个有
- `ImageCompositeMasked` —— 3/8 个有
- `LayerMask: SAM2VideoUltra` —— 3/8 个有
- `LayerMask: SegmentAnythingUltra V2` —— 3/8 个有
- `MaskToImage` —— 3/8 个有
- `SolidMask` —— 3/8 个有
- `easy imageRemBg` —— 3/8 个有
- `CM_FloatToInt` —— 2/8 个有
- `CR Text` —— 2/8 个有
- `ImageFromBatch+` —— 2/8 个有
- `ImpactInt` —— 2/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/8 个有
- `LayerUtility: PurgeVRAM` —— 2/8 个有
- `PrimitiveFloat` —— 2/8 个有
- `PrimitiveStringMultiline` —— 2/8 个有
- `easy float` —— 2/8 个有
- `easy mathInt` —— 2/8 个有
- `easy showAnything` —— 2/8 个有
- `AIO_Preprocessor` —— 1/8 个有
- `GetImageRangeFromBatch` —— 1/8 个有
- `Note Plus (mtb)` —— 1/8 个有
- `PreviewImage` —— 1/8 个有
- `SaveImage` —— 1/8 个有
- `StringToFloatList` —— 1/8 个有
- `WanVideoImageResizeToClosest` —— 1/8 个有
- `easy int` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
