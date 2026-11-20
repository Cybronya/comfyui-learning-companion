---
name: unknown_workflow_upscale_lora_unet_2
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.845
common_nodes: [CLIPLoader, CreateVideo, LoraLoaderModelOnly, MiniMaxH3Director, MiniMaxH3DirectorRefine, MiniMaxH3MemoryEfficientSageAttentionPatch, PathchSageAttentionKJ, PreviewAny, SaveVideo, UNETLoader, UpscaleModelLoader, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/MiniMax_H3_导演台全能工作流_2098938647834882050.json, 图片生成/文生图/MiniMax_H3_导演台全能工作流_2098996350284296193.json, 图片生成/文生图/MiniMax_H3_导演台全能工作流_2099671659048423426.json, 平台全量/MiniMax H3 导演台全能工作流Pika加速版（自用，原作者AI搅拌手）_2114605659261071361.json, 数字人/数字人/MiniMax H3 Director多功能导演台工作流_2100754161838149633.json, 视频生成/图生视频/（加速）MiniMax H3 导演台全能工作流_2090880598213750786.json, 视频生成/文生视频/MiniMax-H3_Director_导演台多参模式_2101083112175394817.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_unet_2

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/MiniMax_H3_导演台全能工作流_2098938647834882050.json、图片生成/文生图/MiniMax_H3_导演台全能工作流_2098996350284296193.json、图片生成/文生图/MiniMax_H3_导演台全能工作流_2099671659048423426.json、平台全量/MiniMax H3 导演台全能工作流Pika加速版（自用，原作者AI搅拌手）_2114605659261071361.json、数字人/数字人/MiniMax H3 Director多功能导演台工作流_2100754161838149633.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CreateVideo`
- `LoraLoaderModelOnly`
- `MiniMaxH3Director`
- `MiniMaxH3DirectorRefine`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `PathchSageAttentionKJ`
- `PreviewAny`
- `SaveVideo`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `BasicScheduler` —— 6/7 个有
- `EmptyImage` —— 3/7 个有
- `PreviewImage` —— 3/7 个有
- `ModelAttentionBackend` —— 2/7 个有
- `ManualSigmas` —— 1/7 个有
- `MiniMaxH3BlockCacheT8` —— 1/7 个有
- `MiniMaxH3DirectorFaceRefine` —— 1/7 个有
- `MiniMaxH3DirectorSelfLift` —— 1/7 个有
- `MiniMaxH3HybridLoader` —— 1/7 个有
- `SolAttnMiniMax` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
