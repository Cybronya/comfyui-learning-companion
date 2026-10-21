---
name: unknown_workflow_video_lora_sampler_851
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8625
common_nodes: [CLIPVisionLoader, GetImageSizeAndCount, ImageFromBatch, ImageSmartSharpen+, Int, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM, LoadImage, LoadWanVideoT5TextEncoder, MathExpression|pysssss, PreviewImage, Text Load Line From File, Text Multiline, VHS_VideoCombine, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader, easy batchAnything, easy cleanGpuUsed, easy clearCacheAll, easy forLoopEnd, easy forLoopStart, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/1949137084427247618.json, 视频生成/文生视频/1954571377661636609.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_851

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/1949137084427247618.json、视频生成/文生视频/1954571377661636609.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：86%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPVisionLoader`
- `GetImageSizeAndCount`
- `ImageFromBatch`
- `ImageSmartSharpen+`
- `Int`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MathExpression|pysssss`
- `PreviewImage`
- `Text Load Line From File`
- `Text Multiline`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`
- `easy batchAnything`
- `easy cleanGpuUsed`
- `easy clearCacheAll`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CR Image Input Switch` —— 1/2 个有
- `ConditionalTextOutput` —— 1/2 个有
- `EmptyImage` —— 1/2 个有
- `GetImageSize` —— 1/2 个有
- `GetNode` —— 1/2 个有
- `ImageResizeKJv2` —— 1/2 个有
- `MergeLayers` —— 1/2 个有
- `NewLayer` —— 1/2 个有
- `SetNode` —— 1/2 个有
- `SimpleMath+` —— 1/2 个有
- `WanVideoBlockSwap` —— 1/2 个有
- `WanVideoClipVisionEncode` —— 1/2 个有
- `WanVideoImageClipEncode` —— 1/2 个有
- `WanVideoImageToVideoEncode` —— 1/2 个有
- `WanVideoTorchCompileSettings` —— 1/2 个有
- `easy convertAnything` —— 1/2 个有
- `easy imageRemBg` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
