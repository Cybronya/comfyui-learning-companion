---
name: unknown_workflow_inpaint_sampler_clip_17
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.869167
common_nodes: [CLIPTextEncode, DualCLIPLoader, FluxGuidance, InpaintModelConditioning, KSampler, LoadImage, SaveImage, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Flux1-fill外扩+Nunchaku加速_1950420625396514818.json, 图片生成/图生图/Flux1-fill外扩_1950412818538479618.json, 图片生成/图生图/flux fill dev 外扩图工作流_1960864869409067009.json, 图片生成/图生图/flux局部重绘_1898927356546109442.json, 图片生成/图生图/扩图-拓展画幅_1988062497779462145.json, 图片生成/图生图/扩图1_2096130539609743362.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_clip_17

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Flux1-fill外扩+Nunchaku加速_1950420625396514818.json、图片生成/图生图/Flux1-fill外扩_1950412818538479618.json、图片生成/图生图/flux fill dev 外扩图工作流_1960864869409067009.json、图片生成/图生图/flux局部重绘_1898927356546109442.json、图片生成/图生图/扩图-拓展画幅_1988062497779462145.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPTextEncode`
- `DualCLIPLoader`
- `FluxGuidance`
- `InpaintModelConditioning`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImagePadForOutpaint` —— 5/6 个有
- `UNETLoader` —— 5/6 个有
- `ConditioningZeroOut` —— 4/6 个有
- `DifferentialDiffusion` —— 3/6 个有
- `Image Comparer (rgthree)` —— 3/6 个有
- `PrimitiveInt` —— 2/6 个有
- `RH_Captioner` —— 2/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/6 个有
- `LayerUtility: PurgeVRAM` —— 1/6 个有
- `NunchakuFluxDiTLoader` —— 1/6 个有
- `SetLatentNoiseMask` —— 1/6 个有
- `图像缩放范围孤海` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 6 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 8 | 6 | 0% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | normal | - | 6 | 83% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 8，6 个样本，取值分散，一致性仅 0%
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 normal，6 个样本，一致性 83%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
