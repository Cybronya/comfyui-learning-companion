---
name: text_to_image_upscale_lora_sampler_15
type: Text To Image
frequency: 6
level: strong
coverage: 0.821
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, GetImageSize+, ImageResize+, ImageScaleBy, KOOK_ImageCompression, KSampler, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, VAEDecode, VAELoader, easy float, easy seed, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen-2512 智能真实人像（8k）_2008818052183363585.json, 图片生成/文生图/Qwen-2512 真实人像洗图（8k）_2014237098886307842.json, 图片生成/文生图/Qwen-2512真实人像8K在线_2007642592116215810.json, 图片生成/文生图/Z-Image在线8K_2001940872809836545.json, 图片生成/文生图/Z-Image极致真实图像反推洗图8K版_2003077062523068417.json, 图片生成/文生图/Z-Image直出8K_2016392283901403138.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_15

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/Qwen-2512 智能真实人像（8k）_2008818052183363585.json、图片生成/文生图/Qwen-2512 真实人像洗图（8k）_2014237098886307842.json、图片生成/文生图/Qwen-2512真实人像8K在线_2007642592116215810.json、图片生成/文生图/Z-Image在线8K_2001940872809836545.json、图片生成/文生图/Z-Image极致真实图像反推洗图8K版_2003077062523068417.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `GetImageSize+`
- `ImageResize+`
- `ImageScaleBy`
- `KOOK_ImageCompression`
- `KSampler`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
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
- `easy float`
- `easy seed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/6 个有
- `LoadImage` —— 4/6 个有
- `VAEEncode` —— 4/6 个有
- `Any Switch (rgthree)` —— 3/6 个有
- `DuckHideNode` —— 3/6 个有
- `HFEPostProcessor (lrzjason)` —— 3/6 个有
- `LatentFrequencyEnhancer_lrzjason` —— 3/6 个有
- `easy cleanGpuUsed` —— 3/6 个有
- `AILab_QwenVL` —— 2/6 个有
- `CR Text` —— 2/6 个有
- `Fast Groups Bypasser (rgthree)` —— 2/6 个有
- `PreviewImage` —— 2/6 个有
- `RH_LLMAPI_Pro_Node` —— 2/6 个有
- `Text Multiline` —— 2/6 个有
- `Image Comparer (rgthree)` —— 1/6 个有
- `LayerUtility: ImageReel` —— 1/6 个有
- `LayerUtility: ImageReelComposit` —— 1/6 个有
- `Qwen3_VQA` —— 1/6 个有
- `ShowText|pysssss` —— 1/6 个有
- `TextInput_` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 6 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | res_2s | - | 6 | 50% |
| 调度器 | ddim_uniform | - | 6 | 50% |
| 重绘幅度 | 1 | 0.55 - 1 | 6 | 82% |
| 宽度 | 1080 | 1080 - 1080 | 6 | 100% |
| 高度 | 1920 | 1920 - 1920 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_2s，6 个样本，一致性 50%
- 调度器 最常用 ddim_uniform，6 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 0.55 - 1，6 个样本，取值集中（一致性 82%）
- 宽度 中位数 1080，观测区间 1080 - 1080，6 个样本，取值集中（一致性 100%）
- 高度 中位数 1920，观测区间 1920 - 1920，6 个样本，取值集中（一致性 100%）
- 高发问题（6/6 个样本）：Steps较低可能导致细节不足
