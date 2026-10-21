---
name: unknown_workflow_lora_sampler_clip_156
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9485
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyHunyuanLatentVideo, KSampler, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: [CR Text, CR SDXL Aspect Ratio]
members: [图片生成/文生图/1949870290421637121.json, 图片生成/文生图/1951184476380536834.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_156

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/1949870290421637121.json、图片生成/文生图/1951184476380536834.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：95%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyHunyuanLatentVideo`
- `KSampler`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `BetterFilmGrain` —— 1/2 个有
- `CR SDXL Aspect Ratio` —— 1/2 个有
- `CR Text` —— 1/2 个有
- `EsesImageEffectBloom` —— 1/2 个有
- `ImageSharpen` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 2.25 | - | 2 | 44% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 0.65 | - | 2 | 46% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 10，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 2.25，样本不足，未给区间，2 个样本，取值分散，一致性仅 44%
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 0.65，样本不足，未给区间，2 个样本，取值分散，一致性仅 46%
- 这些节点还没有知识卡，系统对它们的理解有限：CR Text、CR SDXL Aspect Ratio
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
