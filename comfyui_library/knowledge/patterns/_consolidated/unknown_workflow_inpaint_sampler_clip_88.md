---
name: unknown_workflow_inpaint_sampler_clip_88
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.925
common_nodes: [CLIPTextEncode, CLIPVisionLoader, DownloadAndLoadFlorence2Model, Florence2Run, FluxGuidance, GrowMask, ImageScale, InpaintModelConditioning, JoinImageWithAlpha, KSampler, LayerMask: SegmentAnythingUltra V2, LoadImage, PreviewImage, ReduxAdvanced, SaveImage, ShowText|pysssss, StyleModelLoader, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/服装材质迁移_1910490609034166274.json, 图片生成/图生图/服装材质迁移电商换服装_1919553999291219970.json, 平台全量/服装材质迁移电商换服装_1927239678276096002.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_clip_88

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/服装材质迁移_1910490609034166274.json、图片生成/图生图/服装材质迁移电商换服装_1919553999291219970.json、平台全量/服装材质迁移电商换服装_1927239678276096002.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `DownloadAndLoadFlorence2Model`
- `Florence2Run`
- `FluxGuidance`
- `GrowMask`
- `ImageScale`
- `InpaintModelConditioning`
- `JoinImageWithAlpha`
- `KSampler`
- `LayerMask: SegmentAnythingUltra V2`
- `LoadImage`
- `PreviewImage`
- `ReduxAdvanced`
- `SaveImage`
- `ShowText|pysssss`
- `StyleModelLoader`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `AIO_Preprocessor` —— 2/3 个有
- `ConstrainImage|pysssss` —— 2/3 个有
- `ControlNetApplyAdvanced` —— 2/3 个有
- `ControlNetLoader` —— 2/3 个有
- `DualCLIPLoaderGGUF` —— 2/3 个有
- `SetUnionControlNetType` —— 2/3 个有
- `DualCLIPLoader` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | normal | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| ControlNet 权重 | 0.6 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 normal，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 0.6，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
