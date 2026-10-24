---
name: image_to_image_lora_sampler_unet_11
type: Image To Image
frequency: 24
level: moderate
coverage: 0.981917
common_nodes: [CLIPLoader, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/qwen2511图转手绘线条水彩风格图片风格化_2078074989806444546.json, 图片生成/图生图/qwen2511图转手绘线条水彩风格图片风格化_2078077711209291777.json, 图片生成/图生图/qwen2511图转速手绘线条水彩风格_2026148427746254850.json, 图片生成/图生图/qwen2511图转速手绘线条水彩风格_2067415744551411714.json, 图片生成/图生图/qwen2511图转速手绘线条水彩风格_2067446975695511554.json, 图片生成/图生图/qwen2511图转速手绘线条水彩风格_2072947797464276994.json, 图片生成/图生图/qwen2511图转速手绘线条水彩风格_2075144823752978433.json, 图片生成/图生图/qwen2511图转速手绘线条水彩风格_2077588149060067330.json, 图片生成/图生图/qwen2511图转速手绘线条水彩风格_2077666313538990082.json, 图片生成/图生图/qwen2511图转速手绘线条水彩风格_2079102882938445826.json, 图片生成/图生图/qwen2511图转速手绘线条水彩风格_2095794944433811458.json, 图片生成/图生图/qwen2511图转速手绘线条水彩风格_2096151173555380225.json, 图片生成/图生图/qwen2511真人转手绘线条画风_2089264984500035585.json, 图片生成/图生图/qwen_image_edit_2511_2004461710926901250.json, 图片生成/图生图/【橘子AI】Qwen Image Edit Plus 单图+多图编辑_1971464154261471234.json, 图片生成/图生图/一句话提取衣服_1990645950131691522.json, 图片生成/文生图/三图参考生成组合_1993498915181969409.json, 视频生成/图生视频/一键佩戴饰品+生成讲解视频_1989475956505104385.json, 视频生成/图生视频/一键换图片背景+生成烧菜视频_1987684744014049282.json, 视频生成/图生视频/一键生成和小时候的自己对话_1987671585945489409.json, 视频生成/图生视频/三图参考生成两个人物对话视频_1987680109538816002.json, 视频生成/图生视频/指定人物对话_1987680874936381442.json, 视频生成/图生视频/生成人物视角转换视频_1987676437924745217.json, 视频生成/文生视频/一句话生成和小时候的自己对话_1987677418305556481.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_11

> 由 `engine/knowledge_consolidation` 从 24 个 workflow 归纳得出（图片生成/图生图/qwen2511图转手绘线条水彩风格图片风格化_2078074989806444546.json、图片生成/图生图/qwen2511图转手绘线条水彩风格图片风格化_2078077711209291777.json、图片生成/图生图/qwen2511图转速手绘线条水彩风格_2026148427746254850.json、图片生成/图生图/qwen2511图转速手绘线条水彩风格_2067415744551411714.json、图片生成/图生图/qwen2511图转速手绘线条水彩风格_2067446975695511554.json…）

- **类型**：Image To Image
- **样本数**：24
- **可信度**：中等可信
- **平均知识覆盖**：98%

## 共有节点

全部 24 个 workflow 都包含：
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `SaveImage` —— 21/24 个有
- `DifferentialDiffusion` —— 13/24 个有
- `ReferenceLatent` —— 13/24 个有
- `ResizeImagesByLongerEdge` —— 13/24 个有
- `CFGNorm` —— 11/24 个有
- `ImageScaleToTotalPixels` —— 11/24 个有
- `EmptySD3LatentImage` —— 10/24 个有
- `RH_Sora2_I2V` —— 8/24 个有
- `SaveVideo` —— 8/24 个有
- `PrimitiveStringMultiline` —— 5/24 个有
- `CR SDXL Aspect Ratio` —— 1/24 个有
- `ImageStitch` —— 1/24 个有
- `PathchSageAttentionKJ` —— 1/24 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 12 | 4 - 12 | 24 | 52% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 24 | 100% |
| 采样算法 | euler | - | 24 | 100% |
| 调度器 | beta | - | 24 | 54% |
| 重绘幅度 | 1 | 1 - 1 | 24 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/24 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 12，观测区间 4 - 12，24 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，24 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，24 个样本，一致性 100%
- 调度器 最常用 beta，24 个样本，一致性 54%
- 重绘幅度 中位数 1，观测区间 1 - 1，24 个样本，取值集中（一致性 100%）
