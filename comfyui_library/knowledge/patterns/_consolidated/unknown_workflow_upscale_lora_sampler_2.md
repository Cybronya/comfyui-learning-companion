---
name: unknown_workflow_upscale_lora_sampler_2
type: Unknown Workflow
frequency: 21
level: strong
coverage: 0.800143
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, GetImageSize+, INTConstant, ImageCASharpening+, ImageResize+, ImageScaleBy, KSamplerAdvanced, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SimpleMath+, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/KOOK_Qwen_2512+Zimage_真实人像_2008858245770776578.json, 图片生成/文生图/KOOK_Qwen_2512+Zimage_真实人像_2010269932264628226.json, 图片生成/文生图/KQ12Z真实人像-超绝美感文生图_2013823669788741633.json, 图片生成/文生图/KQ12Z真实人像-超绝美感文生图_2074657845320175618.json, 图片生成/文生图/KQ12Z真实人像-超绝美感文生图_2074692863551692802.json, 图片生成/文生图/KQ12Z真实人像-超绝美感文生图_2075470852719734785.json, 图片生成/文生图/KQ12Z真实人像-超绝美感文生图_2075817140413878274.json, 图片生成/文生图/KQ12Z真实人像-超绝美感文生图_2075837721544847361.json, 图片生成/文生图/KQ12Z真实人像-超绝美感文生图_2076191998444400642.json, 图片生成/文生图/KQ12Z真实人像-超绝美感文生图_2077040712000040961.json, 图片生成/文生图/KQ12Z真实人像-超绝美感文生图_2077437427169447937.json, 图片生成/文生图/KQ12Z真实人像-超绝美感文生图_2077632073862565890.json, 图片生成/文生图/KQ12Z真实人像-超绝美感文生图_2077644719638798338.json, 图片生成/文生图/KQ12Z真实人像-超绝美感文生图_2078125261467508738.json, 图片生成/文生图/KQ12Z真实人像-超绝美感文生图_2086075434315378689.json, 图片生成/文生图/KQ12Z真实人像-超绝美感文生图_2087086586902179841.json, 图片生成/文生图/Qwen2512+Zimage真实人像文生图_2009222406086336514.json, 图片生成/文生图/【Supermate 优化】Qwen2512与Z-image双剑合璧KOOK_真实人像_2009155316952342529.json, 图片生成/文生图/极致真实人像（qwen2512出图+Zimage细化+seedvr高清放大）_2020462495428775938.json, 图片生成/文生图/薯条-Qwen_2512+Zimage_真实人像_2012441118742417409.json, 图片生成/文生图/薯条-Qwen_2512+Zimage_真实人像_2013087422246035458.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_2

> 由 `engine/knowledge_consolidation` 从 21 个 workflow 归纳得出（图片生成/文生图/KOOK_Qwen_2512+Zimage_真实人像_2008858245770776578.json、图片生成/文生图/KOOK_Qwen_2512+Zimage_真实人像_2010269932264628226.json、图片生成/文生图/KQ12Z真实人像-超绝美感文生图_2013823669788741633.json、图片生成/文生图/KQ12Z真实人像-超绝美感文生图_2074657845320175618.json、图片生成/文生图/KQ12Z真实人像-超绝美感文生图_2074692863551692802.json…）

- **类型**：Unknown Workflow
- **样本数**：21
- **可信度**：强结论
- **平均知识覆盖**：80%

## 共有节点

全部 21 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `GetImageSize+`
- `INTConstant`
- `ImageCASharpening+`
- `ImageResize+`
- `ImageScaleBy`
- `KSamplerAdvanced`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SimpleMath+`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 20/21 个有
- `KOOK_SaveJPGImage` —— 20/21 个有
- `CR Text` —— 19/21 个有
- `RunningHub Deepcleaner` —— 19/21 个有
- `CR Text Concatenate` —— 15/21 个有
- `GetNode` —— 15/21 个有
- `LoadImage` —— 15/21 个有
- `SetNode` —— 15/21 个有
- `QwenMultiangleCameraNode` —— 14/21 个有
- `RHHiddenNodes` —— 14/21 个有
- `PreviewImage` —— 8/21 个有
- `Image Comparer (rgthree)` —— 3/21 个有
- `LatentFrequencyEnhancer_lrzjason` —— 2/21 个有
- `LayerUtility: PurgeVRAM V2` —— 2/21 个有
- `ShowText|pysssss` —— 2/21 个有
- `Text` —— 2/21 个有
- `llama_cpp_instruct_adv` —— 2/21 个有
- `llama_cpp_model_loader` —— 2/21 个有
- `llama_cpp_parameters` —— 2/21 个有
- `Any Switch (rgthree)` —— 1/21 个有
- `AspectRatio` —— 1/21 个有
- `DF_Get_image_size` —— 1/21 个有
- `Fast Groups Muter (rgthree)` —— 1/21 个有
- `ImageScaleToMaxDimension` —— 1/21 个有
- `Label (rgthree)` —— 1/21 个有
- `Text Concatenate` —— 1/21 个有
- `TextCombinerTwo` —— 1/21 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1080 | 512 - 1080 | 21 | 88% |
| 高度 | 1920 | 512 - 1920 | 21 | 81% |
| 采样步数 | randomize | - | 21 | 100% |
| Prompt 约束强度(CFG) | 8 | 8 - 10 | 21 | 90% |
| 采样算法 | 1 | 1 - 1 | 21 | 100% |
| 调度器 | res_2m | - | 21 | 90% |
| 重绘幅度 | sgm_uniform | - | 21 | 90% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1080，观测区间 512 - 1080，21 个样本，取值集中（一致性 88%）
- 高度 中位数 1920，观测区间 512 - 1920，21 个样本，取值集中（一致性 81%）
- 采样步数 最常用 randomize，21 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 8，观测区间 8 - 10，21 个样本，取值集中（一致性 90%）
- 采样算法 中位数 1，观测区间 1 - 1，21 个样本，取值集中（一致性 100%）
- 调度器 最常用 res_2m，21 个样本，一致性 90%
- 重绘幅度 最常用 sgm_uniform，21 个样本，一致性 90%
