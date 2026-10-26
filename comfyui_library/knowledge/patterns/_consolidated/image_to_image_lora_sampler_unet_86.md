---
name: image_to_image_lora_sampler_unet_86
type: Image To Image
frequency: 7
level: strong
coverage: 0.982714
common_nodes: [CLIPLoader, FluxKontextMultiReferenceLatentMethod, KSampler, Krea2OstrisEditModelPatch, LoadImage, LoraLoaderModelOnly, SaveImage, TextEncodeKrea2OstrisEdit, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Krea2 Edit 动漫转写实风格_2080856481674653698.json, 图片生成/图生图/Krea2 Edit 动漫转写实风格_2083388583871868930.json, 图片生成/图生图/Krea2_Edit_动漫转写实风格_2096782005672439809.json, 图片生成/图生图/Krea2_Edit_动漫转写实风格_2096882987966226434.json, 图片生成/图生图/Krea2_图生四视图_2101122733563269121.json, 图片生成/图生图/二次元转写实 Krea2-Anime2Real_2081945637884620801.json, 图片生成/文生图/Krea2_图生四视图角色设定集图像生成工作流_2101369065821528065.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_86

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/Krea2 Edit 动漫转写实风格_2080856481674653698.json、图片生成/图生图/Krea2 Edit 动漫转写实风格_2083388583871868930.json、图片生成/图生图/Krea2_Edit_动漫转写实风格_2096782005672439809.json、图片生成/图生图/Krea2_Edit_动漫转写实风格_2096882987966226434.json、图片生成/图生图/Krea2_图生四视图_2101122733563269121.json…）

- **类型**：Image To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：98%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `FluxKontextMultiReferenceLatentMethod`
- `KSampler`
- `Krea2OstrisEditModelPatch`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `TextEncodeKrea2OstrisEdit`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageScaleByAspectRatio V2` —— 6/7 个有
- `FluxKontextImageScale` —— 4/7 个有
- `Easy_QwenEdit2509` —— 3/7 个有
- `ImageResizeKJv2` —— 2/7 个有
- `Image Comparer (rgthree)` —— 1/7 个有
- `Image_Resize_longsize` —— 1/7 个有
- `Textbox` —— 1/7 个有
- `easy imageConcat` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 8 - 10 | 7 | 89% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | beta57 | - | 7 | 57% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 8 - 10，7 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 beta57，7 个样本，一致性 57%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
