---
name: text_to_image_sampler_clip_vae_9
type: Text To Image
frequency: 2
level: weak
coverage: 0.9585
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, ModelSamplingAuraFlow, NunchakuQwenImageDiTLoader, SaveImage, VAEDecode]
problems: [Steps较低可能导致细节不足]
missing: [LayerUtility: PurgeVRAM]
members: [图片生成/文生图/1959799817432150017.json, 图片生成/文生图/1963549374519414785.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_vae_9

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/1959799817432150017.json、图片生成/文生图/1963549374519414785.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：96%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `ModelSamplingAuraFlow`
- `NunchakuQwenImageDiTLoader`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `AV_VAELoader` —— 1/2 个有
- `CFGNorm` —— 1/2 个有
- `LayerUtility: PurgeVRAM` —— 1/2 个有
- `RH_Translator` —— 1/2 个有
- `VAELoader` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1176 | - | 2 | 87% |
| 高度 | 1176 | - | 2 | 87% |
| 采样步数 | 14 | - | 2 | 57% |
| Prompt 约束强度(CFG) | 1.77 | - | 2 | 56% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1176，样本不足，未给区间，2 个样本，取值集中（一致性 87%）
- 高度 中位数 1176，样本不足，未给区间，2 个样本，取值集中（一致性 87%）
- 采样步数 中位数 14，样本不足，未给区间，2 个样本
- Prompt 约束强度(CFG) 中位数 1.77，样本不足，未给区间，2 个样本
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（1/2 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: PurgeVRAM
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
