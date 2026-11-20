---
name: unknown_workflow_video_lora_sampler_607
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.59775
common_nodes: [BlockifyMask, CLIPVisionLoader, DrawMaskOnImage, DrawViTPose, Fast Groups Bypasser (rgthree), GetImageSizeAndCount, GetNode, GrowMask, INTConstant, ImageResizeKJv2, LoadImage, OnnxDetectionModelLoader, PoseAndFaceDetection, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/长视频动作迁移+迁移人物_2020513230719815681.json, 视频生成/文生视频/Wan-Animate+Sa2VA多人场景角色替换_1989959828757991425.json, 视频生成/文生视频/Wan-Animate-SecNodes角色替换_1977718983715606530.json, 视频生成/文生视频/Wan-Animate多人场景角色替换_1974519641752080386.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_607

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/长视频动作迁移+迁移人物_2020513230719815681.json、视频生成/文生视频/Wan-Animate+Sa2VA多人场景角色替换_1989959828757991425.json、视频生成/文生视频/Wan-Animate-SecNodes角色替换_1977718983715606530.json、视频生成/文生视频/Wan-Animate多人场景角色替换_1974519641752080386.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：60%

## 共有节点

全部 4 个 workflow 都包含：
- `BlockifyMask`
- `CLIPVisionLoader`
- `DrawMaskOnImage`
- `DrawViTPose`
- `Fast Groups Bypasser (rgthree)`
- `GetImageSizeAndCount`
- `GetNode`
- `GrowMask`
- `INTConstant`
- `ImageResizeKJv2`
- `LoadImage`
- `OnnxDetectionModelLoader`
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
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `Float` —— 3/4 个有
- `LayerMask: MaskInvert` —— 3/4 个有
- `PreviewImage` —— 3/4 个有
- `Setter` —— 3/4 个有
- `WanVideoTorchCompileSettings` —— 3/4 个有
- `easy ifElse` —— 3/4 个有
- `easy showAnything` —— 3/4 个有
- `PointsEditor` —— 2/4 个有
- `DownloadAndLoadSAM2Model` —— 1/4 个有
- `FloatConstant` —— 1/4 个有
- `ImageBlend` —— 1/4 个有
- `ImageRemoveBackground+` —— 1/4 个有
- `JWImageExtractFromBatch` —— 1/4 个有
- `LayerMask: SAM2VideoUltra` —— 1/4 个有
- `RemBGSession+` —— 1/4 个有
- `Sa2VANodeTpl` —— 1/4 个有
- `Sam2Segmentation` —— 1/4 个有
- `SeCModelLoader` —— 1/4 个有
- `SeCVideoSegmentation` —— 1/4 个有
- `WanVideoContextOptions` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
