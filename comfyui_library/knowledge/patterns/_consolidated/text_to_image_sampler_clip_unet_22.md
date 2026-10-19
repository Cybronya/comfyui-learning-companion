---
name: text_to_image_sampler_clip_unet_22
type: Text To Image
frequency: 3
level: moderate
coverage: 0.727333
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, ImpactSwitch, KSampler, ModelSamplingAuraFlow, SaveImage, Textbox, UNETLoader, VAEDecode, VAELoader, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: [LayerUtility: PurgeVRAM, StringFunction|pysssss, easy cleanGpuUsed]
members: [图片生成/文生图/1972552564665479169.json, 图片生成/文生图/1986676312603557890.json, 图片生成/文生图/1987705778691878913.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_22

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/1972552564665479169.json、图片生成/文生图/1986676312603557890.json、图片生成/文生图/1987705778691878913.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：73%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `ImpactSwitch`
- `KSampler`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `Textbox`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `PrimitiveString` —— 2/3 个有
- `LayerUtility: PurgeVRAM` —— 1/3 个有
- `LoadImage` —— 1/3 个有
- `LoraLoader` —— 1/3 个有
- `LoraLoaderModelOnly` —— 1/3 个有
- `Qwen3_VQA` —— 1/3 个有
- `StringFunction|pysssss` —— 1/3 个有
- `easy cleanGpuUsed` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 960 | 960 - 1024 | 3 | 97% |
| 高度 | 1280 | 1024 - 1280 | 3 | 90% |
| 采样步数 | 20 | 8 - 30 | 3 | 53% |
| Prompt 约束强度(CFG) | 2.5 | 1 - 2.5 | 3 | 65% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 960，观测区间 960 - 1024，3 个样本，取值集中（一致性 97%）
- 高度 中位数 1280，观测区间 1024 - 1280，3 个样本，取值集中（一致性 90%）
- 采样步数 中位数 20，观测区间 8 - 30，3 个样本
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 1 - 2.5，3 个样本
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: PurgeVRAM、StringFunction|pysssss、easy cleanGpuUsed
