---
name: unknown_workflow_sampler_clip_unet_320
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.7734
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, KSampler, MOSSMergePreset, PreviewAny, PrimitiveStringMultiline, ResolutionSelector, SaveImage, SkipLayerGuidanceDiTSimple, TextGenerate, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/绅士美学文生图V2_2115453703879741441.json, 图片生成/文生图/绅士美学文生图V2_2115640338688864258.json, 图片生成/文生图/超写实高质量Moss Base+sft bf16双模型融合工作流_2115267220510171137.json, 平台全量/超写实高质量Moss Base+sft bf16双模型融合工作流_2115751733669490689.json, 平台全量/超写实高质量Moss_Base+sft_bf16双模型融合工作流_2119974887900139521.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_320

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/绅士美学文生图V2_2115453703879741441.json、图片生成/文生图/绅士美学文生图V2_2115640338688864258.json、图片生成/文生图/超写实高质量Moss Base+sft bf16双模型融合工作流_2115267220510171137.json、平台全量/超写实高质量Moss Base+sft bf16双模型融合工作流_2115751733669490689.json、平台全量/超写实高质量Moss_Base+sft_bf16双模型融合工作流_2119974887900139521.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：77%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `KSampler`
- `MOSSMergePreset`
- `PreviewAny`
- `PrimitiveStringMultiline`
- `ResolutionSelector`
- `SaveImage`
- `SkipLayerGuidanceDiTSimple`
- `TextGenerate`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `孤海注释` —— 4/5 个有
- `CR Text` —— 2/5 个有
- `CR Text Replace` —— 2/5 个有
- `JDCN_StringToList` —— 2/5 个有
- `ProcessString` —— 2/5 个有
- `LoadImage` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 50 | 50 - 50 | 5 | 100% |
| Prompt 约束强度(CFG) | 3 | 3 - 3 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 50，观测区间 50 - 50，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 3，观测区间 3 - 3，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
