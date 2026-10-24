---
name: unknown_workflow_upscale_lora_sampler_7
type: Unknown Workflow
frequency: 17
level: strong
coverage: 0.796588
common_nodes: [CLIPLoader, CLIPTextEncode, Fast Groups Bypasser (rgthree), GetImageSize+, ImageCASharpening+, ImageResize+, ImageScaleBy, KSamplerAdvanced, LoraLoaderModelOnly, ModelSamplingAuraFlow, RunningHub Deepcleaner, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/KOOK_Qwen_2511_anything2real_动漫转真实_2010361622707052546.json, 图片生成/文生图/KOOK_Qwen_2512+Zimage_真实人像_2008858245770776578.json, 图片生成/文生图/KOOK_Qwen_2512+Zimage_真实人像_2010269932264628226.json, 图片生成/文生图/KQ12Z真实人像-超绝美感文生图_2013823669788741633.json, 图片生成/文生图/KQ12Z真实人像-超绝美感文生图_2074657845320175618.json, 图片生成/文生图/KQ12Z真实人像-超绝美感文生图_2074692863551692802.json, 图片生成/文生图/KQ12Z真实人像-超绝美感文生图_2075470852719734785.json, 图片生成/文生图/KQ12Z真实人像-超绝美感文生图_2075817140413878274.json, 图片生成/文生图/KQ12Z真实人像-超绝美感文生图_2075837721544847361.json, 图片生成/文生图/KQ12Z真实人像-超绝美感文生图_2076191998444400642.json, 图片生成/文生图/KQ12Z真实人像-超绝美感文生图_2077040712000040961.json, 图片生成/文生图/KQ12Z真实人像-超绝美感文生图_2077437427169447937.json, 图片生成/文生图/KQ12Z真实人像-超绝美感文生图_2077632073862565890.json, 图片生成/文生图/KQ12Z真实人像-超绝美感文生图_2077644719638798338.json, 图片生成/文生图/KQ12Z真实人像-超绝美感文生图_2078125261467508738.json, 图片生成/文生图/KQ12Z真实人像-超绝美感文生图_2086075434315378689.json, 图片生成/文生图/KQ12Z真实人像-超绝美感文生图_2087086586902179841.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_7

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（图片生成/图生图/KOOK_Qwen_2511_anything2real_动漫转真实_2010361622707052546.json、图片生成/文生图/KOOK_Qwen_2512+Zimage_真实人像_2008858245770776578.json、图片生成/文生图/KOOK_Qwen_2512+Zimage_真实人像_2010269932264628226.json、图片生成/文生图/KQ12Z真实人像-超绝美感文生图_2013823669788741633.json、图片生成/文生图/KQ12Z真实人像-超绝美感文生图_2074657845320175618.json…）

- **类型**：Unknown Workflow
- **样本数**：17
- **可信度**：强结论
- **平均知识覆盖**：80%

## 共有节点

全部 17 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `Fast Groups Bypasser (rgthree)`
- `GetImageSize+`
- `ImageCASharpening+`
- `ImageResize+`
- `ImageScaleBy`
- `KSamplerAdvanced`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
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
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 16/17 个有
- `EmptyLatentImage` —— 16/17 个有
- `INTConstant` —— 16/17 个有
- `KOOK_SaveJPGImage` —— 16/17 个有
- `SimpleMath+` —— 16/17 个有
- `CR Text Concatenate` —— 14/17 个有
- `GetNode` —— 14/17 个有
- `LoadImage` —— 14/17 个有
- `QwenMultiangleCameraNode` —— 14/17 个有
- `RHHiddenNodes` —— 14/17 个有
- `SetNode` —— 14/17 个有
- `PreviewImage` —— 4/17 个有
- `AddLabel` —— 1/17 个有
- `Bjornulf_FreeVRAM` —— 1/17 个有
- `ConditioningZeroOut` —— 1/17 个有
- `Image Comparer (rgthree)` —— 1/17 个有
- `ImageConcatMulti` —— 1/17 个有
- `PreviewAny` —— 1/17 个有
- `PrimitiveStringMultiline` —— 1/17 个有
- `RH_LLMAPI_NODE` —— 1/17 个有
- `TextEncodeQwenImageEditPlusAdvance_lrzjason` —— 1/17 个有
- `easy cleanGpuUsed` —— 1/17 个有
- `string_util_StrConcat` —— 1/17 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 17 | 100% |
| Prompt 约束强度(CFG) | 8 | 8 - 10 | 17 | 94% |
| 采样算法 | 1 | 1 - 1 | 17 | 100% |
| 调度器 | res_2m | - | 17 | 100% |
| 重绘幅度 | sgm_uniform | - | 17 | 100% |
| 宽度 | 1080 | 1024 - 1080 | 16 | 98% |
| 高度 | 1920 | 1536 - 1920 | 16 | 93% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，17 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 8，观测区间 8 - 10，17 个样本，取值集中（一致性 94%）
- 采样算法 中位数 1，观测区间 1 - 1，17 个样本，取值集中（一致性 100%）
- 调度器 最常用 res_2m，17 个样本，一致性 100%
- 重绘幅度 最常用 sgm_uniform，17 个样本，一致性 100%
- 宽度 中位数 1080，观测区间 1024 - 1080，16 个样本，取值集中（一致性 98%）
- 高度 中位数 1920，观测区间 1536 - 1920，16 个样本，取值集中（一致性 93%）
