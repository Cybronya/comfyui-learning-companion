---
name: text_to_image_lora_sampler_clip_221
type: Text To Image
frequency: 3
level: strong
coverage: 0.717333
common_nodes: [CLIPTextEncode, DualCLIPLoader, EmptyLatentImage, FluxGuidance, KSampler, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: [CR Text Input Switch (4 way), Random Number, easy cleanGpuUsed]
members: [图片生成/文生图/1908812406955646977.json, 图片生成/文生图/1950688204880039937.json, 图片生成/文生图/1976848182871314434.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_221

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/1908812406955646977.json、图片生成/文生图/1950688204880039937.json、图片生成/文生图/1976848182871314434.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：72%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `FluxGuidance`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `easy cleanGpuUsed` —— 2/3 个有
- `CR Text Input Switch (4 way)` —— 1/3 个有
- `JjkText` —— 1/3 个有
- `Random Number` —— 1/3 个有
- `ShowText|pysssss` —— 1/3 个有
- `TeaCache` —— 1/3 个有
- `easy showAnything` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 720 | 720 - 1024 | 3 | 83% |
| 高度 | 1280 | 1280 - 1536 | 3 | 91% |
| 采样步数 | 20 | 8 - 20 | 3 | 65% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 720，观测区间 720 - 1024，3 个样本，取值集中（一致性 83%）
- 高度 中位数 1280，观测区间 1280 - 1536，3 个样本，取值集中（一致性 91%）
- 采样步数 中位数 20，观测区间 8 - 20，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：CR Text Input Switch (4 way)、Random Number、easy cleanGpuUsed
