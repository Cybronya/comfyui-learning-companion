---
name: image_to_image_controlnet_upscale_lora_19
type: Image To Image
frequency: 2
level: weak
coverage: 0.867
common_nodes: [CLIPTextEncode, ControlNetApplyAdvanced, ControlNetLoader, DualCLIPLoader, FluxGuidance, Image Comparer (rgthree), ImageListToImageBatch, ImageUpscaleWithModel, KSampler, Latent Noise Injection, LoadImage, LoraLoaderModelOnly, ModelSamplingFlux, PreviewImage, SaveImage, SetUnionControlNetType, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, TTPlanet_TileGF_Preprocessor, UNETLoader, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader, easy imageBatchToImageList, easy imageScaleDownToSize]
problems: []
missing: []
members: [平台全量/图片4倍放大高清无码flux krea_1951059747502010370.json, 平台全量/图片4倍放大高清无码flux_1950493212488159233.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_upscale_lora_19

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/图片4倍放大高清无码flux krea_1951059747502010370.json、平台全量/图片4倍放大高清无码flux_1950493212488159233.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：87%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `DualCLIPLoader`
- `FluxGuidance`
- `Image Comparer (rgthree)`
- `ImageListToImageBatch`
- `ImageUpscaleWithModel`
- `KSampler`
- `Latent Noise Injection`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingFlux`
- `PreviewImage`
- `SaveImage`
- `SetUnionControlNetType`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `TTPlanet_TileGF_Preprocessor`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy imageBatchToImageList`
- `easy imageScaleDownToSize`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.3 | - | 2 | 100% |
| 采样步数 | 30 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 0.3 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 0.3，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 30，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 0.3，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
