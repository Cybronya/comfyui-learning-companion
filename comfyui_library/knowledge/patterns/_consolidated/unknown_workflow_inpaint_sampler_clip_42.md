---
name: unknown_workflow_inpaint_sampler_clip_42
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.9104
common_nodes: [CLIPTextEncode, DualCLIPLoader, FluxGuidance, InpaintModelConditioning, KSampler, LoadImage, SaveImage, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/NunchakuFluxFill扩图_1917225990723145729.json, 图片生成/图生图/修图之扩图_1940017328061059073.json, 图片生成/图生图/扩图工作流_1960881467314376706.json, 平台全量/修图之手部修复_1933483374319419393.json, 平台全量/电商修图之扩图Flux_1926893240484794369.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_clip_42

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/NunchakuFluxFill扩图_1917225990723145729.json、图片生成/图生图/修图之扩图_1940017328061059073.json、图片生成/图生图/扩图工作流_1960881467314376706.json、平台全量/修图之手部修复_1933483374319419393.json、平台全量/电商修图之扩图Flux_1926893240484794369.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 5 个 workflow 都包含：
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
- `ImagePadForOutpaint` —— 4/5 个有
- `Joy_caption_two` —— 4/5 个有
- `Joy_caption_two_load` —— 4/5 个有
- `UNETLoader` —— 4/5 个有
- `RepeatLatentBatch` —— 2/5 个有
- `ShowText|pysssss` —— 2/5 个有
- `InpaintCrop` —— 1/5 个有
- `InpaintResize` —— 1/5 个有
- `InpaintStitch` —— 1/5 个有
- `LayerMask: MaskPreview` —— 1/5 个有
- `NunchakuFluxDiTLoader` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 8 | 5 | 0% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | normal | - | 5 | 80% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 8，5 个样本，取值分散，一致性仅 0%
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 normal，5 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
