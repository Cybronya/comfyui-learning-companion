---
name: text_to_image_upscale_lora_sampler_27
type: Text To Image
frequency: 8
level: strong
coverage: 0.86075
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, GetImageSize+, ImageResize+, ImageScaleBy, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, VAEDecode, VAELoader, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/001.Z-image生图巅峰022.强力洗图+真实+放大_2039695908341813250.json, 图片生成/图生图/Z-image强力洗图+真实+放大_2071979947425615873.json, 图片生成/图生图/Z-极致真实-瑶光图生图-放大工作流_2042410624730271745.json, 图片生成/图生图/z-image强力洗图+结构化提示词强化版_2038949040838152193.json, 图片生成/图生图/z-image强力洗图+结构化提示词强化版【纯本地版】_2038809554556817409.json, 图片生成/图生图/z-image最强洗图+结构化提示词强化版_2038962245627023362.json, 图片生成/图生图/z-image最强洗图+结构化提示词强化版_2039316116807360514.json, 图片生成/文生图/CommintAI：ZIB+Kook_瑶光LoRA_2035232923888132098.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_27

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/001.Z-image生图巅峰022.强力洗图+真实+放大_2039695908341813250.json、图片生成/图生图/Z-image强力洗图+真实+放大_2071979947425615873.json、图片生成/图生图/Z-极致真实-瑶光图生图-放大工作流_2042410624730271745.json、图片生成/图生图/z-image强力洗图+结构化提示词强化版_2038949040838152193.json、图片生成/图生图/z-image强力洗图+结构化提示词强化版【纯本地版】_2038809554556817409.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `GetImageSize+`
- `ImageResize+`
- `ImageScaleBy`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
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
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `AIO_Preprocessor` —— 6/8 个有
- `ColorCorrectOfUtils` —— 6/8 个有
- `DapaoImageAspectRatioResizeNode` —— 6/8 个有
- `DapaoImageCompressionNode` —— 6/8 个有
- `DapaoPromptBrakeNode` —— 6/8 个有
- `Image Comparer (rgthree)` —— 6/8 个有
- `ImageUpscaleWithModel` —— 6/8 个有
- `LayerFilter: FilmV2` —— 6/8 个有
- `LayerUtility: PurgeVRAM` —— 6/8 个有
- `PreviewImage` —— 6/8 个有
- `UpscaleModelLoader` —— 6/8 个有
- `RH_LLMAPI_Pro_Node` —— 4/8 个有
- `llama_cpp_instruct_adv` —— 4/8 个有
- `llama_cpp_model_loader` —— 4/8 个有
- `llama_cpp_parameters` —— 4/8 个有
- `Fast Groups Bypasser (rgthree)` —— 3/8 个有
- `FastFilmGrain` —— 2/8 个有
- `ImageCASharpening+` —— 2/8 个有
- `LayerColor: BrightnessContrastV2` —— 2/8 个有
- `RunningHub Deepcleaner` —— 2/8 个有
- `JjkText` —— 1/8 个有
- `MuyeSizeSelector` —— 1/8 个有
- `Note Plus (mtb)` —— 1/8 个有
- `Qwen3_VQA` —— 1/8 个有
- `ShowText|pysssss` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1080 | 1080 - 1080 | 8 | 100% |
| 高度 | 1920 | 1920 - 1920 | 8 | 100% |
| 采样步数 | 8 | 8 - 8 | 8 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | res_2s | - | 8 | 100% |
| 调度器 | bong_tangent | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1080，观测区间 1080 - 1080，8 个样本，取值集中（一致性 100%）
- 高度 中位数 1920，观测区间 1920 - 1920，8 个样本，取值集中（一致性 100%）
- 采样步数 中位数 8，观测区间 8 - 8，8 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_2s，8 个样本，一致性 100%
- 调度器 最常用 bong_tangent，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 高发问题（8/8 个样本）：Steps较低可能导致细节不足
