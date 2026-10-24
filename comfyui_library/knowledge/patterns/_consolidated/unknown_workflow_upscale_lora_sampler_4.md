---
name: unknown_workflow_upscale_lora_sampler_4
type: Unknown Workflow
frequency: 19
level: moderate
coverage: 0.845737
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyFlux2LatentImage, Fast Groups Bypasser (rgthree), Flux2Scheduler, GetImageSize, ImageResize+, ImageScaleBy, ImageScaleToTotalPixels, KSamplerSelect, LayerUtility: PurgeVRAM, LoraLoaderModelOnly, PreviewImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy imageSize]
problems: []
missing: []
members: [图片生成/图生图/2026最强扩图_2076960103365959682.json, 图片生成/图生图/F.2 True V2洗图+极致真实V2+亿级像素超分放大_2062156616220368898.json, 图片生成/图生图/F.2_True_V2洗图+极致真实V2+亿级像素超分放大_2093243677400453121.json, 图片生成/图生图/F.2_True_V2洗图+极致真实V2+亿级像素超分放大_2093515288326266881.json, 图片生成/图生图/Flux-2-klein-9b扩图工作流_2077569891841961985.json, 图片生成/图生图/Flux-2-klein-9b扩图工作流_2077933705510875138.json, 图片生成/图生图/Flux2 True 洗图+极致真实V2+亿级像素超分放大_2064276916328292354.json, 图片生成/图生图/Posture Transfer Image+Cloning双采样极速洗图超分放大 迁移_2105094113954717698.json, 图片生成/图生图/双采姿态控制洗图+超分放大_2061967972838764546.json, 图片生成/图生图/双采样极速洗图优化版+超清放大_2061401774732439554.json, 图片生成/图生图/双采样极速洗图优化版+超清放大_2097168639156899841.json, 图片生成/图生图/双采样极速洗图优化版+超清放大_2097507812271284226.json, 图片生成/图生图/扩图工作流-Flux-2-klein-9b_2048637797162033154.json, 图片生成/图生图/极致真实V2+亿级像素超分放大_2092234608204144642.json, 图片生成/图生图/极致真实V2+亿级像素超分放大_2100155027561205761.json, 图片生成/文生图/79.Z-image二采生图+超分放大（极致清晰）_2096546420785500161.json, 图片生成/文生图/Krea2 文生图+三采+TTP高清_2100390063279529986.json, 图片生成/文生图/V2+放大_2064158687572348929.json, 数字人/数字人/Image Cloning双采样极速洗图超分放大_2097481053903605762.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_4

> 由 `engine/knowledge_consolidation` 从 19 个 workflow 归纳得出（图片生成/图生图/2026最强扩图_2076960103365959682.json、图片生成/图生图/F.2 True V2洗图+极致真实V2+亿级像素超分放大_2062156616220368898.json、图片生成/图生图/F.2_True_V2洗图+极致真实V2+亿级像素超分放大_2093243677400453121.json、图片生成/图生图/F.2_True_V2洗图+极致真实V2+亿级像素超分放大_2093515288326266881.json、图片生成/图生图/Flux-2-klein-9b扩图工作流_2077569891841961985.json…）

- **类型**：Unknown Workflow
- **样本数**：19
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 19 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `Fast Groups Bypasser (rgthree)`
- `Flux2Scheduler`
- `GetImageSize`
- `ImageResize+`
- `ImageScaleBy`
- `ImageScaleToTotalPixels`
- `KSamplerSelect`
- `LayerUtility: PurgeVRAM`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy imageSize`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 18/19 个有
- `Image Comparer (rgthree)` —— 16/19 个有
- `EmptyLatentImage` —— 15/19 个有
- `easy getNode` —— 15/19 个有
- `easy setNode` —— 15/19 个有
- `llama_cpp_instruct_adv` —— 15/19 个有
- `llama_cpp_model_loader` —— 15/19 个有
- `llama_cpp_parameters` —— 15/19 个有
- `Any Switch (rgthree)` —— 14/19 个有
- `ImageColorMatch+` —— 14/19 个有
- `easy showAnything` —— 14/19 个有
- `KSamplerAdvanced` —— 9/19 个有
- `ModelSamplingAuraFlow` —— 9/19 个有
- `CR Text` —— 8/19 个有
- `PrimitiveInt` —— 8/19 个有
- `AIO_Preprocessor` —— 6/19 个有
- `BasicGuider` —— 6/19 个有
- `FlowMatchEulerDiscreteScheduler (Custom)` —— 6/19 个有
- `GetImageSize+` —— 6/19 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 6/19 个有
- `ModelPatchLoader` —— 6/19 个有
- `ZImageFunControlnet` —— 6/19 个有
- `ColorMatch` —— 5/19 个有
- `DrawMaskOnImage` —— 4/19 个有
- `ImagePadForOutpaint` —— 4/19 个有
- `easy seed` —— 4/19 个有
- `ImageConcanate` —— 3/19 个有
- `easy cleanGpuUsed` —— 3/19 个有
- `Label (rgthree)` —— 2/19 个有
- `CR Prompt Text` —— 1/19 个有
- `EmptyImage` —— 1/19 个有
- `ImageSharpen` —— 1/19 个有
- `Int` —— 1/19 个有
- `LayerUtility: PurgeVRAM V2` —— 1/19 个有
- `PreviewAny` —— 1/19 个有
- `ResolutionSelector` —— 1/19 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 9 | 100% |
| Prompt 约束强度(CFG) | 40 | 3 - 40 | 9 | 68% |
| 采样算法 | 4 | 1 - 4 | 9 | 74% |
| 调度器 | res_multistep | - | 9 | 89% |
| 重绘幅度 | sgm_uniform | - | 9 | 89% |
| 宽度 | 864 | 512 - 864 | 15 | 75% |
| 高度 | 1536 | 512 - 1536 | 15 | 52% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，9 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 40，观测区间 3 - 40，9 个样本
- 采样算法 中位数 4，观测区间 1 - 4，9 个样本
- 调度器 最常用 res_multistep，9 个样本，一致性 89%
- 重绘幅度 最常用 sgm_uniform，9 个样本，一致性 89%
- 宽度 中位数 864，观测区间 512 - 864，15 个样本
- 高度 中位数 1536，观测区间 512 - 1536，15 个样本
- 风险：Prompt 约束强度(CFG) 观测到 40，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
