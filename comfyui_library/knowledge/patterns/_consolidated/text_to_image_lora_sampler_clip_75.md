---
name: text_to_image_lora_sampler_clip_75
type: Text To Image
frequency: 12
level: strong
coverage: 0.922583
common_nodes: [AutoCropFaces, CLIPLoader, CLIPTextEncode, EmptyLatentImage, GetNode, Image Paste Crop, ImageAndMaskPreview, KSampler, LayerMask: SegformerB2ClothesUltra, LayerUtility: ImageRemoveAlpha, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, SetNode, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAELoader, easy int]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Krea2指定人脸图文生图_2071804070330982401.json, 图片生成/文生图/Z-Image 指定人脸文生图_2019605439574450177.json, 图片生成/文生图/Z-image 指定人脸 文生图=B站艾橘溪_1993965350142279682.json, 图片生成/文生图/Z-image指定人脸+参考文生图_2084211147854671873.json, 图片生成/文生图/Z-image指定人脸图文生图_2019947738347085825.json, 图片生成/文生图/指定人脸文生图 Z-image+Qwen双取样 （非人物lora）_2057702162876162050.json, 图片生成/文生图/指定人脸文生图_2052270376771702786.json, 图片生成/文生图/指定人脸文生图_2059644270969180161.json, 图片生成/文生图/指定人脸文生图_2060303424956231681.json, 图片生成/文生图/指定人脸文生图_2060379645148749825.json, 图片生成/文生图/指定人脸文生图_2060940216315244546.json, 图片生成/文生图/指定人脸文生图_2061456401721028610.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_75

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/文生图/Krea2指定人脸图文生图_2071804070330982401.json、图片生成/文生图/Z-Image 指定人脸文生图_2019605439574450177.json、图片生成/文生图/Z-image 指定人脸 文生图=B站艾橘溪_1993965350142279682.json、图片生成/文生图/Z-image指定人脸+参考文生图_2084211147854671873.json、图片生成/文生图/Z-image指定人脸图文生图_2019947738347085825.json…）

- **类型**：Text To Image
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 12 个 workflow 都包含：
- `AutoCropFaces`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `GetNode`
- `Image Paste Crop`
- `ImageAndMaskPreview`
- `KSampler`
- `LayerMask: SegformerB2ClothesUltra`
- `LayerUtility: ImageRemoveAlpha`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `SetNode`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 11/12 个有
- `JjkText` —— 11/12 个有
- `CR Text` —— 1/12 个有
- `DuckQREncodeNode` —— 1/12 个有
- `HAIGC_SaveImagesToZip` —— 1/12 个有
- `easy showAnything` —— 1/12 个有
- `llama_cpp_instruct_adv` —— 1/12 个有
- `llama_cpp_model_loader` —— 1/12 个有
- `llama_cpp_parameters` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 12 | 100% |
| 高度 | 1536 | 1536 - 1536 | 12 | 100% |
| 采样步数 | 8 | 8 - 8 | 12 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 12 | 100% |
| 采样算法 | euler | - | 12 | 92% |
| 调度器 | simple | - | 12 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 13/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，12 个样本，取值集中（一致性 100%）
- 高度 中位数 1536，观测区间 1536 - 1536，12 个样本，取值集中（一致性 100%）
- 采样步数 中位数 8，观测区间 8 - 8，12 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，12 个样本，一致性 92%
- 调度器 最常用 simple，12 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 高发问题（13/12 个样本）：Steps较低可能导致细节不足
