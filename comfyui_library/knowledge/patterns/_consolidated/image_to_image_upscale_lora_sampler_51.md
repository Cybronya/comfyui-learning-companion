---
name: image_to_image_upscale_lora_sampler_51
type: Image To Image
frequency: 3
level: strong
coverage: 0.752333
common_nodes: [CLIPTextEncode, DualCLIPLoader, Image Comparer (rgthree), ImageSmartSharpen+, ImageUpscaleWithModel, KSampler, LoadImage, LoraLoaderModelOnly, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, UpscaleModelLoader, VAEDecodeTiled, VAEEncode, VAELoader, easy imageBatchToImageList, easy imageListToImageBatch]
problems: [Steps较低可能导致细节不足, 发现KSampler但没有VAEDecode]
missing: []
members: [图片生成/图生图/TTP一键高清放大极速版_1965408667019431938.json, 图片生成/图生图/TTP分块降噪-高清放大_1968140606964924418.json, 图片生成/图生图/wan 2.2-一键洗图+高清放大_1977382045880078338.json]
source: knowledge_consolidation
---

# image_to_image_upscale_lora_sampler_51

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/TTP一键高清放大极速版_1965408667019431938.json、图片生成/图生图/TTP分块降噪-高清放大_1968140606964924418.json、图片生成/图生图/wan 2.2-一键洗图+高清放大_1977382045880078338.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：75%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `DualCLIPLoader`
- `Image Comparer (rgthree)`
- `ImageSmartSharpen+`
- `ImageUpscaleWithModel`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAELoader`
- `easy imageBatchToImageList`
- `easy imageListToImageBatch`

**可变部分**（部分 workflow 才有）：
- `Anything Everywhere` —— 2/3 个有
- `Anything Everywhere3` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `ResizeLongestToNode` —— 2/3 个有
- `SaveImage` —— 2/3 个有
- `CLIPLoader` —— 1/3 个有
- `CR Seed` —— 1/3 个有
- `Fast Groups Bypasser (rgthree)` —— 1/3 个有
- `FluxGuidance` —— 1/3 个有
- `GetNode` —— 1/3 个有
- `ImageResizeKJ` —— 1/3 个有
- `ImpactInt` —— 1/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/3 个有
- `LayerUtility: PurgeVRAM` —— 1/3 个有
- `ModelSamplingSD3` —— 1/3 个有
- `PathchSageAttentionKJ` —— 1/3 个有
- `RH_LLMAPI_NODE` —— 1/3 个有
- `SetNode` —— 1/3 个有
- `VAEDecode` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 3 | 100% |
| Prompt 约束强度(CFG) | 2.5 | 1 - 2.5 | 3 | 65% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | sgm_uniform | - | 3 | 100% |
| 重绘幅度 | 0.3 | 0.3 - 0.3 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |
| 发现KSampler但没有VAEDecode | 2/3 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 1 - 2.5，3 个样本
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 sgm_uniform，3 个样本，一致性 100%
- 重绘幅度 中位数 0.3，观测区间 0.3 - 0.3，3 个样本，取值集中（一致性 100%）
- 高发问题（5/3 个样本）：Steps较低可能导致细节不足
- 高发问题（2/3 个样本）：发现KSampler但没有VAEDecode
