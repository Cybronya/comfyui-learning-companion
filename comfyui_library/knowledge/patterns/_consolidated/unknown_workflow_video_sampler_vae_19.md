---
name: unknown_workflow_video_sampler_vae_19
type: Unknown Workflow
frequency: 14
level: moderate
coverage: 0.5565
common_nodes: [BlockifyMask, CLIPVisionLoader, DownloadAndLoadSAM2Model, DrawMaskOnImage, DrawViTPose, LoadImage, OnnxDetectionModelLoader, PoseAndFaceDetection, Sam2Segmentation, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [数字人/数字人/带货视频角色替换稳定版_2019053733203677185.json, 视频生成/图生视频/46b.tonnie-Wan2.2 Animate替换视频中的人物及姿态（自动版）_2005719799860789249.json, 视频生成/图生视频/AI换人术把你代入名场面，本来应该从从容容游刃有余_1976931314983161857.json, 视频生成/图生视频/V2 Wan2.2 Animate 动作迁移  24G显存_1998993890759860225.json, 视频生成/图生视频/V2 Wan2.2 Animate 动作迁移_1991192921735278594.json, 视频生成/图生视频/V2 Wan2.2 Animate 动作迁移_2043632215732523009.json, 视频生成/图生视频/V2 Wan2.2 Animate 动作迁移_2043636277030948866.json, 视频生成/图生视频/V2 Wan2.2 Animate 视频替换人物_产品_背景 (3)_1997005381832478722.json, 视频生成/图生视频/V2 Wan2.2 Animate 视频替换人物_产品_背景_1974719882828845058.json, 视频生成/图生视频/V2 Wan2.3 Animate 超自然动作迁移_2008454973708832769.json, 视频生成/图生视频/V2 Wan2.5 Animate 超自然动作迁移 视频换人_2064595765720346625.json, 视频生成/图生视频/V2+Wan2.2+Animate+动作迁移_2016043271843225601.json, 视频生成/图生视频/Wan2.5  超自然动作迁移，视频换人_2034527249550020609.json, 视频生成/图生视频/动作迁移  V2 Wan2.2 Animate_2030254367873441794.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_19

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（数字人/数字人/带货视频角色替换稳定版_2019053733203677185.json、视频生成/图生视频/46b.tonnie-Wan2.2 Animate替换视频中的人物及姿态（自动版）_2005719799860789249.json、视频生成/图生视频/AI换人术把你代入名场面，本来应该从从容容游刃有余_1976931314983161857.json、视频生成/图生视频/V2 Wan2.2 Animate 动作迁移  24G显存_1998993890759860225.json、视频生成/图生视频/V2 Wan2.2 Animate 动作迁移_1991192921735278594.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：中等可信
- **平均知识覆盖**：56%

## 共有节点

全部 14 个 workflow 都包含：
- `BlockifyMask`
- `CLIPVisionLoader`
- `DownloadAndLoadSAM2Model`
- `DrawMaskOnImage`
- `DrawViTPose`
- `LoadImage`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `Sam2Segmentation`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoAnimateEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoTextEncodeCached`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `GetImageSizeAndCount` —— 13/14 个有
- `GrowMask` —— 13/14 个有
- `INTConstant` —— 13/14 个有
- `ImageResizeKJv2` —— 13/14 个有
- `WanVideoLoraSelectMulti` —— 13/14 个有
- `WanVideoSetLoRAs` —— 13/14 个有
- `GetNode` —— 12/14 个有
- `PointsEditor` —— 12/14 个有
- `SetNode` —— 12/14 个有
- `GetImageSize` —— 11/14 个有
- `ImageConcanate` —— 11/14 个有
- `VHS_VideoInfoLoaded` —— 11/14 个有
- `easy cleanGpuUsed` —— 11/14 个有
- `easy showAnything` —— 11/14 个有
- `JjkText` —— 10/14 个有
- `Label (rgthree)` —— 2/14 个有
- `MuyeLoadImage` —— 2/14 个有
- `SimpleMath+` —— 2/14 个有
- `ACE_ImageFaceCrop` —— 1/14 个有
- `Fast Groups Muter (rgthree)` —— 1/14 个有
- `Float to Int` —— 1/14 个有
- `GrowMaskWithBlur` —— 1/14 个有
- `ImageConcatMulti` —— 1/14 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/14 个有
- `PreviewImage` —— 1/14 个有
- `Primitive integer [Crystools]` —— 1/14 个有
- `RHHiddenNodes` —— 1/14 个有
- `VHS_LoadVideoPath` —— 1/14 个有
- `VHS_VideoInfo` —— 1/14 个有
- `WanVideoContextOptions` —— 1/14 个有
- `WanVideoTeaCache` —— 1/14 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
