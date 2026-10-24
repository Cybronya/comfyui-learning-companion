---
name: text_to_image_upscale_lora_sampler_97
type: Text To Image
frequency: 3
level: weak
coverage: 0.866
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, Image Comparer (rgthree), ImageScale, ImageUpscaleWithModel, KSampler, LoraLoaderModelOnly, SaveImage, UNETLoader, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Wan2.1 文生图+图像高清修复_1945356782250414081.json, 图片生成/文生图/ZImage_场景2K_双LoRA切换_2111937108096151554.json, 图片生成/文生图/ZImage场景文生图2K输出，双LoRA自由切换氛围_2112269862025392129.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_97

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Wan2.1 文生图+图像高清修复_1945356782250414081.json、图片生成/文生图/ZImage_场景2K_双LoRA切换_2111937108096151554.json、图片生成/文生图/ZImage场景文生图2K输出，双LoRA自由切换氛围_2112269862025392129.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：87%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `Image Comparer (rgthree)`
- `ImageScale`
- `ImageUpscaleWithModel`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 2/3 个有
- `INTConstant` —— 2/3 个有
- `JJC_JoyCaption` —— 1/3 个有
- `JjkText` —— 1/3 个有
- `Label (rgthree)` —— 1/3 个有
- `LayerUtility: ImageScaleRestore V2` —— 1/3 个有
- `LoadImage` —— 1/3 个有
- `RH_Translator` —— 1/3 个有
- `ShowText|pysssss` —— 1/3 个有
- `solarL_SaveImagesToZip` —— 1/3 个有
- `孤海注释` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 80 - 1080 | 3 | 37% |
| 高度 | 1920 | 80 - 1920 | 3 | 34% |
| 采样步数 | 6 | 4 - 10 | 3 | 63% |
| Prompt 约束强度(CFG) | 1 | 1 - 4.5 | 3 | 24% |
| 采样算法 | uni_pc | - | 3 | 33% |
| 调度器 | simple | - | 3 | 33% |
| 重绘幅度 | 0.18 | 0.1 - 1 | 3 | 5% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 80 - 1080，3 个样本，取值分散，一致性仅 37%
- 高度 中位数 1920，观测区间 80 - 1920，3 个样本，取值分散，一致性仅 34%
- 采样步数 中位数 6，观测区间 4 - 10，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4.5，3 个样本，取值分散，一致性仅 24%
- 采样算法 最常用 uni_pc，3 个样本，一致性 33%
- 调度器 最常用 simple，3 个样本，一致性 33%
- 重绘幅度 中位数 0.18，观测区间 0.1 - 1，3 个样本，取值分散，一致性仅 5%
- 高发问题（5/3 个样本）：Steps较低可能导致细节不足
