---
name: unknown_workflow_upscale_lora_sampler_122
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.752
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, GetImageSize+, INTConstant, Image Comparer (rgthree), ImageCASharpening+, ImageResize+, ImageScaleBy, KOOK_SaveJPGImage, KSamplerAdvanced, LayerUtility: PurgeVRAM V2, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, RunningHub Deepcleaner, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, ShowText|pysssss, SimpleMath+, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, Text, UNETLoader, VAEDecode, VAEEncode, VAELoader, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters]
problems: []
missing: []
members: [图片生成/文生图/薯条-Qwen_2512+Zimage_真实人像_2012441118742417409.json, 图片生成/文生图/薯条-Qwen_2512+Zimage_真实人像_2013087422246035458.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_122

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/薯条-Qwen_2512+Zimage_真实人像_2012441118742417409.json、图片生成/文生图/薯条-Qwen_2512+Zimage_真实人像_2013087422246035458.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：75%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `GetImageSize+`
- `INTConstant`
- `Image Comparer (rgthree)`
- `ImageCASharpening+`
- `ImageResize+`
- `ImageScaleBy`
- `KOOK_SaveJPGImage`
- `KSamplerAdvanced`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `RunningHub Deepcleaner`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `ShowText|pysssss`
- `SimpleMath+`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `Text`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`

**可变部分**（部分 workflow 才有）：
- `Any Switch (rgthree)` —— 1/2 个有
- `AspectRatio` —— 1/2 个有
- `DF_Get_image_size` —— 1/2 个有
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `Fast Groups Muter (rgthree)` —— 1/2 个有
- `GetNode` —— 1/2 个有
- `ImageScaleToMaxDimension` —— 1/2 个有
- `SetNode` —— 1/2 个有
- `Text Concatenate` —— 1/2 个有
- `TextCombinerTwo` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 2 | 100% |
| Prompt 约束强度(CFG) | 9 | - | 2 | 89% |
| 采样算法 | 1 | - | 2 | 100% |
| 调度器 | res_2m | - | 2 | 100% |
| 重绘幅度 | sgm_uniform | - | 2 | 100% |
| 宽度 | 768 | - | 2 | 67% |
| 高度 | 1024 | - | 2 | 50% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，2 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 9，样本不足，未给区间，2 个样本，取值集中（一致性 89%）
- 采样算法 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 最常用 res_2m，2 个样本，一致性 100%
- 重绘幅度 最常用 sgm_uniform，2 个样本，一致性 100%
- 宽度 中位数 768，样本不足，未给区间，2 个样本
- 高度 中位数 1024，样本不足，未给区间，2 个样本
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
