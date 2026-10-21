---
name: unknown_workflow_sampler_clip_unet_50
type: Unknown Workflow
frequency: 10
level: strong
coverage: 0.7405
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, Int, KSampler, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: [CR Text, Note Plus (mtb), Seed (rgthree), CR Prompt List]
members: [图片生成/文生图/1952916801829146626.json, 图片生成/文生图/1953016614931337218.json, 图片生成/文生图/1953162182935703553.json, 图片生成/文生图/1953624443421687810.json, 图片生成/文生图/1957736066219606018.json, 图片生成/文生图/1960272130506174465.json, 图片生成/文生图/1966311321211985921.json, "图片生成/文生图/千问文生图(比即梦厉害,内有提示词)_2065148780411973633.json", 图片生成/文生图/视频封面_2102206325894770690.json, 视频生成/图生视频/视频封面_2104049803217952770.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_50

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/文生图/1952916801829146626.json、图片生成/文生图/1953016614931337218.json、图片生成/文生图/1953162182935703553.json、图片生成/文生图/1953624443421687810.json、图片生成/文生图/1957736066219606018.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：74%

## 共有节点

全部 10 个 workflow 都包含：
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
- `CR Text` —— 8/10 个有
- `ImpactInt` —— 7/10 个有
- `Seed (rgthree)` —— 6/10 个有
- `GetNode` —— 5/10 个有
- `SetNode` —— 4/10 个有
- `LoadImage` —— 3/10 个有
- `Note Plus (mtb)` —— 2/10 个有
- `CR Prompt List` —— 1/10 个有
- `ConditioningZeroOut` —— 1/10 个有
- `EmptyImage` —— 1/10 个有
- `JjkText` —— 1/10 个有
- `PreviewImage` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 10 | 100% |
| Prompt 约束强度(CFG) | 4 | 1 - 4 | 10 | 73% |
| 采样算法 | euler | - | 10 | 100% |
| 调度器 | simple | - | 10 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，10 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4，观测区间 1 - 4，10 个样本
- 采样算法 最常用 euler，10 个样本，一致性 100%
- 调度器 最常用 simple，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：CR Text、Note Plus (mtb)、Seed (rgthree)、CR Prompt List
