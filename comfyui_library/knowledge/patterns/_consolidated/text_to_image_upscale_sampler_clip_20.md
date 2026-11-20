---
name: text_to_image_upscale_sampler_clip_20
type: Text To Image
frequency: 5
level: moderate
coverage: 0.8688
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JoinStrings, KSampler, Qwen3_VQA, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, ShowText|pysssss, SomethingToString, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Z-image-turbo基础图生图+高清放大_2063183525263798273.json, 图片生成/文生图/Anima3_动漫文生图+Qwen3工作流_2043942915990360065.json, 图片生成/文生图/Anima动漫文生图+Qwen3工作流_2019122223247794178.json, 图片生成/文生图/Anima动漫文生图-角色图像反推（支持二次元热门手游角色）_2019429862456434689.json, 图片生成/文生图/Z-image turbo 文生图 （图生图）_1995303972401557505.json]
source: knowledge_consolidation
---

# text_to_image_upscale_sampler_clip_20

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Z-image-turbo基础图生图+高清放大_2063183525263798273.json、图片生成/文生图/Anima3_动漫文生图+Qwen3工作流_2043942915990360065.json、图片生成/文生图/Anima动漫文生图+Qwen3工作流_2019122223247794178.json、图片生成/文生图/Anima动漫文生图-角色图像反推（支持二次元热门手游角色）_2019429862456434689.json、图片生成/文生图/Z-image turbo 文生图 （图生图）_1995303972401557505.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JoinStrings`
- `KSampler`
- `Qwen3_VQA`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `ShowText|pysssss`
- `SomethingToString`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 4/5 个有
- `ImageScaleToTotalPixels` —— 3/5 个有
- `LoadImage` —— 3/5 个有
- `PreviewAny` —— 3/5 个有
- `TextInput_` —— 3/5 个有
- `ConditioningZeroOut` —— 2/5 个有
- `ImageResizeKJv2` —— 2/5 个有
- `Image Comparer (rgthree)` —— 1/5 个有
- `LoraLoaderModelOnly` —— 1/5 个有
- `StringConstantMultiline` —— 1/5 个有
- `VAEEncode` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 896 | 720 - 1024 | 5 | 89% |
| 高度 | 1152 | 1152 - 1536 | 5 | 88% |
| 采样步数 | 30 | 8 - 30 | 5 | 49% |
| Prompt 约束强度(CFG) | 4 | 1 - 4 | 5 | 48% |
| 采样算法 | er_sde | - | 5 | 60% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 896，观测区间 720 - 1024，5 个样本，取值集中（一致性 89%）
- 高度 中位数 1152，观测区间 1152 - 1536，5 个样本，取值集中（一致性 88%）
- 采样步数 中位数 30，观测区间 8 - 30，5 个样本，取值分散，一致性仅 49%
- Prompt 约束强度(CFG) 中位数 4，观测区间 1 - 4，5 个样本，取值分散，一致性仅 48%
- 采样算法 最常用 er_sde，5 个样本，一致性 60%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
