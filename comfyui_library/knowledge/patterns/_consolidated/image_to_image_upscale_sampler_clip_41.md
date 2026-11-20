---
name: image_to_image_upscale_sampler_clip_41
type: Image To Image
frequency: 4
level: strong
coverage: 0.84325
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, KSampler, LoadImage, SaveImage, UpscaleModelLoader, VAEDecode, VAEEncode]
problems: []
missing: []
members: [图片生成/图生图/真人转绘动漫_1902191520798416898.json, 图片生成/文生图/图生图三重放大工作流_1892316086548008961.json, 平台全量/一键真人转二次元_1906322438920278017.json, 平台全量/图片清晰_2004151265187774465.json]
source: knowledge_consolidation
---

# image_to_image_upscale_sampler_clip_41

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/真人转绘动漫_1902191520798416898.json、图片生成/文生图/图生图三重放大工作流_1892316086548008961.json、平台全量/一键真人转二次元_1906322438920278017.json、平台全量/图片清晰_2004151265187774465.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`

**可变部分**（部分 workflow 才有）：
- `ImageUpscaleWithModel` —— 3/4 个有
- `CLIPSetLastLayer` —— 2/4 个有
- `LatentUpscaleBy` —— 2/4 个有
- `PreviewImage` —— 2/4 个有
- `UltimateSDUpscale` —— 2/4 个有
- `scale` —— 2/4 个有
- `UpscaleImageByUsingModel` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 27.5 | 20 - 30 | 4 | 84% |
| Prompt 约束强度(CFG) | 7 | 6.5 - 7 | 4 | 97% |
| 采样算法 | euler_ancestral | - | 4 | 50% |
| 调度器 | ddim_uniform | - | 4 | 50% |
| 重绘幅度 | 0.555 | 0.5 - 0.6 | 4 | 91% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 27.5，观测区间 20 - 30，4 个样本，取值集中（一致性 84%）
- Prompt 约束强度(CFG) 中位数 7，观测区间 6.5 - 7，4 个样本，取值集中（一致性 97%）
- 采样算法 最常用 euler_ancestral，4 个样本，一致性 50%
- 调度器 最常用 ddim_uniform，4 个样本，一致性 50%
- 重绘幅度 中位数 0.555，观测区间 0.5 - 0.6，4 个样本，取值集中（一致性 91%）
