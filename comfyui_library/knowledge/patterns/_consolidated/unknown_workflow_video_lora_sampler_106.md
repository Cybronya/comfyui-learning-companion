---
name: unknown_workflow_video_lora_sampler_106
type: Unknown Workflow
frequency: 17
level: moderate
coverage: 0.546529
common_nodes: [BlockifyMask, CLIPVisionLoader, DownloadAndLoadSAM2Model, DrawMaskOnImage, GrowMask, ImageResizeKJv2, LoadImage, Sam2Segmentation, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/46b.tonnie-Wan2.2 Animate替换视频中的人物及姿态（自动版）_2005719799860789249.json, 视频生成/图生视频/46c.tonnie-Wan2.2+Animate替换视频中的人物的服装_2006611649658101762.json, 视频生成/图生视频/Wan Animate  视频换脸 _ 动作迁移_2050805055514791937.json, 视频生成/图生视频/Wan Animate  视频换脸 _ 动作迁移工作流 唱歌跳舞视频动作迁移_2096554698164752386.json, 视频生成/图生视频/Wan Animate  视频换脸 _ 动作迁移工作流 唱歌跳舞视频动作迁移_2096575707920027649.json, 视频生成/图生视频/Wan Animate  视频换脸 _ 动作迁移工作流_2050834000423473154.json, 视频生成/图生视频/Wan Animate  视频换脸 _ 动作迁移工作流_2069022324761907201.json, 视频生成/图生视频/Wan Animate  视频换脸 _ 动作迁移工作流_2082813929578909697.json, 视频生成/图生视频/Wan Animate  视频换脸 _ 动作迁移工作流_2104161486053662722.json, 视频生成/图生视频/Wan Animate  视频换脸 _ 动作迁移工作流_2104198098951168001.json, 视频生成/图生视频/Wan Animate  视频换脸 _ 动作迁移工作流_2110913885871099905.json, 视频生成/图生视频/Wan Animate2.2+InfiniteTalk脸部动作身体动作分离修正版V1（无限时长）_1969341000269373441.json, 视频生成/图生视频/Wan Animate2.2+Uni3C运镜+动作迁移Move加速版V2（无限时长）_1969352799354056706.json, 视频生成/图生视频/Wan Animate2.2主体混合mix魔改加速版V2（无限时长）_1969110399318716418.json, 视频生成/文生视频/Wan Animate2.2主体替换MIX单独背景骚操作去油提高一致性加速版V1（无限时长）_1969355024180649986.json, 视频生成/文生视频/Wan Animate2.2主体替换MIX骚操作去油提高一致性加速版V1（无限时长）_1969358943149563905.json, 视频生成/文生视频/Wan Animate2.2非人类主体混合mix魔改加速版V3（无限时长）_1969373357202436097.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_106

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（视频生成/图生视频/46b.tonnie-Wan2.2 Animate替换视频中的人物及姿态（自动版）_2005719799860789249.json、视频生成/图生视频/46c.tonnie-Wan2.2+Animate替换视频中的人物的服装_2006611649658101762.json、视频生成/图生视频/Wan Animate  视频换脸 _ 动作迁移_2050805055514791937.json、视频生成/图生视频/Wan Animate  视频换脸 _ 动作迁移工作流 唱歌跳舞视频动作迁移_2096554698164752386.json、视频生成/图生视频/Wan Animate  视频换脸 _ 动作迁移工作流 唱歌跳舞视频动作迁移_2096575707920027649.json…）

- **类型**：Unknown Workflow
- **样本数**：17
- **可信度**：中等可信
- **平均知识覆盖**：55%

## 共有节点

全部 17 个 workflow 都包含：
- `BlockifyMask`
- `CLIPVisionLoader`
- `DownloadAndLoadSAM2Model`
- `DrawMaskOnImage`
- `GrowMask`
- `ImageResizeKJv2`
- `LoadImage`
- `Sam2Segmentation`
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
- `WanVideoTextEncodeCached`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `DWPreprocessor` —— 16/17 个有
- `FaceMaskFromPoseKeypoints` —— 16/17 个有
- `ImageCropByMaskAndResize` —— 16/17 个有
- `PixelPerfectResolution` —— 16/17 个有
- `PointsEditor` —— 16/17 个有
- `GetImageSizeAndCount` —— 15/17 个有
- `GetNode` —— 15/17 个有
- `ImageConcatMulti` —— 15/17 个有
- `SetNode` —— 15/17 个有
- `WanVideoContextOptions` —— 15/17 个有
- `WanVideoSetLoRAs` —— 15/17 个有
- `INTConstant` —— 11/17 个有
- `CR Prompt Text` —— 6/17 个有
- `JWInteger` —— 6/17 个有
- `WanVideoEncode` —— 6/17 个有
- `WanVideoUni3C_ControlnetLoader` —— 6/17 个有
- `WanVideoUni3C_embeds` —— 6/17 个有
- `Fast Groups Muter (rgthree)` —— 2/17 个有
- `SimpleMath+` —— 2/17 个有
- `ACE_ImageFaceCrop` —— 1/17 个有
- `AudioCrop` —— 1/17 个有
- `AudioSeparation` —— 1/17 个有
- `DownloadAndLoadWav2VecModel` —— 1/17 个有
- `DrawViTPose` —— 1/17 个有
- `EmptyImage` —— 1/17 个有
- `ImageListToImageBatch` —— 1/17 个有
- `MultiTalkModelLoader` —— 1/17 个有
- `MultiTalkWav2VecEmbeds` —— 1/17 个有
- `OnnxDetectionModelLoader` —— 1/17 个有
- `PoseAndFaceDetection` —— 1/17 个有
- `PreviewAny` —— 1/17 个有
- `SDVN Image Repeat` —— 1/17 个有
- `WanVideoCombineEmbeds` —— 1/17 个有
- `WanVideoImageToVideoMultiTalk` —— 1/17 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
