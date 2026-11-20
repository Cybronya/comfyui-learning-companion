---
name: text_to_image_lora_sampler_clip_122
type: Text To Image
frequency: 12
level: strong
coverage: 0.838417
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, ResolutionSelector, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/反推提示词/Qwen Image 2.1全能图像二合一加提示增强，文生图多图编辑自由切换_2103219635977015297.json, 图片生成/反推提示词/Qwen Image 2.1参考生图标准版 参考图输入高质量出图_2105030116769353730.json, 图片生成/图生图/AI换装双图试穿工作流｜Qwen-Image_2.1智能提示词｜服装上身效果图秒出_2112076955049873410.json, 图片生成/图生图/Face+Swap++Qwen-Image-2.1｜模特换头换脸 图生图电商救星_2105546422262263810.json, 图片生成/图生图/Qwen Image 2.1 V2编辑版，图生图处理优化升级方案_2103241696493531137.json, 图片生成/图生图/Qwen Image 2.1全能图片编辑加官方提示词强化，图生图处理质量提升_2103266944416833538.json, 图片生成/图生图/Qwen Image 2.1全能图片编辑官方提示词强化处理工具_2102552758141411330.json, 图片生成/图生图/Qwen+image+2.1图片编辑｜图生图局部修改轻松改细节_2104555432860807170.json, 图片生成/图生图/Qwen-Image2.1全能图片编辑｜官方提示词强化改图更听话_2112932549029879810.json, 图片生成/文生图/Qwen Image 2.1全能文生图官方提示词强化处理工具_2102565199348850689.json, 图片生成/文生图/Qwen Image2.1全能文生图 官方提示词强化场景人物生成工具_2113032764122558466.json, 图片生成/文生图/Qwen-Image2.1全能文生图｜官方提示词强化场景人物通吃_2112904831517159425.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_122

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/反推提示词/Qwen Image 2.1全能图像二合一加提示增强，文生图多图编辑自由切换_2103219635977015297.json、图片生成/反推提示词/Qwen Image 2.1参考生图标准版 参考图输入高质量出图_2105030116769353730.json、图片生成/图生图/AI换装双图试穿工作流｜Qwen-Image_2.1智能提示词｜服装上身效果图秒出_2112076955049873410.json、图片生成/图生图/Face+Swap++Qwen-Image-2.1｜模特换头换脸 图生图电商救星_2105546422262263810.json、图片生成/图生图/Qwen Image 2.1 V2编辑版，图生图处理优化升级方案_2103241696493531137.json…）

- **类型**：Text To Image
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `ResolutionSelector`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `ComfySwitchNode` —— 11/12 个有
- `PrimitiveStringMultiline` —— 11/12 个有
- `TextGenerate` —— 11/12 个有
- `LoadImage` —— 9/12 个有
- `QwenImage21Cache` —— 9/12 个有
- `Fast Groups Bypasser (rgthree)` —— 8/12 个有
- `Image Comparer (rgthree)` —— 8/12 个有
- `ImageScaleToTotalPixels` —— 8/12 个有
- `RegexExtract` —— 8/12 个有
- `BatchImagesNode` —— 7/12 个有
- `PrimitiveBoolean` —— 6/12 个有
- `SeedVR2LoadDiTModel` —— 6/12 个有
- `SeedVR2LoadVAEModel` —— 6/12 个有
- `SeedVR2VideoUpscaler` —— 6/12 个有
- `ShowAnything|Mie` —— 6/12 个有
- `StringFormat` —— 6/12 个有
- `PreviewAny` —— 4/12 个有
- `SaveImageAdvanced` —— 3/12 个有
- `StringConcatenate` —— 3/12 个有
- `PrimitiveInt` —— 2/12 个有
- `CR Text` —— 1/12 个有
- `SeedNode` —— 1/12 个有
- `TextGenerateLTX2Prompt` —— 1/12 个有
- `Textbox` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 12 | 100% |
| 高度 | 80 | 80 - 80 | 12 | 100% |
| 采样步数 | 4 | 4 - 4 | 12 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 12 | 100% |
| 采样算法 | er_sde | - | 12 | 100% |
| 调度器 | beta | - | 12 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 13/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，12 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，12 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，12 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，12 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，12 个样本，一致性 100%
- 调度器 最常用 beta，12 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 高发问题（13/12 个样本）：Steps较低可能导致细节不足
