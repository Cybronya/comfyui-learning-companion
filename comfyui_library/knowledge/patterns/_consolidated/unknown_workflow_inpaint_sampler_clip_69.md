---
name: unknown_workflow_inpaint_sampler_clip_69
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.8825
common_nodes: [CLIPTextEncode, DifferentialDiffusion, DualCLIPLoader, Fast Groups Bypasser (rgthree), FluxGuidance, InpaintModelConditioning, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/局部重绘_2089827740097794050.json, 平台全量/OneReward-3合1工作流(重绘_消除_扩图)_1967261422558306306.json, 平台全量/OneReward-3合1工作流(重绘_消除_扩图)_2004482567862714370.json, 平台全量/QT104-扩图（FLUX）图片秒变大，一键轻松扩图_1946848151351517186.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_clip_69

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/局部重绘_2089827740097794050.json、平台全量/OneReward-3合1工作流(重绘_消除_扩图)_1967261422558306306.json、平台全量/OneReward-3合1工作流(重绘_消除_扩图)_2004482567862714370.json、平台全量/QT104-扩图（FLUX）图片秒变大，一键轻松扩图_1946848151351517186.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `Fast Groups Bypasser (rgthree)`
- `FluxGuidance`
- `InpaintModelConditioning`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `GrowMaskWithBlur` —— 3/4 个有
- `Image Comparer (rgthree)` —— 3/4 个有
- `ImagePadForOutpaint` —— 3/4 个有
- `LoraLoaderModelOnly` —— 3/4 个有
- `ConditioningZeroOut` —— 1/4 个有
- `Image Save` —— 1/4 个有
- `ImageCompositeMasked` —— 1/4 个有
- `InpaintCrop` —— 1/4 个有
- `InpaintStitch` —— 1/4 个有
- `LayerMask: MaskPreview` —— 1/4 个有
- `MaskFillHoles` —— 1/4 个有
- `PlaySound|pysssss` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 16.5 | 8 - 28 | 4 | 46% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | normal | - | 4 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 16.5，观测区间 8 - 28，4 个样本，取值分散，一致性仅 46%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 normal，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（6/4 个样本）：Steps较低可能导致细节不足
