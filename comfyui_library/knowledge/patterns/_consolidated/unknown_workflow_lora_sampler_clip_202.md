---
name: unknown_workflow_lora_sampler_clip_202
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.885333
common_nodes: [CLIPTextEncode, EmptyLatentImage, KSamplerAdvanced, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Z-image 双模型双采样非常版_2048543200930963458.json, 图片生成/文生图/文生图-Qwen2512-真实幻想_2036717743843581954.json, 图片生成/文生图/简单高效写实文生图_2075816029682491393.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_202

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Z-image 双模型双采样非常版_2048543200930963458.json、图片生成/文生图/文生图-Qwen2512-真实幻想_2036717743843581954.json、图片生成/文生图/简单高效写实文生图_2075816029682491393.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSamplerAdvanced`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `CLIPLoaderGGUF` —— 1/3 个有
- `CompressImages` —— 1/3 个有
- `Fast Groups Bypasser (rgthree)` —— 1/3 个有
- `easy clearCacheAll` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 768 - 1080 | 3 | 86% |
| 高度 | 1024 | 1024 - 1920 | 3 | 68% |
| 采样步数 | randomize | - | 3 | 100% |
| Prompt 约束强度(CFG) | 9 | 9 - 12 | 3 | 86% |
| 采样算法 | 1 | 1 - 1 | 3 | 100% |
| 调度器 | euler | - | 3 | 67% |
| 重绘幅度 | FlowMatchEulerDiscreteScheduler | - | 3 | 33% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 768 - 1080，3 个样本，取值集中（一致性 86%）
- 高度 中位数 1024，观测区间 1024 - 1920，3 个样本
- 采样步数 最常用 randomize，3 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 9，观测区间 9 - 12，3 个样本，取值集中（一致性 86%）
- 采样算法 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，3 个样本，一致性 67%
- 重绘幅度 最常用 FlowMatchEulerDiscreteScheduler，3 个样本，一致性 33%
