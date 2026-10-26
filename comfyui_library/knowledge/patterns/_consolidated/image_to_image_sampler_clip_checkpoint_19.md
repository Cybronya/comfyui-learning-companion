---
name: image_to_image_sampler_clip_checkpoint_19
type: Image To Image
frequency: 2
level: weak
coverage: 0.775
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, ImageScaleToTotalPixels, KSampler, LoadImage, SaveImage, VAEDecode, VAEEncode]
problems: []
missing: []
members: [图片生成/文生图/文生图基础款_1983414020642381826.json, 图片生成/文生图/文生图基础款（放大版）_1992815640671219713.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_checkpoint_19

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/文生图基础款_1983414020642381826.json、图片生成/文生图/文生图基础款（放大版）_1992815640671219713.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：78%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`

**可变部分**（部分 workflow 才有）：
- `ImageScaleBy` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `UpscaleImageByUsingModel` —— 1/2 个有
- `UpscaleModelLoader` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 8 | - | 2 | 100% |
| 采样算法 | dpmpp_2m | - | 2 | 50% |
| 调度器 | normal | - | 2 | 50% |
| 重绘幅度 | 0.435 | - | 2 | 0% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_2m，2 个样本，一致性 50%
- 调度器 最常用 normal，2 个样本，一致性 50%
- 重绘幅度 中位数 0.435，样本不足，未给区间，2 个样本，取值分散，一致性仅 0%
- 风险：重绘幅度 观测到 0，低于常用下限 0.1（）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
