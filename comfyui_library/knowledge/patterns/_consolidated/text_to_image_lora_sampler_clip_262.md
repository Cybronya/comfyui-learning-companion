---
name: text_to_image_lora_sampler_clip_262
type: Text To Image
frequency: 8
level: strong
coverage: 0.844375
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, ResolutionSelector, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen Image 2.1 PE文生图提示词优化加速版 高质量画面直出_2109372180118200321.json, 图片生成/文生图/Qwen Image 2.1-PE 加速文生图｜提示词优化一键增强_2112477823029047298.json, 图片生成/文生图/Qwen Image 2.1-PE 提示词优化版｜文生图智能扩写_2112472087343489026.json, 图片生成/文生图/Qwen Image 2.1-PE 文生图加速版｜提示词优化出好图_2112468933998632962.json, 图片生成/文生图/Qwen Image 2.1一体化文生图工作流，7B模型2K高清RGBA透明直出方案_2103624543020601346.json, 图片生成/文生图/Qwen Image 2.1全能文生图处理生成工具_2102476988983365633.json, 图片生成/文生图/Qwen Image 2.1文生图对比流｜不同提示词效果并排出图_2108037643018788866.json, 图片生成/文生图/Qwen Image 2.1文生图工作流，文生图高质量文本到图像生成方案_2108446649474437121.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_262

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/Qwen Image 2.1 PE文生图提示词优化加速版 高质量画面直出_2109372180118200321.json、图片生成/文生图/Qwen Image 2.1-PE 加速文生图｜提示词优化一键增强_2112477823029047298.json、图片生成/文生图/Qwen Image 2.1-PE 提示词优化版｜文生图智能扩写_2112472087343489026.json、图片生成/文生图/Qwen Image 2.1-PE 文生图加速版｜提示词优化出好图_2112468933998632962.json、图片生成/文生图/Qwen Image 2.1一体化文生图工作流，7B模型2K高清RGBA透明直出方案_2103624543020601346.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 8 个 workflow 都包含：
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
- `ComfySwitchNode` —— 7/8 个有
- `SaveImageAdvanced` —— 7/8 个有
- `PrimitiveStringMultiline` —— 6/8 个有
- `PreviewImage` —— 5/8 个有
- `PrimitiveBoolean` —— 5/8 个有
- `QwenImage21_T2IPromptRewrite` —— 4/8 个有
- `RH_QwenImagePromptEnhancer` —— 4/8 个有
- `easy showAnything` —— 4/8 个有
- `JsonExtractString` —— 3/8 个有
- `RegexExtract` —— 3/8 个有
- `StringCompare` —— 3/8 个有
- `TextGenerate` —— 3/8 个有
- `PreviewAny` —— 2/8 个有
- `Text` —— 2/8 个有
- `RegexMatch` —— 1/8 个有
- `StringConcatenate` —— 1/8 个有

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
| Steps较低可能导致细节不足 | 12/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，8 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，8 个样本，一致性 100%
- 调度器 最常用 beta，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 高发问题（12/8 个样本）：Steps较低可能导致细节不足
