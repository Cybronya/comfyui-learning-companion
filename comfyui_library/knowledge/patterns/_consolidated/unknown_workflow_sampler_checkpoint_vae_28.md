---
name: unknown_workflow_sampler_checkpoint_vae_28
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.87375
common_nodes: [CheckpointLoaderSimple, ConditioningZeroOut, KSampler, LoadImage, PrimitiveStringMultiline, SaveImage, TextEncodeQwenImageEditPlusAdvance_lrzjason, VAEDecode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/AI短剧角色换装换动作 Qwen-image-edit2511+SeedVR2高清多图参考图生图_1958122766740369410.json, 图片生成/图生图/AI短剧角色换装换动作-图生图-邻家AI大女孩_2043716982956105729.json, 图片生成/图生图/Qwen-i2i_2068695645808062465.json, 平台全量/单图_双图_多图 姿势参考AI漫剧短剧角色换装换动作 Qwen-image-edit2511+See_2033710447425232898.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_checkpoint_vae_28

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/AI短剧角色换装换动作 Qwen-image-edit2511+SeedVR2高清多图参考图生图_1958122766740369410.json、图片生成/图生图/AI短剧角色换装换动作-图生图-邻家AI大女孩_2043716982956105729.json、图片生成/图生图/Qwen-i2i_2068695645808062465.json、平台全量/单图_双图_多图 姿势参考AI漫剧短剧角色换装换动作 Qwen-image-edit2511+See_2033710447425232898.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 4 个 workflow 都包含：
- `CheckpointLoaderSimple`
- `ConditioningZeroOut`
- `KSampler`
- `LoadImage`
- `PrimitiveStringMultiline`
- `SaveImage`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `WujiCleaner` —— 3/4 个有
- `WujiUpscaler` —— 3/4 个有
- `Fast Groups Bypasser (rgthree)` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 8 | 4 | 75% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | er_sde | - | 4 | 75% |
| 调度器 | beta57 | - | 4 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 8，4 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，4 个样本，一致性 75%
- 调度器 最常用 beta57，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
