---
name: unknown_workflow_video_lora_sampler_139
type: Unknown Workflow
frequency: 12
level: moderate
coverage: 0.549833
common_nodes: [BlockifyMask, CLIPVisionLoader, DownloadAndLoadSAM2Model, DrawMaskOnImage, DrawViTPose, GetImageSizeAndCount, GrowMask, INTConstant, ImageResizeKJv2, LoadImage, OnnxDetectionModelLoader, PointsEditor, PoseAndFaceDetection, Sam2Segmentation, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfoLoaded, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVAELoader, easy cleanGpuUsed, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/V2 Wan2.2 Animate 动作迁移  24G显存_1998993890759860225.json, 视频生成/图生视频/V2 Wan2.2 Animate 动作迁移_1991192921735278594.json, 视频生成/图生视频/V2 Wan2.2 Animate 动作迁移_2043632215732523009.json, 视频生成/图生视频/V2 Wan2.2 Animate 动作迁移_2043636277030948866.json, 视频生成/图生视频/V2 Wan2.2 Animate 视频替换人物_产品_背景 (3)_1997005381832478722.json, 视频生成/图生视频/V2 Wan2.2 Animate 视频替换人物_产品_背景_1974719882828845058.json, 视频生成/图生视频/V2 Wan2.3 Animate 超自然动作迁移_2008454973708832769.json, 视频生成/图生视频/V2 Wan2.5 Animate 超自然动作迁移 视频换人_2064595765720346625.json, 视频生成/图生视频/V2+Wan2.2+Animate+动作迁移_2016043271843225601.json, 视频生成/图生视频/Wan2.2Animate姿态+声音+精准替换_2002155248145842178.json, 视频生成/图生视频/Wan2.5  超自然动作迁移，视频换人_2034527249550020609.json, 视频生成/图生视频/动作迁移  V2 Wan2.2 Animate_2030254367873441794.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_139

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（视频生成/图生视频/V2 Wan2.2 Animate 动作迁移  24G显存_1998993890759860225.json、视频生成/图生视频/V2 Wan2.2 Animate 动作迁移_1991192921735278594.json、视频生成/图生视频/V2 Wan2.2 Animate 动作迁移_2043632215732523009.json、视频生成/图生视频/V2 Wan2.2 Animate 动作迁移_2043636277030948866.json、视频生成/图生视频/V2 Wan2.2 Animate 视频替换人物_产品_背景 (3)_1997005381832478722.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：55%

## 共有节点

全部 12 个 workflow 都包含：
- `BlockifyMask`
- `CLIPVisionLoader`
- `DownloadAndLoadSAM2Model`
- `DrawMaskOnImage`
- `DrawViTPose`
- `GetImageSizeAndCount`
- `GrowMask`
- `INTConstant`
- `ImageResizeKJv2`
- `LoadImage`
- `OnnxDetectionModelLoader`
- `PointsEditor`
- `PoseAndFaceDetection`
- `Sam2Segmentation`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfoLoaded`
- `WanVideoAnimateEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `easy cleanGpuUsed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `GetImageSize` —— 11/12 个有
- `GetNode` —— 11/12 个有
- `ImageConcanate` —— 11/12 个有
- `SetNode` —— 11/12 个有
- `WanVideoLoraSelectMulti` —— 11/12 个有
- `JjkText` —— 10/12 个有
- `MuyeLoadImage` —— 2/12 个有
- `CR Prompt Text` —— 1/12 个有
- `Float to Int` —— 1/12 个有
- `PreviewAny` —— 1/12 个有
- `PreviewImage` —— 1/12 个有
- `Primitive integer [Crystools]` —— 1/12 个有
- `SimpleMath+` —— 1/12 个有
- `VHS_LoadVideoPath` —— 1/12 个有
- `WanVideoLoraSelect` —— 1/12 个有
- `WanVideoTeaCache` —— 1/12 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
