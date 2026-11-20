---
name: unknown_workflow_video_lora_sampler_1018
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.647
common_nodes: [GetNode, INTConstant, ImageBatchExtendWithOverlap, ImageResizeKJv2, LoadImage, LoadWanVideoT5TextEncoder, PrimitiveStringMultiline, SetNode, Text Load Line From File, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSVIProEmbeds, WanVideoSamplerv2, WanVideoSchedulerv2, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSigmaToStep, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader, easy forLoopEnd, easy forLoopStart, easy seed]
problems: []
missing: []
members: [视频生成/文生视频/Wan.-.2.2.SVI.Pro.-.视频延长循环_2007068274437132290.json, 视频生成/文生视频/Wan.-.2.2.SVI.Pro.·图生视频延长循环_2006963154827354113.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_1018

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/文生视频/Wan.-.2.2.SVI.Pro.-.视频延长循环_2007068274437132290.json、视频生成/文生视频/Wan.-.2.2.SVI.Pro.·图生视频延长循环_2006963154827354113.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：65%

## 共有节点

全部 2 个 workflow 都包含：
- `GetNode`
- `INTConstant`
- `ImageBatchExtendWithOverlap`
- `ImageResizeKJv2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `PrimitiveStringMultiline`
- `SetNode`
- `Text Load Line From File`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSVIProEmbeds`
- `WanVideoSamplerv2`
- `WanVideoSchedulerv2`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSigmaToStep`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy seed`

**可变部分**（部分 workflow 才有）：
- `GetImageRangeFromBatch` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `SimpleMath+` —— 1/2 个有
- `VHS_LoadVideo` —— 1/2 个有
- `VHS_VideoInfo` —— 1/2 个有
- `easy batchAnything` —— 1/2 个有
- `easy ifElse` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
