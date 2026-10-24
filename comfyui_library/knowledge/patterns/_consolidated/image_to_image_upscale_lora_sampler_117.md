---
name: image_to_image_upscale_lora_sampler_117
type: Image To Image
frequency: 2
level: weak
coverage: 0.821
common_nodes: [CLIPTextEncode, CR Text, CR Text Concatenate, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, ImageListToImageBatch, ImageScaleBy, ImageUpscaleWithModel, ImpactImageBatchToImageList, KSampler, LayerUtility: JoyCaptionBeta1, LayerUtility: LoadJoyCaptionBeta1Model, LoadImage, LoraLoaderModelOnly, SDXL Empty Latent Image (rgthree), SaveImage, ShowText|pysssss, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, UpscaleModelLoader, VAEDecode, VAEDecodeTiled, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/升级-Flux1-Krea-Dev最强美学模型  + JOP CAPTION BETA最强反推模型_1951105950621048833.json, 图片生成/文生图/升级-Flux1-Krea-Dev最强美学模型  + JOP CAPTION BETA最强反推模型_2039150798575243265.json]
source: knowledge_consolidation
---

# image_to_image_upscale_lora_sampler_117

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/升级-Flux1-Krea-Dev最强美学模型  + JOP CAPTION BETA最强反推模型_1951105950621048833.json、图片生成/文生图/升级-Flux1-Krea-Dev最强美学模型  + JOP CAPTION BETA最强反推模型_2039150798575243265.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：82%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `CR Text`
- `CR Text Concatenate`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `ImageListToImageBatch`
- `ImageScaleBy`
- `ImageUpscaleWithModel`
- `ImpactImageBatchToImageList`
- `KSampler`
- `LayerUtility: JoyCaptionBeta1`
- `LayerUtility: LoadJoyCaptionBeta1Model`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SDXL Empty Latent Image (rgthree)`
- `SaveImage`
- `ShowText|pysssss`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAELoader`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | exponential | - | 2 | 100% |
| 重绘幅度 | 0.9 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 exponential，2 个样本，一致性 100%
- 重绘幅度 中位数 0.9，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
