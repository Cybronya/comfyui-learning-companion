---
name: text_to_image_upscale_lora_sampler_37
type: Text To Image
frequency: 3
level: weak
coverage: 0.949667
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text, CR Text Input Switch (4 way), ColorMatchPro, ConditioningZeroOut, DisTorchPurgeVRAMV2, EmptyLatentImage, EmptySD3LatentImage, Float, FluxKontextMultiReferenceLatentMethod, GetImageSize, INTConstant, ImageUpscaleWithModel, Int, KSampler, Krea2EditGroundedEncode, Krea2EditModelPatch, Krea2OstrisEditModelPatch, Krea2T-Enhancer-Advanced, LayerMask: PersonMaskUltra V2, LayerUtility: CropByMask V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, LoadImage, LoraLoaderModelOnly, RHHiddenNodes, SaveImage, SeedVR2Conditioning, SeedVR2Preprocess, ShowText|pysssss, SimpleMath+, TextEncodeKrea2OstrisEdit, UNETLoader, UpscaleModelLoader, VAEDecode, VAEDecodeTiled, VAEEncodeTiled, VAELoader, easy imageConcat, easy imageRemBg, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters, ttN text7BOX_concat, 图像缩放V2_孤海]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Krea2人物角色设定图IP设计资产分镜特写图生图处理工具_2101722895599886338.json, 图片生成/文生图/Krea2人物角色设定图生成IP设计必备分镜三视图四视图特写图_2100638373655437314.json, 图片生成/文生图/人物角色设定图炸裂生成！IP设计必备！Krea2生成人物资产图分镜三视图四视图特写图可随机可自己写_2098405585346715649.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_37

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Krea2人物角色设定图IP设计资产分镜特写图生图处理工具_2101722895599886338.json、图片生成/文生图/Krea2人物角色设定图生成IP设计必备分镜三视图四视图特写图_2100638373655437314.json、图片生成/文生图/人物角色设定图炸裂生成！IP设计必备！Krea2生成人物资产图分镜三视图四视图特写图可随机可自己写_2098405585346715649.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：95%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `CR Text Input Switch (4 way)`
- `ColorMatchPro`
- `ConditioningZeroOut`
- `DisTorchPurgeVRAMV2`
- `EmptyLatentImage`
- `EmptySD3LatentImage`
- `Float`
- `FluxKontextMultiReferenceLatentMethod`
- `GetImageSize`
- `INTConstant`
- `ImageUpscaleWithModel`
- `Int`
- `KSampler`
- `Krea2EditGroundedEncode`
- `Krea2EditModelPatch`
- `Krea2OstrisEditModelPatch`
- `Krea2T-Enhancer-Advanced`
- `LayerMask: PersonMaskUltra V2`
- `LayerUtility: CropByMask V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `RHHiddenNodes`
- `SaveImage`
- `SeedVR2Conditioning`
- `SeedVR2Preprocess`
- `ShowText|pysssss`
- `SimpleMath+`
- `TextEncodeKrea2OstrisEdit`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAEEncodeTiled`
- `VAELoader`
- `easy imageConcat`
- `easy imageRemBg`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`
- `ttN text7BOX_concat`
- `图像缩放V2_孤海`

**可变部分**（部分 workflow 才有）：
- `JjkText` —— 2/3 个有
- `solarL_SaveImagesToZip` —— 2/3 个有
- `孤海注释` —— 2/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 10 | 3 | 53% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 4.5 | 3 | 51% |
| 采样算法 | er_sde | - | 3 | 67% |
| 调度器 | beta | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 80 | 80 - 1024 | 3 | 0% |
| 高度 | 80 | 80 - 1024 | 3 | 0% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 10，3 个样本
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 4.5，3 个样本
- 采样算法 最常用 er_sde，3 个样本，一致性 67%
- 调度器 最常用 beta，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 1024，3 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 1024，3 个样本，取值分散，一致性仅 0%
- 高发问题（11/3 个样本）：Steps较低可能导致细节不足
