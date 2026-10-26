---
name: unknown_workflow_sampler_unet_vae_238
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.89125
common_nodes: [CLIPLoader, KSampler, LoadImage, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen-image2.1+Vosr2+DLSS5角色定妆五视图_2104424127888187394.json, 图片生成/图生图/Qwen-image2.1-动作迁移_2102372877952704514.json, 图片生成/图生图/Qwen-image2.1-动作迁移_2112535992015089665.json, 图片生成/图生图/qwen2.1 图生图_2102013171056857089.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_238

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Qwen-image2.1+Vosr2+DLSS5角色定妆五视图_2104424127888187394.json、图片生成/图生图/Qwen-image2.1-动作迁移_2102372877952704514.json、图片生成/图生图/Qwen-image2.1-动作迁移_2112535992015089665.json、图片生成/图生图/qwen2.1 图生图_2102013171056857089.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 3/4 个有
- `BodyRatioMapperSDPoseRender` —— 2/4 个有
- `CR Prompt Text` —— 2/4 个有
- `CheckpointLoaderSimple` —— 2/4 个有
- `EmptyLatentImage` —— 2/4 个有
- `Image Comparer (rgthree)` —— 2/4 个有
- `Int` —— 2/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/4 个有
- `ResolutionSelector` —— 2/4 个有
- `SDPoseKeypointExtractor` —— 2/4 个有
- `ComfySwitchNode` —— 1/4 个有
- `Text Multiline` —— 1/4 个有
- `WujiUpscaler2` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1292 | - | 2 | 79% |
| 高度 | 964 | - | 2 | 94% |
| 采样步数 | 25 | 8 - 50 | 4 | 45% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1292，样本不足，未给区间，2 个样本
- 高度 中位数 964，样本不足，未给区间，2 个样本，取值集中（一致性 94%）
- 采样步数 中位数 25，观测区间 8 - 50，4 个样本，取值分散，一致性仅 45%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
