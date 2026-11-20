---
name: unknown_workflow_video_lora_sampler_813
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.501
common_nodes: [BlockifyMask, CLIPVisionLoader, DrawMaskOnImage, DrawViTPose, GetNode, GrowMask, ImageResizeKJv2, LoadImage, OnnxDetectionModelLoader, PoseAndFaceDetection, SeCModelLoader, SeCVideoSegmentation, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [平台全量/Wan2.2动作迁移animate背景锁定+背部？？？_2056022446129598465.json, 平台全量/wan animate v3——优化版_1983149864626364417.json, 视频生成/图生视频/Wan2.2 Animate高质量电商换模特_1972598111484968962.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_813

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/Wan2.2动作迁移animate背景锁定+背部？？？_2056022446129598465.json、平台全量/wan animate v3——优化版_1983149864626364417.json、视频生成/图生视频/Wan2.2 Animate高质量电商换模特_1972598111484968962.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：50%

## 共有节点

全部 3 个 workflow 都包含：
- `BlockifyMask`
- `CLIPVisionLoader`
- `DrawMaskOnImage`
- `DrawViTPose`
- `GetNode`
- `GrowMask`
- `ImageResizeKJv2`
- `LoadImage`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `SeCModelLoader`
- `SeCVideoSegmentation`
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
- `GetImageSizeAndCount` —— 2/3 个有
- `ImageConcatMulti` —— 2/3 个有
- `ImageFromBatch` —— 2/3 个有
- `Int` —— 2/3 个有
- `PointsEditor` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `RepeatImageBatch` —— 2/3 个有
- `VHS_VideoInfo` —— 2/3 个有
- `WanVideoContextOptions` —— 2/3 个有
- `WanVideoEncode` —— 2/3 个有
- `WanVideoTorchCompileSettings` —— 2/3 个有
- `WanVideoUni3C_ControlnetLoader` —— 2/3 个有
- `WanVideoUni3C_embeds` —— 2/3 个有
- `CoordinatePlotter` —— 1/3 个有
- `Fast Groups Bypasser (rgthree)` —— 1/3 个有
- `JWInteger` —— 1/3 个有
- `LazySwitch1way` —— 1/3 个有
- `PoseRetargetPromptHelper` —— 1/3 个有
- `easy boolean` —— 1/3 个有
- `easy cleanGpuUsed` —— 1/3 个有
- `easy sam3ImageSegmentation` —— 1/3 个有
- `easy sam3ModelLoader` —— 1/3 个有
- `easy showAnything` —— 1/3 个有
- `int _O` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
