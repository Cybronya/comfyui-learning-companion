---
name: sd1_5_text2image_sampler_clip_checkpoint
type: SD1.5 Text2Image
frequency: 3
level: strong
coverage: 1
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, EmptyLatentImage, KSampler, SaveImage, VAEDecode]
problems: []
missing: []
members: [sd15_basic_0.json, sd15_basic_1.json, sd15_basic_2.json]
source: knowledge_consolidation
---

# sd1_5_text2image_sampler_clip_checkpoint

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（sd15_basic_0.json、sd15_basic_1.json、sd15_basic_2.json）

- **类型**：SD1.5 Text2Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：100%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `VAEDecode`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| Prompt 约束强度(CFG) | 7 | 7 - 8 | 3 | 94% |
| 采样步数 | 22 | 20 - 25 | 3 | 91% |
| 采样算法 | euler | - | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- Prompt 约束强度(CFG) 中位数 7，观测区间 7 - 8，3 个样本，取值集中（一致性 94%）
- 采样步数 中位数 22，观测区间 20 - 25，3 个样本，取值集中（一致性 91%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
