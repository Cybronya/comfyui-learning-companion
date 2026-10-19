---
name: unknown_workflow_video_lora_sampler_23
type: Unknown Workflow
frequency: 27
level: moderate
coverage: 0.569111
common_nodes: [BlockifyMask, CLIPVisionLoader, DrawMaskOnImage, GrowMask, ImageResizeKJv2, LoadImage, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/2005719799860789249.json, 视频生成/图生视频/2006611649658101762.json, 视频生成/图生视频/2050805055514791937.json, 视频生成/图生视频/Wan Animate  视频换脸 _ 动作迁移工作流 唱歌跳舞视频动作迁移_2096554698164752386.json, 视频生成/图生视频/Wan Animate  视频换脸 _ 动作迁移工作流 唱歌跳舞视频动作迁移_2096575707920027649.json, 视频生成/图生视频/2050834000423473154.json, 视频生成/图生视频/2069022324761907201.json, 视频生成/图生视频/Wan Animate  视频换脸 _ 动作迁移工作流_2082813929578909697.json, 视频生成/图生视频/Wan Animate  视频换脸 _ 动作迁移工作流_2104161486053662722.json, 视频生成/图生视频/Wan Animate  视频换脸 _ 动作迁移工作流_2104198098951168001.json, 视频生成/图生视频/Wan Animate  视频换脸 _ 动作迁移工作流_2110913885871099905.json, 视频生成/图生视频/1969559616474542081.json, 视频生成/图生视频/1972998201764655106.json, 视频生成/图生视频/2073214426706173954.json, 视频生成/图生视频/2073218471797805057.json, 视频生成/图生视频/1969398350657318913.json, 视频生成/图生视频/1962703044544737281.json, 视频生成/图生视频/1969620771280744450.json, 视频生成/图生视频/1969608004544983041.json, 视频生成/图生视频/1971950073557020673.json, 视频生成/图生视频/1971886866809221121.json, 视频生成/图生视频/1971891163009642497.json, 视频生成/图生视频/1972598111484968962.json, 视频生成/图生视频/1968952890041778177.json, 视频生成/图生视频/1998309417806389249.json, 视频生成/图生视频/1975795950243418113.json, 视频生成/图生视频/1988846148821585921.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_23

> 由 `engine/knowledge_consolidation` 从 27 个 workflow 归纳得出（视频生成/图生视频/2005719799860789249.json、视频生成/图生视频/2006611649658101762.json、视频生成/图生视频/2050805055514791937.json、视频生成/图生视频/Wan Animate  视频换脸 _ 动作迁移工作流 唱歌跳舞视频动作迁移_2096554698164752386.json、视频生成/图生视频/Wan Animate  视频换脸 _ 动作迁移工作流 唱歌跳舞视频动作迁移_2096575707920027649.json…）

- **类型**：Unknown Workflow
- **样本数**：27
- **可信度**：中等可信
- **平均知识覆盖**：57%

## 共有节点

全部 27 个 workflow 都包含：
- `BlockifyMask`
- `CLIPVisionLoader`
- `DrawMaskOnImage`
- `GrowMask`
- `ImageResizeKJv2`
- `LoadImage`
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
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `PointsEditor` —— 26/27 个有
- `DownloadAndLoadSAM2Model` —— 25/27 个有
- `GetImageSizeAndCount` —— 25/27 个有
- `ImageConcatMulti` —— 25/27 个有
- `Sam2Segmentation` —— 25/27 个有
- `WanVideoSetLoRAs` —— 25/27 个有
- `WanVideoTorchCompileSettings` —— 25/27 个有
- `GetNode` —— 21/27 个有
- `SetNode` —— 21/27 个有
- `DWPreprocessor` —— 17/27 个有
- `PixelPerfectResolution` —— 17/27 个有
- `WanVideoContextOptions` —— 17/27 个有
- `FaceMaskFromPoseKeypoints` —— 16/27 个有
- `ImageCropByMaskAndResize` —— 16/27 个有
- `INTConstant` —— 13/27 个有
- `OnnxDetectionModelLoader` —— 11/27 个有
- `PoseAndFaceDetection` —— 11/27 个有
- `DrawViTPose` —— 10/27 个有
- `JWInteger` —— 10/27 个有
- `easy showAnything` —— 10/27 个有
- `ACE_ImageFaceCrop` —— 9/27 个有
- `PoseRetargetPromptHelper` —— 8/27 个有
- `SimpleMath+` —— 8/27 个有
- `CR Prompt Text` —— 7/27 个有
- `WanVideoEncode` —— 7/27 个有
- `WanVideoUni3C_ControlnetLoader` —— 7/27 个有
- `WanVideoUni3C_embeds` —— 7/27 个有
- `GetImageRangeFromBatch` —— 6/27 个有
- `PreviewImage` —— 6/27 个有
- `Int` —— 5/27 个有
- `AudioCropProcessUTK` —— 4/27 个有
- `LayerUtility: PurgeVRAM` —— 3/27 个有
- `MathExpression|pysssss` —— 3/27 个有
- `ColorMatch` —— 2/27 个有
- `DF_Text_Box` —— 2/27 个有
- `Fast Groups Muter (rgthree)` —— 2/27 个有
- `Float to Int` —— 2/27 个有
- `JWLoopImageSequence` —— 2/27 个有
- `PrimitiveStringMultiline` —— 2/27 个有
- `SeCModelLoader` —— 2/27 个有
- `SeCVideoSegmentation` —— 2/27 个有
- `Text Multiline` —— 2/27 个有
- `WanVideoLoraSelect` —— 2/27 个有
- `easy float` —— 2/27 个有
- `ImageBatch` —— 1/27 个有
- `ImageFromBatch+` —— 1/27 个有
- `Note Plus (mtb)` —— 1/27 个有
- `RHHiddenNodes` —— 1/27 个有
- `RepeatImageBatch` —— 1/27 个有
- `easy forLoopEnd` —— 1/27 个有
- `easy forLoopStart` —— 1/27 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
