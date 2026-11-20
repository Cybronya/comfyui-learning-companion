---
name: unknown_workflow_video_lora_sampler_160
type: Unknown Workflow
frequency: 12
level: moderate
coverage: 0.626
common_nodes: [CLIPVisionLoader, DWPreprocessor, FaceMaskFromPoseKeypoints, ImageCropByMaskAndResize, ImageResizeKJv2, LoadImage, PixelPerfectResolution, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/02角色迁移更新+全节点注释_2055549996304478210.json, 视频生成/图生视频/Animate Wan2.2 动作迁移2_1992566625708691457.json, 视频生成/图生视频/Animate wan2.2   抖音快手爆火美女跳舞_1986294172028207106.json, 视频生成/图生视频/Best_Wan2.2_图片跳舞指定动作_1973849425091104769.json, 视频生成/图生视频/WAN2.2Animate美女图片跳舞工作流【动作，表情迁移】_1971382412112510978.json, 视频生成/图生视频/Wan  图生视频 人物角色迁移 动作模仿+唱歌跳舞+舞剑   动作迁移 人物替换_2046059624503185409.json, 视频生成/图生视频/Wan Animate2.2动作迁移Move加速版V1_1969195120677580801.json, 视频生成/图生视频/Wan Animate2.2动作迁移_1969366584278085634.json, 视频生成/图生视频/Wan2.2 Animate 视频换人 视频人物替换_2018529838486790146.json, 视频生成/图生视频/Wan2.2-Animate-视频换脸+换装+动作模仿+迁移跳舞_1993696432154755073.json, 视频生成/图生视频/WanAnimate_去油版_1969228156349673474.json, 视频生成/图生视频/wan annimateGGUF_1970833810306801666.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_160

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（视频生成/图生视频/02角色迁移更新+全节点注释_2055549996304478210.json、视频生成/图生视频/Animate Wan2.2 动作迁移2_1992566625708691457.json、视频生成/图生视频/Animate wan2.2   抖音快手爆火美女跳舞_1986294172028207106.json、视频生成/图生视频/Best_Wan2.2_图片跳舞指定动作_1973849425091104769.json、视频生成/图生视频/WAN2.2Animate美女图片跳舞工作流【动作，表情迁移】_1971382412112510978.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：63%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPVisionLoader`
- `DWPreprocessor`
- `FaceMaskFromPoseKeypoints`
- `ImageCropByMaskAndResize`
- `ImageResizeKJv2`
- `LoadImage`
- `PixelPerfectResolution`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoAnimateEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 11/12 个有
- `SetNode` —— 11/12 个有
- `JWInteger` —— 10/12 个有
- `WanVideoLoraSelectMulti` —— 10/12 个有
- `ImageConcatMulti` —— 8/12 个有
- `LayerUtility: PurgeVRAM` —— 7/12 个有
- `easy cleanGpuUsed` —— 7/12 个有
- `BlockifyMask` —— 6/12 个有
- `DrawMaskOnImage` —— 6/12 个有
- `GrowMask` —— 6/12 个有
- `VHS_VideoInfo` —— 6/12 个有
- `GetImageSizeAndCount` —— 4/12 个有
- `LayerMask: SegformerB2ClothesUltra` —— 4/12 个有
- `SimpleMath+` —— 4/12 个有
- `WanVideoTorchCompileSettings` —— 4/12 个有
- `Int` —— 3/12 个有
- `PreviewImage` —— 3/12 个有
- `Text` —— 3/12 个有
- `Anything Everywhere` —— 2/12 个有
- `LayerMask: LoadSegmentAnythingModels` —— 2/12 个有
- `LayerMask: SegmentAnythingUltra V3` —— 2/12 个有
- `PrimitiveInt` —— 2/12 个有
- `WanVideoLoraSelect` —— 2/12 个有
- `ttN float` —— 2/12 个有
- `CM_IntToFloat` —— 1/12 个有
- `ImageFromBatch` —— 1/12 个有
- `ImageFromBatch+` —— 1/12 个有
- `Label (rgthree)` —— 1/12 个有
- `LayerUtility: ImageScaleByAspectRatio` —— 1/12 个有
- `MathExpression|pysssss` —— 1/12 个有
- `Textbox` —— 1/12 个有
- `WanVideoContextOptions` —— 1/12 个有
- `easy showAnything` —— 1/12 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
