---
name: unknown_workflow_inpaint_sampler_clip_28
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.7806
common_nodes: [CLIPTextEncode, CR Latent Batch Size, ConditioningZeroOut, DifferentialDiffusion, DualCLIPLoader, FluxGuidance, Image Comparer (rgthree), InpaintModelConditioning, KSampler, LoadImage, MaskPreview+, PreviewImage, RH_Translator, SaveImage, ShowText|pysssss, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/局部重绘---适合非常小的局部 (新节点）_1962323843031482369.json, 图片生成/图生图/局部重绘---适合非常小的局部_1941299544011468802.json, 图片生成/图生图/局部重绘---适合非常小的局部_1953682902464778241.json, 图片生成/图生图/局部重绘Flux_Fill_OneReward——自动合层工作流（加速版）【阿夕AI】_2099872308956581889.json, 图片生成/图生图/局部重绘OneReward---适合非常小的局部（加速版）_1966492793738833922.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_clip_28

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/局部重绘---适合非常小的局部 (新节点）_1962323843031482369.json、图片生成/图生图/局部重绘---适合非常小的局部_1941299544011468802.json、图片生成/图生图/局部重绘---适合非常小的局部_1953682902464778241.json、图片生成/图生图/局部重绘Flux_Fill_OneReward——自动合层工作流（加速版）【阿夕AI】_2099872308956581889.json、图片生成/图生图/局部重绘OneReward---适合非常小的局部（加速版）_1966492793738833922.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：78%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPTextEncode`
- `CR Latent Batch Size`
- `ConditioningZeroOut`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `FluxGuidance`
- `Image Comparer (rgthree)`
- `InpaintModelConditioning`
- `KSampler`
- `LoadImage`
- `MaskPreview+`
- `PreviewImage`
- `RH_Translator`
- `SaveImage`
- `ShowText|pysssss`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `InpaintCropImproved` —— 3/5 个有
- `InpaintStitchImproved` —— 3/5 个有
- `LoraLoaderModelOnly` —— 3/5 个有
- `UNETLoader` —— 3/5 个有
- `InpaintCrop` —— 2/5 个有
- `InpaintResize` —— 2/5 个有
- `InpaintStitch` —— 2/5 个有
- `NunchakuFluxDiTLoader` —— 2/5 个有
- `Fast Groups Muter (rgthree)` —— 1/5 个有
- `ImageCompositeMasked` —— 1/5 个有
- `MaskToImage` —— 1/5 个有
- `Text` —— 1/5 个有
- `Text Prompt (JPS)` —— 1/5 个有
- `孤海注释` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 20 | 5 | 54% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | normal | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 20，5 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 normal，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（3/5 个样本）：Steps较低可能导致细节不足
