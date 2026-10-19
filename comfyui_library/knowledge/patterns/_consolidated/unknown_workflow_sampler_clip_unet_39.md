---
name: unknown_workflow_sampler_clip_unet_39
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.752143
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, Int, KSampler, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: [CR Text, Note Plus (mtb), Seed (rgthree), CR Prompt List]
members: [图片生成/文生图/1952916801829146626.json, 图片生成/文生图/1953016614931337218.json, 图片生成/文生图/1953624443421687810.json, 图片生成/文生图/1957736066219606018.json, 图片生成/文生图/1960272130506174465.json, 图片生成/文生图/1966311321211985921.json, 视频生成/图生视频/视频封面_2104049803217952770.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_39

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/1952916801829146626.json、图片生成/文生图/1953016614931337218.json、图片生成/文生图/1953624443421687810.json、图片生成/文生图/1957736066219606018.json、图片生成/文生图/1960272130506174465.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：75%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `Int`
- `KSampler`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 6/7 个有
- `ImpactInt` —— 5/7 个有
- `Seed (rgthree)` —— 4/7 个有
- `GetNode` —— 3/7 个有
- `LoadImage` —— 2/7 个有
- `SetNode` —— 2/7 个有
- `CR Prompt List` —— 1/7 个有
- `EmptyImage` —— 1/7 个有
- `JjkText` —— 1/7 个有
- `Note Plus (mtb)` —— 1/7 个有
- `PreviewImage` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 7 | 100% |
| Prompt 约束强度(CFG) | 4 | 1 - 4 | 7 | 71% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4，观测区间 1 - 4，7 个样本
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：CR Text、Note Plus (mtb)、Seed (rgthree)、CR Prompt List
