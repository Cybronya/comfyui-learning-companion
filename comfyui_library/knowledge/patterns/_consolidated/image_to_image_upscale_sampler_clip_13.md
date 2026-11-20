---
name: image_to_image_upscale_sampler_clip_13
type: Image To Image
frequency: 11
level: moderate
coverage: 0.868818
common_nodes: [CLIPTextEncode, DualCLIPLoader, Image Comparer (rgthree), ImageUpscaleWithModel, KSampler, LoadImage, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, UpscaleModelLoader, VAEDecodeTiled, VAEEncode, VAELoader, easy imageBatchToImageList]
problems: [Steps较低可能导致细节不足, 发现KSampler但没有VAEDecode]
missing: []
members: [图片生成/图生图/TTP一键高清放大极速版_1965408667019431938.json, 图片生成/图生图/TTP分块降噪-高清放大_1968140606964924418.json, 图片生成/图生图/[CQ808]_FULX高清放大_2116136934639759361.json, 图片生成/图生图/全能图片G-image-2场景噪点高清修复_2069614535090204673.json, 图片生成/图生图/场景图高清放大-FULX提速增质放大_1964225290094395394.json, 平台全量/FULX高清放大-提速增质_2109490202623430658.json, 平台全量/TTP一键放大图片到2K 4K 8K 高清放大图片极速版_1978134353815461890.json, 平台全量/[CQ808] FULX高清放大_2011304830773497857.json, 平台全量/图片放大-TTP-极速版2_2020425701102456834.json, 平台全量/图片放大-TTP-极速版_2020413903049596930.json, 平台全量/场景高清放大-V1版本_2051132853043376130.json]
source: knowledge_consolidation
---

# image_to_image_upscale_sampler_clip_13

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/TTP一键高清放大极速版_1965408667019431938.json、图片生成/图生图/TTP分块降噪-高清放大_1968140606964924418.json、图片生成/图生图/[CQ808]_FULX高清放大_2116136934639759361.json、图片生成/图生图/全能图片G-image-2场景噪点高清修复_2069614535090204673.json、图片生成/图生图/场景图高清放大-FULX提速增质放大_1964225290094395394.json…）

- **类型**：Image To Image
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPTextEncode`
- `DualCLIPLoader`
- `Image Comparer (rgthree)`
- `ImageUpscaleWithModel`
- `KSampler`
- `LoadImage`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAELoader`
- `easy imageBatchToImageList`

**可变部分**（部分 workflow 才有）：
- `SaveImage` —— 10/11 个有
- `ConditioningZeroOut` —— 8/11 个有
- `ImageListToImageBatch` —— 8/11 个有
- `ImageResize+` —— 8/11 个有
- `ImageScaleToTotalPixels` —— 8/11 个有
- `LoraLoaderModelOnly` —— 8/11 个有
- `LoraLoader` —— 7/11 个有
- `Anything Everywhere3` —— 5/11 个有
- `Anything Everywhere` —— 3/11 个有
- `ImageSmartSharpen+` —— 3/11 个有
- `easy imageListToImageBatch` —— 3/11 个有
- `FluxGuidance` —— 2/11 个有
- `ImageResizeKJ` —— 2/11 个有
- `PreviewImage` —— 2/11 个有
- `GetNode` —— 1/11 个有
- `Label (rgthree)` —— 1/11 个有
- `ResizeLongestToNode` —— 1/11 个有
- `SetNode` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 11 | 74% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 11 | 62% |
| 采样算法 | euler | - | 11 | 100% |
| 调度器 | simple | - | 11 | 73% |
| 重绘幅度 | 0.3 | 0.1 - 0.3 | 11 | 60% |
| LoRA 模型强度 | 1 | 1 - 1 | 7 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |
| 发现KSampler但没有VAEDecode | 11/11 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，11 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，11 个样本
- 采样算法 最常用 euler，11 个样本，一致性 100%
- 调度器 最常用 simple，11 个样本，一致性 73%
- 重绘幅度 中位数 0.3，观测区间 0.1 - 0.3，11 个样本
- LoRA 模型强度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（11/11 个样本）：Steps较低可能导致细节不足
- 高发问题（11/11 个样本）：发现KSampler但没有VAEDecode
