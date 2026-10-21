---
name: unknown_workflow_upscale_lora_sampler_30
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.723333
common_nodes: [Anything Everywhere3, CLIPTextEncode, CR Prompt Text, CheckpointLoaderSimple, DuckDecodeNode, DuckHideNode, Fast Groups Bypasser (rgthree), GetImageSize+, Image Comparer (rgthree), Image Tiled, ImageConcanate, ImageFromBatch, ImageResize+, ImageScaleBy, ImageScaleToTotalPixels, ImageUpscaleWithModel, KSamplerAdvanced, LoadImage, LoraLoaderModelOnly, PreviewImage, QwenImageLatentAspectRatio, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, TwoWaySwitch, UltimateSDUpscaleNoUpscale, UpscaleModelLoader, VAEDecode, easy cleanGpuUsed, easy showAnything]
problems: []
missing: []
members: [图片生成/文生图/文生图，图生图。影楼级别皮肤细化 4K 8K_2007805496383774722.json, 图片生成/文生图/文生图，图生图。影楼级别皮肤细化 4K 8K_2058765912265805825.json, 图片生成/文生图/文生图，图生图。最强皮肤质感，8K影楼级别，感谢蓝神_2013623446646820865.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_30

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/文生图，图生图。影楼级别皮肤细化 4K 8K_2007805496383774722.json、图片生成/文生图/文生图，图生图。影楼级别皮肤细化 4K 8K_2058765912265805825.json、图片生成/文生图/文生图，图生图。最强皮肤质感，8K影楼级别，感谢蓝神_2013623446646820865.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：72%

## 共有节点

全部 3 个 workflow 都包含：
- `Anything Everywhere3`
- `CLIPTextEncode`
- `CR Prompt Text`
- `CheckpointLoaderSimple`
- `DuckDecodeNode`
- `DuckHideNode`
- `Fast Groups Bypasser (rgthree)`
- `GetImageSize+`
- `Image Comparer (rgthree)`
- `Image Tiled`
- `ImageConcanate`
- `ImageFromBatch`
- `ImageResize+`
- `ImageScaleBy`
- `ImageScaleToTotalPixels`
- `ImageUpscaleWithModel`
- `KSamplerAdvanced`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `QwenImageLatentAspectRatio`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `TwoWaySwitch`
- `UltimateSDUpscaleNoUpscale`
- `UpscaleModelLoader`
- `VAEDecode`
- `easy cleanGpuUsed`
- `easy showAnything`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 3 | 100% |
| Prompt 约束强度(CFG) | 9 | 9 - 9 | 3 | 100% |
| 采样算法 | 1 | 1 - 1 | 3 | 100% |
| 调度器 | euler | - | 3 | 100% |
| 重绘幅度 | ddim_uniform | - | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，3 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 9，观测区间 9 - 9，3 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，3 个样本，一致性 100%
- 重绘幅度 最常用 ddim_uniform，3 个样本，一致性 100%
