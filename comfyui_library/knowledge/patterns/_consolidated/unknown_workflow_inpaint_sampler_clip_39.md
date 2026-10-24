---
name: unknown_workflow_inpaint_sampler_clip_39
type: Unknown Workflow
frequency: 3
level: strong
coverage: 1
common_nodes: [CLIPTextEncodeFlux, ConditioningZeroOut, DifferentialDiffusion, DualCLIPLoader, InpaintModelConditioning, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/41.tonnie-One Reward换脸（不如重绘像）_2004262619282370562.json, 图片生成/图生图/7.tonnie-flux-fill扩图_1992165551143276545.json, 图片生成/图生图/FLUX 超强扩图_1910955503214653442.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_clip_39

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/41.tonnie-One Reward换脸（不如重绘像）_2004262619282370562.json、图片生成/图生图/7.tonnie-flux-fill扩图_1992165551143276545.json、图片生成/图生图/FLUX 超强扩图_1910955503214653442.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：100%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncodeFlux`
- `ConditioningZeroOut`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `InpaintModelConditioning`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImagePadForOutpaint` —— 2/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/3 个有
- `ApplyPulidFlux` —— 1/3 个有
- `EcomIDFaceAnalysis` —— 1/3 个有
- `ImageResize+` —— 1/3 个有
- `LoraLoaderModelOnly` —— 1/3 个有
- `Mask Fill Holes` —— 1/3 个有
- `PulidFluxEvaClipLoader` —— 1/3 个有
- `PulidFluxModelLoader` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 10 - 30 | 3 | 59% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | beta | - | 3 | 33% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 10 - 30，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 33%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
