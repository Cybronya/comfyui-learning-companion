---
name: unknown_workflow_upscale_lora_sampler_47
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.8
common_nodes: [Anything Everywhere3, CLIPLoader, CLIPTextEncode, ComfyUI-Krea2T-Enhancer, GetImageSize+, Image Comparer (rgthree), ImageResize+, ImageScaleBy, JoinStringMulti, KOOK_SaveJPGImage, KSamplerAdvanced, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, RunningHub Deepcleaner, SaveImage, Seed (rgthree), SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, ShowText|pysssss, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, VAEDecode, VAELoader, easy positive, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters, 忽略多组孤海]
problems: []
missing: []
members: [图片生成/图生图/K2-90SuYing-图生图，小红书洗图，抖音洗图_2101892401622245378.json, 图片生成/图生图/K2-最屌文生图-超强现实感-手机拍摄-90SuYing_2115233214133530625.json, 图片生成/图生图/K2-最屌文生图-超强现实感-手机拍摄-90SuYing_2115433218446020609.json, 图片生成/图生图/K2-最屌文生图-超强现实感-手机拍摄-90SuYing_2115658836358025218.json, 图片生成/文生图/K2-最屌文生图-超强现实感-手机拍摄-90SuYing_2103534090388590593.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_47

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/K2-90SuYing-图生图，小红书洗图，抖音洗图_2101892401622245378.json、图片生成/图生图/K2-最屌文生图-超强现实感-手机拍摄-90SuYing_2115233214133530625.json、图片生成/图生图/K2-最屌文生图-超强现实感-手机拍摄-90SuYing_2115433218446020609.json、图片生成/图生图/K2-最屌文生图-超强现实感-手机拍摄-90SuYing_2115658836358025218.json、图片生成/文生图/K2-最屌文生图-超强现实感-手机拍摄-90SuYing_2103534090388590593.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：80%

## 共有节点

全部 5 个 workflow 都包含：
- `Anything Everywhere3`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyUI-Krea2T-Enhancer`
- `GetImageSize+`
- `Image Comparer (rgthree)`
- `ImageResize+`
- `ImageScaleBy`
- `JoinStringMulti`
- `KOOK_SaveJPGImage`
- `KSamplerAdvanced`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `RunningHub Deepcleaner`
- `SaveImage`
- `Seed (rgthree)`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `ShowText|pysssss`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy positive`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`
- `忽略多组孤海`

**可变部分**（部分 workflow 才有）：
- `EmptyLatentImage` —— 4/5 个有
- `ResolutionSelector` —— 3/5 个有
- `easy boolean` —— 3/5 个有
- `easy ifElse` —— 3/5 个有
- `AddNoise` —— 1/5 个有
- `BasicScheduler` —— 1/5 个有
- `INTConstant` —— 1/5 个有
- `ImageScaleToTotalPixels` —— 1/5 个有
- `LatentUpscaleBy` —— 1/5 个有
- `LayerColor: AutoAdjustV2` —— 1/5 个有
- `LayerColor: Exposure` —— 1/5 个有
- `LayerFilter: SoftLight` —— 1/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/5 个有
- `PreviewImage` —— 1/5 个有
- `RandomNoise` —— 1/5 个有
- `VAEEncode` —— 1/5 个有
- `easy imageColorMatch` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 5 | 100% |
| Prompt 约束强度(CFG) | 9 | 9 - 9 | 5 | 100% |
| 采样算法 | 1 | 1 - 1 | 5 | 100% |
| 调度器 | euler_ancestral | - | 5 | 100% |
| 重绘幅度 | beta | - | 5 | 100% |
| 宽度 | 1440 | 1440 - 1440 | 4 | 100% |
| 高度 | 1920 | 1920 - 1920 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，5 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 9，观测区间 9 - 9，5 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler_ancestral，5 个样本，一致性 100%
- 重绘幅度 最常用 beta，5 个样本，一致性 100%
- 宽度 中位数 1440，观测区间 1440 - 1440，4 个样本，取值集中（一致性 100%）
- 高度 中位数 1920，观测区间 1920 - 1920，4 个样本，取值集中（一致性 100%）
