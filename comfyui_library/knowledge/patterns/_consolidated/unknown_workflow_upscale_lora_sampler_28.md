---
name: unknown_workflow_upscale_lora_sampler_28
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.729714
common_nodes: [Anything Everywhere3, CLIPTextEncode, CR Prompt Text, CheckpointLoaderSimple, DuckDecodeNode, DuckHideNode, Fast Groups Bypasser (rgthree), GetImageSize+, Image Comparer (rgthree), Image Tiled, ImageConcanate, ImageFromBatch, ImageResize+, ImageScaleBy, ImageScaleToTotalPixels, ImageUpscaleWithModel, KSamplerAdvanced, LoadImage, LoraLoaderModelOnly, PreviewImage, QwenImageLatentAspectRatio, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, TwoWaySwitch, UltimateSDUpscaleNoUpscale, UpscaleModelLoader, VAEDecode, easy cleanGpuUsed, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/文生图  快速生成_2048948949922357250.json, 图片生成/文生图/文生图青花瓷小唐风_2047280664713633793.json, 图片生成/文生图/文生图，图生图。影楼级别皮肤细化 4K 8K_2007805496383774722.json, 图片生成/文生图/文生图，图生图。影楼级别皮肤细化 4K 8K_2058765912265805825.json, 图片生成/文生图/文生图，图生图。最强皮肤质感，8K影楼级别，感谢蓝神_2013623446646820865.json, 图片生成/文生图/文生图，大唐文成公主_2047144389541105665.json, 图片生成/文生图/自用_2046532042887794690.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_28

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/文生图  快速生成_2048948949922357250.json、图片生成/文生图/文生图青花瓷小唐风_2047280664713633793.json、图片生成/文生图/文生图，图生图。影楼级别皮肤细化 4K 8K_2007805496383774722.json、图片生成/文生图/文生图，图生图。影楼级别皮肤细化 4K 8K_2058765912265805825.json、图片生成/文生图/文生图，图生图。最强皮肤质感，8K影楼级别，感谢蓝神_2013623446646820865.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：73%

## 共有节点

全部 7 个 workflow 都包含：
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

**可变部分**（部分 workflow 才有）：
- `CompressImages` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 7 | 100% |
| Prompt 约束强度(CFG) | 9 | 9 - 9 | 7 | 100% |
| 采样算法 | 1 | 1 - 1 | 7 | 100% |
| 调度器 | euler | - | 7 | 100% |
| 重绘幅度 | ddim_uniform | - | 7 | 86% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，7 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 9，观测区间 9 - 9，7 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，7 个样本，一致性 100%
- 重绘幅度 最常用 ddim_uniform，7 个样本，一致性 86%
