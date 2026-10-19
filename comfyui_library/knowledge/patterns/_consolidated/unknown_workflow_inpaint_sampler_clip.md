---
name: unknown_workflow_inpaint_sampler_clip
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.780667
common_nodes: [CLIPTextEncode, CLIPVisionLoader, ConditioningZeroOut, DifferentialDiffusion, DualCLIPLoader, FluxGuidance, InpaintModelConditioning, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, ReduxAdvanced, SaveImage, StyleModelLoader, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: [LayerUtility: ImageScaleByAspectRatio V2, Mask Fill Holes, easy makeImageForICLora]
members: [图片生成/图生图/2098602158307500034.json, 图片生成/图生图/2098948233119756290.json, 图片生成/文生图/1922203325390061569.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_clip

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/2098602158307500034.json、图片生成/图生图/2098948233119756290.json、图片生成/文生图/1922203325390061569.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：78%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `ConditioningZeroOut`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `FluxGuidance`
- `InpaintModelConditioning`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `ReduxAdvanced`
- `SaveImage`
- `StyleModelLoader`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 2/3 个有
- `ImageCrop` —— 2/3 个有
- `Mask Fill Holes` —— 2/3 个有
- `easy makeImageForICLora` —— 2/3 个有
- `ImageConcanate` —— 1/3 个有
- `ImagePadForOutpaint` —— 1/3 个有
- `LoraLoader` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 25 - 30 | 3 | 91% |
| Prompt 约束强度(CFG) | 1 | 1 - 3.5 | 3 | 36% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | beta | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 25 - 30，3 个样本，取值集中（一致性 91%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3.5，3 个样本，取值分散，一致性仅 36%
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: ImageScaleByAspectRatio V2、Mask Fill Holes、easy makeImageForICLora
