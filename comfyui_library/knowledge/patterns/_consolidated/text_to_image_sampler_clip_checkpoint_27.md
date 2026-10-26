---
name: text_to_image_sampler_clip_checkpoint_27
type: Text To Image
frequency: 2
level: weak
coverage: 0.7595
common_nodes: [CLIPTextEncode, CR Prompt Text, CheckpointLoaderSimple, EmptyLatentImage, Image Pixelate, ImageScale, ImageScaleBy, ImpactImageBatchToImageList, ImpactMakeAnyList, KSampler, KSamplerAdvanced, Latent Noise Injection, PreviewImage, PrimitiveInt, SaveImage, VAEDecode, VAEEncode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-image AIO 破解随机性：揭秘核心算法漏洞，轻松掌控图像生成不确定性_1999257917524148226.json, 视频生成/图生视频/AI短剧制作全流程_2113561880127164418.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_checkpoint_27

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/Z-image AIO 破解随机性：揭秘核心算法漏洞，轻松掌控图像生成不确定性_1999257917524148226.json、视频生成/图生视频/AI短剧制作全流程_2113561880127164418.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：76%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `CR Prompt Text`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `Image Pixelate`
- `ImageScale`
- `ImageScaleBy`
- `ImpactImageBatchToImageList`
- `ImpactMakeAnyList`
- `KSampler`
- `KSamplerAdvanced`
- `Latent Noise Injection`
- `PreviewImage`
- `PrimitiveInt`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`

**可变部分**（部分 workflow 才有）：
- `EmptyImage` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 2 | 100% |
| Prompt 约束强度(CFG) | 10 | - | 2 | 100% |
| 采样算法 | 1 | - | 2 | 100% |
| 调度器 | er_sde | - | 2 | 100% |
| 重绘幅度 | simple | - | 2 | 100% |
| 宽度 | 400 | - | 2 | 100% |
| 高度 | 600 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 最常用 fixed，2 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 10，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 最常用 er_sde，2 个样本，一致性 100%
- 重绘幅度 最常用 simple，2 个样本，一致性 100%
- 宽度 中位数 400，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 600，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
