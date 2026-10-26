---
name: unknown_workflow_upscale_lora_unet_6
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8595
common_nodes: [BasicScheduler, BlockSparseAttention, CLIPLoader, CreateVideo, ExtendIntermediateSigmas, LoadImage, LoraLoaderModelOnly, MiniMaxH3Director, MiniMaxH3DirectorGroupReferenceToVideo, MiniMaxH3DirectorGroupsCombine, ModelAttentionBackend, PlaySound|pysssss, PreviewAny, PrimitiveFloat, PrimitiveStringMultiline, RH_Upscale, SaveImage, SaveVideo, UNETLoader, VAELoader, easy imageChooser, kkVideoFirstLastFrames]
problems: []
missing: []
members: [视频生成/图生视频/minmax h3导演台单采直出+rh upscale1015竖屏_2110432551184719874.json, 视频生成/图生视频/minmax_h3导演台单采直出+rh_upscale1015竖屏_2114184811266002946.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_unet_6

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/minmax h3导演台单采直出+rh upscale1015竖屏_2110432551184719874.json、视频生成/图生视频/minmax_h3导演台单采直出+rh_upscale1015竖屏_2114184811266002946.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：86%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicScheduler`
- `BlockSparseAttention`
- `CLIPLoader`
- `CreateVideo`
- `ExtendIntermediateSigmas`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3Director`
- `MiniMaxH3DirectorGroupReferenceToVideo`
- `MiniMaxH3DirectorGroupsCombine`
- `ModelAttentionBackend`
- `PlaySound|pysssss`
- `PreviewAny`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RH_Upscale`
- `SaveImage`
- `SaveVideo`
- `UNETLoader`
- `VAELoader`
- `easy imageChooser`
- `kkVideoFirstLastFrames`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
