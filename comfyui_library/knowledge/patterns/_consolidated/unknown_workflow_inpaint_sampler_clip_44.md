---
name: unknown_workflow_inpaint_sampler_clip_44
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.94
common_nodes: [CLIPTextEncode, DualCLIPLoader, FluxGuidance, ImagePadForOutpaint, InpaintModelConditioning, KSampler, LoadImage, SaveImage, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/NunchakuFluxFill扩图_1917225990723145729.json, 图片生成/图生图/修图之扩图_1940017328061059073.json, 图片生成/图生图/扩图工作流_1960881467314376706.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_clip_44

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/NunchakuFluxFill扩图_1917225990723145729.json、图片生成/图生图/修图之扩图_1940017328061059073.json、图片生成/图生图/扩图工作流_1960881467314376706.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `DualCLIPLoader`
- `FluxGuidance`
- `ImagePadForOutpaint`
- `InpaintModelConditioning`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Joy_caption_two` —— 2/3 个有
- `Joy_caption_two_load` —— 2/3 个有
- `UNETLoader` —— 2/3 个有
- `LayerMask: MaskPreview` —— 1/3 个有
- `NunchakuFluxDiTLoader` —— 1/3 个有
- `RepeatLatentBatch` —— 1/3 个有
- `ShowText|pysssss` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 8 | 3 | 1% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | normal | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 8，3 个样本，取值分散，一致性仅 1%
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 normal，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
