---
name: unknown_workflow_sampler_clip_unet_242
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.9505
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptySD3LatentImage, KSampler, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/柔美手写字体一键直出 - 媲美即梦 - Qwen-Image文生图_1953769832510574594.json, 图片生成/文生图/通义千问 Qwen-image文生图丨中文渲染系列出图_1953691322731429889.json, 图片生成/文生图/通义千问Qwen-image文生图_1953143788371906562.json, 图片生成/文生图/通义千问Qwen-文生图-8步出图_1959478057306370049.json, 数字人/数字人/Qwen-Image手写体艺术字生成_2072489495907356674.json, 数字人/数字人/电商模特IP Lora_1985545576563548161.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_242

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/柔美手写字体一键直出 - 媲美即梦 - Qwen-Image文生图_1953769832510574594.json、图片生成/文生图/通义千问 Qwen-image文生图丨中文渲染系列出图_1953691322731429889.json、图片生成/文生图/通义千问Qwen-image文生图_1953143788371906562.json、图片生成/文生图/通义千问Qwen-文生图-8步出图_1959478057306370049.json、数字人/数字人/Qwen-Image手写体艺术字生成_2072489495907356674.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptySD3LatentImage`
- `KSampler`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 3/6 个有
- `Int` —— 1/6 个有
- `JjkText` —— 1/6 个有
- `Text Find and Replace` —— 1/6 个有
- `Text Multiline` —— 1/6 个有
- `Text String` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 5 - 20 | 6 | 59% |
| Prompt 约束强度(CFG) | 1.75 | 1 - 2.5 | 6 | 57% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 83% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 5 - 20，6 个样本
- Prompt 约束强度(CFG) 中位数 1.75，观测区间 1 - 2.5，6 个样本
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 83%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
