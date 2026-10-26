---
name: image_to_image_lora_sampler_vae_8
type: Image To Image
frequency: 9
level: strong
coverage: 0.858111
common_nodes: [CFGNorm, ImageScaleToTotalPixels, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/2509-批量测试_2001951383052009474.json, 图片生成/图生图/Qwen-Edit-2511 风格迁移_2031922726943854593.json, 图片生成/图生图/Qwen-Edit-2511 风格迁移_2034195279104184321.json, 图片生成/图生图/Qwen-Edit-2511 风格迁移_2034202489414750209.json, 图片生成/图生图/Qwen-Edit-2511 风格迁移_2058000912211337217.json, 图片生成/图生图/Qwen-edit万能一键去水印_2077302903462785026.json, 图片生成/图生图/ywt低价版1.0_2059986818820567041.json, 图片生成/图生图/【电商版】2509-LORA万能背景增加人物流_1985936658019299330.json, 图片生成/图生图/千问Edit 2509版 单图编辑_1983858753294471169.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_vae_8

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/2509-批量测试_2001951383052009474.json、图片生成/图生图/Qwen-Edit-2511 风格迁移_2031922726943854593.json、图片生成/图生图/Qwen-Edit-2511 风格迁移_2034195279104184321.json、图片生成/图生图/Qwen-Edit-2511 风格迁移_2034202489414750209.json、图片生成/图生图/Qwen-Edit-2511 风格迁移_2058000912211337217.json…）

- **类型**：Image To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 9 个 workflow 都包含：
- `CFGNorm`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 8/9 个有
- `Image Comparer (rgthree)` —— 8/9 个有
- `PreviewImage` —— 8/9 个有
- `UNETLoader` —— 8/9 个有
- `LayerUtility: ImageReel` —— 7/9 个有
- `LayerUtility: ImageReelComposit` —— 7/9 个有
- `CR Seed` —— 5/9 个有
- `CR Text` —— 5/9 个有
- `FluxKontextMultiReferenceLatentMethod` —— 5/9 个有
- `ImageStitch` —— 4/9 个有
- `easy imageSize` —— 2/9 个有
- `LoadDiffusionModelShared //Inspire` —— 1/9 个有
- `LoadTextEncoderShared //Inspire` —— 1/9 个有
- `MuyeTextEditOutput` —— 1/9 个有
- `RH_LLMAPI_NODE` —— 1/9 个有
- `RH_Nano_Banana_Image2Image` —— 1/9 个有
- `TextEncodeQwenImageEdit` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 8 | 9 | 83% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | euler | - | 9 | 100% |
| 调度器 | simple | - | 9 | 100% |
| 重绘幅度 | 1 | 0.72 - 1 | 9 | 91% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 17/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 8，9 个样本，取值集中（一致性 83%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，9 个样本，一致性 100%
- 调度器 最常用 simple，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.72 - 1，9 个样本，取值集中（一致性 91%）
- 高发问题（17/9 个样本）：Steps较低可能导致细节不足
