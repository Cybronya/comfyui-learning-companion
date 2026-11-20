---
name: text_to_image_sampler_clip_unet_236
type: Text To Image
frequency: 2
level: weak
coverage: 0.95
common_nodes: [CLIPLoaderGGUF, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-image文生图极速版_2080574582356013057.json, 图片生成/文生图/Zimage基础文生图工作流-入门学习版_2079907512651964418.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_236

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/Z-image文生图极速版_2080574582356013057.json、图片生成/文生图/Zimage基础文生图工作流-入门学习版_2079907512651964418.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：95%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoaderGGUF`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LatentUpscaleBy` —— 1/2 个有
- `LayerUtility: Seed` —— 1/2 个有
- `ModelSamplingAuraFlow` —— 1/2 个有
- `RHLoraLoader` —— 1/2 个有
- `ttN concat` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 14 | - | 2 | 57% |
| Prompt 约束强度(CFG) | 3.75 | - | 2 | 27% |
| 采样算法 | res_multistep | - | 2 | 50% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |
| 宽度 | 1280 | - | 2 | 80% |
| 高度 | 944 | - | 2 | 92% |
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 14，样本不足，未给区间，2 个样本
- Prompt 约束强度(CFG) 中位数 3.75，样本不足，未给区间，2 个样本，取值分散，一致性仅 27%
- 采样算法 最常用 res_multistep，2 个样本，一致性 50%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 1280，样本不足，未给区间，2 个样本，取值集中（一致性 80%）
- 高度 中位数 944，样本不足，未给区间，2 个样本，取值集中（一致性 92%）
- 高发问题（1/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
