---
name: unknown_workflow_video_lora_sampler_371
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.6285
common_nodes: [CLIPVisionLoader, DrawViTPose, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, OnnxDetectionModelLoader, PoseAndFaceDetection, PreviewImage, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [数字人/数字人/原始视频收集或拍摄+Animate人物替换_1998606846065803265.json, 数字人/数字人/原始视频收集或拍摄+Animate人物替换_2053330594825818113.json, 数字人/数字人/数字人板块：Animate视频人物替换工作流_2051238079196872705.json, 视频生成/图生视频/Animate视频人物替换工作流_2069422147151417345.json, 视频生成/图生视频/Wan2.2 Animate V2版-视频转绘动作迁移_1976593221134454786.json, 视频生成/图生视频/Wan2.2 Animate V2版-视频转绘动作迁移_2000375060164640769.json, 视频生成/图生视频/【阡陌】Wan2.2 Animate KJ手动版人物角色替换_1983039224398131201.json, 视频生成/图生视频/【阡陌】Wan2.2 Animate KJ自动版人物角色替换_1982691601984167937.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_371

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（数字人/数字人/原始视频收集或拍摄+Animate人物替换_1998606846065803265.json、数字人/数字人/原始视频收集或拍摄+Animate人物替换_2053330594825818113.json、数字人/数字人/数字人板块：Animate视频人物替换工作流_2051238079196872705.json、视频生成/图生视频/Animate视频人物替换工作流_2069422147151417345.json、视频生成/图生视频/Wan2.2 Animate V2版-视频转绘动作迁移_1976593221134454786.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：63%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPVisionLoader`
- `DrawViTPose`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `PreviewImage`
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
- `BlockifyMask` —— 6/8 个有
- `DrawMaskOnImage` —— 6/8 个有
- `GetNode` —— 6/8 个有
- `ImageFromBatch` —— 6/8 个有
- `ImageResize+` —— 6/8 个有
- `SeCModelLoader` —— 6/8 个有
- `SeCVideoSegmentation` —— 6/8 个有
- `SetNode` —— 6/8 个有
- `WanVideoSetBlockSwap` —— 6/8 个有
- `WanVideoSetLoRAs` —— 6/8 个有
- `easy showAnything` —— 6/8 个有
- `LayerMask: MaskPreview` —— 5/8 个有
- `PointsEditor` —— 5/8 个有
- `ImageConcanate` —— 4/8 个有
- `GrowMask` —— 3/8 个有
- `SaveImage` —— 3/8 个有
- `AddMask` —— 2/8 个有
- `ImageResizeKJv2` —— 2/8 个有
- `LayerMask: MaskGrow` —— 2/8 个有
- `RH_Nano_Banana_Image2Image` —— 2/8 个有
- `SDPoseOODLoader` —— 2/8 个有
- `SDPoseOODProcessor` —— 2/8 个有
- `SeCModelLoader_Ultra-Fast` —— 2/8 个有
- `SeCVideoSegmentation_Ultra-Fast` —— 2/8 个有
- `CR Text` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
