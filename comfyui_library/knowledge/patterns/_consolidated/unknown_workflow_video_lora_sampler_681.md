---
name: unknown_workflow_video_lora_sampler_681
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.665
common_nodes: [GetNode, INTConstant, ImageBatchExtendWithOverlap, ImageResizeKJv2, LoadImage, LoadWanVideoT5TextEncoder, SetNode, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSVIProEmbeds, WanVideoSamplerv2, WanVideoSchedulerv2, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSigmaToStep, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [平台全量/Wan2.2 SVI Pro视频延长循环_2014743840191680513.json, 平台全量/Wan2.2 SVI Pro视频延长循环_2017568074668449793.json, 视频生成/文生视频/Wan.-.2.2.SVI.Pro.-.视频延长循环_2007068274437132290.json, 视频生成/文生视频/Wan.-.2.2.SVI.Pro.·图生视频延长循环_2006963154827354113.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_681

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（平台全量/Wan2.2 SVI Pro视频延长循环_2014743840191680513.json、平台全量/Wan2.2 SVI Pro视频延长循环_2017568074668449793.json、视频生成/文生视频/Wan.-.2.2.SVI.Pro.-.视频延长循环_2007068274437132290.json、视频生成/文生视频/Wan.-.2.2.SVI.Pro.·图生视频延长循环_2006963154827354113.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：66%

## 共有节点

全部 4 个 workflow 都包含：
- `GetNode`
- `INTConstant`
- `ImageBatchExtendWithOverlap`
- `ImageResizeKJv2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `SetNode`
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

**可变部分**（部分 workflow 才有）：
- `GetImageRangeFromBatch` —— 3/4 个有
- `PreviewImage` —— 3/4 个有
- `PrimitiveStringMultiline` —— 3/4 个有
- `SimpleMath+` —— 3/4 个有
- `Text Load Line From File` —— 3/4 个有
- `VHS_LoadVideo` —— 3/4 个有
- `VHS_VideoInfo` —— 3/4 个有
- `easy forLoopEnd` —— 3/4 个有
- `easy forLoopStart` —— 3/4 个有
- `easy ifElse` —— 3/4 个有
- `easy seed` —— 3/4 个有
- `easy batchAnything` —— 2/4 个有
- `JjkText` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
