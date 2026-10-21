---
name: text_to_image_sampler_clip_unet_24
type: Text To Image
frequency: 13
level: moderate
coverage: 0.879154
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/krea2文生图+lora工作流_2094980704298946561.json, 图片生成/文生图/krea2文生图_2069618400707567618.json, 图片生成/文生图/krea2文生图_2069962144506011649.json, 图片生成/文生图/krea2文生图_2087794601284431873.json, 图片生成/文生图/krea2的极致美学_2069777686637142018.json, 图片生成/文生图/pipi-anima-普通采样器基础文生图工作流_2064683171064672258.json, 图片生成/文生图/qwen image  文生图 超细致彩色铅笔_2079613769243774977.json, 图片生成/文生图/qwen image2512文生图双采样真实感增强加速_2007460875501834242.json, 图片生成/文生图/qwen+image+2512文生图基础工作流(含丰富提示词示例)_2016839544758341634.json, 图片生成/文生图/千问最新2512文生图工作流（20+提示词演示）_2015617931069100033.json, 图片生成/文生图/最新qwen image 2512文生图基础工作流(含丰富提示词示例)_2013206726975164418.json, 图片生成/文生图/最新qwen image 2512文生图基础工作流(含丰富提示词示例)_2069259090022453250.json, 图片生成/文生图/最新qwen image2512文生图基础工作流_2007337522422095873.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_24

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/文生图/krea2文生图+lora工作流_2094980704298946561.json、图片生成/文生图/krea2文生图_2069618400707567618.json、图片生成/文生图/krea2文生图_2069962144506011649.json、图片生成/文生图/krea2文生图_2087794601284431873.json、图片生成/文生图/krea2的极致美学_2069777686637142018.json…）

- **类型**：Text To Image
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 13 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 10/13 个有
- `ConditioningZeroOut` —— 9/13 个有
- `ModelSamplingAuraFlow` —— 7/13 个有
- `CFGNorm` —— 6/13 个有
- `CR Seed` —— 6/13 个有
- `Text Multiline` —— 6/13 个有
- `PreviewImage` —— 3/13 个有
- `LatentUpscaleBy` —— 1/13 个有
- `ResolutionSelector` —— 1/13 个有
- `basicIn_Sampler` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 800 - 1920 | 13 | 74% |
| 高度 | 1280 | 1024 - 1536 | 13 | 82% |
| 采样步数 | 10 | 8 - 25 | 13 | 48% |
| Prompt 约束强度(CFG) | 2.5 | 1 - 4.5 | 13 | 44% |
| 采样算法 | euler | - | 13 | 77% |
| 调度器 | simple | - | 13 | 85% |
| 重绘幅度 | 1 | 0.35 - 1 | 13 | 82% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 800 - 1920，13 个样本
- 高度 中位数 1280，观测区间 1024 - 1536，13 个样本，取值集中（一致性 82%）
- 采样步数 中位数 10，观测区间 8 - 25，13 个样本，取值分散，一致性仅 48%
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 1 - 4.5，13 个样本，取值分散，一致性仅 44%
- 采样算法 最常用 euler，13 个样本，一致性 77%
- 调度器 最常用 simple，13 个样本，一致性 85%
- 重绘幅度 中位数 1，观测区间 0.35 - 1，13 个样本，取值集中（一致性 82%）
