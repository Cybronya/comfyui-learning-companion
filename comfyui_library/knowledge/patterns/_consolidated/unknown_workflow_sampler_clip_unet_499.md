---
name: unknown_workflow_sampler_clip_unet_499
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.944
common_nodes: [CLIPTextEncode, DualCLIPLoader, FluxGuidance, ImageConcanate, InstructPixToPixConditioning, KSampler, LayerMask: LoadFlorence2Model, LayerUtility: Florence2Image2Prompt, LayerUtility: PurgeVRAM, LayerUtility: TextJoin, LoadImage, PreviewImage, RHHiddenNodes, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/雪人自由——万切皆可化成雪_1884419307244503041.json, 平台全量/堆雪人自由_1870839866731962370.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_499

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/雪人自由——万切皆可化成雪_1884419307244503041.json、平台全量/堆雪人自由_1870839866731962370.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：94%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `DualCLIPLoader`
- `FluxGuidance`
- `ImageConcanate`
- `InstructPixToPixConditioning`
- `KSampler`
- `LayerMask: LoadFlorence2Model`
- `LayerUtility: Florence2Image2Prompt`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: TextJoin`
- `LoadImage`
- `PreviewImage`
- `RHHiddenNodes`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | normal | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 normal，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
