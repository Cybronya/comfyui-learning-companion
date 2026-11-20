---
name: unknown_workflow_upscale_lora_sampler_90
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.836
common_nodes: [Anything Everywhere3, CLIPLoader, CLIPTextEncode, ComfyUI-Krea2T-Enhancer, GetImageSize+, Image Comparer (rgthree), ImageResize+, ImageScaleBy, JoinStringMulti, KOOK_SaveJPGImage, KSamplerAdvanced, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, RunningHub Deepcleaner, SaveImage, Seed (rgthree), SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, ShowText|pysssss, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, VAEDecode, VAELoader, easy positive, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters, 忽略多组孤海]
problems: []
missing: []
members: [图片生成/图生图/K2-90SuYing-图生图，小红书洗图，抖音洗图_2101892401622245378.json, 图片生成/文生图/K2-最屌文生图-超强现实感-手机拍摄-90SuYing_2103534090388590593.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_90

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/K2-90SuYing-图生图，小红书洗图，抖音洗图_2101892401622245378.json、图片生成/文生图/K2-最屌文生图-超强现实感-手机拍摄-90SuYing_2103534090388590593.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：84%

## 共有节点

全部 2 个 workflow 都包含：
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
- `AddNoise` —— 1/2 个有
- `BasicScheduler` —— 1/2 个有
- `EmptyLatentImage` —— 1/2 个有
- `INTConstant` —— 1/2 个有
- `ImageScaleToTotalPixels` —— 1/2 个有
- `LatentUpscaleBy` —— 1/2 个有
- `LayerColor: AutoAdjustV2` —— 1/2 个有
- `LayerColor: Exposure` —— 1/2 个有
- `LayerFilter: SoftLight` —— 1/2 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `RandomNoise` —— 1/2 个有
- `VAEEncode` —— 1/2 个有
- `easy imageColorMatch` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 2 | 100% |
| Prompt 约束强度(CFG) | 9 | - | 2 | 100% |
| 采样算法 | 1 | - | 2 | 100% |
| 调度器 | euler_ancestral | - | 2 | 100% |
| 重绘幅度 | beta | - | 2 | 100% |
| 宽度 | 1440 | - | 1 | 100% |
| 高度 | 1920 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，2 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 9，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler_ancestral，2 个样本，一致性 100%
- 重绘幅度 最常用 beta，2 个样本，一致性 100%
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
