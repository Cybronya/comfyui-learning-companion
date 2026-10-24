---
name: image_to_image_controlnet_sampler_clip_18
type: Image To Image
frequency: 2
level: weak
coverage: 0.8435
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, ControlNetApply, ControlNetLoader, Image Comparer (rgthree), KSampler, LineArtPreprocessor, LoadImage, PreviewImage, SaveImage, VAEDecode, VAEEncode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/【AI小王子】17.Controlnet线稿工作流（动漫真人互转）_2046806320371732481.json, 图片生成/文生图/根据提示词就可以转换各种风格_1832312545226174466.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_sampler_clip_18

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/【AI小王子】17.Controlnet线稿工作流（动漫真人互转）_2046806320371732481.json、图片生成/文生图/根据提示词就可以转换各种风格_1832312545226174466.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：84%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ControlNetApply`
- `ControlNetLoader`
- `Image Comparer (rgthree)`
- `KSampler`
- `LineArtPreprocessor`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`

**可变部分**（部分 workflow 才有）：
- `ImageScale` —— 1/2 个有
- `MiDaS-DepthMapPreprocessor` —— 1/2 个有
- `PlaySound|pysssss` —— 1/2 个有
- `RepeatLatentBatch` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 14 | - | 2 | 57% |
| Prompt 约束强度(CFG) | 6.25 | - | 2 | 80% |
| 采样算法 | dpmpp_2m_sde | - | 2 | 50% |
| 调度器 | karras | - | 2 | 100% |
| 重绘幅度 | 0.95 | - | 2 | 95% |
| ControlNet 权重 | 0.625 | - | 2 | 72% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 14，样本不足，未给区间，2 个样本
- Prompt 约束强度(CFG) 中位数 6.25，样本不足，未给区间，2 个样本，取值集中（一致性 80%）
- 采样算法 最常用 dpmpp_2m_sde，2 个样本，一致性 50%
- 调度器 最常用 karras，2 个样本，一致性 100%
- 重绘幅度 中位数 0.95，样本不足，未给区间，2 个样本，取值集中（一致性 95%）
- ControlNet 权重 中位数 0.625，样本不足，未给区间，2 个样本
- 高发问题（1/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
