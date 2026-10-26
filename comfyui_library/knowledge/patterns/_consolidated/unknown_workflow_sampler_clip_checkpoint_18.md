---
name: unknown_workflow_sampler_clip_checkpoint_18
type: Unknown Workflow
frequency: 5
level: weak
coverage: 0.8872
common_nodes: [BrushNetLoader, CLIPTextEncode, CheckpointLoaderSimple, GrowMask, Image Blend by Mask, ImpactGaussianBlurMask, InvertMask, KSampler, LoadImage, MaskToImage, PowerPaint, PowerPaintCLIPLoader, SaveImage, VAEDecode]
problems: []
missing: []
members: [图片生成/图生图/一键万物消除完美无痕_1917141953652396033.json, 图片生成/图生图/物体消除工作流_1901904669449592833.json, 图片生成/图生图/物体消除工作流_1914573483743899649.json, 图片生成/图生图/物体消除工作流_1930071205267804162.json, 图片生成/图生图/画面物体快速消除或增加_1914914461046767617.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_checkpoint_18

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/一键万物消除完美无痕_1917141953652396033.json、图片生成/图生图/物体消除工作流_1901904669449592833.json、图片生成/图生图/物体消除工作流_1914573483743899649.json、图片生成/图生图/物体消除工作流_1930071205267804162.json、图片生成/图生图/画面物体快速消除或增加_1914914461046767617.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：89%

## 共有节点

全部 5 个 workflow 都包含：
- `BrushNetLoader`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `GrowMask`
- `Image Blend by Mask`
- `ImpactGaussianBlurMask`
- `InvertMask`
- `KSampler`
- `LoadImage`
- `MaskToImage`
- `PowerPaint`
- `PowerPaintCLIPLoader`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 4/5 个有
- `CLIPTextEncodeFlux` —— 1/5 个有
- `ConditioningZeroOut` —— 1/5 个有
- `DifferentialDiffusion` —— 1/5 个有
- `DualCLIPLoader` —— 1/5 个有
- `Image Comparer (rgthree)` —— 1/5 个有
- `InpaintModelConditioning` —— 1/5 个有
- `UNETLoader` —— 1/5 个有
- `VAELoader` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 5 | 100% |
| Prompt 约束强度(CFG) | 7.5 | 1 - 7.5 | 5 | 58% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | normal | - | 5 | 100% |
| 重绘幅度 | 0.1 | 0.1 - 1 | 5 | 0% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 7.5，观测区间 1 - 7.5，5 个样本
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 normal，5 个样本，一致性 100%
- 重绘幅度 中位数 0.1，观测区间 0.1 - 1，5 个样本，取值分散，一致性仅 0%
