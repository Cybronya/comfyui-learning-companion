---
name: unknown_workflow_sampler_unet_vae_165
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.90225
common_nodes: [CLIPLoader, ConditioningZeroOut, EmptyFlux2LatentImage, Int, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/换装（角色换装，高一致性，高质感）_2098737953890721794.json, 图片生成/文生图/Fk2-图像编辑低限版_2039297322311487489.json, 平台全量/Flux+2+Klein 超强一致换装 电商产品模特 全自动换装 一致性超强_2016688429932748801.json, 平台全量/Flux2 Klein   指定图片极速换脸 PuLID最强换脸组合_1921720668835217409.json, 平台全量/Flux2 Klein 全自动换头换脸 指定换脸真实自然 写实换脸换装_2021888045309497345.json, 平台全量/指定换头换脸  Flux+2+Klein 全自动换脸真实自然 写实换脸换装_2016703712894390274.json, 平台全量/换头换脸FLUX.2-Klein9b 全自动换头换脸  图片高清修复 写实无损放大 指定换脸真实自然_2031575686237917185.json, 平台全量/换装（角色换装，高一致性，高质感）Klein_2065675934207922177.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_165

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/换装（角色换装，高一致性，高质感）_2098737953890721794.json、图片生成/文生图/Fk2-图像编辑低限版_2039297322311487489.json、平台全量/Flux+2+Klein 超强一致换装 电商产品模特 全自动换装 一致性超强_2016688429932748801.json、平台全量/Flux2 Klein   指定图片极速换脸 PuLID最强换脸组合_1921720668835217409.json、平台全量/Flux2 Klein 全自动换头换脸 指定换脸真实自然 写实换脸换装_2021888045309497345.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `Int`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 7/8 个有
- `Flux2KleinEditTextEncode_EditUtils` —— 7/8 个有
- `LoraLoaderModelOnly` —— 6/8 个有
- `Image Comparer (rgthree)` —— 5/8 个有
- `PreviewImage` —— 5/8 个有
- `RMBG` —— 4/8 个有
- `LayerMask: SegformerB2ClothesUltra` —— 3/8 个有
- `LayerUtility: ImageRemoveAlpha` —— 3/8 个有
- `CR Text` —— 1/8 个有
- `TextEncodeQwenImageEditPlusAdvance_lrzjason` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 8 | 71% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | euler | - | 8 | 100% |
| 调度器 | simple | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，8 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，8 个样本，一致性 100%
- 调度器 最常用 simple，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 高发问题（8/8 个样本）：Steps较低可能导致细节不足
