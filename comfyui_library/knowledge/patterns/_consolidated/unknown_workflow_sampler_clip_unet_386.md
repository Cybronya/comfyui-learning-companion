---
name: unknown_workflow_sampler_clip_unet_386
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.958667
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/flux3_klien3快速-电商必备文生图_2110994732565483522.json, 图片生成/文生图/flux3_klien3文生图_2110978915194990593.json, 图片生成/文生图/文生图V2_2087151483677659138.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_386

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/flux3_klien3快速-电商必备文生图_2110994732565483522.json、图片生成/文生图/flux3_klien3文生图_2110978915194990593.json、图片生成/文生图/文生图V2_2087151483677659138.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSamplerSelect`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Int` —— 2/3 个有
- `ManualSigmas` —— 2/3 个有
- `PrimitiveStringMultiline` —— 2/3 个有
- `RH_Translator` —— 2/3 个有
- `BasicScheduler` —— 1/3 个有
- `LoraLoader` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1080 | 3 | 97% |
| 高度 | 1024 | 1024 - 1920 | 3 | 68% |
| LoRA 模型强度 | 0 | - | 1 | 100% |
| LoRA 文本强度 | 0 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1080，3 个样本，取值集中（一致性 97%）
- 高度 中位数 1024，观测区间 1024 - 1920，3 个样本
