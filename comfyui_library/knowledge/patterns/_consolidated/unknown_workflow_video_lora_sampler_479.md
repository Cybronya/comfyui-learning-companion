---
name: unknown_workflow_video_lora_sampler_479
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.49
common_nodes: [CLIPVisionLoader, GetNode, INTConstant, ImageResizeKJv2, LoadImage, OnnxDetectionModelLoader, PoseAndFaceDetection, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/2037017744700346369.json, 视频生成/图生视频/2037029152141877249.json, 视频生成/图生视频/2037063850230550530.json, 视频生成/图生视频/2043495684220915714.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_479

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/2037017744700346369.json、视频生成/图生视频/2037029152141877249.json、视频生成/图生视频/2037063850230550530.json、视频生成/图生视频/2043495684220915714.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：49%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPVisionLoader`
- `GetNode`
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
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `Bookmark (rgthree)` —— 3/4 个有
- `PlaySound|pysssss` —— 3/4 个有
- `easy cleanGpuUsed` —— 3/4 个有
- `BlockifyMask` —— 2/4 个有
- `DWPreprocessor` —— 2/4 个有
- `DrawMaskOnImage` —— 2/4 个有
- `ResizeImageMaskNode` —— 2/4 个有
- `easy framesEditor` —— 2/4 个有
- `easy imageSizeBySide` —— 2/4 个有
- `easy sam3ModelLoader` —— 2/4 个有
- `easy sam3VideoModelExtraConfig` —— 2/4 个有
- `easy sam3VideoSegmentation` —— 2/4 个有
- `CR Prompt Text` —— 1/4 个有
- `DrawViTPose` —— 1/4 个有
- `Fast Groups Bypasser (rgthree)` —— 1/4 个有
- `GrowMask` —— 1/4 个有
- `GrowMaskWithBlur` —— 1/4 个有
- `ImageConcatMulti` —— 1/4 个有
- `SDPoseOODLoader` —— 1/4 个有
- `SDPoseOODProcessor` —— 1/4 个有
- `VHS_VideoInfoLoaded` —— 1/4 个有
- `YOLOModelLoader` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
