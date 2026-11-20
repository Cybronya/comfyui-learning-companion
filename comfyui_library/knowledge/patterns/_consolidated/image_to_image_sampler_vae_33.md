---
name: image_to_image_sampler_vae_33
type: Image To Image
frequency: 3
level: strong
coverage: 0.955333
common_nodes: [Int, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, RHHiddenNodes, SaveImage, TextEncodeQwenImageEditPlus, VAEDecode, VAEEncode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/电商模特摆姿1图分裂12图（鞋子）千问2511_2098923123256152066.json, 图片生成/图生图/电商模特摆姿分裂图V3.0（鞋子，服装，包）_1980818100138459137.json, 图片生成/图生图/电商模特摆姿分裂图V3.0（鞋子，服装，包）_1984064390028787714.json]
source: knowledge_consolidation
---

# image_to_image_sampler_vae_33

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/电商模特摆姿1图分裂12图（鞋子）千问2511_2098923123256152066.json、图片生成/图生图/电商模特摆姿分裂图V3.0（鞋子，服装，包）_1980818100138459137.json、图片生成/图生图/电商模特摆姿分裂图V3.0（鞋子，服装，包）_1984064390028787714.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：96%

## 共有节点

全部 3 个 workflow 都包含：
- `Int`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `RHHiddenNodes`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode`
- `VAEEncode`

**可变部分**（部分 workflow 才有）：
- `ProcessString` —— 2/3 个有
- `ShellAgentPluginOutputText` —— 2/3 个有
- `easy promptLine` —— 2/3 个有
- `easy showAnything` —— 2/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | sa_solver | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 sa_solver，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
