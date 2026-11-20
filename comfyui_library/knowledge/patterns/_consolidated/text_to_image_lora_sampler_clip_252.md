---
name: text_to_image_lora_sampler_clip_252
type: Text To Image
frequency: 8
level: strong
coverage: 0.714
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, ResolutionSelector, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Image 2.1图像编辑图生图处理生成工具_2102557478423715841.json, 图片生成/图生图/Qwen Image 2.1图像编辑最多十张参考图，2K原生输出图生图处理工具_2106447204092309505.json, 图片生成/图生图/Qwen Image 2.1图片编辑，简洁实用的图生图处理工作流_2103255755200749569.json, 图片生成/图生图/Qwen Image 2.1图生图提示词增强处理生成工具_2102560585291493377.json, 图片生成/图生图/Qwen Image 2.1多合一工作流图生图文生图处理工具_2102465754015821825.json, 图片生成/图生图/千问2.1多图像编辑工作流｜提示词自动优化省心出图_2103724810600804354.json, 图片生成/文生图/Qwen Image 2.1多合一工作流 全能图像编辑方案_2109008831576625154.json, 图片生成/文生图/Qwen image 2.1图像编辑加文生图 二合一工作流_2105110276558381057.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_252

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/Qwen Image 2.1图像编辑图生图处理生成工具_2102557478423715841.json、图片生成/图生图/Qwen Image 2.1图像编辑最多十张参考图，2K原生输出图生图处理工具_2106447204092309505.json、图片生成/图生图/Qwen Image 2.1图片编辑，简洁实用的图生图处理工作流_2103255755200749569.json、图片生成/图生图/Qwen Image 2.1图生图提示词增强处理生成工具_2102560585291493377.json、图片生成/图生图/Qwen Image 2.1多合一工作流图生图文生图处理工具_2102465754015821825.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：71%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
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
- `QwenImage21Cache` —— 7/8 个有
- `easy showAnything` —— 7/8 个有
- `BatchImagesNode` —— 6/8 个有
- `Fast Groups Bypasser (rgthree)` —— 6/8 个有
- `GetNode` —— 6/8 个有
- `SetNode` —— 6/8 个有
- `TextGenerateLTX2Prompt` —— 6/8 个有
- `PrimitiveStringMultiline` —— 5/8 个有
- `ComfySwitchNode` —— 4/8 个有
- `Image Comparer (rgthree)` —— 3/8 个有
- `ConditioningZeroOut` —— 2/8 个有
- `CropWithPadInfo_EditUtils` —— 2/8 个有
- `EditTextEncode_EditUtils` —— 2/8 个有
- `FastGroupsBypassSwitch` —— 2/8 个有
- `PreviewImage` —— 2/8 个有
- `PrimitiveBoolean` —— 2/8 个有
- `PrimitiveInt` —— 2/8 个有
- `QwenImage21ConfigPreparer_EditUtils` —— 2/8 个有
- `QwenImage21ModelConfig_EditUtils` —— 2/8 个有
- `QwenPERewriteT8` —— 2/8 个有
- `SaveImageAdvanced` —— 2/8 个有
- `GH_ImageVideoComparer` —— 1/8 个有
- `ImageScaleToTotalPixels` —— 1/8 个有
- `Seed (rgthree)` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 8 | 100% |
| 高度 | 80 | 80 - 80 | 8 | 100% |
| 采样步数 | 4 | 4 - 4 | 8 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 8 | 100% |
| 采样算法 | er_sde | - | 8 | 100% |
| 调度器 | beta | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，8 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，8 个样本，一致性 100%
- 调度器 最常用 beta，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 高发问题（8/8 个样本）：Steps较低可能导致细节不足
