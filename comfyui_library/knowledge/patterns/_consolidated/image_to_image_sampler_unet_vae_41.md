---
name: image_to_image_sampler_unet_vae_41
type: Image To Image
frequency: 6
level: strong
coverage: 0.786667
common_nodes: [CFGNorm, CLIPLoader, ImageScaleToTotalPixels, KSampler, LoadImage, ModelSamplingAuraFlow, SaveImage, Text, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen-edit 胸部增强 丰胸神器 1.0_1994406310353510401.json, 图片生成/图生图/qwen-edit胸部增强模型-丰胸自动流程_1984437814957850626.json, 图片生成/图生图/丰胸神器_2040754896382726145.json, 图片生成/图生图/局部编辑+🐻变大+自定义强度+全节点注释_2057684290074398722.json, 图片生成/图生图/胸部增强_2085270174135046146.json, 图片生成/图生图/胸部增强，一键运行，即刻变美！_2005667509246324737.json]
source: knowledge_consolidation
---

# image_to_image_sampler_unet_vae_41

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Qwen-edit 胸部增强 丰胸神器 1.0_1994406310353510401.json、图片生成/图生图/qwen-edit胸部增强模型-丰胸自动流程_1984437814957850626.json、图片生成/图生图/丰胸神器_2040754896382726145.json、图片生成/图生图/局部编辑+🐻变大+自定义强度+全节点注释_2057684290074398722.json、图片生成/图生图/胸部增强_2085270174135046146.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：79%

## 共有节点

全部 6 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `Text`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `Int` —— 5/6 个有
- `LoraLoaderModelOnly` —— 5/6 个有
- `PrimitiveFloat` —— 5/6 个有
- `SeedVR2` —— 5/6 个有
- `SeedVR2BlockSwap` —— 5/6 个有
- `Image Comparer (rgthree)` —— 4/6 个有
- `PreviewImage` —— 3/6 个有
- `RHHiddenNodes` —— 2/6 个有
- `ColorMatchPro` —— 1/6 个有
- `ConditioningZeroOut` —— 1/6 个有
- `GetNode` —— 1/6 个有
- `SetNode` —— 1/6 个有
- `TT_img_enc_v2` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 1 - 4 | 6 | 68% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 1 - 4，6 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（6/6 个样本）：Steps较低可能导致细节不足
