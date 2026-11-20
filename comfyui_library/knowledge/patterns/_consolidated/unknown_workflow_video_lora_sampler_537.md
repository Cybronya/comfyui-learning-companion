---
name: unknown_workflow_video_lora_sampler_537
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.63175
common_nodes: [BlockifyMask, CLIPVisionLoader, DrawMaskOnImage, DrawViTPose, GrowMask, LayerMask: MaskPreview, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, OnnxDetectionModelLoader, PointsEditor, PoseAndFaceDetection, SeCModelLoader, SeCVideoSegmentation, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [数字人/数字人/原始视频收集或拍摄+Animate人物替换_1998606846065803265.json, 数字人/数字人/原始视频收集或拍摄+Animate人物替换_2053330594825818113.json, 数字人/数字人/数字人板块：Animate视频人物替换工作流_2051238079196872705.json, 视频生成/图生视频/Animate人物替换（不限长度）_2015018676868616194.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_537

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（数字人/数字人/原始视频收集或拍摄+Animate人物替换_1998606846065803265.json、数字人/数字人/原始视频收集或拍摄+Animate人物替换_2053330594825818113.json、数字人/数字人/数字人板块：Animate视频人物替换工作流_2051238079196872705.json、视频生成/图生视频/Animate人物替换（不限长度）_2015018676868616194.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：63%

## 共有节点

全部 4 个 workflow 都包含：
- `BlockifyMask`
- `CLIPVisionLoader`
- `DrawMaskOnImage`
- `DrawViTPose`
- `GrowMask`
- `LayerMask: MaskPreview`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `OnnxDetectionModelLoader`
- `PointsEditor`
- `PoseAndFaceDetection`
- `SeCModelLoader`
- `SeCVideoSegmentation`
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

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 3/4 个有
- `ImageFromBatch` —— 3/4 个有
- `ImageResize+` —— 3/4 个有
- `PreviewImage` —— 3/4 个有
- `SetNode` —— 3/4 个有
- `WanVideoSetBlockSwap` —— 3/4 个有
- `WanVideoSetLoRAs` —— 3/4 个有
- `AddMask` —— 2/4 个有
- `CR Text` —— 2/4 个有
- `ImageConcanate` —— 2/4 个有
- `SDPoseOODLoader` —— 2/4 个有
- `SDPoseOODProcessor` —— 2/4 个有
- `SeCModelLoader_Ultra-Fast` —— 2/4 个有
- `SeCVideoSegmentation_Ultra-Fast` —— 2/4 个有
- `easy showAnything` —— 2/4 个有
- `ImageResizeKJv2` —— 1/4 个有
- `ImpactConditionalBranch` —— 1/4 个有
- `Int` —— 1/4 个有
- `SaveImage` —— 1/4 个有
- `VHS_VideoInfo` —— 1/4 个有
- `WanVideoContextOptions` —— 1/4 个有
- `WanVideoTorchCompileSettings` —— 1/4 个有
- `easy compare` —— 1/4 个有
- `easy int` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
