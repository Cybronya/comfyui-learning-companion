---
name: unknown_workflow_inpaint_lora_sampler_124
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9365
common_nodes: [CLIPTextEncodeFlux, CLIPVisionLoader, ConditioningZeroOut, DualCLIPLoader, EmptyImage, ImageCrop+, ImageResize+, ImageToMask, InpaintModelConditioning, Int, KSampler, LoadImage, LoraLoader, PreviewImage, ReduxAdvanced, RepeatLatentBatch, SaveImage, StyleModelLoader, UNETLoader, VAEDecode, VAELoader, easy imageConcat]
problems: []
missing: []
members: [平台全量/万物迁移 模特服装替换 服装迁移_1922888694305538050.json, 平台全量/万物迁移之模特全自动换脸_1923325698399006722.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_lora_sampler_124

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/万物迁移 模特服装替换 服装迁移_1922888694305538050.json、平台全量/万物迁移之模特全自动换脸_1923325698399006722.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：94%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncodeFlux`
- `CLIPVisionLoader`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `EmptyImage`
- `ImageCrop+`
- `ImageResize+`
- `ImageToMask`
- `InpaintModelConditioning`
- `Int`
- `KSampler`
- `LoadImage`
- `LoraLoader`
- `PreviewImage`
- `ReduxAdvanced`
- `RepeatLatentBatch`
- `SaveImage`
- `StyleModelLoader`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy imageConcat`

**可变部分**（部分 workflow 才有）：
- `CLIPTextEncode` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 24 | - | 2 | 96% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |
| LoRA 模型强度 | 1 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 24，样本不足，未给区间，2 个样本，取值集中（一致性 96%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
