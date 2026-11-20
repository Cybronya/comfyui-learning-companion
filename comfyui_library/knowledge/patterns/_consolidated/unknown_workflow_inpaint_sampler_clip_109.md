---
name: unknown_workflow_inpaint_sampler_clip_109
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.95
common_nodes: [CLIPTextEncode, DualCLIPLoader, FluxGuidance, ImpactGaussianBlurMask, InpaintModelConditioning, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/人像美化，皮肤匀净淡化痘印、斑点、细纹，保留真实毛孔，肤色通透校正 ，五官立体，画质细腻_2092174339276894209.json, 平台全量/工作流基础篇-6-Flux局部重绘工作流_2048773053320007681.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_clip_109

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/人像美化，皮肤匀净淡化痘印、斑点、细纹，保留真实毛孔，肤色通透校正 ，五官立体，画质细腻_2092174339276894209.json、平台全量/工作流基础篇-6-Flux局部重绘工作流_2048773053320007681.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：95%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `DualCLIPLoader`
- `FluxGuidance`
- `ImpactGaussianBlurMask`
- `InpaintModelConditioning`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ColorCorrect` —— 1/2 个有
- `ConditioningZeroOut` —— 1/2 个有
- `DifferentialDiffusion` —— 1/2 个有
- `GrowMask` —— 1/2 个有
- `LayerMask: PersonMaskUltra V2` —— 1/2 个有
- `UnsharpMask` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 21 | - | 2 | 95% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 0.675 | - | 2 | 52% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 21，样本不足，未给区间，2 个样本，取值集中（一致性 95%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 0.675，样本不足，未给区间，2 个样本
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
