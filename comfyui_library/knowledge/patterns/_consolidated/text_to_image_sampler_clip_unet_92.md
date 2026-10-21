---
name: text_to_image_sampler_clip_unet_92
type: Text To Image
frequency: 5
level: moderate
coverage: 0.9122
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-Image Base +ControlNet_2022640984902864898.json, 图片生成/文生图/Z-Image Turbo 文生图_2009309148017598465.json, 图片生成/文生图/Z-iamge文生图千问VL反推无需提示词自动文生图_1993913264711155713.json, 图片生成/文生图/Z-image-trubo_深度控制_2090688273374081025.json, 图片生成/文生图/z image controlnet（cnet）【支持切换】_2001231394615554050.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_92

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/Z-Image Base +ControlNet_2022640984902864898.json、图片生成/文生图/Z-Image Turbo 文生图_2009309148017598465.json、图片生成/文生图/Z-iamge文生图千问VL反推无需提示词自动文生图_1993913264711155713.json、图片生成/文生图/Z-image-trubo_深度控制_2090688273374081025.json、图片生成/文生图/z image controlnet（cnet）【支持切换】_2001231394615554050.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 4/5 个有
- `ModelSamplingAuraFlow` —— 4/5 个有
- `ConditioningZeroOut` —— 3/5 个有
- `ModelPatchLoader` —— 3/5 个有
- `AIO_Preprocessor` —— 2/5 个有
- `PreviewImage` —— 2/5 个有
- `ZImageFunControlnet` —— 2/5 个有
- `AILab_QwenVL` —— 1/5 个有
- `ConditioningNoiseInjection` —— 1/5 个有
- `DF_Float` —— 1/5 个有
- `DF_Text_Box` —— 1/5 个有
- `Image Switch (JPS)` —— 1/5 个有
- `JWInteger` —— 1/5 个有
- `QwenImageDiffsynthControlnet` —— 1/5 个有
- `Zoe-DepthMapPreprocessor` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 768 | 720 - 1200 | 5 | 77% |
| 高度 | 1280 | 1024 - 1536 | 5 | 83% |
| 采样步数 | 10 | 8 - 30 | 5 | 39% |
| Prompt 约束强度(CFG) | 1 | 1 - 3 | 5 | 43% |
| 采样算法 | euler | - | 5 | 80% |
| 调度器 | simple | - | 5 | 80% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 768，观测区间 720 - 1200，5 个样本
- 高度 中位数 1280，观测区间 1024 - 1536，5 个样本，取值集中（一致性 83%）
- 采样步数 中位数 10，观测区间 8 - 30，5 个样本，取值分散，一致性仅 39%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3，5 个样本，取值分散，一致性仅 43%
- 采样算法 最常用 euler，5 个样本，一致性 80%
- 调度器 最常用 simple，5 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
