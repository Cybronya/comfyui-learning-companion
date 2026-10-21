---
name: text_to_image_sampler_clip_unet_116
type: Text To Image
frequency: 4
level: strong
coverage: 0.9565
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/文生图V2_2006090856985530370.json, 图片生成/文生图/文生图_2002461454764765185.json, 图片生成/文生图/文生图_2083074458058846209.json, 图片生成/文生图/节点系列10-PromptList节点_2012025090799575042.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_116

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/文生图V2_2006090856985530370.json、图片生成/文生图/文生图_2002461454764765185.json、图片生成/文生图/文生图_2083074458058846209.json、图片生成/文生图/节点系列10-PromptList节点_2012025090799575042.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：96%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 3/4 个有
- `easy promptList` —— 3/4 个有
- `ModelSamplingAuraFlow` —— 2/4 个有
- `ttN concat` —— 2/4 个有
- `Lora Loader Stack (rgthree)` —— 1/4 个有
- `Seed (rgthree)` —— 1/4 个有
- `Text List to Text` —— 1/4 个有
- `easy showAnything` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | 8 - 9 | 4 | 95% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 75% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 872 | 720 - 1280 | 4 | 75% |
| 高度 | 1408 | 1280 - 1560 | 4 | 91% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 9，观测区间 8 - 9，4 个样本，取值集中（一致性 95%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 75%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 872，观测区间 720 - 1280，4 个样本
- 高度 中位数 1408，观测区间 1280 - 1560，4 个样本，取值集中（一致性 91%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
