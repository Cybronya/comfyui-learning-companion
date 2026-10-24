---
name: unknown_workflow_sampler_unet_vae_90
type: Unknown Workflow
frequency: 10
level: strong
coverage: 0.8537
common_nodes: [CLIPLoader, Image Comparer (rgthree), ImageConcanate, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, MaskPreview+, PainterFluxImageEdit, SaveImage, SolidMask, UNETLoader, VAEDecode, VAELoader, easy ifElse, easy imageRemBg, easy isMaskEmpty]
problems: [Steps较低可能导致细节不足]
missing: []
members: ["图片生成/图生图/Face Swap, Head Swap换脸换头++换脸换装多图编辑_2094608453212925953.json", 图片生成/图生图/Flux 2 Klein 换头极速版_2016335569361575937.json, 图片生成/图生图/Flux 2 Klein换头换脸-光影自动融合_2039931189670191106.json, 图片生成/图生图/Flux 2 Klein换头换脸_2016156557255380994.json, 图片生成/图生图/Flux 2 Klein换头换脸_2016316866293141505.json, 图片生成/图生图/Flux 2 Klein换头换脸_2018969931152367617.json, 图片生成/图生图/Flux 2 Klein换头换脸（80%一致性-30秒出图） 林耀_2016532491355561986.json, 图片生成/图生图/一键换头换脸高质量Flux 2 Klein_2024366116075741185.json, 图片生成/图生图/换脸klein9b_2026610134717304834.json, 图片生成/图生图/换脸klein9b超绝一致性_2036752635256119298.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_90

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/Face Swap, Head Swap换脸换头++换脸换装多图编辑_2094608453212925953.json、图片生成/图生图/Flux 2 Klein 换头极速版_2016335569361575937.json、图片生成/图生图/Flux 2 Klein换头换脸-光影自动融合_2039931189670191106.json、图片生成/图生图/Flux 2 Klein换头换脸_2016156557255380994.json、图片生成/图生图/Flux 2 Klein换头换脸_2016316866293141505.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `Image Comparer (rgthree)`
- `ImageConcanate`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `MaskPreview+`
- `PainterFluxImageEdit`
- `SaveImage`
- `SolidMask`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy ifElse`
- `easy imageRemBg`
- `easy isMaskEmpty`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 7/10 个有
- `ColorMatch` —— 3/10 个有
- `LoraLoaderModelOnly` —— 3/10 个有
- `Int` —— 2/10 个有
- `CustomAddLabel` —— 1/10 个有
- `Note Plus (mtb)` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 10 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 10 | 100% |
| 采样算法 | euler | - | 10 | 100% |
| 调度器 | simple | - | 10 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，10 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，10 个样本，一致性 100%
- 调度器 最常用 simple，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 高发问题（10/10 个样本）：Steps较低可能导致细节不足
