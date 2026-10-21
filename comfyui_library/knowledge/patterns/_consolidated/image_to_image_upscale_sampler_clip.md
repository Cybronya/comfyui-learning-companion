---
name: image_to_image_upscale_sampler_clip
type: Image To Image
frequency: 14
level: moderate
coverage: 0.685286
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, Fast Groups Bypasser (rgthree), Image Comparer (rgthree), ImpactInt, JoinStrings, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, PreviewImage, Qwen3_VQA, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TextInput_, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy showAnything]
problems: []
missing: [LayerUtility: ImageReel, LayerUtility: ImageReelComposit, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM, easy convertAnything, easy imageConcat, easy indexAnything]
members: [图片生成/反推提示词/qwen3反推Krea2洗图重绘去除Ai感+SeedVR放大_2077040370852130818.json, 图片生成/图生图/1995894229622800386.json, 图片生成/图生图/2077040370852130818.json, 图片生成/图生图/2105957638642167810.json, 图片生成/文生图/Z-IMAGE：图反推关键词+生图+高清放大_1995435685152796674.json, 图片生成/文生图/Z-IMAGE：小而美图像模型：自动反推洗图_1993918755539451906.json, 图片生成/文生图/Z-Image：图片去除Ai感工作流_1999383021906259970.json, 图片生成/文生图/Z-Image：图片去除Ai感工作流_2056552554821148673.json, 图片生成/文生图/Z-Image：图片去除Ai感工作流_2061617318295330817.json, 图片生成/文生图/Z-Image：图片去除Ai感工作流_2069967256154628097.json, 图片生成/文生图/qwen3反推Krea2洗图重绘去除Ai感+SeedVR放大_2089514888220725249.json, 图片生成/文生图/qwen3反推提示词并生图_2056909255499935745.json, 图片生成/文生图/qwen3反推提示词并生图_2057720195904532481.json, 图片生成/文生图/图片AI感消失 Z-Image：工作流_1999400749585006593.json]
source: knowledge_consolidation
---

# image_to_image_upscale_sampler_clip

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（图片生成/反推提示词/qwen3反推Krea2洗图重绘去除Ai感+SeedVR放大_2077040370852130818.json、图片生成/图生图/1995894229622800386.json、图片生成/图生图/2077040370852130818.json、图片生成/图生图/2105957638642167810.json、图片生成/文生图/Z-IMAGE：图反推关键词+生图+高清放大_1995435685152796674.json…）

- **类型**：Image To Image
- **样本数**：14
- **可信度**：中等可信
- **平均知识覆盖**：69%

## 共有节点

全部 14 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `Fast Groups Bypasser (rgthree)`
- `Image Comparer (rgthree)`
- `ImpactInt`
- `JoinStrings`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `PreviewImage`
- `Qwen3_VQA`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `TextInput_`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `ImageScaleBy` —— 12/14 个有
- `LayerUtility: ImageReel` —— 12/14 个有
- `LayerUtility: ImageReelComposit` —— 12/14 个有
- `ShowText|pysssss` —— 12/14 个有
- `LayerUtility: PurgeVRAM` —— 10/14 个有
- `easy imageConcat` —— 10/14 个有
- `LoraLoaderModelOnly` —— 3/14 个有
- `Float` —— 2/14 个有
- `MemoryCleaner` —— 2/14 个有
- `easy saveText` —— 2/14 个有
- `孤海注释` —— 2/14 个有
- `MuyeTextEditOutput` —— 1/14 个有
- `SomethingToString` —— 1/14 个有
- `easy convertAnything` —— 1/14 个有
- `easy indexAnything` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 10 - 40 | 14 | 36% |
| Prompt 约束强度(CFG) | 1 | 0.9 - 1 | 14 | 96% |
| 采样算法 | euler | - | 14 | 79% |
| 调度器 | simple | - | 14 | 100% |
| 重绘幅度 | 0.7 | 0.6 - 0.7 | 14 | 93% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 10，观测区间 10 - 40，14 个样本，取值分散，一致性仅 36%
- Prompt 约束强度(CFG) 中位数 1，观测区间 0.9 - 1，14 个样本，取值集中（一致性 96%）
- 采样算法 最常用 euler，14 个样本，一致性 79%
- 调度器 最常用 simple，14 个样本，一致性 100%
- 重绘幅度 中位数 0.7，观测区间 0.6 - 0.7，14 个样本，取值集中（一致性 93%）
- 风险：Prompt 约束强度(CFG) 观测到 0.9，低于常用下限 1（CFG 过低可能导致 Prompt 约束不足、结果偏离描述）
- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: ImageReel、LayerUtility: ImageReelComposit、LayerUtility: ImageScaleByAspectRatio V2、LayerUtility: PurgeVRAM、easy convertAnything
