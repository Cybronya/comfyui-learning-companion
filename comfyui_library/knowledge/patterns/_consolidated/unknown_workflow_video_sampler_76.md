---
name: unknown_workflow_video_sampler_76
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.862
common_nodes: [GetImageRangeFromBatch, GetImageSizeAndCount, GetImageSizeRatio, ImageConcatMulti, ImageResize+, Int, LayerUtility: ImageScaleByAspectRatio V2, LoadWanVideoT5TextEncoder, MathExpression|pysssss, PrimitiveStringMultiline, VHS_LoadVideo, VHS_VideoCombine, WanVideoAddFlashVSRInput, WanVideoBlockSwap, WanVideoContextOptions, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoExtraModelSelect, WanVideoFlashVSRDecoderLoader, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings]
problems: []
missing: []
members: [平台全量/视频高清修复视频极速版wan_1979807382991704065.json, 平台全量/高清修复视频工作流_1984455366069141506.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_76

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/视频高清修复视频极速版wan_1979807382991704065.json、平台全量/高清修复视频工作流_1984455366069141506.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：86%

## 共有节点

全部 2 个 workflow 都包含：
- `GetImageRangeFromBatch`
- `GetImageSizeAndCount`
- `GetImageSizeRatio`
- `ImageConcatMulti`
- `ImageResize+`
- `Int`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadWanVideoT5TextEncoder`
- `MathExpression|pysssss`
- `PrimitiveStringMultiline`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoAddFlashVSRInput`
- `WanVideoBlockSwap`
- `WanVideoContextOptions`
- `WanVideoDecode`
- `WanVideoEmptyEmbeds`
- `WanVideoExtraModelSelect`
- `WanVideoFlashVSRDecoderLoader`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
