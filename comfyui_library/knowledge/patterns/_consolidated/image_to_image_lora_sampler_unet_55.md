---
name: image_to_image_lora_sampler_unet_55
type: Image To Image
frequency: 10
level: moderate
coverage: 0.8382
common_nodes: [CFGNorm, CLIPLoader, ImageScaleToTotalPixels, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen-edit 超自然重打光_2054846333298724865.json, 图片生成/图生图/Qwen-edit_万物重打光_2099321308822724609.json, 图片生成/图生图/Qwen-edit_万物重打光_2099665295848861698.json, 图片生成/图生图/Qwen-image-edit2511指哪打哪工作流_1959082223985176577.json, 图片生成/图生图/QwenEdit2509服装白底图提取_1993628856821235713.json, 图片生成/图生图/☯️千问Edit_单图编辑_1972192308055764994.json, 图片生成/图生图/一键生成Hello Kitty中国风头像_2013190174729052161.json, 图片生成/图生图/人像写真重打光_2076370520215474177.json, 图片生成/图生图/人像写真重打光_2077926058837504001.json, 图片生成/图生图/人像写真重打光_2077938985393020930.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_55

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/Qwen-edit 超自然重打光_2054846333298724865.json、图片生成/图生图/Qwen-edit_万物重打光_2099321308822724609.json、图片生成/图生图/Qwen-edit_万物重打光_2099665295848861698.json、图片生成/图生图/Qwen-image-edit2511指哪打哪工作流_1959082223985176577.json、图片生成/图生图/QwenEdit2509服装白底图提取_1993628856821235713.json…）

- **类型**：Image To Image
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 10 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 9/10 个有
- `JjkText` —— 7/10 个有
- `TextEncodeQwenImageEdit` —— 7/10 个有
- `ColorMatch` —— 6/10 个有
- `LayerUtility: PurgeVRAM V2` —— 6/10 个有
- `TextEncodeQwenImageEditPlus` —— 4/10 个有
- `Canny` —— 3/10 个有
- `LayerUtility: ImageReel` —— 3/10 个有
- `LayerUtility: ImageReelComposit` —— 3/10 个有
- `ModelPatchLoader` —— 3/10 个有
- `QwenImageDiffsynthControlnet` —— 3/10 个有
- `CR Text` —— 1/10 个有
- `Image Comparer (rgthree)` —— 1/10 个有
- `ImageAndMaskPreview` —— 1/10 个有
- `Textbox` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 30 | 10 | 29% |
| Prompt 约束强度(CFG) | 1 | 0.99 - 1 | 10 | 100% |
| 采样算法 | euler | - | 10 | 100% |
| 调度器 | simple | - | 10 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 30，10 个样本，取值分散，一致性仅 29%
- Prompt 约束强度(CFG) 中位数 1，观测区间 0.99 - 1，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，10 个样本，一致性 100%
- 调度器 最常用 simple，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 风险：Prompt 约束强度(CFG) 观测到 0.99，低于常用下限 1（CFG 过低可能导致 Prompt 约束不足、结果偏离描述）
- 高发问题（6/10 个样本）：Steps较低可能导致细节不足
