---
name: image_to_image_sampler_clip_unet_105
type: Image To Image
frequency: 5
level: weak
coverage: 0.9002
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/28.tonnie-Wan2.2文生图、洗图工作流_2001258902077534210.json, 图片生成/文生图/Anima Preview2图生图_2033542974574956546.json, 图片生成/文生图/Magic-Wan-V2加速图生图_1991143691563696129.json, 图片生成/文生图/Magic-Wan-V2图生图_1991113183234732033.json, 视频生成/图生视频/【动漫】Anima Preview2图生图_2038098911314841602.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_105

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/28.tonnie-Wan2.2文生图、洗图工作流_2001258902077534210.json、图片生成/文生图/Anima Preview2图生图_2033542974574956546.json、图片生成/文生图/Magic-Wan-V2加速图生图_1991143691563696129.json、图片生成/文生图/Magic-Wan-V2图生图_1991113183234732033.json、视频生成/图生视频/【动漫】Anima Preview2图生图_2038098911314841602.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ModelSamplingSD3` —— 3/5 个有
- `PreviewImage` —— 3/5 个有
- `ImageResizeKJv2` —— 2/5 个有
- `LoraLoaderModelOnly` —— 2/5 个有
- `Seed (rgthree)` —— 2/5 个有
- `WD14Tagger|pysssss` —— 2/5 个有
- `image_scale_pixel_v2` —— 2/5 个有
- `EmptyHunyuanVideo15Latent` —— 1/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 4 - 40 | 5 | 32% |
| Prompt 约束强度(CFG) | 3 | 1 - 4 | 5 | 49% |
| 采样算法 | dpmpp_2m_sde_gpu | - | 5 | 40% |
| 调度器 | sgm_uniform | - | 5 | 40% |
| 重绘幅度 | 0.75 | 0.3 - 0.75 | 5 | 73% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 25，观测区间 4 - 40，5 个样本，取值分散，一致性仅 32%
- Prompt 约束强度(CFG) 中位数 3，观测区间 1 - 4，5 个样本，取值分散，一致性仅 49%
- 采样算法 最常用 dpmpp_2m_sde_gpu，5 个样本，一致性 40%
- 调度器 最常用 sgm_uniform，5 个样本，一致性 40%
- 重绘幅度 中位数 0.75，观测区间 0.3 - 0.75，5 个样本
- 高发问题（3/5 个样本）：Steps较低可能导致细节不足
