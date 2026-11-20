---
name: text_to_image_lora_sampler_clip_59
type: Text To Image
frequency: 16
level: strong
coverage: 0.922813
common_nodes: [AutoCropFaces, CLIPLoader, CLIPTextEncode, EmptyLatentImage, GetNode, Image Paste Crop, ImageAndMaskPreview, KSampler, LayerMask: SegformerB2ClothesUltra, LayerUtility: ImageRemoveAlpha, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, SetNode, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAELoader, easy int]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Z-image-指定人物换脸+换发型_2010967930858639361.json, 图片生成/图生图/Z-image图生图 抖音小唐_2062237608138338305.json, 图片生成/图生图/图生图+指定人脸+Z-image=B站艾橘溪_2010655204034744322.json, 图片生成/图生图/指定人脸文生图_2057260510957096961.json, 图片生成/文生图/Krea2指定人脸图文生图_2071804070330982401.json, 图片生成/文生图/Z-Image 指定人脸文生图_2019605439574450177.json, 图片生成/文生图/Z-image 指定人脸 文生图=B站艾橘溪_1993965350142279682.json, 图片生成/文生图/Z-image指定人脸+参考文生图_2084211147854671873.json, 图片生成/文生图/Z-image指定人脸图文生图_2019947738347085825.json, 图片生成/文生图/指定人脸文生图 Z-image+Qwen双取样 （非人物lora）_2057702162876162050.json, 图片生成/文生图/指定人脸文生图_2052270376771702786.json, 图片生成/文生图/指定人脸文生图_2059644270969180161.json, 图片生成/文生图/指定人脸文生图_2060303424956231681.json, 图片生成/文生图/指定人脸文生图_2060379645148749825.json, 图片生成/文生图/指定人脸文生图_2060940216315244546.json, 图片生成/文生图/指定人脸文生图_2061456401721028610.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_59

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（图片生成/图生图/Z-image-指定人物换脸+换发型_2010967930858639361.json、图片生成/图生图/Z-image图生图 抖音小唐_2062237608138338305.json、图片生成/图生图/图生图+指定人脸+Z-image=B站艾橘溪_2010655204034744322.json、图片生成/图生图/指定人脸文生图_2057260510957096961.json、图片生成/文生图/Krea2指定人脸图文生图_2071804070330982401.json…）

- **类型**：Text To Image
- **样本数**：16
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 16 个 workflow 都包含：
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
- `ConditioningZeroOut` —— 15/16 个有
- `JjkText` —— 15/16 个有
- `AILab_QwenVL` —— 3/16 个有
- `ImageScaleDownToSize` —— 3/16 个有
- `CR Text` —— 1/16 个有
- `DuckQREncodeNode` —— 1/16 个有
- `HAIGC_SaveImagesToZip` —— 1/16 个有
- `easy showAnything` —— 1/16 个有
- `llama_cpp_instruct_adv` —— 1/16 个有
- `llama_cpp_model_loader` —— 1/16 个有
- `llama_cpp_parameters` —— 1/16 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 6 - 10 | 16 | 89% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 16 | 100% |
| 采样算法 | euler | - | 16 | 94% |
| 调度器 | simple | - | 16 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 16 | 100% |
| 宽度 | 1024 | 720 - 1024 | 16 | 93% |
| 高度 | 1536 | 1280 - 1536 | 16 | 96% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 17/16 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 6 - 10，16 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，16 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，16 个样本，一致性 94%
- 调度器 最常用 simple，16 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，16 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 720 - 1024，16 个样本，取值集中（一致性 93%）
- 高度 中位数 1536，观测区间 1280 - 1536，16 个样本，取值集中（一致性 96%）
- 高发问题（17/16 个样本）：Steps较低可能导致细节不足
