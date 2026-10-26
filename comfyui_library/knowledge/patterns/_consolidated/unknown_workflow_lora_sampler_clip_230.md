---
name: unknown_workflow_lora_sampler_clip_230
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.839
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyHunyuanLatentVideo, Int, JjkText, KSampler, LoraLoaderModelOnly, ModelSamplingAuraFlow, PathchSageAttentionKJ, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/奇怪猫动漫二次元风格图片生成工作流_1978400790064861186.json, 图片生成/文生图/树叶拼图风格 Leaf puzzle style For QwenImage_1974367997215289345.json, 图片生成/文生图/神都猫千问人像摄影lora_1970053781490724865.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_230

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/奇怪猫动漫二次元风格图片生成工作流_1978400790064861186.json、图片生成/文生图/树叶拼图风格 Leaf puzzle style For QwenImage_1974367997215289345.json、图片生成/文生图/神都猫千问人像摄影lora_1970053781490724865.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyHunyuanLatentVideo`
- `Int`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PathchSageAttentionKJ`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConcatText_Zho` —— 2/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 10 - 20 | 3 | 65% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 3 | 53% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 10，观测区间 10 - 20，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，3 个样本
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
