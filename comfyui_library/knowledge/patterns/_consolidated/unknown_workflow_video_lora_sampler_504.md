---
name: unknown_workflow_video_lora_sampler_504
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.561
common_nodes: [CLIPVisionLoader, DWPreprocessor, FaceMaskFromPoseKeypoints, GetNode, ImageConcatMulti, ImageCropByMaskAndResize, ImageFromBatch, ImageResizeKJv2, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, MathExpression|pysssss, PreviewImage, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/WanAnimate 姿势参考（KJ版）_1969999696024510466.json, 视频生成/图生视频/视频编辑视频转绘视频主体替换Wan-Animate（KJ）_1969558465037410306.json, 视频生成/图生视频/（KJ版）主体替换WanAnimate_1969378063396073473.json, 视频生成/图生视频/（KJ版）姿势参考WanAnimate_1969410370047799298.json, 视频生成/图生视频/（KJ版）姿势参考WanAnimate_1970135564894826498.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_504

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/WanAnimate 姿势参考（KJ版）_1969999696024510466.json、视频生成/图生视频/视频编辑视频转绘视频主体替换Wan-Animate（KJ）_1969558465037410306.json、视频生成/图生视频/（KJ版）主体替换WanAnimate_1969378063396073473.json、视频生成/图生视频/（KJ版）姿势参考WanAnimate_1969410370047799298.json、视频生成/图生视频/（KJ版）姿势参考WanAnimate_1970135564894826498.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：56%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPVisionLoader`
- `DWPreprocessor`
- `FaceMaskFromPoseKeypoints`
- `GetNode`
- `ImageConcatMulti`
- `ImageCropByMaskAndResize`
- `ImageFromBatch`
- `ImageResizeKJv2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `MathExpression|pysssss`
- `PreviewImage`
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
- `WanVideoTextEncodeCached`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `BlockifyMask` —— 4/5 个有
- `DrawMaskOnImage` —— 4/5 个有
- `GrowMask` —— 4/5 个有
- `ImpactInt` —— 4/5 个有
- `Int` —— 4/5 个有
- `LayerMask: LoadSegmentAnythingModels` —— 4/5 个有
- `LayerMask: SegmentAnythingUltra V3` —— 4/5 个有
- `Textbox` —— 4/5 个有
- `WanVideoContextOptions` —— 4/5 个有
- `WanVideoSetLoRAs` —— 4/5 个有
- `Anything Everywhere3` —— 1/5 个有
- `PrimitiveInt` —— 1/5 个有
- `PrimitiveStringMultiline` —— 1/5 个有
- `easy cleanGpuUsed` —— 1/5 个有
- `easy showAnything` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
