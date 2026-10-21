---
name: unknown_workflow_upscale_lora_sampler_4
type: Unknown Workflow
frequency: 12
level: moderate
coverage: 0.853333
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyFlux2LatentImage, EmptyLatentImage, Fast Groups Bypasser (rgthree), Flux2Scheduler, GetImageSize, Image Comparer (rgthree), ImageScaleToTotalPixels, KSamplerSelect, LayerUtility: PurgeVRAM, LoraLoaderModelOnly, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy getNode, easy setNode, llama_cpp_instruct_adv, llama_cpp_model_loader]
problems: []
missing: []
members: [图片生成/文生图/79.Z-image二采生图+超分放大（极致清晰）_2096546420785500161.json, 图片生成/文生图/Krea2 文生图+三采+TTP高清_2100390063279529986.json, 图片生成/文生图/V2+放大_2064158687572348929.json, 图片生成/文生图/Z-image Base & Turbo+Klein三重采样文生图_2063539477594857474.json, 图片生成/文生图/ZIT情绪高清文生图-AIGC大赏_2059815473482657794.json, 图片生成/文生图/去AI感高清人像（3采样+超分放大）_2086099313301737473.json, 图片生成/文生图/提示词自动优化+极致真实V2+亿级像素超分放大_2090073751546318849.json, 图片生成/文生图/最强大模型组合：极致高清人像生成+3次采样+超分放大（去AI感）_2070673952455880706.json, 图片生成/文生图/最强大模型组合：极致高清人像生成+3次采样+超分放大（去AI感）图片反推_2071793609908772865.json, 图片生成/文生图/极致真实V2+亿级像素超分放大-QM_2091885341887254529.json, 图片生成/文生图/极致真实V2+亿级像素超分放大_2059627101044695042.json, 数字人/数字人/Image Cloning双采样极速洗图超分放大_2097481053903605762.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_4

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/文生图/79.Z-image二采生图+超分放大（极致清晰）_2096546420785500161.json、图片生成/文生图/Krea2 文生图+三采+TTP高清_2100390063279529986.json、图片生成/文生图/V2+放大_2064158687572348929.json、图片生成/文生图/Z-image Base & Turbo+Klein三重采样文生图_2063539477594857474.json、图片生成/文生图/ZIT情绪高清文生图-AIGC大赏_2059815473482657794.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 12 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `Flux2Scheduler`
- `GetImageSize`
- `Image Comparer (rgthree)`
- `ImageScaleToTotalPixels`
- `KSamplerSelect`
- `LayerUtility: PurgeVRAM`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy getNode`
- `easy setNode`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`

**可变部分**（部分 workflow 才有）：
- `ImageResize+` —— 11/12 个有
- `ImageScaleBy` —— 11/12 个有
- `KSamplerAdvanced` —— 11/12 个有
- `PreviewImage` —— 11/12 个有
- `SaveImage` —— 11/12 个有
- `TTP_Image_Assy` —— 11/12 个有
- `TTP_Image_Tile_Batch` —— 11/12 个有
- `TTP_Tile_image_size` —— 11/12 个有
- `easy imageSize` —— 11/12 个有
- `easy showAnything` —— 11/12 个有
- `llama_cpp_parameters` —— 11/12 个有
- `CR Text` —— 10/12 个有
- `ImageColorMatch+` —— 10/12 个有
- `ModelSamplingAuraFlow` —— 10/12 个有
- `Any Switch (rgthree)` —— 9/12 个有
- `LoadImage` —— 9/12 个有
- `PrimitiveInt` —— 9/12 个有
- `Label (rgthree)` —— 4/12 个有
- `ColorMatch` —— 2/12 个有
- `AIO_Preprocessor` —— 1/12 个有
- `BasicGuider` —— 1/12 个有
- `CR Prompt Text` —— 1/12 个有
- `CompressImages` —— 1/12 个有
- `FlowMatchEulerDiscreteScheduler (Custom)` —— 1/12 个有
- `GetImageSize+` —— 1/12 个有
- `ImageSharpen` —— 1/12 个有
- `Int` —— 1/12 个有
- `JindouyunShowAnything` —— 1/12 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/12 个有
- `LayerUtility: PurgeVRAM V2` —— 1/12 个有
- `ModelPatchLoader` —— 1/12 个有
- `PreviewAny` —— 1/12 个有
- `ResolutionSelector` —— 1/12 个有
- `ZImageFunControlnet` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 11 | 100% |
| Prompt 约束强度(CFG) | 40 | 3 - 40 | 11 | 62% |
| 采样算法 | 4 | 1 - 4 | 11 | 67% |
| 调度器 | res_multistep | - | 11 | 82% |
| 重绘幅度 | sgm_uniform | - | 11 | 82% |
| 宽度 | 864 | 512 - 864 | 12 | 84% |
| 高度 | 1536 | 512 - 1536 | 12 | 72% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，11 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 40，观测区间 3 - 40，11 个样本
- 采样算法 中位数 4，观测区间 1 - 4，11 个样本
- 调度器 最常用 res_multistep，11 个样本，一致性 82%
- 重绘幅度 最常用 sgm_uniform，11 个样本，一致性 82%
- 宽度 中位数 864，观测区间 512 - 864，12 个样本，取值集中（一致性 84%）
- 高度 中位数 1536，观测区间 512 - 1536，12 个样本
- 风险：Prompt 约束强度(CFG) 观测到 40，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
