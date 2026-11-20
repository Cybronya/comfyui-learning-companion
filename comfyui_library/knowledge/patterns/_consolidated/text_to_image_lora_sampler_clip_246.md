---
name: text_to_image_lora_sampler_clip_246
type: Text To Image
frequency: 8
level: strong
coverage: 0.900375
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, Image Comparer (rgthree), JjkText, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Krea2局部重绘PS版工作流｜提示词反推写实图生图_2097491218342178818.json, 图片生成/图生图/LEON 产品精修｜图生图商品图一键出高级感 商详必备_2097581380665438210.json, 图片生成/图生图/LEON 无损放大｜细节恢复加肌理强化 图生图画质起飞_2097573526676000770.json, 图片生成/图生图/Qwen Image 2.1图像编辑最新版 透明抠图换背景工具_2113383323958595585.json, 图片生成/图生图/Qwen Image 2.1图片清晰度增强与细节修复V2 画质提升方案_2109180598479835138.json, 图片生成/图生图/Qwen Image 2.1图片清晰度增强与细节修复V2 画质提升方案_2109778326498926594.json, 图片生成/图生图/Qwen Image 2.1清晰度增强V2 细节修复画质提升_2110251910526754817.json, 图片生成/图生图/Qwen Image 2.1清晰度增强V2 细节修复画质提升_2110366228245204993.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_246

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/Krea2局部重绘PS版工作流｜提示词反推写实图生图_2097491218342178818.json、图片生成/图生图/LEON 产品精修｜图生图商品图一键出高级感 商详必备_2097581380665438210.json、图片生成/图生图/LEON 无损放大｜细节恢复加肌理强化 图生图画质起飞_2097573526676000770.json、图片生成/图生图/Qwen Image 2.1图像编辑最新版 透明抠图换背景工具_2113383323958595585.json、图片生成/图生图/Qwen Image 2.1图片清晰度增强与细节修复V2 画质提升方案_2109180598479835138.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `Image Comparer (rgthree)`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 5/8 个有
- `QwenImage21Cache` —— 5/8 个有
- `TextEncodeQwenImage21` —— 5/8 个有
- `SeedNode` —— 4/8 个有
- `SplitImageWithAlpha` —— 4/8 个有
- `RHHiddenNodes` —— 3/8 个有
- `ConditioningZeroOut` —— 1/8 个有
- `GoogleTranslator` —— 1/8 个有
- `Int` —— 1/8 个有
- `KSamplerAdvanced` —— 1/8 个有
- `TextInput_` —— 1/8 个有
- `VAEEncode` —— 1/8 个有
- `ttN int` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 8 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 8 | 100% |
| 采样算法 | er_sde | - | 8 | 100% |
| 调度器 | beta | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |
| 宽度 | 80 | 80 - 80 | 8 | 100% |
| 高度 | 80 | 80 - 80 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 13/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，8 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，8 个样本，一致性 100%
- 调度器 最常用 beta，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 高发问题（13/8 个样本）：Steps较低可能导致细节不足
