---
name: unknown_workflow_video_upscale_lora_10
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.8525
common_nodes: [BasicScheduler, BlockSparseAttention, CLIPLoader, ExtendIntermediateSigmas, LoraLoaderModelOnly, MiniMaxH3Director, MiniMaxH3DirectorFaceRefine, MiniMaxH3DirectorRefine, MiniMaxH3DirectorSelfLift, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3SigmaShift, ModelAttentionBackend, PathchSageAttentionKJ, PreviewAny, PrimitiveStringMultiline, UNETLoader, UpscaleModelLoader, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/B_H3五分钟_参考主体_22帧_重绘0.5_2108831912314884097.json, 视频生成/图生视频/H3长视频生成-maod-字节4步模型_2109960679385026561.json, 视频生成/图生视频/允希_V8.2_闭唇正脸_一秒轻触_主体参考_单图外接_2111022282851315713.json, 视频生成/图生视频/允希_V8.2_闭唇正脸_一秒轻触_首尾帧_单图外接_2111022898654830593.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_lora_10

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/B_H3五分钟_参考主体_22帧_重绘0.5_2108831912314884097.json、视频生成/图生视频/H3长视频生成-maod-字节4步模型_2109960679385026561.json、视频生成/图生视频/允希_V8.2_闭唇正脸_一秒轻触_主体参考_单图外接_2111022282851315713.json、视频生成/图生视频/允希_V8.2_闭唇正脸_一秒轻触_首尾帧_单图外接_2111022898654830593.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicScheduler`
- `BlockSparseAttention`
- `CLIPLoader`
- `ExtendIntermediateSigmas`
- `LoraLoaderModelOnly`
- `MiniMaxH3Director`
- `MiniMaxH3DirectorFaceRefine`
- `MiniMaxH3DirectorRefine`
- `MiniMaxH3DirectorSelfLift`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3SigmaShift`
- `ModelAttentionBackend`
- `PathchSageAttentionKJ`
- `PreviewAny`
- `PrimitiveStringMultiline`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 3/4 个有
- `MiniMaxH3DirectorGroupsCombine` —— 3/4 个有
- `CreateVideo` —— 2/4 个有
- `MiniMaxH3DirectorGroupReferenceToVideo` —— 2/4 个有
- `ModelPreviewOverrideKJ` —— 2/4 个有
- `SaveVideo` —— 2/4 个有
- `Video Slice` —— 2/4 个有
- `easy cleanGpuUsed` —— 2/4 个有
- `MiniMaxH3DirectorGroupImageToVideo` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
