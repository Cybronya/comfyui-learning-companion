---
name: unknown_workflow_sampler_unet_vae_268
type: Unknown Workflow
frequency: 3
level: strong
coverage: 1
common_nodes: [CLIPLoader, ConditioningZeroOut, Int, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/换装（角色换装，高一致性，高质感）_2098737953890721794.json, 图片生成/文生图/Fk2-图像编辑低限版_2039297322311487489.json, 图片生成/文生图/Qwen-Edit-2511-三图融合-一致性加强版本_2026276649716682754.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_268

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/换装（角色换装，高一致性，高质感）_2098737953890721794.json、图片生成/文生图/Fk2-图像编辑低限版_2039297322311487489.json、图片生成/文生图/Qwen-Edit-2511-三图融合-一致性加强版本_2026276649716682754.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：100%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `ConditioningZeroOut`
- `Int`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 2/3 个有
- `EmptyFlux2LatentImage` —— 2/3 个有
- `LoraLoaderModelOnly` —— 2/3 个有
- `TextEncodeQwenImageEditPlusAdvance_lrzjason` —— 2/3 个有
- `CR Prompt Text` —— 1/3 个有
- `EmptySD3LatentImage` —— 1/3 个有
- `Flux2KleinEditTextEncode_EditUtils` —— 1/3 个有
- `LayerMask: SegformerB2ClothesUltra` —— 1/3 个有
- `LayerUtility: ImageRemoveAlpha` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 8 | 3 | 72% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 67% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 8，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 67%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
