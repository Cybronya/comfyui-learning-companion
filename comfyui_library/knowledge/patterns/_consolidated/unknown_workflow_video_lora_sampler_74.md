---
name: unknown_workflow_video_lora_sampler_74
type: Unknown Workflow
frequency: 18
level: moderate
coverage: 0.546833
common_nodes: [BlockifyMask, CLIPVisionLoader, DownloadAndLoadSAM2Model, DrawMaskOnImage, GetImageSizeAndCount, GetNode, GrowMask, ImageConcatMulti, ImageResizeKJv2, LoadImage, Sam2Segmentation, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Wan Animate2.2+InfiniteTalk脸部动作身体动作分离修正版V1（无限时长）_1969341000269373441.json, 视频生成/图生视频/Wan Animate2.2+Uni3C运镜+动作迁移Move加速版V2（无限时长）_1969352799354056706.json, 视频生成/图生视频/Wan Animate2.2主体混合mix加速版V1_1969219198985662465.json, 视频生成/图生视频/Wan Animate2.2主体混合mix魔改加速版V2（无限时长）_1969110399318716418.json, 视频生成/图生视频/Wan Animate2.2人物融合_2073212185333026818.json, 视频生成/图生视频/Wan Animate2.2加速版无限时长_1969703078859579394.json, 视频生成/图生视频/Wan Animate2.2动作迁移Move魔改加速版V2（无限时长）_1969116607094157313.json, 视频生成/图生视频/Wan Animate2.2动作迁移_2073212149740163073.json, 视频生成/图生视频/Wan2.2-Animate 视频换脸+动作迁移_1981706242731196418.json, 视频生成/图生视频/WanAnimate 场景三 视频换脸_1970283537297514497.json, 视频生成/图生视频/WanAnimate 场景三 视频换脸_2059310361421115394.json, 视频生成/图生视频/WanAnimate 场景九 多人视频精准替换_2044021235868241922.json, 视频生成/图生视频/WanAnimate 场景六 单独面部表情迁移_1970399426625892354.json, 视频生成/文生视频/Wan Animate2.2主体替换MIX单独背景骚操作去油提高一致性加速版V1（无限时长）_1969355024180649986.json, 视频生成/文生视频/Wan Animate2.2主体替换MIX骚操作去油提高一致性加速版V1（无限时长）_1969358943149563905.json, 视频生成/文生视频/Wan Animate2.2非人类主体混合mix提示词加强+葫芦娃SAM2加速版V4（无限时长）_1969371914298925058.json, 视频生成/文生视频/Wan Animate2.2非人类主体混合mix魔改加速版V3（无限时长）_1969373357202436097.json, 视频生成/文生视频/Wan2.2 Animate V2模型高质量版本动物姿态Mix主体混合特别版V1_1974432637244805122.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_74

> 由 `engine/knowledge_consolidation` 从 18 个 workflow 归纳得出（视频生成/图生视频/Wan Animate2.2+InfiniteTalk脸部动作身体动作分离修正版V1（无限时长）_1969341000269373441.json、视频生成/图生视频/Wan Animate2.2+Uni3C运镜+动作迁移Move加速版V2（无限时长）_1969352799354056706.json、视频生成/图生视频/Wan Animate2.2主体混合mix加速版V1_1969219198985662465.json、视频生成/图生视频/Wan Animate2.2主体混合mix魔改加速版V2（无限时长）_1969110399318716418.json、视频生成/图生视频/Wan Animate2.2人物融合_2073212185333026818.json…）

- **类型**：Unknown Workflow
- **样本数**：18
- **可信度**：中等可信
- **平均知识覆盖**：55%

## 共有节点

全部 18 个 workflow 都包含：
- `BlockifyMask`
- `CLIPVisionLoader`
- `DownloadAndLoadSAM2Model`
- `DrawMaskOnImage`
- `GetImageSizeAndCount`
- `GetNode`
- `GrowMask`
- `ImageConcatMulti`
- `ImageResizeKJv2`
- `LoadImage`
- `Sam2Segmentation`
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
- `DWPreprocessor` —— 17/18 个有
- `FaceMaskFromPoseKeypoints` —— 17/18 个有
- `ImageCropByMaskAndResize` —— 17/18 个有
- `PixelPerfectResolution` —— 17/18 个有
- `PointsEditor` —— 17/18 个有
- `WanVideoContextOptions` —— 15/18 个有
- `JWInteger` —— 13/18 个有
- `CR Prompt Text` —— 12/18 个有
- `WanVideoEncode` —— 10/18 个有
- `WanVideoUni3C_ControlnetLoader` —— 10/18 个有
- `WanVideoUni3C_embeds` —— 10/18 个有
- `INTConstant` —— 5/18 个有
- `EmptyImage` —— 3/18 个有
- `LayerUtility: PurgeVRAM` —— 3/18 个有
- `RH_Captioner` —— 2/18 个有
- `ShowText` —— 2/18 个有
- `easy promptConcat` —— 2/18 个有
- `AnimalPosePreprocessor` —— 1/18 个有
- `AudioCrop` —— 1/18 个有
- `AudioSeparation` —— 1/18 个有
- `DownloadAndLoadWav2VecModel` —— 1/18 个有
- `ImageConcanate` —— 1/18 个有
- `ImageListToImageBatch` —— 1/18 个有
- `LayerMask: LoadSegmentAnythingModels` —— 1/18 个有
- `LayerMask: SegmentAnythingUltra V3` —— 1/18 个有
- `MultiTalkModelLoader` —— 1/18 个有
- `MultiTalkWav2VecEmbeds` —— 1/18 个有
- `PDIMAGE_LongerSize` —— 1/18 个有
- `PreviewAny` —— 1/18 个有
- `SDVN Image Repeat` —— 1/18 个有
- `WanVideoCombineEmbeds` —— 1/18 个有
- `WanVideoImageToVideoMultiTalk` —— 1/18 个有
- `easy cleanGpuUsed` —— 1/18 个有
- `easy showAnything` —— 1/18 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
