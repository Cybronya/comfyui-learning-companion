---
name: image_to_image_lora_sampler_unet_99
type: Image To Image
frequency: 7
level: moderate
coverage: 0.862286
common_nodes: [CFGNorm, CLIPLoader, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/生图-图生成正面白底图-qwen-Edit-2509-8步_2000610701750173697.json, 图片生成/图生图/电商产品多视角_1992474545672220673.json, 图片生成/图生图/电商场景增加模特单人_多人_2026915719539073026.json, 图片生成/图生图/白模转材质_1991804491599278082.json, 图片生成/图生图/神都猫的Qwenedit稳定器lora 基本使用工作流_1967962698203934722.json, 图片生成/图生图/神都猫的Qwenedit稳定器lora+填补图案空缺_1967985030410678274.json, 图片生成/图生图/神都猫的Qwenedit稳定器lora+电商产品换背景工作流_1967977222789279745.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_99

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/生图-图生成正面白底图-qwen-Edit-2509-8步_2000610701750173697.json、图片生成/图生图/电商产品多视角_1992474545672220673.json、图片生成/图生图/电商场景增加模特单人_多人_2026915719539073026.json、图片生成/图生图/白模转材质_1991804491599278082.json、图片生成/图生图/神都猫的Qwenedit稳定器lora 基本使用工作流_1967962698203934722.json…）

- **类型**：Image To Image
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 7 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageScaleToTotalPixels` —— 6/7 个有
- `PreviewImage` —— 5/7 个有
- `Image Comparer (rgthree)` —— 4/7 个有
- `ImageConcanate` —— 4/7 个有
- `TextEncodeQwenImageEditPlus` —— 4/7 个有
- `EmptySD3LatentImage` —— 3/7 个有
- `Get resolution [Crystools]` —— 3/7 个有
- `Text` —— 3/7 个有
- `TextEncodeQwenImageEdit` —— 3/7 个有
- `TextJoinMulti` —— 3/7 个有
- `easy imageSize` —— 2/7 个有
- `AILab_MiniCPM_4_V` —— 1/7 个有
- `Fast Groups Bypasser (rgthree)` —— 1/7 个有
- `GetImageSizeAndCount` —— 1/7 个有
- `PreviewAny` —— 1/7 个有
- `Switch any [Crystools]` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 8 - 20 | 7 | 63% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 7 | 57% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 8 - 20，7 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，7 个样本
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
