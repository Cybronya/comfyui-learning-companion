---
name: unknown_workflow_inpaint_clip_unet_7
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.952333
common_nodes: [CLIPTextEncode, CLIPVisionLoader, DifferentialDiffusion, DualCLIPLoader, FluxGuidance, ImageToMask, InpaintModelConditioning, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, MaskToImage, ReduxAdvanced, SaveImage, StyleModelLoader, UNETLoader, VAEDecode, VAELoader, easy imageConcat]
problems: []
missing: []
members: [图片生成/图生图/flux fill+redu万物迁移_1950148533690220546.json, 图片生成/图生图/redux风格迁移Reduced Adebance节点_1922216491712970754.json, 平台全量/小明看这里_1889930054804316161.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_clip_unet_7

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/flux fill+redu万物迁移_1950148533690220546.json、图片生成/图生图/redux风格迁移Reduced Adebance节点_1922216491712970754.json、平台全量/小明看这里_1889930054804316161.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `FluxGuidance`
- `ImageToMask`
- `InpaintModelConditioning`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `MaskToImage`
- `ReduxAdvanced`
- `SaveImage`
- `StyleModelLoader`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy imageConcat`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 2/3 个有
- `EmptyImage` —— 2/3 个有
- `KSampler` —— 2/3 个有
- `DeepTranslatorTextNode` —— 1/3 个有
- `FluxLoraLoader` —— 1/3 个有
- `GrowMask` —— 1/3 个有
- `Image Comparer (rgthree)` —— 1/3 个有
- `ImageResize+` —— 1/3 个有
- `ImpactGaussianBlurMask` —— 1/3 个有
- `KSamplerAdvanced` —— 1/3 个有
- `LayerUtility: ColorImage V2` —— 1/3 个有
- `PreviewImage` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | - | 2 | 80% |
| Prompt 约束强度(CFG) | 3.5 | 1 - 30 | 3 | 0% |
| 采样算法 | euler | - | 3 | 67% |
| 调度器 | beta | - | 3 | 33% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，样本不足，未给区间，2 个样本，取值集中（一致性 80%）
- Prompt 约束强度(CFG) 中位数 3.5，观测区间 1 - 30，3 个样本，取值分散，一致性仅 0%
- 采样算法 最常用 euler，3 个样本，一致性 67%
- 调度器 最常用 beta，3 个样本，一致性 33%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 风险：Prompt 约束强度(CFG) 观测到 30，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
