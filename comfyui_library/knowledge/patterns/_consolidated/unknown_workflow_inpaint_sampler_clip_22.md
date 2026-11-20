---
name: unknown_workflow_inpaint_sampler_clip_22
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.735125
common_nodes: [CLIPTextEncode, CR Latent Batch Size, ConditioningZeroOut, DifferentialDiffusion, DualCLIPLoader, FluxGuidance, Image Comparer (rgthree), InpaintModelConditioning, KSampler, LoadImage, MaskPreview+, PreviewImage, RH_Translator, SaveImage, ShowText|pysssss, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/局部重绘---适合非常小的局部 (新节点）_1962323843031482369.json, 图片生成/图生图/局部重绘---适合非常小的局部_1941299544011468802.json, 图片生成/图生图/局部重绘---适合非常小的局部_1953682902464778241.json, 图片生成/图生图/局部重绘Flux_Fill_OneReward——自动合层工作流（加速版）【阿夕AI】_2099872308956581889.json, 图片生成/图生图/局部重绘OneReward---适合非常小的局部（加速版）_1966492793738833922.json, 平台全量/【功能】局部重绘_1981292990843052034.json, 平台全量/局部重绘Flux_Fill_OneReward——自动合层工作流（加速版）【阿夕AI】_2053797875498397697.json, 平台全量/局部重绘完美移除版OneReward——自动合层工作流（加速版）【阿夕AI】_2057771003970932737.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_clip_22

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/局部重绘---适合非常小的局部 (新节点）_1962323843031482369.json、图片生成/图生图/局部重绘---适合非常小的局部_1941299544011468802.json、图片生成/图生图/局部重绘---适合非常小的局部_1953682902464778241.json、图片生成/图生图/局部重绘Flux_Fill_OneReward——自动合层工作流（加速版）【阿夕AI】_2099872308956581889.json、图片生成/图生图/局部重绘OneReward---适合非常小的局部（加速版）_1966492793738833922.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：74%

## 共有节点

全部 8 个 workflow 都包含：
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
- `InpaintCropImproved` —— 6/8 个有
- `InpaintStitchImproved` —— 6/8 个有
- `LoraLoaderModelOnly` —— 6/8 个有
- `UNETLoader` —— 6/8 个有
- `Text Prompt (JPS)` —— 3/8 个有
- `孤海注释` —— 3/8 个有
- `InpaintCrop` —— 2/8 个有
- `InpaintResize` —— 2/8 个有
- `InpaintStitch` —— 2/8 个有
- `NunchakuFluxDiTLoader` —— 2/8 个有
- `Text` —— 2/8 个有
- `Fast Groups Muter (rgthree)` —— 1/8 个有
- `ImageCompositeMasked` —— 1/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/8 个有
- `MaskToImage` —— 1/8 个有
- `PrimitiveInt` —— 1/8 个有
- `SDVN Get Mask Size` —— 1/8 个有
- `easy showAnything` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 20 | 8 | 53% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | euler | - | 8 | 88% |
| 调度器 | normal | - | 8 | 88% |
| 重绘幅度 | 1 | 0.4 - 1 | 8 | 79% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 20，8 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，8 个样本，一致性 88%
- 调度器 最常用 normal，8 个样本，一致性 88%
- 重绘幅度 中位数 1，观测区间 0.4 - 1，8 个样本
- 高发问题（6/8 个样本）：Steps较低可能导致细节不足
