---
name: unknown_workflow_sampler_clip_unet_378
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.883
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyHunyuanLatentVideo, KSampler, ModelSamplingSD3, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Wan2.2 文生图_1954733353410949121.json, 图片生成/文生图/Wan2.2文生图_1949897867035107330.json, 图片生成/文生图/Wan2.2文生图最优实现_1950849465034940417.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_378

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Wan2.2 文生图_1954733353410949121.json、图片生成/文生图/Wan2.2文生图_1949897867035107330.json、图片生成/文生图/Wan2.2文生图最优实现_1950849465034940417.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyHunyuanLatentVideo`
- `KSampler`
- `ModelSamplingSD3`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 2/3 个有
- `PrimitiveInt` —— 2/3 个有
- `CFGZeroStarAndInit` —— 1/3 个有
- `LoadImage` —— 1/3 个有
- `LoraLoader` —— 1/3 个有
- `String Literal` —— 1/3 个有
- `easy seed` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.8 | - | 1 | 100% |
| LoRA 文本强度 | 0.8 | - | 1 | 100% |
| 采样步数 | 20 | 8 - 20 | 3 | 65% |
| Prompt 约束强度(CFG) | 3.5 | 3.5 - 3.5 | 3 | 100% |
| 采样算法 | euler | - | 3 | 67% |
| 调度器 | bong_tangent | - | 3 | 67% |
| 重绘幅度 | 1 | 0.5 - 1 | 3 | 72% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 20，3 个样本
- Prompt 约束强度(CFG) 中位数 3.5，观测区间 3.5 - 3.5，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 67%
- 调度器 最常用 bong_tangent，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 0.5 - 1，3 个样本
