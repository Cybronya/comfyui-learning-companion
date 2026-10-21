---
name: text_to_image_sampler_clip_vae_15
type: Text To Image
frequency: 4
level: moderate
coverage: 0.66425
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, ModelSamplingAuraFlow, NunchakuQwenImageDiTLoader, RH_Prompter, SaveImage, TextCombinerTwo, VAEDecode, VAELoader, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: [easy anythingIndexSwitch, easy cleanGpuUsed]
members: [图片生成/文生图/1959819102569312258.json, 图片生成/文生图/1963080046766436353.json, 图片生成/文生图/1972548833475489794.json, 图片生成/文生图/1987531654463950849.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_vae_15

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/1959819102569312258.json、图片生成/文生图/1963080046766436353.json、图片生成/文生图/1972548833475489794.json、图片生成/文生图/1987531654463950849.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：66%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `ModelSamplingAuraFlow`
- `NunchakuQwenImageDiTLoader`
- `RH_Prompter`
- `SaveImage`
- `TextCombinerTwo`
- `VAEDecode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CFGNorm` —— 3/4 个有
- `ConditioningZeroOut` —— 3/4 个有
- `ImpactSwitch` —— 3/4 个有
- `Int` —— 3/4 个有
- `easy anythingIndexSwitch` —— 3/4 个有
- `easy cleanGpuUsed` —— 3/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 20 | 4 | 53% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 4 | 53% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 512 | 512 - 512 | 4 | 100% |
| 高度 | 512 | 512 - 512 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 20，4 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，4 个样本
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 512，观测区间 512 - 512，4 个样本，取值集中（一致性 100%）
- 高度 中位数 512，观测区间 512 - 512，4 个样本，取值集中（一致性 100%）
- 高发问题（3/4 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：easy anythingIndexSwitch、easy cleanGpuUsed
