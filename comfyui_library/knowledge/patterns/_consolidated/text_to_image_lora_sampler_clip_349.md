---
name: text_to_image_lora_sampler_clip_349
type: Text To Image
frequency: 6
level: moderate
coverage: 0.812333
common_nodes: [CFGNorm, CLIPLoader, CLIPTextEncode, CR Seed, ConditioningZeroOut, EmptyLatentImage, KSampler, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, Text Multiline, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/qwen image2512文生图双采样真实感增强加速_2007460875501834242.json, 图片生成/文生图/qwen+image+2512文生图基础工作流(含丰富提示词示例)_2016839544758341634.json, 图片生成/文生图/千问最新2512文生图工作流（20+提示词演示）_2015617931069100033.json, 图片生成/文生图/最新qwen image 2512文生图基础工作流(含丰富提示词示例)_2013206726975164418.json, 图片生成/文生图/最新qwen image 2512文生图基础工作流(含丰富提示词示例)_2069259090022453250.json, 图片生成/文生图/最新qwen image2512文生图基础工作流_2007337522422095873.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_349

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/qwen image2512文生图双采样真实感增强加速_2007460875501834242.json、图片生成/文生图/qwen+image+2512文生图基础工作流(含丰富提示词示例)_2016839544758341634.json、图片生成/文生图/千问最新2512文生图工作流（20+提示词演示）_2015617931069100033.json、图片生成/文生图/最新qwen image 2512文生图基础工作流(含丰富提示词示例)_2013206726975164418.json、图片生成/文生图/最新qwen image 2512文生图基础工作流(含丰富提示词示例)_2069259090022453250.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：81%

## 共有节点

全部 6 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Seed`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `Text Multiline`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 2/6 个有
- `LatentUpscaleBy` —— 1/6 个有
- `basicIn_Sampler` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 10 - 25 | 6 | 75% |
| Prompt 约束强度(CFG) | 4 | 1.5 - 4 | 6 | 74% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 83% |
| 重绘幅度 | 1 | 0.35 - 1 | 6 | 73% |
| 宽度 | 1280 | 1024 - 1536 | 6 | 80% |
| 高度 | 1280 | 1024 - 1536 | 6 | 80% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 10 - 25，6 个样本
- Prompt 约束强度(CFG) 中位数 4，观测区间 1.5 - 4，6 个样本
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 83%
- 重绘幅度 中位数 1，观测区间 0.35 - 1，6 个样本
- 宽度 中位数 1280，观测区间 1024 - 1536，6 个样本，取值集中（一致性 80%）
- 高度 中位数 1280，观测区间 1024 - 1536，6 个样本，取值集中（一致性 80%）
