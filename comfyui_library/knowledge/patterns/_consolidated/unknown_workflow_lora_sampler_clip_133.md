---
name: unknown_workflow_lora_sampler_clip_133
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.9436
common_nodes: [CLIPTextEncodeFlux, DualCLIPLoader, EmptyLatentImage, FluxSamplerParams+, LoraLoader, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/反推提示词/Florence反推图像提示词_1979382942315220994.json, 图片生成/文生图/flux文生图_1988984318296985601.json, 平台全量/flux生图_1971839713608921090.json, 平台全量/虎咪-flux-t2i_1990582991317602306.json, 数字人/数字人/修手LORA_1972649415360073729.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_133

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/反推提示词/Florence反推图像提示词_1979382942315220994.json、图片生成/文生图/flux文生图_1988984318296985601.json、平台全量/flux生图_1971839713608921090.json、平台全量/虎咪-flux-t2i_1990582991317602306.json、数字人/数字人/修手LORA_1972649415360073729.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPTextEncodeFlux`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `FluxSamplerParams+`
- `LoraLoader`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 2/5 个有
- `RH_Translator` —— 2/5 个有
- `Florence2ModelLoader` —— 1/5 个有
- `Florence2Run` —— 1/5 个有
- `LoadImage` —— 1/5 个有
- `LorasForFluxParams+` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 768 - 1920 | 5 | 64% |
| 高度 | 1080 | 1024 - 1352 | 5 | 88% |
| LoRA 模型强度 | 1 | 0.9 - 1 | 5 | 96% |
| LoRA 文本强度 | 1 | 0.7 - 1 | 5 | 87% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 768 - 1920，5 个样本
- 高度 中位数 1080，观测区间 1024 - 1352，5 个样本，取值集中（一致性 88%）
- LoRA 模型强度 中位数 1，观测区间 0.9 - 1，5 个样本，取值集中（一致性 96%）
- LoRA 文本强度 中位数 1，观测区间 0.7 - 1，5 个样本，取值集中（一致性 87%）
