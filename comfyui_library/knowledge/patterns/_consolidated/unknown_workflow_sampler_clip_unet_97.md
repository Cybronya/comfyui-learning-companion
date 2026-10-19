---
name: unknown_workflow_sampler_clip_unet_97
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.7735
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyHunyuanLatentVideo, KSampler, LoadImage, PreviewImage, PrimitiveInt, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: [CR Text, LayerColor: Brightness & Contrast]
members: [图片生成/文生图/1949348912306561025.json, 图片生成/文生图/1949897867035107330.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_97

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/1949348912306561025.json、图片生成/文生图/1949897867035107330.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：77%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyHunyuanLatentVideo`
- `KSampler`
- `LoadImage`
- `PreviewImage`
- `PrimitiveInt`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 1/2 个有
- `FilmGrain` —— 1/2 个有
- `LayerColor: Brightness & Contrast` —— 1/2 个有
- `LoraLoader` —— 1/2 个有
- `ModelSamplingSD3` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 14 | - | 2 | 57% |
| Prompt 约束强度(CFG) | 2.25 | - | 2 | 44% |
| 采样算法 | res_2s | - | 2 | 100% |
| 调度器 | bong_tangent | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |
| LoRA 模型强度 | 0.45 | - | 1 | 100% |
| LoRA 文本强度 | 0.45 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 14，样本不足，未给区间，2 个样本
- Prompt 约束强度(CFG) 中位数 2.25，样本不足，未给区间，2 个样本，取值分散，一致性仅 44%
- 采样算法 最常用 res_2s，2 个样本，一致性 100%
- 调度器 最常用 bong_tangent，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（1/2 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：CR Text、LayerColor: Brightness & Contrast
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
