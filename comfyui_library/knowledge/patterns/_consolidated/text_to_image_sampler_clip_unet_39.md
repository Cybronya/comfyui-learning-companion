---
name: text_to_image_sampler_clip_unet_39
type: Text To Image
frequency: 13
level: weak
coverage: 0.859
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/MOSS image 最强开源文生图｜开源生图的黑马_2112029308096176130.json, 图片生成/文生图/MOSS image 最强开源文生图｜电商海报文字清晰_2112488209677635586.json, 图片生成/文生图/Moss-image SFT 文生图稳定版｜SFT调优出图更稳_2112416033981161473.json, 图片生成/文生图/Moss-image SFT文生图_2112104895800242178.json, 图片生成/文生图/Moss文生图+8步加速_2112030480005689345.json, 图片生成/文生图/Qwen Image 2.1 PE文生图提示词优化加速版 高质量画面直出_2109372180118200321.json, 图片生成/文生图/Qwen Image 2.1 V2文生图，文本到图像生成升级版本工作流_2103243206614937601.json, 图片生成/文生图/Qwen Image 2.1-PE 加速文生图｜提示词优化一键增强_2112477823029047298.json, 图片生成/文生图/Qwen Image 2.1-PE 提示词优化版｜文生图智能扩写_2112472087343489026.json, 图片生成/文生图/Qwen Image 2.1-PE 文生图加速版｜提示词优化出好图_2112468933998632962.json, 图片生成/文生图/Qwen Image 2.1全能文生图处理生成工具_2102476988983365633.json, 图片生成/文生图/Qwen Image 2.1文生图对比流｜不同提示词效果并排出图_2108037643018788866.json, 图片生成/文生图/Qwen Image 2.1文生图工作流，文生图高质量文本到图像生成方案_2108446649474437121.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_39

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/文生图/MOSS image 最强开源文生图｜开源生图的黑马_2112029308096176130.json、图片生成/文生图/MOSS image 最强开源文生图｜电商海报文字清晰_2112488209677635586.json、图片生成/文生图/Moss-image SFT 文生图稳定版｜SFT调优出图更稳_2112416033981161473.json、图片生成/文生图/Moss-image SFT文生图_2112104895800242178.json、图片生成/文生图/Moss文生图+8步加速_2112030480005689345.json…）

- **类型**：Text To Image
- **样本数**：13
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：86%

## 共有节点

全部 13 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 12/13 个有
- `JjkText` —— 11/13 个有
- `ResolutionSelector` —— 11/13 个有
- `solarL_SaveImagesToZip` —— 10/13 个有
- `孤海注释` —— 10/13 个有
- `SaveImageAdvanced` —— 8/13 个有
- `TextEncodeQwenImage21` —— 8/13 个有
- `ComfySwitchNode` —— 7/13 个有
- `PreviewImage` —— 7/13 个有
- `PrimitiveStringMultiline` —— 7/13 个有
- `TextGenerate` —— 7/13 个有
- `PrimitiveBoolean` —— 5/13 个有
- `QwenImage21_T2IPromptRewrite` —— 4/13 个有
- `RH_QwenImagePromptEnhancer` —— 4/13 个有
- `RegexExtract` —— 4/13 个有
- `easy showAnything` —— 4/13 个有
- `JsonExtractString` —— 3/13 个有
- `PreviewAny` —— 3/13 个有
- `SkipLayerGuidanceDiTSimple` —— 3/13 个有
- `StringCompare` —— 3/13 个有
- `MuyeTextEditOutput` —— 2/13 个有
- `StringConcatenate` —— 2/13 个有
- `Text` —— 2/13 个有
- `RegexMatch` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 50 | 13 | 0% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 4.5 | 13 | 67% |
| 采样算法 | er_sde | - | 13 | 92% |
| 调度器 | beta | - | 13 | 77% |
| 重绘幅度 | 1 | 1 - 1 | 13 | 100% |
| 宽度 | 80 | 80 - 1200 | 13 | 0% |
| 高度 | 80 | 80 - 1600 | 13 | 0% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 17/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 50，13 个样本，取值分散，一致性仅 0%
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 4.5，13 个样本
- 采样算法 最常用 er_sde，13 个样本，一致性 92%
- 调度器 最常用 beta，13 个样本，一致性 77%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 1200，13 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 1600，13 个样本，取值分散，一致性仅 0%
- 高发问题（17/13 个样本）：Steps较低可能导致细节不足
