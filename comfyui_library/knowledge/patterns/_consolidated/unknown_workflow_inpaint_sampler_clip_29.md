---
name: unknown_workflow_inpaint_sampler_clip_29
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.85275
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, DifferentialDiffusion, DualCLIPLoader, FluxGuidance, INPAINT_ApplyFooocusInpaint, INPAINT_InpaintWithModel, INPAINT_LoadFooocusInpaint, INPAINT_LoadInpaintModel, INPAINT_VAEEncodeInpaintConditioning, ImagePadForOutpaint, InpaintModelConditioning, KSampler, LoadImage, SaveImage, UNETLoader, UnetLoaderGGUF, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/FLUX扩图工作流（大全）_2049475582244687873.json, 图片生成/图生图/扩图、高清放大_2005982795740692481.json, 图片生成/图生图/扩图，高清放大_2028343345428307969.json, 图片生成/图生图/🔥无痕 高清扩图工作流，一键补全画面，毫无违和感！_2107016511822065665.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_clip_29

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/FLUX扩图工作流（大全）_2049475582244687873.json、图片生成/图生图/扩图、高清放大_2005982795740692481.json、图片生成/图生图/扩图，高清放大_2028343345428307969.json、图片生成/图生图/🔥无痕 高清扩图工作流，一键补全画面，毫无违和感！_2107016511822065665.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `FluxGuidance`
- `INPAINT_ApplyFooocusInpaint`
- `INPAINT_InpaintWithModel`
- `INPAINT_LoadFooocusInpaint`
- `INPAINT_LoadInpaintModel`
- `INPAINT_VAEEncodeInpaintConditioning`
- `ImagePadForOutpaint`
- `InpaintModelConditioning`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `UnetLoaderGGUF`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 3/4 个有
- `PreviewImage` —— 3/4 个有
- `ImageScaleBy` —— 2/4 个有
- `ImageUpscaleWithModel` —— 2/4 个有
- `PMRF` —— 2/4 个有
- `UltimateSDUpscale` —— 2/4 个有
- `UpscaleModelLoader` —— 2/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 4 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 8 | 4 | 22% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | normal | - | 4 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 8，4 个样本，取值分散，一致性仅 22%
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 normal，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
