---
name: unknown_workflow_inpaint_lora_sampler_37
type: Unknown Workflow
frequency: 5
level: weak
coverage: 0.9536
common_nodes: [CLIPLoader, CLIPTextEncode, InpaintModelConditioning, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen文生图&重绘加速流_1956274474318528513.json, 平台全量/Qwen局部重绘工作流_1954879864228777986.json, 平台全量/Qwen最强修手工作流_1958164408205717505.json, 平台全量/Wan2.2最强修手工作流！_1957788675336929282.json, 平台全量/图片修复（最强修手修脚）_1945381810341650433.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_lora_sampler_37

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/Qwen文生图&重绘加速流_1956274474318528513.json、平台全量/Qwen局部重绘工作流_1954879864228777986.json、平台全量/Qwen最强修手工作流_1958164408205717505.json、平台全量/Wan2.2最强修手工作流！_1957788675336929282.json、平台全量/图片修复（最强修手修脚）_1945381810341650433.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：95%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `InpaintModelConditioning`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Mask Fill Holes` —— 3/5 个有
- `ModelSamplingAuraFlow` —— 3/5 个有
- `ModelSamplingSD3` —— 2/5 个有
- `EmptyHunyuanLatentVideo` —— 1/5 个有
- `Fast Groups Bypasser (rgthree)` —— 1/5 个有
- `INPAINT_ExpandMask` —— 1/5 个有
- `Image Comparer (rgthree)` —— 1/5 个有
- `easy float` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 6 - 10 | 5 | 82% |
| Prompt 约束强度(CFG) | 2.5 | 1 - 4 | 5 | 48% |
| 采样算法 | euler | - | 5 | 80% |
| 调度器 | simple | - | 5 | 60% |
| 重绘幅度 | 0.5 | 0.15 - 1 | 5 | 44% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 6 - 10，5 个样本，取值集中（一致性 82%）
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 1 - 4，5 个样本，取值分散，一致性仅 48%
- 采样算法 最常用 euler，5 个样本，一致性 80%
- 调度器 最常用 simple，5 个样本，一致性 60%
- 重绘幅度 中位数 0.5，观测区间 0.15 - 1，5 个样本，取值分散，一致性仅 44%
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
