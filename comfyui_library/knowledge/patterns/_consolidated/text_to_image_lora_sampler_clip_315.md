---
name: text_to_image_lora_sampler_clip_315
type: Text To Image
frequency: 3
level: weak
coverage: 0.854333
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, Flux2KleinEditTextEncode_EditUtils, GetImageSize, GetNode, INTConstant, Image Comparer (rgthree), KSampler, LCSColorAnchor, LCSLoadData, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleRestore V2, LoraLoaderModelOnly, MemoryCleaner, PreviewImage, SaveImage, SetNode, SimpleMath+, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, VAEDecode, VAELoader, easy imageBatchToImageList, easy imageColorMatch, easy imageListToImageBatch]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/（国风工笔风格版）krea2+高清细节放大——含提示词模板_2087523449446166530.json, 图片生成/文生图/（风格版）krea2+高清放大_2078098003075878914.json, 数字人/数字人/Klein加TTP图片高清去AI感去油处理工具_2100676962036572162.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_315

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/（国风工笔风格版）krea2+高清细节放大——含提示词模板_2087523449446166530.json、图片生成/文生图/（风格版）krea2+高清放大_2078098003075878914.json、数字人/数字人/Klein加TTP图片高清去AI感去油处理工具_2100676962036572162.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：85%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `Flux2KleinEditTextEncode_EditUtils`
- `GetImageSize`
- `GetNode`
- `INTConstant`
- `Image Comparer (rgthree)`
- `KSampler`
- `LCSColorAnchor`
- `LCSLoadData`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleRestore V2`
- `LoraLoaderModelOnly`
- `MemoryCleaner`
- `PreviewImage`
- `SaveImage`
- `SetNode`
- `SimpleMath+`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy imageBatchToImageList`
- `easy imageColorMatch`
- `easy imageListToImageBatch`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 2/3 个有
- `PreviewAny` —— 2/3 个有
- `ResolutionSelector` —— 2/3 个有
- `llama_cpp_instruct_adv` —— 2/3 个有
- `llama_cpp_model_loader` —— 2/3 个有
- `llama_cpp_parameters` —— 2/3 个有
- `GoohaiAnyExists` —— 1/3 个有
- `JjkText` —— 1/3 个有
- `LoadImage` —— 1/3 个有
- `MathExpression|pysssss` —— 1/3 个有
- `solarL_SaveImagesToZip` —— 1/3 个有
- `孤海注释` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 80 - 1024 | 3 | 37% |
| 高度 | 1024 | 80 - 1024 | 3 | 37% |
| 采样步数 | 10 | 4 - 10 | 3 | 65% |
| Prompt 约束强度(CFG) | 1 | 1 - 4.5 | 3 | 24% |
| 采样算法 | euler | - | 3 | 67% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 80 - 1024，3 个样本，取值分散，一致性仅 37%
- 高度 中位数 1024，观测区间 80 - 1024，3 个样本，取值分散，一致性仅 37%
- 采样步数 中位数 10，观测区间 4 - 10，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4.5，3 个样本，取值分散，一致性仅 24%
- 采样算法 最常用 euler，3 个样本，一致性 67%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（4/3 个样本）：Steps较低可能导致细节不足
