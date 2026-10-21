---
name: text_to_image_lora_sampler_clip_364
type: Text To Image
frequency: 2
level: weak
coverage: 0.389
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, EmptyLatentImage, KSampler, Lora Loader Stack (rgthree), SaveImage, StringFunction|pysssss, VAEDecode, easy int, easy positive, easy seed]
problems: []
missing: [StringFunction|pysssss, easy int, easy positive, Lora Loader Stack (rgthree), easy seed]
members: [图片生成/文生图/1983052029968941058.json, 图片生成/文生图/1983053127081426946.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_364

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/1983052029968941058.json、图片生成/文生图/1983053127081426946.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：39%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `KSampler`
- `Lora Loader Stack (rgthree)`
- `SaveImage`
- `StringFunction|pysssss`
- `VAEDecode`
- `easy int`
- `easy positive`
- `easy seed`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 8 | - | 2 | 100% |
| 采样算法 | euler_ancestral | - | 2 | 100% |
| 调度器 | karras | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |
| 宽度 | 896 | - | 2 | 86% |
| 高度 | 640 | - | 2 | 80% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，2 个样本，一致性 100%
- 调度器 最常用 karras，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 896，样本不足，未给区间，2 个样本，取值集中（一致性 86%）
- 高度 中位数 640，样本不足，未给区间，2 个样本，取值集中（一致性 80%）
- 这些节点还没有知识卡，系统对它们的理解有限：StringFunction|pysssss、easy int、easy positive、Lora Loader Stack (rgthree)、easy seed
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
