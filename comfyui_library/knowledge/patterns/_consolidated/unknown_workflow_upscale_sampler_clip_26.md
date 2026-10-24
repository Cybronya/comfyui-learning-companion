---
name: unknown_workflow_upscale_sampler_clip_26
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.835333
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, Fast Groups Bypasser (rgthree), GetImageSize+, Image Comparer (rgthree), ImageResize+, ImageScaleBy, KSamplerAdvanced, PrimitiveStringMultiline, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/VividMuse Z-Image + Z-Image-Turbo realistic photography V3_2051592508924276737.json, 图片生成/文生图/VividMuse Z-Image-Turbo ControlNet_2051502577258377217.json, 图片生成/文生图/VividMuse Z-Image-Turbo-Melancholy_2048012453967040514.json, 图片生成/文生图/VividMuse Z-Image-Turbo-PurpleDreams_2046563756121006081.json, 图片生成/文生图/VividMuse Z-Image真实人像工作流V4_2078129234219982850.json, 图片生成/文生图/Z-Image-真实人像高清出图_2083208404511846401.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_sampler_clip_26

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/VividMuse Z-Image + Z-Image-Turbo realistic photography V3_2051592508924276737.json、图片生成/文生图/VividMuse Z-Image-Turbo ControlNet_2051502577258377217.json、图片生成/文生图/VividMuse Z-Image-Turbo-Melancholy_2048012453967040514.json、图片生成/文生图/VividMuse Z-Image-Turbo-PurpleDreams_2046563756121006081.json、图片生成/文生图/VividMuse Z-Image真实人像工作流V4_2078129234219982850.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `GetImageSize+`
- `Image Comparer (rgthree)`
- `ImageResize+`
- `ImageScaleBy`
- `KSamplerAdvanced`
- `PrimitiveStringMultiline`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 5/6 个有
- `Seed (rgthree)` —— 5/6 个有
- `easy promptList` —— 5/6 个有
- `LoraLoaderModelOnly` —— 4/6 个有
- `AIO_Preprocessor` —— 3/6 个有
- `LoadImage` —— 3/6 个有
- `ModelPatchLoader` —— 3/6 个有
- `QwenImageDiffsynthControlnet` —— 3/6 个有
- `easy imageRemBg` —— 3/6 个有
- `ComfySwitchNode` —— 2/6 个有
- `Flux2Scheduler` —— 2/6 个有
- `KSamplerSelect` —— 2/6 个有
- `MuterSwitcher` —— 2/6 个有
- `PrimitiveBoolean` —— 2/6 个有
- `ReferenceLatent` —— 2/6 个有
- `ResolutionSelector` —— 2/6 个有
- `SamplerCustom` —— 2/6 个有
- `Switch string [Crystools]` —— 2/6 个有
- `VAEEncode` —— 2/6 个有
- `easy loraStack` —— 2/6 个有
- `easy loraStackApply` —— 2/6 个有
- `easy showAnything` —— 2/6 个有
- `llama_cpp_instruct_adv` —— 2/6 个有
- `llama_cpp_model_loader` —— 2/6 个有
- `LayerColor: ColorAdapter` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 6 | 100% |
| Prompt 约束强度(CFG) | 8 | 8 - 10 | 6 | 89% |
| 采样算法 | 1 | 1 - 1 | 6 | 100% |
| 调度器 | euler_ancestral | - | 6 | 67% |
| 重绘幅度 | beta57 | - | 6 | 67% |
| 宽度 | 1536 | 512 - 1536 | 6 | 60% |
| 高度 | 2048 | 512 - 2048 | 6 | 53% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，6 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 8，观测区间 8 - 10，6 个样本，取值集中（一致性 89%）
- 采样算法 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler_ancestral，6 个样本，一致性 67%
- 重绘幅度 最常用 beta57，6 个样本，一致性 67%
- 宽度 中位数 1536，观测区间 512 - 1536，6 个样本
- 高度 中位数 2048，观测区间 512 - 2048，6 个样本
