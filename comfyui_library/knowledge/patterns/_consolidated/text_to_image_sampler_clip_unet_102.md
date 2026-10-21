---
name: text_to_image_sampler_clip_unet_102
type: Text To Image
frequency: 4
level: moderate
coverage: 0.96625
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Anima vs Anima Preview3 vs Illustrious 对比测试_2100439731292168193.json, 图片生成/文生图/Anima 示例工作流_2055183971406884866.json, 图片生成/文生图/Anima正式版-文生图工作流个人自用_2076592631471230977.json, 图片生成/文生图/Z-Image VS Z-Image-turbo VS Qwen image 2512_2016491036381552641.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_102

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/Anima vs Anima Preview3 vs Illustrious 对比测试_2100439731292168193.json、图片生成/文生图/Anima 示例工作流_2055183971406884866.json、图片生成/文生图/Anima正式版-文生图工作流个人自用_2076592631471230977.json、图片生成/文生图/Z-Image VS Z-Image-turbo VS Qwen image 2512_2016491036381552641.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 3/4 个有
- `AddLabel` —— 2/4 个有
- `ImageConcanate` —— 2/4 个有
- `LoadImage` —— 2/4 个有
- `easy seed` —— 2/4 个有
- `CheckpointLoaderSimple` —— 1/4 个有
- `ConditioningZeroOut` —— 1/4 个有
- `Fast Groups Bypasser (rgthree)` —— 1/4 个有
- `KSamplerAdvanced` —— 1/4 个有
- `Text` —— 1/4 个有
- `easy promptList` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 12 | 6 - 30 | 3 | 36% |
| Prompt 约束强度(CFG) | 2.5 | 1 - 8 | 4 | 18% |
| 采样算法 | er_sde | - | 4 | 50% |
| 调度器 | beta57 | - | 4 | 25% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 1024 | 896 - 1024 | 4 | 94% |
| 高度 | 1344 | 1024 - 1536 | 4 | 83% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 12，观测区间 6 - 30，3 个样本，取值分散，一致性仅 36%
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 1 - 8，4 个样本，取值分散，一致性仅 18%
- 采样算法 最常用 er_sde，4 个样本，一致性 50%
- 调度器 最常用 beta57，4 个样本，一致性 25%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 896 - 1024，4 个样本，取值集中（一致性 94%）
- 高度 中位数 1344，观测区间 1024 - 1536，4 个样本，取值集中（一致性 83%）
