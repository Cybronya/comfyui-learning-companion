---
name: unknown_workflow_video_lora_sampler_363
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.552286
common_nodes: [BlockifyMask, CLIPVisionLoader, DownloadAndLoadSAM2Model, DrawMaskOnImage, GetImageSizeAndCount, GetNode, INTConstant, ImageResizeKJv2, LoadImage, OnnxDetectionModelLoader, PoseAndFaceDetection, Sam2Segmentation, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Wan-Animate-KJ工作流（自动遮罩）_1970452175312875521.json, 视频生成/图生视频/WanAnimateV2-人物编辑_1975882698759737345.json, 视频生成/图生视频/WanAnimate_V2_视频人物自动替换(单人)_2006252507227496450.json, 视频生成/图生视频/WanAnimate_V2_视频动作迁移(单人)_2006246424253571074.json, 视频生成/图生视频/自动抠图--最新Animate图片主体替换视频主体_1970425229413654530.json, 视频生成/文生视频/Wan2.2 Animate KJ版 人物动作迁移视频生成视频_1970355314094710785.json, 视频生成/文生视频/Wan2.2 Animate-KJ 美女跳舞 动作一键迁移复制姿势_1971474322126782465.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_363

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/Wan-Animate-KJ工作流（自动遮罩）_1970452175312875521.json、视频生成/图生视频/WanAnimateV2-人物编辑_1975882698759737345.json、视频生成/图生视频/WanAnimate_V2_视频人物自动替换(单人)_2006252507227496450.json、视频生成/图生视频/WanAnimate_V2_视频动作迁移(单人)_2006246424253571074.json、视频生成/图生视频/自动抠图--最新Animate图片主体替换视频主体_1970425229413654530.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：55%

## 共有节点

全部 7 个 workflow 都包含：
- `BlockifyMask`
- `CLIPVisionLoader`
- `DownloadAndLoadSAM2Model`
- `DrawMaskOnImage`
- `GetImageSizeAndCount`
- `GetNode`
- `INTConstant`
- `ImageResizeKJv2`
- `LoadImage`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
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
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `DownloadAndLoadGIMMVFIModel` —— 6/7 个有
- `GIMMVFI_interpolate` —— 6/7 个有
- `ImageConcatMulti` —— 6/7 个有
- `GrowMask` —— 5/7 个有
- `ImageBlend` —— 5/7 个有
- `PreviewImage` —— 5/7 个有
- `WanVideoTorchCompileSettings` —— 5/7 个有
- `DrawViTPose` —— 4/7 个有
- `LayerUtility: PurgeVRAM V2` —— 3/7 个有
- `GrowMaskWithBlur` —— 2/7 个有
- `SimpleMath+` —— 2/7 个有
- `Text Multiline` —— 2/7 个有
- `FloatConstant` —— 1/7 个有
- `GetImageRangeFromBatch` —— 1/7 个有
- `Primitive integer [Crystools]` —— 1/7 个有
- `PrimitiveStringMultiline` —— 1/7 个有
- `WanVideoContextOptions` —— 1/7 个有
- `WanVideoEncode` —— 1/7 个有
- `WanVideoExperimentalArgs` —— 1/7 个有
- `WanVideoSLG` —— 1/7 个有
- `WanVideoScheduler` —— 1/7 个有
- `WanVideoUni3C_ControlnetLoader` —— 1/7 个有
- `WanVideoUni3C_embeds` —— 1/7 个有
- `easy showAnything` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
