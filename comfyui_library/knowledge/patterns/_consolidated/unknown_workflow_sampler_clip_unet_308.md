---
name: unknown_workflow_sampler_clip_unet_308
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.8874
common_nodes: [CLIPTextEncode, DualCLIPLoader, EmptyLatentImage, FluxSamplerParams+, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/FLUX1-DEV-FP16文生图_2032756063350562818.json, 图片生成/文生图/FLUX1-DEV-FP16文生图_2043001809165361153.json, 图片生成/文生图/Flux文生图_2041424074966044673.json, 图片生成/文生图/文生图生成精美的手工设计图_1892852557050777602.json, 平台全量/FLUX_充气膨胀背景_1962718401800089601.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_308

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/FLUX1-DEV-FP16文生图_2032756063350562818.json、图片生成/文生图/FLUX1-DEV-FP16文生图_2043001809165361153.json、图片生成/文生图/Flux文生图_2041424074966044673.json、图片生成/文生图/文生图生成精美的手工设计图_1892852557050777602.json、平台全量/FLUX_充气膨胀背景_1962718401800089601.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `FluxSamplerParams+`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Int2String` —— 2/5 个有
- `LoraLoader` —— 2/5 个有
- `PreviewImage` —— 2/5 个有
- `Seed_` —— 2/5 个有
- `DeepTranslatorTextNode` —— 1/5 个有
- `JjkText` —— 1/5 个有
- `Note _O` —— 1/5 个有
- `TextCombinerTwo` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 768 | 768 - 1024 | 5 | 86% |
| 高度 | 1024 | 1024 - 1024 | 5 | 100% |
| LoRA 模型强度 | 1 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 768，观测区间 768 - 1024，5 个样本，取值集中（一致性 86%）
- 高度 中位数 1024，观测区间 1024 - 1024，5 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
