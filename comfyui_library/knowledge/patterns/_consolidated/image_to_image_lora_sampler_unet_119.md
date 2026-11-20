---
name: image_to_image_lora_sampler_unet_119
type: Image To Image
frequency: 7
level: strong
coverage: 0.956143
common_nodes: [CFGNorm, CLIPLoader, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/角色一致性_1916660896893177858.json, 图片生成/图生图/角色多视角生成_1987538986363195394.json, 图片生成/图生图/超好用🔥人物多角度出图-角度按需自调-超低价_2056578309579952129.json, 图片生成/图生图/转现实场景qwen_2001592460314853378.json, 图片生成/文生图/Qwen Image Edit 2511 基础图像编辑_2003694338204942337.json, 图片生成/文生图/Qwen-Edit-2509-多角度切换_1991129925849579521.json, 平台全量/Qwen-Image-Edit-2511 光影重构 婚纱影楼艺术照  美白肌肤 一键添加光效 造光_2008103440219639809.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_119

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/角色一致性_1916660896893177858.json、图片生成/图生图/角色多视角生成_1987538986363195394.json、图片生成/图生图/超好用🔥人物多角度出图-角度按需自调-超低价_2056578309579952129.json、图片生成/图生图/转现实场景qwen_2001592460314853378.json、图片生成/文生图/Qwen Image Edit 2511 基础图像编辑_2003694338204942337.json…）

- **类型**：Image To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：96%

## 共有节点

全部 7 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 4/7 个有
- `ImageScaleToTotalPixels` —— 3/7 个有
- `ConstrainImage|pysssss` —— 2/7 个有
- `Image Comparer (rgthree)` —— 2/7 个有
- `ReferenceLatent` —— 2/7 个有
- `Anything Everywhere` —— 1/7 个有
- `Anything Everywhere3` —— 1/7 个有
- `CLIPTextEncode` —— 1/7 个有
- `ImageResizeKJv2` —— 1/7 个有
- `Text` —— 1/7 个有
- `easy imageSize` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 7 | 65% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 57% |
| 调度器 | simple | - | 7 | 57% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 23/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，7 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 57%
- 调度器 最常用 simple，7 个样本，一致性 57%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（23/7 个样本）：Steps较低可能导致细节不足
