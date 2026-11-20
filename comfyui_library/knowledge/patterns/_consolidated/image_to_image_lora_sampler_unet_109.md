---
name: image_to_image_lora_sampler_unet_109
type: Image To Image
frequency: 7
level: moderate
coverage: 0.915429
common_nodes: [CLIPLoader, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen redit2509 无位移 水彩风格_1996087667999883266.json, 图片生成/图生图/Qwen2511 细节一致性修复工作流_2017865949512208386.json, 图片生成/图生图/qwen edit 2509 双人合影工作流_1973757541383581697.json, 图片生成/图生图/【3月】小红书[FireRed-Image-Edit1.1] 单图编辑_2030660710887333889.json, 图片生成/图生图/换装迁移-小红书firered超高一致性_2045202503913967618.json, 图片生成/文生图/nunchaku-qwen2509无偏移_1985975205229146114.json, 平台全量/换装迁移小红书firered超高一致性_2058307129873887233.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_109

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/Qwen redit2509 无位移 水彩风格_1996087667999883266.json、图片生成/图生图/Qwen2511 细节一致性修复工作流_2017865949512208386.json、图片生成/图生图/qwen edit 2509 双人合影工作流_1973757541383581697.json、图片生成/图生图/【3月】小红书[FireRed-Image-Edit1.1] 单图编辑_2030660710887333889.json、图片生成/图生图/换装迁移-小红书firered超高一致性_2045202503913967618.json…）

- **类型**：Image To Image
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CFGNorm` —— 6/7 个有
- `ConditioningZeroOut` —— 6/7 个有
- `Image Comparer (rgthree)` —— 6/7 个有
- `ModelSamplingAuraFlow` —— 6/7 个有
- `CR Text` —— 5/7 个有
- `PreviewImage` —— 5/7 个有
- `ImageResizeKJv2` —— 4/7 个有
- `CLIPTextEncode` —— 3/7 个有
- `FluxKontextImageScale` —— 3/7 个有
- `LayerUtility: PurgeVRAM V2` —— 3/7 个有
- `ReferenceLatent` —— 3/7 个有
- `ImageScaleToTotalPixels` —— 2/7 个有
- `InvertMask` —— 2/7 个有
- `PDIMAGE_LongerSize` —— 2/7 个有
- `easy imageConcat` —— 2/7 个有
- `easy imageCropFromMask` —— 2/7 个有
- `CR SDXL Aspect Ratio` —— 1/7 个有
- `EmptySD3LatentImage` —— 1/7 个有
- `JWInteger` —— 1/7 个有
- `LayerMask: MaskPreview` —— 1/7 个有
- `NunchakuQwenImageDiTLoader` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 20 | 7 | 50% |
| Prompt 约束强度(CFG) | 1 | 1 - 3.5 | 7 | 36% |
| 采样算法 | euler | - | 7 | 86% |
| 调度器 | simple | - | 7 | 86% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 20，7 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3.5，7 个样本，取值分散，一致性仅 36%
- 采样算法 最常用 euler，7 个样本，一致性 86%
- 调度器 最常用 simple，7 个样本，一致性 86%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（9/7 个样本）：Steps较低可能导致细节不足
