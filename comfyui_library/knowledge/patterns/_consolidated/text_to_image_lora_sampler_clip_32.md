---
name: text_to_image_lora_sampler_clip_32
type: Text To Image
frequency: 21
level: strong
coverage: 0.77319
common_nodes: [CLIPLoader, CLIPTextEncode, DF_Text_Box, EmptyLatentImage, GoohaiRatioAndResolution, GoohaiRouteBlocker, JjkText, KSampler, LoraLoaderModelOnly, QwenImage21BlockCacheT8, QwenImage21SageAttentionT8, QwenImage21SpectrumT8, QwenImagePromptOptimizer, RestoreQwenImage21GH, SaveImage, ShowText|pysssss, TextEncodeQwenImage21GH, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/反推提示词/Qwen Image 2.1文生图像编辑一体化 二合一工作流_2105396924613488642.json, 图片生成/反推提示词/Qwen Image 2.1文生图像编辑一体化工作流，自动扩写提示词多场景覆盖_2106471030431772674.json, 图片生成/反推提示词/Qwen Image 2.1文生图像编辑一体化，文生图反推提示词图生图方案_2105789328726257666.json, 图片生成/反推提示词/Qwen Image 2.1文生图像编辑一体化，文生图反推提示词图生图方案_2106409021661077505.json, 图片生成/反推提示词/Qwen Image 2.1文生图像编辑一体化，文生图反推提示词图生图方案_2106890611747020802.json, 图片生成/图生图/AI生图多图参考编辑｜Qwen-Image_2.1智能提示词版｜局部重绘改图全能_2112078603507814401.json, 图片生成/图生图/Qwen Image 2.1图像扩展工作流，图生图图像扩展处理工具_2108322972124672002.json, 图片生成/图生图/Qwen Image 2.1图像编辑多图编辑 高质量改图方案_2109787910236102658.json, 图片生成/图生图/Qwen Image 2.1多图编辑图像处理 一键精准改图高质量方案_2110341027134533634.json, 图片生成/图生图/Qwen Image 2.1多图编辑图像处理 一键精准改图高质量方案_2110350170553671681.json, 图片生成/图生图/Qwen Image 2.1文生与图像编辑一体化，图生图高效_2111530551059501058.json, 图片生成/图生图/Qwen Image 2.1文生与图像编辑一体化｜一个流搞定两类活_2111287562131304450.json, 图片生成/图生图/Qwen Image 2.1文生图单图编辑多图编辑图像编辑一体化，局部重绘工具_2105794011696033793.json, 图片生成/图生图/Qwen-Image_2.1多图参考智能提示词，AI生图编辑一步到位_2112340219432357890.json, 图片生成/图生图/Qwen_Image_2.1文生图像编辑一体化，文生图反推提示词图生图方案_2109091158382174210.json, 图片生成/图生图/文生图加图像编辑一体化｜Qwen Image 2.1 单图多图编辑都拿手_2105537049335001089.json, 图片生成/文生图/AI生图编辑Qwen Image 2.1多图参考智能提示词 高质量出图_2108638666338955265.json, 图片生成/文生图/Qwen Image 2.1文生图像编辑一体化工作台，文生图图生图处理方案_2107961997731131393.json, 图片生成/文生图/Qwen Image 2.1文生图图像编辑V2 GH加速版，媲美全能图片G2.5方案_2105800342549127170.json, 图片生成/文生图/QwenImage 2.1 V2 GH加速版｜文生图图像编辑 媲美全能图片G2.5_2105562013975011330.json, 图片生成/文生图/千问2.1文生图加图像编辑孤海加速版，媲美全能图片G2.5方案_2105709104563048449.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_32

> 由 `engine/knowledge_consolidation` 从 21 个 workflow 归纳得出（图片生成/反推提示词/Qwen Image 2.1文生图像编辑一体化 二合一工作流_2105396924613488642.json、图片生成/反推提示词/Qwen Image 2.1文生图像编辑一体化工作流，自动扩写提示词多场景覆盖_2106471030431772674.json、图片生成/反推提示词/Qwen Image 2.1文生图像编辑一体化，文生图反推提示词图生图方案_2105789328726257666.json、图片生成/反推提示词/Qwen Image 2.1文生图像编辑一体化，文生图反推提示词图生图方案_2106409021661077505.json、图片生成/反推提示词/Qwen Image 2.1文生图像编辑一体化，文生图反推提示词图生图方案_2106890611747020802.json…）

- **类型**：Text To Image
- **样本数**：21
- **可信度**：强结论
- **平均知识覆盖**：77%

## 共有节点

全部 21 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `DF_Text_Box`
- `EmptyLatentImage`
- `GoohaiRatioAndResolution`
- `GoohaiRouteBlocker`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `QwenImage21BlockCacheT8`
- `QwenImage21SageAttentionT8`
- `QwenImage21SpectrumT8`
- `QwenImagePromptOptimizer`
- `RestoreQwenImage21GH`
- `SaveImage`
- `ShowText|pysssss`
- `TextEncodeQwenImage21GH`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 20/21 个有
- `孤海注释` —— 20/21 个有
- `Image Comparer (rgthree)` —— 19/21 个有
- `GetNode` —— 18/21 个有
- `LoadImageGoohai` —— 18/21 个有
- `SetNode` —— 18/21 个有
- `PreviewImage` —— 4/21 个有
- `CS_Preview_Any` —— 3/21 个有
- `ComfySwitchNode` —— 3/21 个有
- `Fast Groups Bypasser (rgthree)` —— 3/21 个有
- `FastGroupsBypassSwitch` —— 3/21 个有
- `ImageScaleToTotalPixels` —— 3/21 个有
- `JWFloat` —— 3/21 个有
- `KSamplerAdvanced` —— 3/21 个有
- `LatentSwitch` —— 3/21 个有
- `PDIMAGE_LongerSize` —— 3/21 个有
- `PrimitiveBoolean` —— 3/21 个有
- `ReferenceLatent` —— 3/21 个有
- `VAEEncode` —— 3/21 个有
- `easy showAnything` —— 3/21 个有
- `CM_FloatToInt` —— 1/21 个有
- `EmptyImage` —— 1/21 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 21 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 21 | 100% |
| 采样算法 | er_sde | - | 21 | 100% |
| 调度器 | beta | - | 21 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 21 | 100% |
| 宽度 | 80 | 80 - 80 | 21 | 100% |
| 高度 | 80 | 80 - 80 | 21 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 25/21 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，21 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，21 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，21 个样本，一致性 100%
- 调度器 最常用 beta，21 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，21 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，21 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，21 个样本，取值集中（一致性 100%）
- 高发问题（25/21 个样本）：Steps较低可能导致细节不足
