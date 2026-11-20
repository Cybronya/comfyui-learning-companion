---
name: unknown_workflow_video_lora_sampler_924
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.537
common_nodes: [CM_FloatToInt, GetImageRangeFromBatch, GetNode, GrowMaskWithBlur, ImageConcanate, ImageResizeKJv2, LoadImage, MaskPreview, MochaEmbeds, OnnxDetectionModelLoader, PoseAndFaceDetection, PreviewImage, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVAELoader, easy float, easy int]
problems: []
missing: []
members: [视频生成/图生视频/mocha_指定人物_1990430709800198145.json, 视频生成/图生视频/mocha单人物替换，无需标点_1983354803063562242.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_924

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/mocha_指定人物_1990430709800198145.json、视频生成/图生视频/mocha单人物替换，无需标点_1983354803063562242.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：54%

## 共有节点

全部 2 个 workflow 都包含：
- `CM_FloatToInt`
- `GetImageRangeFromBatch`
- `GetNode`
- `GrowMaskWithBlur`
- `ImageConcanate`
- `ImageResizeKJv2`
- `LoadImage`
- `MaskPreview`
- `MochaEmbeds`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `PreviewImage`
- `SetNode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoTextEncodeCached`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `easy float`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `DownloadAndLoadSAM2Model` —— 1/2 个有
- `PrimitiveStringMultiline` —— 1/2 个有
- `Sa2VANodeTpl` —— 1/2 个有
- `Sam2Segmentation` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
