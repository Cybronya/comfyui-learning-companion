---
name: unknown_workflow_video_lora_sampler_681
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.403667
common_nodes: [CLIPVisionLoader, GetNode, INTConstant, ImageResizeKJv2, LoadImage, OnnxDetectionModelLoader, PlaySound|pysssss, PreviewImage, PrimitiveFloat, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/2022695116523180034.json, 视频生成/图生视频/2003413399671377922.json, 视频生成/图生视频/2042773742413156353.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_681

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/2022695116523180034.json、视频生成/图生视频/2003413399671377922.json、视频生成/图生视频/2042773742413156353.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：40%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPVisionLoader`
- `GetNode`
- `INTConstant`
- `ImageResizeKJv2`
- `LoadImage`
- `OnnxDetectionModelLoader`
- `PlaySound|pysssss`
- `PreviewImage`
- `PrimitiveFloat`
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
- `PoseAndFaceDetection` —— 2/3 个有
- `RHHiddenNodes` —— 2/3 个有
- `SDPoseOODLoader` —— 2/3 个有
- `SDPoseOODProcessor` —— 2/3 个有
- `YOLOModelLoader` —— 2/3 个有
- `easy showAnything` —— 2/3 个有
- `BBoxYOLO` —— 1/3 个有
- `CheckpointLoaderSimple` —— 1/3 个有
- `DWPreprocessor` —— 1/3 个有
- `DrawViTPose` —— 1/3 个有
- `GetImageRangeFromBatch` —— 1/3 个有
- `NumberComparison` —— 1/3 个有
- `PixelPerfectResolution` —— 1/3 个有
- `SDPoseDrawKeypoints` —— 1/3 个有
- `SDPoseKeypointExtractor` —— 1/3 个有
- `VHS_VideoInfo` —— 1/3 个有
- `easy ifElse` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
