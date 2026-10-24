---
name: unknown_workflow_upscale_sampler_clip_37
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.872333
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, FluxGuidance, Image Comparer (rgthree), ImageScaleToTotalPixels, ImageUpscaleWithModel, KSamplerSelect, LoadImage, PreviewImage, RandomNoise, SamplerCustomAdvanced, SaveImage, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, UpscaleModelLoader, VAEDecodeTiled, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/TTP-8K超清放大_1952003516434952193.json, 图片生成/图生图/TTP极致分块-放大修复_1992492280156147713.json, 图片生成/图生图/TTP极致分块放大修复_1961047996962160642.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_sampler_clip_37

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/TTP-8K超清放大_1952003516434952193.json、图片生成/图生图/TTP极致分块-放大修复_1992492280156147713.json、图片生成/图生图/TTP极致分块放大修复_1961047996962160642.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `FluxGuidance`
- `Image Comparer (rgthree)`
- `ImageScaleToTotalPixels`
- `ImageUpscaleWithModel`
- `KSamplerSelect`
- `LoadImage`
- `PreviewImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Florence2ModelLoader` —— 2/3 个有
- `Florence2Run` —— 2/3 个有
- `FluxKontextImageScale` —— 2/3 个有
- `ImageListToImageBatch` —— 2/3 个有
- `ImpactImageBatchToImageList` —— 2/3 个有
- `Power Lora Loader (rgthree)` —— 2/3 个有
- `ShowText|pysssss` —— 2/3 个有
- `TTP_CoordinateSplitter` —— 2/3 个有
- `TTP_condsetarea_merge` —— 2/3 个有
- `TTP_condtobatch` —— 2/3 个有
- `ConditioningZeroOut` —— 1/3 个有
- `ImageSmartSharpen+` —— 1/3 个有
- `InjectLatentNoise+` —— 1/3 个有
- `KSamplerAdvanced //Inspire` —— 1/3 个有
- `RH_Captioner` —— 1/3 个有
- `TiledDiffusion` —— 1/3 个有
- `VAEDecode` —— 1/3 个有
- `easy imageBatchToImageList` —— 1/3 个有
- `easy imageListToImageBatch` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 1 | 100% |
| Prompt 约束强度(CFG) | 20 | - | 1 | 100% |
| 采样算法 | 1 | - | 1 | 100% |
| 调度器 | euler | - | 1 | 100% |
| 重绘幅度 | simple | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
