---
name: text_to_image_lora_sampler_clip_224
type: Text To Image
frequency: 5
level: strong
coverage: 0.8492
common_nodes: [CLIPLoader, CLIPTextEncode, DF_Text_Box, EmptyLatentImage, GH_ImageVideoComparer, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, QwenImage21Cache, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 图像缩放V2_孤海]
problems: [Steps较低可能导致细节不足]
missing: [图像缩放V2_孤海, 布尔孤海, LayerUtility: ImageScaleByAspectRatio V2]
members: [图片生成/图生图/2102264426807255042.json, 图片生成/图生图/2102265852648312834.json, 图片生成/图生图/2102313763641847810.json, 图片生成/图生图/2102508530350772225.json, 图片生成/图生图/2102546574596460545.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_224

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/2102264426807255042.json、图片生成/图生图/2102265852648312834.json、图片生成/图生图/2102313763641847810.json、图片生成/图生图/2102508530350772225.json、图片生成/图生图/2102546574596460545.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `DF_Text_Box`
- `EmptyLatentImage`
- `GH_ImageVideoComparer`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `QwenImage21Cache`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `图像缩放V2_孤海`

**可变部分**（部分 workflow 才有）：
- `GoohaiUniversalSlider` —— 4/5 个有
- `ResolutionSelector` —— 4/5 个有
- `easy ifElse` —— 4/5 个有
- `孤海注释` —— 4/5 个有
- `布尔孤海` —— 4/5 个有
- `GoohaiRatioAndResolution` —— 1/5 个有
- `ImpactMinMax` —— 1/5 个有
- `KepStringLiteral` —— 1/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/5 个有
- `SeedVR2LoadDiTModel` —— 1/5 个有
- `SeedVR2LoadVAEModel` —— 1/5 个有
- `SeedVR2VideoUpscaler` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 5 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 5 | 100% |
| 采样算法 | er_sde | - | 5 | 100% |
| 调度器 | beta | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| 宽度 | 80 | 80 - 80 | 5 | 100% |
| 高度 | 80 | 80 - 80 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，5 个样本，一致性 100%
- 调度器 最常用 beta，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：图像缩放V2_孤海、布尔孤海、LayerUtility: ImageScaleByAspectRatio V2
