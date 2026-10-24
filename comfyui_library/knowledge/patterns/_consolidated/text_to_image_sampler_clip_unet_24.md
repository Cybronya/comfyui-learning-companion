---
name: text_to_image_sampler_clip_unet_24
type: Text To Image
frequency: 15
level: weak
coverage: 0.907667
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, Fast Groups Bypasser (rgthree), KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Krea2+MuseByStable+单图文生图+批量文生图_2084187096876666882.json, 图片生成/文生图/Boogu Image 风格微调LoRA测试流 Base+Turbo_2073325674210877442.json, 图片生成/文生图/Boogu-Image VS Z-Image-Turbo VS Ernie-Image_2068170711595831297.json, 图片生成/文生图/Ernie-Image-Flex-V1_2058033549370028034.json, 图片生成/文生图/Ernie-Image-Turbo 4_8steps VS ErnieTurbo_extracted_lora VS Z-Image-Turbo_2045838209761939457.json, 图片生成/文生图/Krea2 MuseByStable 单图文生图+批量文生图_2075851087260766210.json, 图片生成/文生图/Krea2 MuseByStable 单图文生图+批量文生图_2084089644026781698.json, 图片生成/文生图/Krea2 MuseByStable 单图文生图+批量文生图_2084098279272439810.json, 图片生成/文生图/Krea2 MuseByStable 单图文生图+批量文生图_2084123057798598658.json, 图片生成/文生图/Krea2 MuseByStable 单图文生图+批量文生图_2084159014056841218.json, 图片生成/文生图/Krea2 MuseByStable 单图文生图+批量文生图_2084160465382494209.json, 图片生成/文生图/VividMuse Ernie Image工作流_2044768393248641026.json, 图片生成/文生图/VividMuse Juggernaut Z-8steps VS Z-Image-8steps_2056009146180358146.json, 图片生成/文生图/VividMuse Krea2-Turbo VS Z-Image_2069775605947785218.json, 图片生成/文生图/VividMuse Z-Image-Engineer-V6-Workflow_2065785395203362818.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_24

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（图片生成/图生图/Krea2+MuseByStable+单图文生图+批量文生图_2084187096876666882.json、图片生成/文生图/Boogu Image 风格微调LoRA测试流 Base+Turbo_2073325674210877442.json、图片生成/文生图/Boogu-Image VS Z-Image-Turbo VS Ernie-Image_2068170711595831297.json、图片生成/文生图/Ernie-Image-Flex-V1_2058033549370028034.json、图片生成/文生图/Ernie-Image-Turbo 4_8steps VS ErnieTurbo_extracted_lora VS Z-Image-Turbo_2045838209761939457.json…）

- **类型**：Text To Image
- **样本数**：15
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 15 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 14/15 个有
- `Seed (rgthree)` —— 14/15 个有
- `easy promptList` —— 14/15 个有
- `PreviewImage` —— 12/15 个有
- `LayerUtility: ImageReel` —— 8/15 个有
- `LayerUtility: ImageReelComposit` —— 8/15 个有
- `TTResolutionSelector` —— 8/15 个有
- `HAIGC_SaveImagesToZip` —— 7/15 个有
- `Label (rgthree)` —— 7/15 个有
- `PrimitiveStringMultiline` —— 7/15 个有
- `TextInputNode` —— 7/15 个有
- `KSamplerAdvanced` —— 4/15 个有
- `LayerColor: ColorAdapter` —— 2/15 个有
- `ResolutionSelector` —— 2/15 个有
- `ClipLoaderGGUF` —— 1/15 个有
- `easy promptConcat` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 768 | 512 - 1728 | 15 | 66% |
| 高度 | 1280 | 512 - 2304 | 15 | 72% |
| 采样步数 | 10 | 4 - 50 | 15 | 14% |
| Prompt 约束强度(CFG) | 1 | 1 - 5 | 15 | 18% |
| 采样算法 | euler | - | 15 | 73% |
| 调度器 | simple | - | 15 | 80% |
| 重绘幅度 | 1 | 1 - 1 | 15 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 16/15 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 768，观测区间 512 - 1728，15 个样本
- 高度 中位数 1280，观测区间 512 - 2304，15 个样本
- 采样步数 中位数 10，观测区间 4 - 50，15 个样本，取值分散，一致性仅 14%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 5，15 个样本，取值分散，一致性仅 18%
- 采样算法 最常用 euler，15 个样本，一致性 73%
- 调度器 最常用 simple，15 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
- 高发问题（16/15 个样本）：Steps较低可能导致细节不足
