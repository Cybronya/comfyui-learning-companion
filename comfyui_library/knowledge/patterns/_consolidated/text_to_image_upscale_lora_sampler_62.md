---
name: text_to_image_upscale_lora_sampler_62
type: Text To Image
frequency: 2
level: weak
coverage: 0.899
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text Concatenate, EmptyLatentImage, FastFilmGrain, GetImageSize+, ImageCASharpening+, ImageResize+, ImageScaleBy, KOOK_SaveJPGImage, KSampler, LayerColor: BrightnessContrastV2, LoraLoaderModelOnly, RunningHub Deepcleaner, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Zimage强化+瑶光+晓玉V3（文生图）_2042119298440765442.json, 图片生成/文生图/小姐姐名字：mzqr01。指定该角色 文生图（zimage turbo）_2040783114238173186.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_62

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/Zimage强化+瑶光+晓玉V3（文生图）_2042119298440765442.json、图片生成/文生图/小姐姐名字：mzqr01。指定该角色 文生图（zimage turbo）_2040783114238173186.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text Concatenate`
- `EmptyLatentImage`
- `FastFilmGrain`
- `GetImageSize+`
- `ImageCASharpening+`
- `ImageResize+`
- `ImageScaleBy`
- `KOOK_SaveJPGImage`
- `KSampler`
- `LayerColor: BrightnessContrastV2`
- `LoraLoaderModelOnly`
- `RunningHub Deepcleaner`
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
- `CR Text` —— 1/2 个有
- `CR Text Replace` —— 1/2 个有
- `JDCN_StringToList` —— 1/2 个有
- `MemoryCleaner` —— 1/2 个有
- `ModelSamplingAuraFlow` —— 1/2 个有
- `ProcessString` —— 1/2 个有
- `ShowText|pysssss` —— 1/2 个有
- `TTResolutionSelector` —— 1/2 个有
- `Text Multiline` —— 1/2 个有
- `llama_cpp_instruct_adv` —— 1/2 个有
- `llama_cpp_model_loader` —— 1/2 个有
- `llama_cpp_parameters` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1080 | - | 2 | 100% |
| 高度 | 1920 | - | 2 | 100% |
| 采样步数 | 8 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | res_2s | - | 2 | 100% |
| 调度器 | bong_tangent | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1080，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1920，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_2s，2 个样本，一致性 100%
- 调度器 最常用 bong_tangent，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
