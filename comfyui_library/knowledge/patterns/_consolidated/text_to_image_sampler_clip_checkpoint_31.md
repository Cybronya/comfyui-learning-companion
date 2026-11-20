---
name: text_to_image_sampler_clip_checkpoint_31
type: Text To Image
frequency: 2
level: weak
coverage: 0.9445
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, EmptyLatentImage, KSampler, SaveImage, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Flux_Commercial_FaceLock_2004750671989665794.json, 图片生成/文生图/workflow_Qwen_image_character_2033556347710607362.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_checkpoint_31

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/Flux_Commercial_FaceLock_2004750671989665794.json、图片生成/文生图/workflow_Qwen_image_character_2033556347710607362.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：94%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `DualCLIPLoader` —— 1/2 个有
- `IPAdapterAdvanced` —— 1/2 个有
- `IPAdapterUnifiedLoader` —— 1/2 个有
- `LoadImageFromUrl` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 26.5 | - | 2 | 94% |
| Prompt 约束强度(CFG) | 4.75 | - | 2 | 74% |
| 采样算法 | euler | - | 2 | 50% |
| 调度器 | simple | - | 2 | 50% |
| 重绘幅度 | 1 | - | 2 | 100% |
| 宽度 | 988 | - | 2 | 91% |
| 高度 | 1536 | - | 2 | 75% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 26.5，样本不足，未给区间，2 个样本，取值集中（一致性 94%）
- Prompt 约束强度(CFG) 中位数 4.75，样本不足，未给区间，2 个样本
- 采样算法 最常用 euler，2 个样本，一致性 50%
- 调度器 最常用 simple，2 个样本，一致性 50%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 988，样本不足，未给区间，2 个样本，取值集中（一致性 91%）
- 高度 中位数 1536，样本不足，未给区间，2 个样本
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
