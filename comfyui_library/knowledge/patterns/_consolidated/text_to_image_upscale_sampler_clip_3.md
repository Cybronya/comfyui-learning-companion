---
name: text_to_image_upscale_sampler_clip_3
type: Text To Image
frequency: 2
level: weak
coverage: 0.831
common_nodes: [ArgosTranslateTextNode, CLIPTextEncode, CheckpointLoaderSimple, ConditioningCombine, EmptyLatentImage, Image Comparer (rgthree), ImageUpscaleWithModel, KSampler, PreviewImage, SaveImage, UpscaleModelLoader, VAEDecode, easy stylesSelector]
problems: []
missing: [easy stylesSelector]
members: [图片生成/文生图/1964422987531341826.json, 图片生成/文生图/1964984606757896194.json]
source: knowledge_consolidation
---

# text_to_image_upscale_sampler_clip_3

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/1964422987531341826.json、图片生成/文生图/1964984606757896194.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：83%

## 共有节点

全部 2 个 workflow 都包含：
- `ArgosTranslateTextNode`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ConditioningCombine`
- `EmptyLatentImage`
- `Image Comparer (rgthree)`
- `ImageUpscaleWithModel`
- `KSampler`
- `PreviewImage`
- `SaveImage`
- `UpscaleModelLoader`
- `VAEDecode`
- `easy stylesSelector`

**可变部分**（部分 workflow 才有）：
- `ImageScaleBy` —— 1/2 个有
- `LatentUpscaleBy` —— 1/2 个有
- `UltimateSDUpscale` —— 1/2 个有
- `VAEEncode` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 8 | - | 2 | 100% |
| 采样算法 | dpmpp_2m_sde | - | 2 | 100% |
| 调度器 | karras | - | 2 | 100% |
| 重绘幅度 | 0.775 | - | 2 | 71% |
| 宽度 | 1024 | - | 2 | 100% |
| 高度 | 1024 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 30，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_2m_sde，2 个样本，一致性 100%
- 调度器 最常用 karras，2 个样本，一致性 100%
- 重绘幅度 中位数 0.775，样本不足，未给区间，2 个样本
- 宽度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：easy stylesSelector
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
