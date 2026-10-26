---
name: text_to_image_controlnet_sampler_clip_2
type: Text To Image
frequency: 12
level: moderate
coverage: 0.90775
common_nodes: [AIO_Preprocessor, CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, ModelPatchLoader, PreviewImage, QwenImageDiffsynthControlnet, SaveImage, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Red-Z-Image去网红感美女姿势复刻打造+高清2K_1998286200039440386.json, 图片生成/图生图/Z-Image-CN控制2.0（姿态）_1996924955315081217.json, 图片生成/图生图/Z-Image-CN控制2.0（条线）_2000907171892260866.json, 图片生成/图生图/Z-Image-CN控制2.0（深度）_2000906048024309762.json, 图片生成/图生图/Z-Image-CN控制工作流_1996205475135889410.json, 图片生成/图生图/Z-Image-CN控制洗图_2002171998161780737.json, 图片生成/图生图/Z-Image-CN控制（2.1）_2001999689794875393.json, 图片生成/图生图/Z-Image姿势控制+高清2K_1997959165559603201.json, 图片生成/图生图/Z-Image姿势控制2.0+高清放大2K_2000726955454590978.json, 数字人/数字人/Z-Image姿势控制+高清2K_2063590785538416642.json, 数字人/数字人/Z-Image姿势控制+高清2K_2063983202640945153.json, 数字人/数字人/Z-Image姿势控制+高清2K_2063997957313228801.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_sampler_clip_2

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/Red-Z-Image去网红感美女姿势复刻打造+高清2K_1998286200039440386.json、图片生成/图生图/Z-Image-CN控制2.0（姿态）_1996924955315081217.json、图片生成/图生图/Z-Image-CN控制2.0（条线）_2000907171892260866.json、图片生成/图生图/Z-Image-CN控制2.0（深度）_2000906048024309762.json、图片生成/图生图/Z-Image-CN控制工作流_1996205475135889410.json…）

- **类型**：Text To Image
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 12 个 workflow 都包含：
- `AIO_Preprocessor`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `ModelPatchLoader`
- `PreviewImage`
- `QwenImageDiffsynthControlnet`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `UNETLoader` —— 11/12 个有
- `ConditioningZeroOut` —— 6/12 个有
- `LoraLoaderModelOnly` —— 6/12 个有
- `SeedVR2` —— 6/12 个有
- `SeedVR2BlockSwap` —— 6/12 个有
- `SeedVR2ExtraArgs` —— 6/12 个有
- `Text` —— 6/12 个有
- `Qwen3_VQA` —— 2/12 个有
- `RH_RhartImageG2ImageToImage` —— 2/12 个有
- `AILab_QwenVL` —— 1/12 个有
- `CheckpointLoaderSimple` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 900 | 720 - 1080 | 12 | 80% |
| 高度 | 1600 | 1280 - 1920 | 12 | 80% |
| 采样步数 | 7.5 | 3 - 10 | 12 | 68% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 12 | 100% |
| 采样算法 | euler | - | 12 | 75% |
| 调度器 | simple | - | 12 | 92% |
| 重绘幅度 | 1 | 0.7 - 1 | 12 | 84% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 13/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 900，观测区间 720 - 1080，12 个样本，取值集中（一致性 80%）
- 高度 中位数 1600，观测区间 1280 - 1920，12 个样本，取值集中（一致性 80%）
- 采样步数 中位数 7.5，观测区间 3 - 10，12 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，12 个样本，一致性 75%
- 调度器 最常用 simple，12 个样本，一致性 92%
- 重绘幅度 中位数 1，观测区间 0.7 - 1，12 个样本，取值集中（一致性 84%）
- 高发问题（13/12 个样本）：Steps较低可能导致细节不足
