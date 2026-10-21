---
name: image_to_image_sampler_checkpoint_vae
type: Image To Image
frequency: 2
level: weak
coverage: 0.85
common_nodes: [CheckpointLoaderSimple, ImageScaleToTotalPixels, KSampler, LoadImage, PreviewImage, SaveImage, VAEDecode, VAEEncode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/1977650991560577025.json, 图片生成/文生图/文生图基础款（放大版）_1992815640671219713.json]
source: knowledge_consolidation
---

# image_to_image_sampler_checkpoint_vae

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/1977650991560577025.json、图片生成/文生图/文生图基础款（放大版）_1992815640671219713.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：85%

## 共有节点

全部 2 个 workflow 都包含：
- `CheckpointLoaderSimple`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`

**可变部分**（部分 workflow 才有）：
- `CLIPTextEncode` —— 1/2 个有
- `ImageScaleBy` —— 1/2 个有
- `TextEncodeQwenImageEditPlus` —— 1/2 个有
- `UpscaleImageByUsingModel` —— 1/2 个有
- `UpscaleModelLoader` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 12 | - | 2 | 33% |
| Prompt 约束强度(CFG) | 4.5 | - | 2 | 22% |
| 采样算法 | sa_solver | - | 2 | 50% |
| 调度器 | beta | - | 2 | 50% |
| 重绘幅度 | 0.5 | - | 2 | 0% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 12，样本不足，未给区间，2 个样本，取值分散，一致性仅 33%
- Prompt 约束强度(CFG) 中位数 4.5，样本不足，未给区间，2 个样本，取值分散，一致性仅 22%
- 采样算法 最常用 sa_solver，2 个样本，一致性 50%
- 调度器 最常用 beta，2 个样本，一致性 50%
- 重绘幅度 中位数 0.5，样本不足，未给区间，2 个样本，取值分散，一致性仅 0%
- 风险：重绘幅度 观测到 0，低于常用下限 0.1（）
- 高发问题（1/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
