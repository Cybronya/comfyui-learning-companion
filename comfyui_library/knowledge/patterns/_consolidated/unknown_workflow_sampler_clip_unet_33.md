---
name: unknown_workflow_sampler_clip_unet_33
type: Unknown Workflow
frequency: 13
level: weak
coverage: 0.933615
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ColorMatch, ConditioningZeroOut, EmptyFlux2LatentImage, EmptyLatentImage, Flux2Scheduler, GetImageSize, ImageScaleToTotalPixels, KSamplerAdvanced, KSamplerSelect, ModelSamplingAuraFlow, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Krea2三采流-全自动文生图_2070323178886492161.json, 图片生成/文生图/Krea2三采流-全自动文生图全模式_2070336281514692609.json, 图片生成/文生图/Krea2三采流-全自动文生图全模式_2071434528807280641.json, 图片生成/文生图/Krea2三采流-全自动风格迁移_2070148898408198146.json, 图片生成/文生图/Krea2三采流-全自动风格迁移_2070376782905298945.json, 图片生成/文生图/Krea2三采流-全自动风格迁移_2082656076536836098.json, 图片生成/文生图/Krea2双采流+高清放大-全自动提示词文生图_2071838011926605825.json, 图片生成/文生图/Krea2文生图_三采_2074852704572239873.json, 图片生成/文生图/Krea2文生图美学感_风格化_2074430949265330178.json, 图片生成/文生图/Z-Image-超写实人像质感_2017821123303444482.json, 图片生成/文生图/全自动文生图Krea2_2101530861849104385.json, 图片生成/文生图/👾怪獸-国风角色设计👾_2058099509644840962.json, 视频生成/图生视频/2063550240493498369.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_33

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/文生图/Krea2三采流-全自动文生图_2070323178886492161.json、图片生成/文生图/Krea2三采流-全自动文生图全模式_2070336281514692609.json、图片生成/文生图/Krea2三采流-全自动文生图全模式_2071434528807280641.json、图片生成/文生图/Krea2三采流-全自动风格迁移_2070148898408198146.json、图片生成/文生图/Krea2三采流-全自动风格迁移_2070376782905298945.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：93%

## 共有节点

全部 13 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ColorMatch`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `EmptyLatentImage`
- `Flux2Scheduler`
- `GetImageSize`
- `ImageScaleToTotalPixels`
- `KSamplerAdvanced`
- `KSamplerSelect`
- `ModelSamplingAuraFlow`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageSharpen` —— 12/13 个有
- `LayerUtility: PurgeVRAM V2` —— 12/13 个有
- `Int` —— 11/13 个有
- `INTConstant` —— 10/13 个有
- `PreviewImage` —— 10/13 个有
- `CR Prompt Text` —— 9/13 个有
- `PreviewAny` —— 9/13 个有
- `llama_cpp_instruct_adv` —— 9/13 个有
- `llama_cpp_model_loader` —— 9/13 个有
- `llama_cpp_parameters` —— 8/13 个有
- `LoadImage` —— 5/13 个有
- `Image Comparer (rgthree)` —— 4/13 个有
- `easy showAnything` —— 4/13 个有
- `CR Text` —— 3/13 个有
- `LoraLoaderModelOnly` —— 3/13 个有
- `Fast Groups Bypasser (rgthree)` —— 2/13 个有
- `RH_LLMAPI_Pro_Node` —— 2/13 个有
- `SeedVR2LoadDiTModel` —— 2/13 个有
- `SeedVR2LoadVAEModel` —— 2/13 个有
- `SeedVR2VideoUpscaler` —— 2/13 个有
- `Any Switch (rgthree)` —— 1/13 个有
- `CR Text Concatenate` —— 1/13 个有
- `LayerUtility: PurgeVRAM` —— 1/13 个有
- `PrimitiveInt` —— 1/13 个有
- `PrimitiveStringMultiline` —— 1/13 个有
- `ProcessString` —— 1/13 个有
- `RH_Captioner` —— 1/13 个有
- `TTResolutionSelector` —— 1/13 个有
- `easy getNode` —— 1/13 个有
- `easy promptLine` —— 1/13 个有
- `easy setNode` —— 1/13 个有
- `孤海注释` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 512 - 1024 | 13 | 86% |
| 高度 | 1536 | 512 - 1536 | 13 | 81% |
| 采样步数 | randomize | - | 13 | 92% |
| Prompt 约束强度(CFG) | 3 | 3 - 40 | 13 | 0% |
| 采样算法 | 2 | 1 - 4 | 13 | 66% |
| 调度器 | euler | - | 13 | 92% |
| 重绘幅度 | simple | - | 13 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 512 - 1024，13 个样本，取值集中（一致性 86%）
- 高度 中位数 1536，观测区间 512 - 1536，13 个样本，取值集中（一致性 81%）
- 采样步数 最常用 randomize，13 个样本，一致性 92%
- Prompt 约束强度(CFG) 中位数 3，观测区间 3 - 40，13 个样本，取值分散，一致性仅 0%
- 采样算法 中位数 2，观测区间 1 - 4，13 个样本
- 调度器 最常用 euler，13 个样本，一致性 92%
- 重绘幅度 最常用 simple，13 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 40，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
