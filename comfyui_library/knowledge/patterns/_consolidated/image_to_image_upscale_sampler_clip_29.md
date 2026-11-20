---
name: image_to_image_upscale_sampler_clip_29
type: Image To Image
frequency: 6
level: moderate
coverage: 0.785167
common_nodes: [CLIPLoader, CLIPTextEncode, Image Comparer (rgthree), ImageListToImageBatch, ImageUpscaleWithModel, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, ModelSamplingSD3, SaveImage, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, UpscaleModelLoader, VAEEncode, VAELoader]
problems: [发现KSampler但没有VAEDecode]
missing: []
members: [图片生成/图生图/千府AI二次高清放大工作流_1963484062110535681.json, 平台全量/Wan2.2 人物细节修复 人像高清放大TTP+WAN 2.2修复皮肤质感和面部细节 去AI塑料感_2022930720154456065.json, 平台全量/Wan2.2+TTP放大_零变形不油腻_1938108302855159809.json, 平台全量/flux-fill丨最强扩图_1899338400196116481.json, 平台全量/人像细节修复_2037447277056368642.json, 平台全量/全能图片V1图像编辑_高清放大_1960600808368857089.json]
source: knowledge_consolidation
---

# image_to_image_upscale_sampler_clip_29

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/千府AI二次高清放大工作流_1963484062110535681.json、平台全量/Wan2.2 人物细节修复 人像高清放大TTP+WAN 2.2修复皮肤质感和面部细节 去AI塑料感_2022930720154456065.json、平台全量/Wan2.2+TTP放大_零变形不油腻_1938108302855159809.json、平台全量/flux-fill丨最强扩图_1899338400196116481.json、平台全量/人像细节修复_2037447277056368642.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：79%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `Image Comparer (rgthree)`
- `ImageListToImageBatch`
- `ImageUpscaleWithModel`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `ModelSamplingSD3`
- `SaveImage`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageScaleToTotalPixels` —— 5/6 个有
- `PathchSageAttentionKJ` —— 5/6 个有
- `VAEDecode` —— 5/6 个有
- `easy cleanGpuUsed` —— 5/6 个有
- `easy imageBatchToImageList` —— 5/6 个有
- `GetNode` —— 4/6 个有
- `LoraLoaderModelOnly` —— 4/6 个有
- `PreviewImage` —— 4/6 个有
- `SetNode` —— 4/6 个有
- `Anything Everywhere3` —— 3/6 个有
- `CR Text` —— 1/6 个有
- `ConditioningZeroOut` —— 1/6 个有
- `DifferentialDiffusion` —— 1/6 个有
- `DualCLIPLoader` —— 1/6 个有
- `FluxGuidance` —— 1/6 个有
- `ImagePadForOutpaint` —— 1/6 个有
- `ImpactImageBatchToImageList` —— 1/6 个有
- `InpaintModelConditioning` —— 1/6 个有
- `LayerUtility: NumberCalculatorV2` —— 1/6 个有
- `LoraLoader` —— 1/6 个有
- `Primitive integer [Crystools]` —— 1/6 个有
- `PrimitiveInt` —— 1/6 个有
- `RH_Captioner` —— 1/6 个有
- `RH_Nano_Banana_Image2Image` —— 1/6 个有
- `VAEDecodeTiled` —— 1/6 个有
- `easy imageSize` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.4 | - | 1 | 100% |
| LoRA 文本强度 | 0.4 | - | 1 | 100% |
| 采样步数 | 10 | 10 - 10 | 6 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 50% |
| 调度器 | beta | - | 6 | 83% |
| 重绘幅度 | 0.08 | 0.06 - 0.33 | 6 | 19% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| 发现KSampler但没有VAEDecode | 1/6 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 10，观测区间 10 - 10，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 50%
- 调度器 最常用 beta，6 个样本，一致性 83%
- 重绘幅度 中位数 0.08，观测区间 0.06 - 0.33，6 个样本，取值分散，一致性仅 19%
- 风险：重绘幅度 观测到 0.06，低于常用下限 0.1（）
