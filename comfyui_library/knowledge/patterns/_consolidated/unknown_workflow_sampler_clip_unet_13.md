---
name: unknown_workflow_sampler_clip_unet_13
type: Unknown Workflow
frequency: 19
level: weak
coverage: 0.9
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen Image 3.0提示词增强生图工作流｜两段式闭环_2103056782804480002.json, 图片生成/文生图/Qwen Image 3.0文生图工作流｜阿里旗舰图像模型_2103055683909410817.json, 图片生成/文生图/Qwen黑丝长腿丝袜美腿_2019644098361171969.json, 图片生成/文生图/Z-ImageBase-MeanCache加速-文生图_2019218139791237121.json, 图片生成/文生图/Z-image Base Distilled蒸馏加速版_2019063606171668481.json, 图片生成/文生图/Z-image Base Meancache加速版V1_2019064610539704322.json, 图片生成/文生图/Z-image Base Meancache加速版（好用质量高）_2019220127853580289.json, 图片生成/文生图/image_qwen_Image_2512 BF16_2073295897374584833.json, 图片生成/文生图/qwen2512文生图工作流_2068284987354476546.json, 图片生成/文生图/qwen_image工作流_1991713723383640065.json, 图片生成/文生图/qwen高级风格场景_2106951966848016385.json, 图片生成/文生图/z-image base 水墨风 文生图 工作流_2019406284654645249.json, 图片生成/文生图/【老金驿站】Z-image高清细节DejpegV2_1997835100480016386.json, 图片生成/文生图/【老金驿站】z-image8步文生图工作流_1994293848790728706.json, 图片生成/文生图/全能图片G-Image-2.5文生图工作流_2098372445806878721.json, 图片生成/文生图/墨宝映画人物设定_2015364874955657217.json, 图片生成/文生图/文生图 硕阳_2016782171092029441.json, 图片生成/文生图/（贞贞版4图版）Qwen 2512 Kook千问美人+真实幻想+极致真实文生图V1_2008746844083462145.json, 图片生成/文生图/（贞贞版）Qwen Image 2512 Kook写实人像文生图V1_2007898049535807489.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_13

> 由 `engine/knowledge_consolidation` 从 19 个 workflow 归纳得出（图片生成/文生图/Qwen Image 3.0提示词增强生图工作流｜两段式闭环_2103056782804480002.json、图片生成/文生图/Qwen Image 3.0文生图工作流｜阿里旗舰图像模型_2103055683909410817.json、图片生成/文生图/Qwen黑丝长腿丝袜美腿_2019644098361171969.json、图片生成/文生图/Z-ImageBase-MeanCache加速-文生图_2019218139791237121.json、图片生成/文生图/Z-image Base Distilled蒸馏加速版_2019063606171668481.json…）

- **类型**：Unknown Workflow
- **样本数**：19
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 19 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ModelSamplingAuraFlow` —— 15/19 个有
- `LoraLoaderModelOnly` —— 12/19 个有
- `CR Prompt Text` —— 7/19 个有
- `PrimitiveStringMultiline` —— 4/19 个有
- `MeanCache_ZImage` —— 3/19 个有
- `TextEncodeQwenImageEditPlus` —— 3/19 个有
- `RH_QwenImagePromptEnhancer` —— 1/19 个有
- `UnetLoaderGGUF` —— 1/19 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 4 - 50 | 19 | 29% |
| Prompt 约束强度(CFG) | 2.5 | 1 - 6 | 19 | 40% |
| 采样算法 | euler | - | 19 | 68% |
| 调度器 | simple | - | 19 | 89% |
| 重绘幅度 | 1 | 1 - 1 | 19 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/19 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 4 - 50，19 个样本，取值分散，一致性仅 29%
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 1 - 6，19 个样本，取值分散，一致性仅 40%
- 采样算法 最常用 euler，19 个样本，一致性 68%
- 调度器 最常用 simple，19 个样本，一致性 89%
- 重绘幅度 中位数 1，观测区间 1 - 1，19 个样本，取值集中（一致性 100%）
- 高发问题（10/19 个样本）：Steps较低可能导致细节不足
