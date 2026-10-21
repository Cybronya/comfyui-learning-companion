---
name: unknown_workflow_video_lora_sampler_109
type: Unknown Workflow
frequency: 14
level: moderate
coverage: 0.549857
common_nodes: [BlockifyMask, CLIPVisionLoader, DownloadAndLoadSAM2Model, DrawMaskOnImage, GetImageSizeAndCount, GrowMask, INTConstant, ImageResizeKJv2, LoadImage, OnnxDetectionModelLoader, PoseAndFaceDetection, Sam2Segmentation, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1998993890759860225.json, 视频生成/图生视频/1991192921735278594.json, 视频生成/图生视频/2043632215732523009.json, 视频生成/图生视频/2043636277030948866.json, 视频生成/图生视频/1997005381832478722.json, 视频生成/图生视频/1974719882828845058.json, 视频生成/图生视频/2008454973708832769.json, 视频生成/图生视频/2064595765720346625.json, 视频生成/图生视频/2016043271843225601.json, 视频生成/图生视频/2002155248145842178.json, 视频生成/图生视频/2034527249550020609.json, 视频生成/图生视频/1975882698759737345.json, 视频生成/图生视频/2030254367873441794.json, 视频生成/文生视频/1970355314094710785.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_109

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（视频生成/图生视频/1998993890759860225.json、视频生成/图生视频/1991192921735278594.json、视频生成/图生视频/2043632215732523009.json、视频生成/图生视频/2043636277030948866.json、视频生成/图生视频/1997005381832478722.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：中等可信
- **平均知识覆盖**：55%

## 共有节点

全部 14 个 workflow 都包含：
- `BlockifyMask`
- `CLIPVisionLoader`
- `DownloadAndLoadSAM2Model`
- `DrawMaskOnImage`
- `GetImageSizeAndCount`
- `GrowMask`
- `INTConstant`
- `ImageResizeKJv2`
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
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `DrawViTPose` —— 13/14 个有
- `GetNode` —— 13/14 个有
- `SetNode` —— 13/14 个有
- `WanVideoLoraSelectMulti` —— 13/14 个有
- `PointsEditor` —— 12/14 个有
- `VHS_VideoInfoLoaded` —— 12/14 个有
- `easy cleanGpuUsed` —— 12/14 个有
- `easy showAnything` —— 12/14 个有
- `GetImageSize` —— 11/14 个有
- `ImageConcanate` —— 11/14 个有
- `JjkText` —— 10/14 个有
- `PreviewImage` —— 3/14 个有
- `DownloadAndLoadGIMMVFIModel` —— 2/14 个有
- `GIMMVFI_interpolate` —— 2/14 个有
- `ImageBlend` —— 2/14 个有
- `MuyeLoadImage` —— 2/14 个有
- `Primitive integer [Crystools]` —— 2/14 个有
- `SimpleMath+` —— 2/14 个有
- `CR Prompt Text` —— 1/14 个有
- `Float to Int` —— 1/14 个有
- `ImageConcatMulti` —— 1/14 个有
- `PreviewAny` —— 1/14 个有
- `VHS_LoadVideoPath` —— 1/14 个有
- `WanVideoLoraSelect` —— 1/14 个有
- `WanVideoTeaCache` —— 1/14 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
