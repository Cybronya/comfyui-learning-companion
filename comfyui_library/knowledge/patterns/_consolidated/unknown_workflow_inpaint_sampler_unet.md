---
name: unknown_workflow_inpaint_sampler_unet
type: Unknown Workflow
frequency: 12
level: moderate
coverage: 0.92175
common_nodes: [InpaintModelConditioning, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Magic-Wan2.2-修手工作流_1995477299732656129.json, 图片生成/图生图/Moss-image-局部重绘_2112544404337676289.json, 图片生成/图生图/Qwen-image2.1-万能局部重绘_2108164582689824769.json, 图片生成/图生图/Qwen-image2.1-万能局部重绘_2110648449984196609.json, 图片生成/图生图/Qwen-image2.1-万能局部重绘_2111278068961730562.json, 图片生成/图生图/Qwen-image2.1-参考图+局部重绘_2108186043651551234.json, 图片生成/图生图/局部重绘移除(河南ai之神)_1931906923506151425.json, 平台全量/Fill One reward万物移除工作流_1966516003863736322.json, 平台全量/Fill One reward局部重绘工作流_1966521617511821313.json, 平台全量/Flux-fill-Oneward万物移除工作流_1985883620487376898.json, 平台全量/Flux-fill-Oneward局部重绘工作流_1986442165700227074.json, 平台全量/▶Flux万物移除流_2079140997283540994.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_unet

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/Magic-Wan2.2-修手工作流_1995477299732656129.json、图片生成/图生图/Moss-image-局部重绘_2112544404337676289.json、图片生成/图生图/Qwen-image2.1-万能局部重绘_2108164582689824769.json、图片生成/图生图/Qwen-image2.1-万能局部重绘_2110648449984196609.json、图片生成/图生图/Qwen-image2.1-万能局部重绘_2111278068961730562.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 12 个 workflow 都包含：
- `InpaintModelConditioning`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Mask Fill Holes` —— 11/12 个有
- `Image Comparer (rgthree)` —— 10/12 个有
- `CLIPTextEncode` —— 8/12 个有
- `DifferentialDiffusion` —— 7/12 个有
- `LoraLoaderModelOnly` —— 7/12 个有
- `CLIPLoader` —— 6/12 个有
- `DualCLIPLoader` —— 6/12 个有
- `FluxGuidance` —— 6/12 个有
- `ConditioningZeroOut` —— 5/12 个有
- `TextEncodeQwenImage21` —— 4/12 个有
- `ImageAndMaskPreview` —— 3/12 个有
- `Int` —— 2/12 个有
- `JjkText` —— 2/12 个有
- `CR Text` —— 1/12 个有
- `DeepTranslatorTextNode` —— 1/12 个有
- `MaskFillHoles` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 17.5 | 6 - 50 | 12 | 38% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 12 | 63% |
| 采样算法 | euler | - | 12 | 100% |
| 调度器 | beta | - | 12 | 50% |
| 重绘幅度 | 1 | 0.36 - 1 | 12 | 81% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 17.5，观测区间 6 - 50，12 个样本，取值分散，一致性仅 38%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，12 个样本
- 采样算法 最常用 euler，12 个样本，一致性 100%
- 调度器 最常用 beta，12 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 0.36 - 1，12 个样本，取值集中（一致性 81%）
