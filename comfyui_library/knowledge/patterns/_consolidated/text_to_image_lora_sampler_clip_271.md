---
name: text_to_image_lora_sampler_clip_271
type: Text To Image
frequency: 7
level: moderate
coverage: 0.815286
common_nodes: [CLIPLoader, CLIPTextEncode, CR Seed, ConditioningZeroOut, EmptyLatentImage, KSampler, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/krea2双采放大+LORA_2074673669418340353.json, 图片生成/文生图/qwen image2512文生图双采样真实感增强加速_2007460875501834242.json, 图片生成/文生图/qwen+image+2512文生图基础工作流(含丰富提示词示例)_2016839544758341634.json, 图片生成/文生图/千问最新2512文生图工作流（20+提示词演示）_2015617931069100033.json, 图片生成/文生图/最新qwen image 2512文生图基础工作流(含丰富提示词示例)_2013206726975164418.json, 图片生成/文生图/最新qwen image 2512文生图基础工作流(含丰富提示词示例)_2069259090022453250.json, 图片生成/文生图/最新qwen image2512文生图基础工作流_2007337522422095873.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_271

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/krea2双采放大+LORA_2074673669418340353.json、图片生成/文生图/qwen image2512文生图双采样真实感增强加速_2007460875501834242.json、图片生成/文生图/qwen+image+2512文生图基础工作流(含丰富提示词示例)_2016839544758341634.json、图片生成/文生图/千问最新2512文生图工作流（20+提示词演示）_2015617931069100033.json、图片生成/文生图/最新qwen image 2512文生图基础工作流(含丰富提示词示例)_2013206726975164418.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Seed`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CFGNorm` —— 6/7 个有
- `ModelSamplingAuraFlow` —— 6/7 个有
- `Text Multiline` —— 6/7 个有
- `PreviewImage` —— 3/7 个有
- `LatentUpscaleBy` —— 2/7 个有
- `ConditioningKrea2Rebalance` —— 1/7 个有
- `Fast Groups Bypasser (rgthree)` —— 1/7 个有
- `VAEDecodeTiled` —— 1/7 个有
- `basicIn_Sampler` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 8 - 25 | 7 | 65% |
| Prompt 约束强度(CFG) | 4 | 1 - 4 | 7 | 61% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 86% |
| 重绘幅度 | 1 | 0.35 - 1 | 7 | 70% |
| 宽度 | 1024 | 1024 - 1536 | 7 | 80% |
| 高度 | 1536 | 1024 - 1536 | 7 | 81% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 25，观测区间 8 - 25，7 个样本
- Prompt 约束强度(CFG) 中位数 4，观测区间 1 - 4，7 个样本
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 86%
- 重绘幅度 中位数 1，观测区间 0.35 - 1，7 个样本
- 宽度 中位数 1024，观测区间 1024 - 1536，7 个样本
- 高度 中位数 1536，观测区间 1024 - 1536，7 个样本，取值集中（一致性 81%）
