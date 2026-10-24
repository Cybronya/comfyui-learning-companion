---
name: unknown_workflow_sampler_clip_vae_73
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9335
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSamplerAdvanced, LoadImage, SaveImage, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Qwen Turbo Ultra X真实人像_1987072256373362689.json, 图片生成/文生图/【遇见AI】z-image + z-image turbo双采样_2053789587369144322.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_73

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/Qwen Turbo Ultra X真实人像_1987072256373362689.json、图片生成/文生图/【遇见AI】z-image + z-image turbo双采样_2053789587369144322.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：93%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSamplerAdvanced`
- `LoadImage`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `AILab_QwenVL` —— 1/2 个有
- `CheckpointLoaderSimple` —— 1/2 个有
- `ImageConcatMulti` —— 1/2 个有
- `UNETLoader` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 872 | - | 2 | 83% |
| 高度 | 1408 | - | 2 | 91% |
| 采样步数 | randomize | - | 2 | 100% |
| Prompt 约束强度(CFG) | 10.5 | - | 2 | 86% |
| 采样算法 | 1 | - | 2 | 100% |
| 调度器 | euler | - | 2 | 100% |
| 重绘幅度 | karras | - | 2 | 50% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 872，样本不足，未给区间，2 个样本，取值集中（一致性 83%）
- 高度 中位数 1408，样本不足，未给区间，2 个样本，取值集中（一致性 91%）
- 采样步数 最常用 randomize，2 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 10.5，样本不足，未给区间，2 个样本，取值集中（一致性 86%）
- 采样算法 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，2 个样本，一致性 100%
- 重绘幅度 最常用 karras，2 个样本，一致性 50%
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
