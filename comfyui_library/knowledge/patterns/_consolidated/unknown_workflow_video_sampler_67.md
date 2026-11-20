---
name: unknown_workflow_video_sampler_67
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.5485
common_nodes: [GetImageRangeFromBatch, GetImageSizeAndCount, GetNode, ImageConcatMulti, LayerUtility: ImageScaleByAspectRatio V2, LoadWanVideoT5TextEncoder, MathExpression|pysssss, PreviewAny, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoAddFlashVSRInput, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoExtraModelSelect, WanVideoFlashVSRDecoderLoader, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, easy batchAnything, easy cleanGpuUsed, easy compare, easy convertAnything, easy float, easy forLoopEnd, easy forLoopStart, easy ifElse, easy int]
problems: []
missing: []
members: [平台全量/45.[超清细节修复] 低分辨率和模糊视频的FlashVSR长视频工作流_1979488880019804161.json, 平台全量/模糊视频高清修复FlashVSR长视频_1981295172204003330.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_67

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/45.[超清细节修复] 低分辨率和模糊视频的FlashVSR长视频工作流_1979488880019804161.json、平台全量/模糊视频高清修复FlashVSR长视频_1981295172204003330.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：55%

## 共有节点

全部 2 个 workflow 都包含：
- `GetImageRangeFromBatch`
- `GetImageSizeAndCount`
- `GetNode`
- `ImageConcatMulti`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadWanVideoT5TextEncoder`
- `MathExpression|pysssss`
- `PreviewAny`
- `SetNode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoAddFlashVSRInput`
- `WanVideoDecode`
- `WanVideoEmptyEmbeds`
- `WanVideoExtraModelSelect`
- `WanVideoFlashVSRDecoderLoader`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `easy batchAnything`
- `easy cleanGpuUsed`
- `easy compare`
- `easy convertAnything`
- `easy float`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy ifElse`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `Bjornulf_ShowInt` —— 1/2 个有
- `ColorMatch` —— 1/2 个有
- `Int` —— 1/2 个有
- `JjkText` —— 1/2 个有
- `WanVideoBlockSwap` —— 1/2 个有
- `WanVideoContextOptions` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
