---
name: unknown_workflow_ipadapter_lora_sampler
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.6365
common_nodes: [ApplyFluxIPAdapter, CLIPTextEncode, CLIPTextEncodeFlux, DualCLIPLoader, EmptyLatentImage, GetNode, INTConstant, Image Comparer (rgthree), ImageScale, LoadFluxIPAdapter, LoadImage, LoraLoader, PreviewImage, SaveImage, SetNode, UNETLoader, VAEDecode, VAELoader, XlabsSampler]
problems: []
missing: []
members: [图片生成/图生图/多图风格融合  Flux+IPAdapter_1915051485367889922.json, 图片生成/文生图/Flux+IPAdapter 文生同风格图片_1914704276978106370.json]
source: knowledge_consolidation
---

# unknown_workflow_ipadapter_lora_sampler

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/多图风格融合  Flux+IPAdapter_1915051485367889922.json、图片生成/文生图/Flux+IPAdapter 文生同风格图片_1914704276978106370.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：64%

## 共有节点

全部 2 个 workflow 都包含：
- `ApplyFluxIPAdapter`
- `CLIPTextEncode`
- `CLIPTextEncodeFlux`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `GetNode`
- `INTConstant`
- `Image Comparer (rgthree)`
- `ImageScale`
- `LoadFluxIPAdapter`
- `LoadImage`
- `LoraLoader`
- `PreviewImage`
- `SaveImage`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `XlabsSampler`

**可变部分**（部分 workflow 才有）：
- `ImpactMakeImageBatch` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |
| 宽度 | 636 | - | 2 | 79% |
| 高度 | 768 | - | 2 | 67% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 636，样本不足，未给区间，2 个样本
- 高度 中位数 768，样本不足，未给区间，2 个样本
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
