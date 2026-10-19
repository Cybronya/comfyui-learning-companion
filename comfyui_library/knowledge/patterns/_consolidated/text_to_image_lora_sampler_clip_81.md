---
name: text_to_image_lora_sampler_clip_81
type: Text To Image
frequency: 10
level: strong
coverage: 0.7372
common_nodes: [CLIPLoader, CLIPTextEncode, DF_Text_Box, EmptyLatentImage, GetNode, GoohaiRatioAndResolution, GoohaiRouteBlocker, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, QwenImage21BlockCacheT8, QwenImage21SageAttentionT8, QwenImage21SpectrumT8, QwenImagePromptOptimizer, RestoreQwenImage21GH, SaveImage, SetNode, ShowText|pysssss, TextEncodeQwenImage21GH, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/反推提示词/Qwen Image 2.1文生图像编辑一体化 二合一工作流_2105396924613488642.json, 图片生成/反推提示词/Qwen Image 2.1文生图像编辑一体化工作流，自动扩写提示词多场景覆盖_2106471030431772674.json, 图片生成/反推提示词/Qwen Image 2.1文生图像编辑一体化，文生图反推提示词图生图方案_2105789328726257666.json, 图片生成/反推提示词/Qwen Image 2.1文生图像编辑一体化，文生图反推提示词图生图方案_2106409021661077505.json, 图片生成/反推提示词/Qwen Image 2.1文生图像编辑一体化，文生图反推提示词图生图方案_2106890611747020802.json, 图片生成/文生图/Qwen Image 2.1文生图图像编辑V2 GH加速版，媲美全能图片G2.5方案_2105800342549127170.json, 图片生成/文生图/Qwen Image 2.1文生多图像编辑一体化工作流，文生图图生图处理方案_2106487983930175490.json, 图片生成/文生图/QwenImage 2.1 V2 GH加速版｜文生图图像编辑 媲美全能图片G2.5_2105562013975011330.json, 图片生成/文生图/千问2.1文生图加图像编辑孤海加速版，媲美全能图片G2.5方案_2105709104563048449.json, 图片生成/文生图/文生图图像编辑一体化｜Qwen Image 2.1 一套工作流全搞定_2105558671576100866.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_81

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/反推提示词/Qwen Image 2.1文生图像编辑一体化 二合一工作流_2105396924613488642.json、图片生成/反推提示词/Qwen Image 2.1文生图像编辑一体化工作流，自动扩写提示词多场景覆盖_2106471030431772674.json、图片生成/反推提示词/Qwen Image 2.1文生图像编辑一体化，文生图反推提示词图生图方案_2105789328726257666.json、图片生成/反推提示词/Qwen Image 2.1文生图像编辑一体化，文生图反推提示词图生图方案_2106409021661077505.json、图片生成/反推提示词/Qwen Image 2.1文生图像编辑一体化，文生图反推提示词图生图方案_2106890611747020802.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：74%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `DF_Text_Box`
- `EmptyLatentImage`
- `GetNode`
- `GoohaiRatioAndResolution`
- `GoohaiRouteBlocker`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `QwenImage21BlockCacheT8`
- `QwenImage21SageAttentionT8`
- `QwenImage21SpectrumT8`
- `QwenImagePromptOptimizer`
- `RestoreQwenImage21GH`
- `SaveImage`
- `SetNode`
- `ShowText|pysssss`
- `TextEncodeQwenImage21GH`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 9/10 个有
- `LoadImageGoohai` —— 5/10 个有
- `CS_Preview_Any` —— 3/10 个有
- `Fast Groups Bypasser (rgthree)` —— 3/10 个有
- `FastGroupsBypassSwitch` —— 3/10 个有
- `ImageScaleToTotalPixels` —— 3/10 个有
- `JWFloat` —— 3/10 个有
- `KSamplerAdvanced` —— 3/10 个有
- `LatentSwitch` —— 3/10 个有
- `PDIMAGE_LongerSize` —— 3/10 个有
- `PreviewImage` —— 3/10 个有
- `ReferenceLatent` —— 3/10 个有
- `VAEEncode` —— 3/10 个有
- `easy showAnything` —— 3/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 10 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 10 | 100% |
| 采样算法 | er_sde | - | 10 | 100% |
| 调度器 | beta | - | 10 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |
| 宽度 | 80 | 80 - 80 | 10 | 100% |
| 高度 | 80 | 80 - 80 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，10 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，10 个样本，一致性 100%
- 调度器 最常用 beta，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，10 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，10 个样本，取值集中（一致性 100%）
- 高发问题（11/10 个样本）：Steps较低可能导致细节不足
