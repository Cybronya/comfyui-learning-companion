---
name: image_to_image_upscale_sampler_clip_47
type: Image To Image
frequency: 2
level: weak
coverage: 0.8055
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, ImageUpscaleWithModel, KSampler, LoadImage, SaveImage, UpscaleModelLoader, VAEDecode, VAEEncode]
problems: []
missing: []
members: [图片生成/图生图/真人转绘动漫_1902191520798416898.json, 图片生成/文生图/图生图三重放大工作流_1892316086548008961.json]
source: knowledge_consolidation
---

# image_to_image_upscale_sampler_clip_47

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/真人转绘动漫_1902191520798416898.json、图片生成/文生图/图生图三重放大工作流_1892316086548008961.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：81%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ImageUpscaleWithModel`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`

**可变部分**（部分 workflow 才有）：
- `CLIPSetLastLayer` —— 1/2 个有
- `LatentUpscaleBy` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `UltimateSDUpscale` —— 1/2 个有
- `scale` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 27.5 | - | 2 | 91% |
| Prompt 约束强度(CFG) | 7 | - | 2 | 100% |
| 采样算法 | euler_ancestral | - | 2 | 50% |
| 调度器 | ddim_uniform | - | 2 | 50% |
| 重绘幅度 | 0.505 | - | 2 | 99% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 27.5，样本不足，未给区间，2 个样本，取值集中（一致性 91%）
- Prompt 约束强度(CFG) 中位数 7，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，2 个样本，一致性 50%
- 调度器 最常用 ddim_uniform，2 个样本，一致性 50%
- 重绘幅度 中位数 0.505，样本不足，未给区间，2 个样本，取值集中（一致性 99%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
