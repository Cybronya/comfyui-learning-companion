---
name: text_to_image_controlnet_sampler_clip_3
type: Text To Image
frequency: 9
level: strong
coverage: 0.914222
common_nodes: [AIO_Preprocessor, CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, ModelPatchLoader, PreviewImage, QwenImageDiffsynthControlnet, SaveImage, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Red-Z-Image去网红感美女姿势复刻打造+高清2K_1998286200039440386.json, 图片生成/图生图/Z-Image-CN控制2.0（姿态）_1996924955315081217.json, 图片生成/图生图/Z-Image-CN控制2.0（条线）_2000907171892260866.json, 图片生成/图生图/Z-Image-CN控制2.0（深度）_2000906048024309762.json, 图片生成/图生图/Z-Image-CN控制工作流_1996205475135889410.json, 图片生成/图生图/Z-Image-CN控制洗图_2002171998161780737.json, 图片生成/图生图/Z-Image-CN控制（2.1）_2001999689794875393.json, 图片生成/图生图/Z-Image姿势控制+高清2K_1997959165559603201.json, 图片生成/图生图/Z-Image姿势控制2.0+高清放大2K_2000726955454590978.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_sampler_clip_3

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/Red-Z-Image去网红感美女姿势复刻打造+高清2K_1998286200039440386.json、图片生成/图生图/Z-Image-CN控制2.0（姿态）_1996924955315081217.json、图片生成/图生图/Z-Image-CN控制2.0（条线）_2000907171892260866.json、图片生成/图生图/Z-Image-CN控制2.0（深度）_2000906048024309762.json、图片生成/图生图/Z-Image-CN控制工作流_1996205475135889410.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 9 个 workflow 都包含：
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
- `UNETLoader` —— 8/9 个有
- `ConditioningZeroOut` —— 3/9 个有
- `LoraLoaderModelOnly` —— 3/9 个有
- `SeedVR2` —— 3/9 个有
- `SeedVR2BlockSwap` —— 3/9 个有
- `SeedVR2ExtraArgs` —— 3/9 个有
- `Text` —— 3/9 个有
- `AILab_QwenVL` —— 1/9 个有
- `CheckpointLoaderSimple` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 720 | 720 - 1080 | 9 | 80% |
| 高度 | 1280 | 1280 - 1920 | 9 | 80% |
| 采样步数 | 10 | 7 - 10 | 9 | 84% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | euler | - | 9 | 78% |
| 调度器 | simple | - | 9 | 89% |
| 重绘幅度 | 1 | 0.7 - 1 | 9 | 84% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 720，观测区间 720 - 1080，9 个样本
- 高度 中位数 1280，观测区间 1280 - 1920，9 个样本
- 采样步数 中位数 10，观测区间 7 - 10，9 个样本，取值集中（一致性 84%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，9 个样本，一致性 78%
- 调度器 最常用 simple，9 个样本，一致性 89%
- 重绘幅度 中位数 1，观测区间 0.7 - 1，9 个样本，取值集中（一致性 84%）
- 高发问题（7/9 个样本）：Steps较低可能导致细节不足
