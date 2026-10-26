---
name: text_to_image_lora_sampler_clip_20
type: Text To Image
frequency: 25
level: strong
coverage: 0.7994
common_nodes: [CLIPLoader, CLIPTextEncode, DF_Text_Box, EmptyLatentImage, GoohaiRatioAndResolution, GoohaiRouteBlocker, JjkText, KSampler, LoraLoaderModelOnly, QwenImage21BlockCacheT8, QwenImage21SageAttentionT8, QwenImage21SpectrumT8, QwenImagePromptOptimizer, RestoreQwenImage21GH, SaveImage, TextEncodeQwenImage21GH, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/反推提示词/Qwen Image 2.1文生图像编辑一体化 二合一工作流_2105396924613488642.json, 图片生成/反推提示词/Qwen Image 2.1文生图像编辑一体化工作流，自动扩写提示词多场景覆盖_2106471030431772674.json, 图片生成/反推提示词/Qwen Image 2.1文生图像编辑一体化，文生图反推提示词图生图方案_2105789328726257666.json, 图片生成/反推提示词/Qwen Image 2.1文生图像编辑一体化，文生图反推提示词图生图方案_2106409021661077505.json, 图片生成/反推提示词/Qwen Image 2.1文生图像编辑一体化，文生图反推提示词图生图方案_2106890611747020802.json, 图片生成/图生图/AI生图多图参考编辑｜Qwen-Image_2.1智能提示词版｜局部重绘改图全能_2112078603507814401.json, 图片生成/图生图/Qwen Image 2.1图像扩展工作流，图生图图像扩展处理工具_2108322972124672002.json, 图片生成/图生图/Qwen Image 2.1图像编辑多图编辑 高质量改图方案_2109787910236102658.json, 图片生成/图生图/Qwen Image 2.1多图编辑图像处理 一键精准改图高质量方案_2110341027134533634.json, 图片生成/图生图/Qwen Image 2.1多图编辑图像处理 一键精准改图高质量方案_2110350170553671681.json, 图片生成/图生图/Qwen Image 2.1文生与图像编辑一体化，图生图高效_2111530551059501058.json, 图片生成/图生图/Qwen Image 2.1文生与图像编辑一体化｜一个流搞定两类活_2111287562131304450.json, 图片生成/图生图/Qwen Image 2.1文生图单图编辑多图编辑图像编辑一体化，局部重绘工具_2105794011696033793.json, 图片生成/图生图/Qwen Image 2.1文生编辑一体化 局部重绘处理工具_2113752014848090113.json, 图片生成/图生图/Qwen-Image_2.1多图参考智能提示词，AI生图编辑一步到位_2112340219432357890.json, 图片生成/图生图/Qwen_Image_2.1文生图像编辑一体化，文生图反推提示词图生图方案_2109091158382174210.json, 图片生成/图生图/文生图加图像编辑一体化｜Qwen Image 2.1 单图多图编辑都拿手_2105537049335001089.json, 图片生成/文生图/AI生图编辑Qwen Image 2.1多图参考智能提示词 高质量出图_2108638666338955265.json, 图片生成/文生图/Qwen Image 2.1文生图像编辑一体化工作台，文生图图生图处理方案_2107961997731131393.json, 图片生成/文生图/Qwen Image 2.1文生图图像编辑一体，反推提示词智能出图_2112264989141721089.json, 图片生成/文生图/Qwen Image 2.1文生图编辑一体化｜抠图扩图局部重绘多图融合｜全自动扩写提示词_2112121620461608962.json, 图片生成/文生图/Qwen Image 2.1文生多图像编辑一体化工作流，文生图图生图处理方案_2106487983930175490.json, 图片生成/文生图/Qwen-Image 2.1多图参考生图编辑｜智能提示词工作流_2108439442263461890.json, 图片生成/文生图/Qwen-Image-2.1 加速简洁版，中文繁体招牌王_2111938255540285442.json, 图片生成/文生图/文生图图像编辑一体化｜Qwen Image 2.1 一套工作流全搞定_2105558671576100866.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_20

> 由 `engine/knowledge_consolidation` 从 25 个 workflow 归纳得出（图片生成/反推提示词/Qwen Image 2.1文生图像编辑一体化 二合一工作流_2105396924613488642.json、图片生成/反推提示词/Qwen Image 2.1文生图像编辑一体化工作流，自动扩写提示词多场景覆盖_2106471030431772674.json、图片生成/反推提示词/Qwen Image 2.1文生图像编辑一体化，文生图反推提示词图生图方案_2105789328726257666.json、图片生成/反推提示词/Qwen Image 2.1文生图像编辑一体化，文生图反推提示词图生图方案_2106409021661077505.json、图片生成/反推提示词/Qwen Image 2.1文生图像编辑一体化，文生图反推提示词图生图方案_2106890611747020802.json…）

- **类型**：Text To Image
- **样本数**：25
- **可信度**：强结论
- **平均知识覆盖**：80%

## 共有节点

全部 25 个 workflow 都包含：
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
- `TextEncodeQwenImage21GH`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 24/25 个有
- `LoadImage` —— 24/25 个有
- `孤海注释` —— 24/25 个有
- `LoadImageGoohai` —— 23/25 个有
- `ShowText|pysssss` —— 23/25 个有
- `GetNode` —— 21/25 个有
- `SetNode` —— 21/25 个有
- `ComfySwitchNode` —— 4/25 个有
- `PrimitiveBoolean` —— 4/25 个有
- `GoohaiAnyExists` —— 2/25 个有
- `GoohaiDisplayAny` —— 2/25 个有
- `easy ifElse` —— 2/25 个有
- `CM_FloatToInt` —— 1/25 个有
- `EmptyImage` —— 1/25 个有
- `PreviewImage` —— 1/25 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 25 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 25 | 100% |
| 采样算法 | er_sde | - | 25 | 100% |
| 调度器 | beta | - | 25 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 25 | 100% |
| 宽度 | 80 | 80 - 80 | 25 | 100% |
| 高度 | 80 | 80 - 80 | 25 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 29/25 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，25 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，25 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，25 个样本，一致性 100%
- 调度器 最常用 beta，25 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，25 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，25 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，25 个样本，取值集中（一致性 100%）
- 高发问题（29/25 个样本）：Steps较低可能导致细节不足
