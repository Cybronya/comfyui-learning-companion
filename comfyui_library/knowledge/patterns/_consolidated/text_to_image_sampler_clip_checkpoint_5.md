---
name: text_to_image_sampler_clip_checkpoint_5
type: Text To Image
frequency: 11
level: moderate
coverage: 0.966909
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, EmptyLatentImage, KSampler, SaveImage, VAEDecode]
problems: [Steps较低可能导致细节不足]
missing: [KSampler //Inspire]
members: [图片生成/文生图/1932244857421819905.json, 图片生成/文生图/1934059209472266242.json, 图片生成/文生图/1939591843099361281.json, 图片生成/文生图/1940024417504366593.json, 图片生成/文生图/1944927998945714178.json, 图片生成/文生图/1945720948937072641.json, 图片生成/文生图/1946045125619314689.json, 图片生成/文生图/1946346552236339202.json, 图片生成/文生图/1947173020802265089.json, 图片生成/文生图/1947277056507793410.json, 图片生成/文生图/文生图动漫工作流_2087082317775982593.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_checkpoint_5

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/文生图/1932244857421819905.json、图片生成/文生图/1934059209472266242.json、图片生成/文生图/1939591843099361281.json、图片生成/文生图/1940024417504366593.json、图片生成/文生图/1944927998945714178.json…）

- **类型**：Text To Image
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 4/11 个有
- `BNK_CLIPTextEncodeAdvanced` —— 2/11 个有
- `KSampler //Inspire` —— 2/11 个有
- `LoraLoaderModelOnly` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 768 | 512 - 1024 | 11 | 82% |
| 高度 | 1024 | 512 - 1536 | 11 | 70% |
| 采样步数 | 20 | 8 - 29 | 11 | 77% |
| Prompt 约束强度(CFG) | 8 | 1 - 8 | 11 | 38% |
| 采样算法 | euler | - | 11 | 55% |
| 调度器 | normal | - | 11 | 55% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 768，观测区间 512 - 1024，11 个样本，取值集中（一致性 82%）
- 高度 中位数 1024，观测区间 512 - 1536，11 个样本
- 采样步数 中位数 20，观测区间 8 - 29，11 个样本
- Prompt 约束强度(CFG) 中位数 8，观测区间 1 - 8，11 个样本，取值分散，一致性仅 38%
- 采样算法 最常用 euler，11 个样本，一致性 55%
- 调度器 最常用 normal，11 个样本，一致性 55%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：KSampler //Inspire
