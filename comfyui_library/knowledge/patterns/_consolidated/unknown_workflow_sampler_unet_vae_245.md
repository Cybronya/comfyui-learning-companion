---
name: unknown_workflow_sampler_unet_vae_245
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.8546
common_nodes: [CLIPLoader, CR Text, GrowMaskWithBlur, Image Comparer (rgthree), KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, MaskPreview+, PainterFluxImageEdit, RH_LLMAPI_Pro_Node, SaveImage, UNETLoader, VAEDecode, VAELoader, easy imageDetailTransfer]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/FLUX-Klein电商产品极速换背景保持原图架构不变+细节迁移_2013210709567475713.json, 平台全量/FLUX-Klein电商产品换背景+细节迁移_2012413650090332161.json, 平台全量/Flux2-Klein电商产品更换背景_2019590705437478914.json, 平台全量/Flux2-Klein电商产品更换背景_2020011722014199810.json, 平台全量/Flux2-Klein电商产品更换背景_2071149002829164545.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_245

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/FLUX-Klein电商产品极速换背景保持原图架构不变+细节迁移_2013210709567475713.json、平台全量/FLUX-Klein电商产品换背景+细节迁移_2012413650090332161.json、平台全量/Flux2-Klein电商产品更换背景_2019590705437478914.json、平台全量/Flux2-Klein电商产品更换背景_2020011722014199810.json、平台全量/Flux2-Klein电商产品更换背景_2071149002829164545.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CR Text`
- `GrowMaskWithBlur`
- `Image Comparer (rgthree)`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `MaskPreview+`
- `PainterFluxImageEdit`
- `RH_LLMAPI_Pro_Node`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy imageDetailTransfer`

**可变部分**（部分 workflow 才有）：
- `easy imageRemBg` —— 3/5 个有
- `easy showAnything` —— 3/5 个有
- `LayerMask: BiRefNetUltraV2` —— 2/5 个有
- `LayerMask: LoadBiRefNetModelV2` —— 2/5 个有
- `LayerUtility: ImageReel` —— 2/5 个有
- `LayerUtility: ImageReelComposit` —— 2/5 个有
- `ShowText|pysssss` —— 2/5 个有
- `easy imageConcat` —— 2/5 个有
- `RHHiddenNodes` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（6/5 个样本）：Steps较低可能导致细节不足
