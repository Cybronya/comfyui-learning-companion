---
name: text_to_image_upscale_lora_sampler_5
type: Text To Image
frequency: 17
level: strong
coverage: 0.917647
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, GetImageSize+, ImageResize+, ImageScaleBy, KSampler, LoraLoaderModelOnly, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/8K究极高清图像极速直出(异域风情性感比基尼)_20款任你挑选_2038860113427042305.json, 图片生成/文生图/KOOK_Qwen_2512_真实人像_2006334912823037953.json, 图片生成/文生图/Kook_Zimage_瑶光_2033767418278977537.json, 图片生成/文生图/Kook_Zimage_瑶光_2072528894925819906.json, 图片生成/文生图/Qwen Image 2512 Kook 真实人像文生图V1_2008514200146022401.json, 图片生成/文生图/Qwen Image 2512 Kook 真实人像文生图V1_2009133925792227330.json, 图片生成/文生图/Z-image 真实照片效果_2037377240018722818.json, 图片生成/文生图/Zimage超级真实人像_2052365553586712578.json, 图片生成/文生图/Zimage超级真实人像_Kook大佬瑶光lora_2052288192912605186.json, 图片生成/文生图/希帆解说漫-人设图生成_2051932454398775297.json, 图片生成/文生图/文生图_2047653558849376258.json, 图片生成/文生图/文生图_Zimage_瑶光_2036105144634449921.json, 图片生成/文生图/文生图_Zimage_高清_2039868544275451905.json, 图片生成/文生图/无Ai感超强文生图_2076312965044858881.json, 图片生成/文生图/自用提示词生成人物_2084129308481773570.json, 图片生成/文生图/（Kook版-贞贞lora）Z-Image-Base文生图+高清化_2035938949620830209.json, 图片生成/文生图/💫老许Gary：Z-image瑶光丨文生图_图像反推+SeedVR放大_2035003906622754817.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_5

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（图片生成/文生图/8K究极高清图像极速直出(异域风情性感比基尼)_20款任你挑选_2038860113427042305.json、图片生成/文生图/KOOK_Qwen_2512_真实人像_2006334912823037953.json、图片生成/文生图/Kook_Zimage_瑶光_2033767418278977537.json、图片生成/文生图/Kook_Zimage_瑶光_2072528894925819906.json、图片生成/文生图/Qwen Image 2512 Kook 真实人像文生图V1_2008514200146022401.json…）

- **类型**：Text To Image
- **样本数**：17
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 17 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `GetImageSize+`
- `ImageResize+`
- `ImageScaleBy`
- `KSampler`
- `LoraLoaderModelOnly`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `KOOK_SaveJPGImage` —— 16/17 个有
- `SaveImage` —— 14/17 个有
- `ImageCASharpening+` —— 13/17 个有
- `RunningHub Deepcleaner` —— 13/17 个有
- `FastFilmGrain` —— 12/17 个有
- `LayerColor: BrightnessContrastV2` —— 12/17 个有
- `PreviewImage` —— 7/17 个有
- `ModelSamplingAuraFlow` —— 4/17 个有
- `KOOK_ImageCompression` —— 3/17 个有
- `HAIGC_SaveImagesToZip` —— 2/17 个有
- `LatentFrequencyEnhancer_lrzjason` —— 2/17 个有
- `CR Text` —— 1/17 个有
- `Fast Groups Bypasser (rgthree)` —— 1/17 个有
- `Float` —— 1/17 个有
- `GetImageSize` —— 1/17 个有
- `ImpactSwitch` —— 1/17 个有
- `Int` —— 1/17 个有
- `MultiLinePromptIndex` —— 1/17 个有
- `PhotoShakeNode` —— 1/17 个有
- `Text` —— 1/17 个有
- `Text Multiline` —— 1/17 个有
- `easy cleanGpuUsed` —— 1/17 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1080 | 1080 - 1920 | 17 | 82% |
| 高度 | 1920 | 1080 - 1920 | 17 | 89% |
| 采样步数 | 8 | 8 - 20 | 17 | 68% |
| Prompt 约束强度(CFG) | 1 | 1 - 1.5 | 17 | 89% |
| 采样算法 | res_2s | - | 17 | 94% |
| 调度器 | bong_tangent | - | 17 | 76% |
| 重绘幅度 | 1 | 1 - 1 | 17 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 16/17 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1080，观测区间 1080 - 1920，17 个样本，取值集中（一致性 82%）
- 高度 中位数 1920，观测区间 1080 - 1920，17 个样本，取值集中（一致性 89%）
- 采样步数 中位数 8，观测区间 8 - 20，17 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1.5，17 个样本，取值集中（一致性 89%）
- 采样算法 最常用 res_2s，17 个样本，一致性 94%
- 调度器 最常用 bong_tangent，17 个样本，一致性 76%
- 重绘幅度 中位数 1，观测区间 1 - 1，17 个样本，取值集中（一致性 100%）
- 高发问题（16/17 个样本）：Steps较低可能导致细节不足
