---
name: text_to_image_lora_sampler_clip_178
type: Text To Image
frequency: 7
level: moderate
coverage: 0.873286
common_nodes: [Any Switch (rgthree), CLIPLoader, CLIPTextEncode, CR Seed, CR Text, CheckpointLoaderSimple, ConditioningZeroOut, EmptyLatentImage, Flux2KleinEditTextEncode_EditUtils, GetImageSize, INTConstant, ImageScaleBy, KSampler, KSamplerAdvanced, LCSColorAnchor, LCSLoadData, LCSSharpnessCalibrate, LCSSharpnessIntervene, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleRestore V2, Lora Loader Stack (rgthree), MathExpression|pysssss, MemoryCleaner, PreviewImage, SaveImage, SimpleMath+, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, VAEDecode, VAELoader, easy imageBatchToImageList, easy imageColorMatch, easy imageListToImageBatch]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/白玉CCDV2_2067255929720102913.json, 图片生成/文生图/白玉CCD参考横屏四张_2065281329696174081.json, 图片生成/文生图/白玉CCD文生图-横屏四张_2065307512013934593.json, 图片生成/文生图/白玉CCD文生图-竖屏四张_2065314398050275330.json, 图片生成/文生图/豹豹喵呜制作：白玉AIO三采超高清写真生成_2059551581825228802.json, 图片生成/文生图/豹豹喵呜制作：白玉AIO三采超高清写真生成_2067766984112173057.json, 视频生成/文生视频/Engineer V6+白玉AIO三采文生图_2065288263987974146.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_178

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/白玉CCDV2_2067255929720102913.json、图片生成/文生图/白玉CCD参考横屏四张_2065281329696174081.json、图片生成/文生图/白玉CCD文生图-横屏四张_2065307512013934593.json、图片生成/文生图/白玉CCD文生图-竖屏四张_2065314398050275330.json、图片生成/文生图/豹豹喵呜制作：白玉AIO三采超高清写真生成_2059551581825228802.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 7 个 workflow 都包含：
- `Any Switch (rgthree)`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Seed`
- `CR Text`
- `CheckpointLoaderSimple`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `Flux2KleinEditTextEncode_EditUtils`
- `GetImageSize`
- `INTConstant`
- `ImageScaleBy`
- `KSampler`
- `KSamplerAdvanced`
- `LCSColorAnchor`
- `LCSLoadData`
- `LCSSharpnessCalibrate`
- `LCSSharpnessIntervene`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleRestore V2`
- `Lora Loader Stack (rgthree)`
- `MathExpression|pysssss`
- `MemoryCleaner`
- `PreviewImage`
- `SaveImage`
- `SimpleMath+`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy imageBatchToImageList`
- `easy imageColorMatch`
- `easy imageListToImageBatch`

**可变部分**（部分 workflow 才有）：
- `FloatConstant` —— 6/7 个有
- `LoadImage` —— 6/7 个有
- `LoraLoaderModelOnly` —— 6/7 个有
- `easy showAnything` —— 6/7 个有
- `llama_cpp_instruct_adv` —— 6/7 个有
- `llama_cpp_model_loader` —— 6/7 个有
- `ComfySwitchNode` —— 5/7 个有
- `Fast Groups Bypasser (rgthree)` —— 5/7 个有
- `easy boolean` —— 5/7 个有
- `RepeatLatentBatch` —— 4/7 个有
- `easy saveText` —— 4/7 个有
- `Int` —— 2/7 个有
- `CLIPLoaderGGUF` —— 1/7 个有
- `CR Prompt List` —— 1/7 个有
- `ImpactSwitch` —— 1/7 个有
- `String Literal` —— 1/7 个有
- `Text Concatenate (JPS)` —— 1/7 个有
- `easy positive` —— 1/7 个有
- `忽略多组孤海` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 6 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 8 | 7 | 0% |
| 采样算法 | res_2s | - | 7 | 86% |
| 调度器 | linear_quadratic | - | 7 | 86% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| 宽度 | 1888 | 1080 - 1888 | 7 | 84% |
| 高度 | 1080 | 1080 - 1920 | 7 | 76% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 14/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 8，7 个样本，取值分散，一致性仅 0%
- 采样算法 最常用 res_2s，7 个样本，一致性 86%
- 调度器 最常用 linear_quadratic，7 个样本，一致性 86%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 宽度 中位数 1888，观测区间 1080 - 1888，7 个样本，取值集中（一致性 84%）
- 高度 中位数 1080，观测区间 1080 - 1920，7 个样本
- 高发问题（14/7 个样本）：Steps较低可能导致细节不足
