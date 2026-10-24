---
name: image_to_image_sampler_unet_vae_15
type: Image To Image
frequency: 11
level: moderate
coverage: 0.975636
common_nodes: [CLIPLoader, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/qwen_image图生图支持中文_1953775268991303681.json, 图片生成/图生图/qwen千问图片编辑神器发布v1.0_1957726030365818881.json, 图片生成/图生图/qwen编辑图片_1958176395472080898.json, 图片生成/图生图/一键生成丰富表情包_1972210558072254466.json, 图片生成/图生图/一键生成表情包_1972131190742380546.json, 图片生成/图生图/动漫转真人 _ Workflow for Qwen-Edit_1958005330036797442.json, 图片生成/图生图/卡通动漫一致性 动作修改｜人物保持_1959186353315590146.json, 图片生成/图生图/最新 Qwen-edit 一键服装模特试穿_1958042179543478274.json, 图片生成/图生图/真人转动漫风格 _ Workflow for Qwen_1958700602907848706.json, 图片生成/图生图/鲜明亮丽的插画风格_1970083139890651138.json, 图片生成/图生图/（志佬开源）QwenEdit一致性图像编辑V2_1968246710134812674.json]
source: knowledge_consolidation
---

# image_to_image_sampler_unet_vae_15

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/qwen_image图生图支持中文_1953775268991303681.json、图片生成/图生图/qwen千问图片编辑神器发布v1.0_1957726030365818881.json、图片生成/图生图/qwen编辑图片_1958176395472080898.json、图片生成/图生图/一键生成丰富表情包_1972210558072254466.json、图片生成/图生图/一键生成表情包_1972131190742380546.json…）

- **类型**：Image To Image
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：98%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPTextEncode` —— 10/11 个有
- `TextEncodeQwenImageEdit` —— 10/11 个有
- `FluxKontextImageScale` —— 9/11 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 9/11 个有
- `CR Prompt Text` —— 8/11 个有
- `easy imageConcat` —— 7/11 个有
- `ConditioningZeroOut` —— 2/11 个有
- `LoraLoaderModelOnly` —— 2/11 个有
- `ModelSamplingAuraFlow` —— 2/11 个有
- `PreviewImage` —— 2/11 个有
- `Image Comparer (rgthree)` —— 1/11 个有
- `ImageConcanate` —— 1/11 个有
- `RH_LLMAPI_NODE` —— 1/11 个有
- `ShowText|pysssss` —— 1/11 个有
- `TextEncodeQwenImageEdit_lrzjason` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 30 | 11 | 76% |
| Prompt 约束强度(CFG) | 2.5 | 1 - 4 | 11 | 73% |
| 采样算法 | euler | - | 11 | 100% |
| 调度器 | normal | - | 11 | 82% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 30，11 个样本
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 1 - 4，11 个样本
- 采样算法 最常用 euler，11 个样本，一致性 100%
- 调度器 最常用 normal，11 个样本，一致性 82%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
