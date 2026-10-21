---
name: text_to_image_lora_sampler_clip_71
type: Text To Image
frequency: 12
level: strong
coverage: 0.75125
common_nodes: [CLIPLoader, CLIPTextEncode, DF_Text_Box, EmptyLatentImage, GoohaiRatioAndResolution, GoohaiRouteBlocker, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, QwenImage21BlockCacheT8, QwenImage21SageAttentionT8, QwenImage21SpectrumT8, QwenImagePromptOptimizer, RestoreQwenImage21GH, SaveImage, ShowText|pysssss, TextEncodeQwenImage21GH, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/反推提示词/Qwen Image 2.1文生图像编辑一体化 二合一工作流_2105396924613488642.json, 图片生成/反推提示词/Qwen Image 2.1文生图像编辑一体化工作流，自动扩写提示词多场景覆盖_2106471030431772674.json, 图片生成/反推提示词/Qwen Image 2.1文生图像编辑一体化，文生图反推提示词图生图方案_2105789328726257666.json, 图片生成/反推提示词/Qwen Image 2.1文生图像编辑一体化，文生图反推提示词图生图方案_2106409021661077505.json, 图片生成/反推提示词/Qwen Image 2.1文生图像编辑一体化，文生图反推提示词图生图方案_2106890611747020802.json, 图片生成/文生图/Qwen Image 2.1文生图像编辑一体化工作台，文生图图生图处理方案_2107961997731131393.json, 图片生成/文生图/Qwen Image 2.1文生图图像编辑V2 GH加速版，媲美全能图片G2.5方案_2105800342549127170.json, 图片生成/文生图/Qwen Image 2.1文生多图像编辑一体化工作流，文生图图生图处理方案_2106487983930175490.json, 图片生成/文生图/Qwen-Image 2.1多图参考生图编辑｜智能提示词工作流_2108439442263461890.json, 图片生成/文生图/QwenImage 2.1 V2 GH加速版｜文生图图像编辑 媲美全能图片G2.5_2105562013975011330.json, 图片生成/文生图/千问2.1文生图加图像编辑孤海加速版，媲美全能图片G2.5方案_2105709104563048449.json, 图片生成/文生图/文生图图像编辑一体化｜Qwen Image 2.1 一套工作流全搞定_2105558671576100866.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_71

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/反推提示词/Qwen Image 2.1文生图像编辑一体化 二合一工作流_2105396924613488642.json、图片生成/反推提示词/Qwen Image 2.1文生图像编辑一体化工作流，自动扩写提示词多场景覆盖_2106471030431772674.json、图片生成/反推提示词/Qwen Image 2.1文生图像编辑一体化，文生图反推提示词图生图方案_2105789328726257666.json、图片生成/反推提示词/Qwen Image 2.1文生图像编辑一体化，文生图反推提示词图生图方案_2106409021661077505.json、图片生成/反推提示词/Qwen Image 2.1文生图像编辑一体化，文生图反推提示词图生图方案_2106890611747020802.json…）

- **类型**：Text To Image
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：75%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `DF_Text_Box`
- `EmptyLatentImage`
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
- `ShowText|pysssss`
- `TextEncodeQwenImage21GH`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 11/12 个有
- `Image Comparer (rgthree)` —— 11/12 个有
- `SetNode` —— 11/12 个有
- `LoadImageGoohai` —— 7/12 个有
- `CS_Preview_Any` —— 3/12 个有
- `Fast Groups Bypasser (rgthree)` —— 3/12 个有
- `FastGroupsBypassSwitch` —— 3/12 个有
- `ImageScaleToTotalPixels` —— 3/12 个有
- `JWFloat` —— 3/12 个有
- `KSamplerAdvanced` —— 3/12 个有
- `LatentSwitch` —— 3/12 个有
- `PDIMAGE_LongerSize` —— 3/12 个有
- `PreviewImage` —— 3/12 个有
- `ReferenceLatent` —— 3/12 个有
- `VAEEncode` —— 3/12 个有
- `easy showAnything` —— 3/12 个有
- `ComfySwitchNode` —— 1/12 个有
- `PrimitiveBoolean` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 12 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 12 | 100% |
| 采样算法 | er_sde | - | 12 | 100% |
| 调度器 | beta | - | 12 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |
| 宽度 | 80 | 80 - 80 | 12 | 100% |
| 高度 | 80 | 80 - 80 | 12 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 13/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，12 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，12 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，12 个样本，一致性 100%
- 调度器 最常用 beta，12 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，12 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，12 个样本，取值集中（一致性 100%）
- 高发问题（13/12 个样本）：Steps较低可能导致细节不足
