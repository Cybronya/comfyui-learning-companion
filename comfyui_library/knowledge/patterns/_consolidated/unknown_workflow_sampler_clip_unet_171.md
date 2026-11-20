---
name: unknown_workflow_sampler_clip_unet_171
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.79825
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Y-image_chroma1_radiance_text_to_image_1971904444222926850.json, 图片生成/文生图/Z-Image-BEYOND REALITY SUPER Z IMAGE 3.0 淡妆浓抹_2018826875602214914.json, 图片生成/文生图/Z-Image-Base - 文生图 官方基础版_2016349336380121090.json, 图片生成/文生图/Z-Image-Base-Text to Image_2016308651929116673.json, 图片生成/文生图/Z-Image-Base文生图-自然美学v260128_2016358691083128834.json, 图片生成/文生图/基础文生海报_1932345808937807873.json, 图片生成/文生图/文生图-极致自然-Z-Image-Base_2016417634937475073.json, 图片生成/文生图/文生图对比Z-Image-bf16 res vs bf16 euler vs turbo_2016748618899787777.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_171

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/Y-image_chroma1_radiance_text_to_image_1971904444222926850.json、图片生成/文生图/Z-Image-BEYOND REALITY SUPER Z IMAGE 3.0 淡妆浓抹_2018826875602214914.json、图片生成/文生图/Z-Image-Base - 文生图 官方基础版_2016349336380121090.json、图片生成/文生图/Z-Image-Base-Text to Image_2016308651929116673.json、图片生成/文生图/Z-Image-Base文生图-自然美学v260128_2016358691083128834.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：80%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptySD3LatentImage` —— 7/8 个有
- `easy cleanGpuUsed` —— 5/8 个有
- `SDXL Resolutions (JPS)` —— 4/8 个有
- `LayerUtility: ImageReel` —— 2/8 个有
- `LayerUtility: ImageReelComposit` —— 2/8 个有
- `ConditioningZeroOut` —— 1/8 个有
- `EmptyChromaRadianceLatentImage` —— 1/8 个有
- `LoadImage` —— 1/8 个有
- `MuyeTextEditOutput` —— 1/8 个有
- `SDXLAspectRatio` —— 1/8 个有
- `T5TokenizerOptions` —— 1/8 个有
- `easy seed` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 27.5 | 10 - 50 | 8 | 48% |
| Prompt 约束强度(CFG) | 4 | 1 - 4 | 8 | 60% |
| 采样算法 | euler | - | 8 | 88% |
| 调度器 | simple | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 27.5，观测区间 10 - 50，8 个样本，取值分散，一致性仅 48%
- Prompt 约束强度(CFG) 中位数 4，观测区间 1 - 4，8 个样本
- 采样算法 最常用 euler，8 个样本，一致性 88%
- 调度器 最常用 simple，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
