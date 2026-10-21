---
name: unknown_workflow_sampler_clip_unet_127
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.8932
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/AI分镜脚本生成器工作流_2098422425359839233.json, 图片生成/文生图/AI漫剧分镜生成器-故事文案转提示词_2094268434623320065.json, 图片生成/文生图/Dark Beast Z 黑兽 V2.5_2009627862525026305.json, 图片生成/文生图/Ernie 生图工作流(PE)_2048933090613010434.json, 图片生成/文生图/Ernie-Turbo 8步生图_2048944617202130945.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_127

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/AI分镜脚本生成器工作流_2098422425359839233.json、图片生成/文生图/AI漫剧分镜生成器-故事文案转提示词_2094268434623320065.json、图片生成/文生图/Dark Beast Z 黑兽 V2.5_2009627862525026305.json、图片生成/文生图/Ernie 生图工作流(PE)_2048933090613010434.json、图片生成/文生图/Ernie-Turbo 8步生图_2048944617202130945.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `TextGenerate` —— 4/5 个有
- `EmptySD3LatentImage` —— 3/5 个有
- `JWInteger` —— 3/5 个有
- `PreviewAny` —— 3/5 个有
- `PrimitiveStringMultiline` —— 3/5 个有
- `CR Prompt Text` —— 2/5 个有
- `EmptyFlux2LatentImage` —— 2/5 个有
- `StringReplace` —— 2/5 个有
- `TextEncodeQwenImageEditPlus` —— 2/5 个有
- `ConditioningZeroOut` —— 1/5 个有
- `Seed (rgthree)` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 24 | 8 - 50 | 5 | 35% |
| Prompt 约束强度(CFG) | 2.5 | 1 - 4 | 5 | 49% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 80% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 24，观测区间 8 - 50，5 个样本，取值分散，一致性仅 35%
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 1 - 4，5 个样本，取值分散，一致性仅 49%
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
