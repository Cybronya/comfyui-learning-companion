---
name: unknown_workflow_clip_unet_vae_13
type: Unknown Workflow
frequency: 3
level: weak
coverage: 0.817333
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyHunyuanLatentVideo, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: [CR Text, LayerColor: Brightness & Contrast]
members: [图片生成/文生图/1949348912306561025.json, 图片生成/文生图/1949897867035107330.json, 图片生成/文生图/1958551825752420353.json]
source: knowledge_consolidation
---

# unknown_workflow_clip_unet_vae_13

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/1949348912306561025.json、图片生成/文生图/1949897867035107330.json、图片生成/文生图/1958551825752420353.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：82%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyHunyuanLatentVideo`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 2/3 个有
- `KSampler` —— 2/3 个有
- `LoadImage` —— 2/3 个有
- `LoraLoader` —— 2/3 个有
- `ModelSamplingSD3` —— 2/3 个有
- `PrimitiveInt` —— 2/3 个有
- `FilmGrain` —— 1/3 个有
- `JWInteger` —— 1/3 个有
- `KSamplerAdvanced` —— 1/3 个有
- `LayerColor: Brightness & Contrast` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 14 | - | 2 | 57% |
| Prompt 约束强度(CFG) | 3.5 | 1 - 14 | 3 | 9% |
| 采样算法 | res_2s | - | 3 | 67% |
| 调度器 | bong_tangent | - | 3 | 67% |
| 重绘幅度 | 1 | - | 2 | 100% |
| LoRA 模型强度 | 0.725 | - | 2 | 62% |
| LoRA 文本强度 | 0.725 | - | 2 | 62% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 14，样本不足，未给区间，2 个样本
- Prompt 约束强度(CFG) 中位数 3.5，观测区间 1 - 14，3 个样本，取值分散，一致性仅 9%
- 采样算法 最常用 res_2s，3 个样本，一致性 67%
- 调度器 最常用 bong_tangent，3 个样本，一致性 67%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0.725，样本不足，未给区间，2 个样本
- LoRA 文本强度 中位数 0.725，样本不足，未给区间，2 个样本
- 风险：Prompt 约束强度(CFG) 观测到 14，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
- 这些节点还没有知识卡，系统对它们的理解有限：CR Text、LayerColor: Brightness & Contrast
