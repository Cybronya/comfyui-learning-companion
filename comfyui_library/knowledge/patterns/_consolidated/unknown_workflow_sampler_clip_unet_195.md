---
name: unknown_workflow_sampler_clip_unet_195
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.807571
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Y-image_chroma1_radiance_text_to_image_1971904444222926850.json, 图片生成/文生图/Z-Image-BEYOND REALITY SUPER Z IMAGE 3.0 淡妆浓抹_2018826875602214914.json, 图片生成/文生图/Z-Image-Base - 文生图 官方基础版_2016349336380121090.json, 图片生成/文生图/Z-Image-Base-Text to Image_2016308651929116673.json, 图片生成/文生图/Z-Image-Base文生图-自然美学v260128_2016358691083128834.json, 图片生成/文生图/基础文生海报_1932345808937807873.json, 图片生成/文生图/文生图对比Z-Image-bf16 res vs bf16 euler vs turbo_2016748618899787777.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_195

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/Y-image_chroma1_radiance_text_to_image_1971904444222926850.json、图片生成/文生图/Z-Image-BEYOND REALITY SUPER Z IMAGE 3.0 淡妆浓抹_2018826875602214914.json、图片生成/文生图/Z-Image-Base - 文生图 官方基础版_2016349336380121090.json、图片生成/文生图/Z-Image-Base-Text to Image_2016308651929116673.json、图片生成/文生图/Z-Image-Base文生图-自然美学v260128_2016358691083128834.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：81%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptySD3LatentImage` —— 6/7 个有
- `SDXL Resolutions (JPS)` —— 4/7 个有
- `easy cleanGpuUsed` —— 4/7 个有
- `LayerUtility: ImageReel` —— 2/7 个有
- `LayerUtility: ImageReelComposit` —— 2/7 个有
- `ConditioningZeroOut` —— 1/7 个有
- `EmptyChromaRadianceLatentImage` —— 1/7 个有
- `LoadImage` —— 1/7 个有
- `MuyeTextEditOutput` —— 1/7 个有
- `SDXLAspectRatio` —— 1/7 个有
- `T5TokenizerOptions` —— 1/7 个有
- `easy seed` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 10 - 50 | 7 | 46% |
| Prompt 约束强度(CFG) | 4 | 1 - 4 | 7 | 57% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 30，观测区间 10 - 50，7 个样本，取值分散，一致性仅 46%
- Prompt 约束强度(CFG) 中位数 4，观测区间 1 - 4，7 个样本
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
