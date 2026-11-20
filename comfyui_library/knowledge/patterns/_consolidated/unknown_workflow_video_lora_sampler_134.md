---
name: unknown_workflow_video_lora_sampler_134
type: Unknown Workflow
frequency: 15
level: moderate
coverage: 0.5224
common_nodes: [BlockifyMask, CLIPVisionLoader, DrawMaskOnImage, DrawViTPose, GetNode, GrowMask, LoadImage, OnnxDetectionModelLoader, PointsEditor, PoseAndFaceDetection, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncodeCached, WanVideoVAELoader, easy showAnything]
problems: []
missing: []
members: [平台全量/Wan2.2 Animate V2+SeC遮罩优化版_1977197157231022082.json, 平台全量/Wan2.2 Animate V2视频人物替换+SeC遮罩最新版_2028100957145403393.json, 平台全量/Wan2.2Animate视频换人物_2062474652877942786.json, 平台全量/动作迁移  V2 Wan2.2 Animate_2028994297055416322.json, 平台全量/自用换视频_2001631616843825154.json, 数字人/数字人/Wan Animate V2版 视频多人场景精准替换_1970675787114422273.json, 视频生成/图生视频/V2 Wan2.2 Animate 动作迁移  24G显存_1998993890759860225.json, 视频生成/图生视频/V2 Wan2.2 Animate 动作迁移_1991192921735278594.json, 视频生成/图生视频/V2 Wan2.2 Animate 动作迁移_2043632215732523009.json, 视频生成/图生视频/V2 Wan2.2 Animate 动作迁移_2043636277030948866.json, 视频生成/图生视频/V2 Wan2.2 Animate 视频替换人物_产品_背景 (3)_1997005381832478722.json, 视频生成/图生视频/V2 Wan2.2 Animate 视频替换人物_产品_背景_1974719882828845058.json, 视频生成/图生视频/V2 Wan2.3 Animate 超自然动作迁移_2008454973708832769.json, 视频生成/图生视频/V2 Wan2.5 Animate 超自然动作迁移 视频换人_2064595765720346625.json, 视频生成/图生视频/V2+Wan2.2+Animate+动作迁移_2016043271843225601.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_134

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（平台全量/Wan2.2 Animate V2+SeC遮罩优化版_1977197157231022082.json、平台全量/Wan2.2 Animate V2视频人物替换+SeC遮罩最新版_2028100957145403393.json、平台全量/Wan2.2Animate视频换人物_2062474652877942786.json、平台全量/动作迁移  V2 Wan2.2 Animate_2028994297055416322.json、平台全量/自用换视频_2001631616843825154.json…）

- **类型**：Unknown Workflow
- **样本数**：15
- **可信度**：中等可信
- **平均知识覆盖**：52%

## 共有节点

全部 15 个 workflow 都包含：
- `BlockifyMask`
- `CLIPVisionLoader`
- `DrawMaskOnImage`
- `DrawViTPose`
- `GetNode`
- `GrowMask`
- `LoadImage`
- `OnnxDetectionModelLoader`
- `PointsEditor`
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
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `ImageConcanate` —— 14/15 个有
- `WanVideoSetBlockSwap` —— 14/15 个有
- `WanVideoSetLoRAs` —— 14/15 个有
- `DownloadAndLoadSAM2Model` —— 12/15 个有
- `GetImageSize` —— 12/15 个有
- `GetImageSizeAndCount` —— 12/15 个有
- `INTConstant` —— 12/15 个有
- `ImageResizeKJv2` —— 12/15 个有
- `Sam2Segmentation` —— 12/15 个有
- `VHS_VideoInfoLoaded` —— 12/15 个有
- `WanVideoTorchCompileSettings` —— 12/15 个有
- `easy cleanGpuUsed` —— 12/15 个有
- `JjkText` —— 11/15 个有
- `PreviewImage` —— 4/15 个有
- `ImageResize+` —— 3/15 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/15 个有
- `Float to Int` —— 2/15 个有
- `MuyeLoadImage` —— 2/15 个有
- `SeCModelLoader` —— 2/15 个有
- `SeCVideoSegmentation` —— 2/15 个有
- `AdaptiveWanVideoAnimateEmbeds` —— 1/15 个有
- `Frame Select` —— 1/15 个有
- `LayerMask: MaskPreview` —— 1/15 个有
- `SaveVideoRGBA` —— 1/15 个有
- `VHS_LoadVideoPath` —— 1/15 个有
- `Vignette` —— 1/15 个有
- `WanVideoTeaCache` —— 1/15 个有
- `easy sam3ModelLoader` —— 1/15 个有
- `easy sam3VideoSegmentation` —— 1/15 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
