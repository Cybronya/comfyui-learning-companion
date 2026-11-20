---
name: unknown_workflow_video_lora_sampler_742
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.7315
common_nodes: [BlockifyMask, CLIPVisionLoader, DownloadAndLoadSAM2Model, DrawMaskOnImage, DrawViTPose, GetImageSizeAndCount, GrowMask, ImageResizeKJv2, LoadImage, OnnxDetectionModelLoader, PoseAndFaceDetection, Sam2Segmentation, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Wan2.2+Animate+V2模运动迁移Uni3c运镜_1976670695512068097.json, 视频生成/图生视频/Wan2.2Animate姿态+声音+精准替换_2002155248145842178.json, 视频生成/图生视频/Wan2.5  超自然动作迁移，视频换人_2034527249550020609.json, 视频生成/图生视频/动作迁移  V2 Wan2.2 Animate_2030254367873441794.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_742

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/Wan2.2+Animate+V2模运动迁移Uni3c运镜_1976670695512068097.json、视频生成/图生视频/Wan2.2Animate姿态+声音+精准替换_2002155248145842178.json、视频生成/图生视频/Wan2.5  超自然动作迁移，视频换人_2034527249550020609.json、视频生成/图生视频/动作迁移  V2 Wan2.2 Animate_2030254367873441794.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：73%

## 共有节点

全部 4 个 workflow 都包含：
- `BlockifyMask`
- `CLIPVisionLoader`
- `DownloadAndLoadSAM2Model`
- `DrawMaskOnImage`
- `DrawViTPose`
- `GetImageSizeAndCount`
- `GrowMask`
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
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `INTConstant` —— 3/4 个有
- `PointsEditor` —— 3/4 个有
- `SetNode` —— 3/4 个有
- `VHS_VideoInfoLoaded` —— 3/4 个有
- `WanVideoLoraSelectMulti` —— 3/4 个有
- `WanVideoTorchCompileSettings` —— 3/4 个有
- `easy cleanGpuUsed` —— 3/4 个有
- `easy showAnything` —— 3/4 个有
- `GetImageSize` —— 2/4 个有
- `GetNode` —— 2/4 个有
- `ImageConcanate` —— 2/4 个有
- `JjkText` —— 2/4 个有
- `CR Prompt Text` —— 1/4 个有
- `GetImageSize+` —— 1/4 个有
- `PreviewAny` —— 1/4 个有
- `PreviewImage` —— 1/4 个有
- `Primitive integer [Crystools]` —— 1/4 个有
- `SimpleMath+` —— 1/4 个有
- `WanVideoEncode` —— 1/4 个有
- `WanVideoLoraSelect` —— 1/4 个有
- `WanVideoUni3C_ControlnetLoader` —— 1/4 个有
- `WanVideoUni3C_embeds` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
