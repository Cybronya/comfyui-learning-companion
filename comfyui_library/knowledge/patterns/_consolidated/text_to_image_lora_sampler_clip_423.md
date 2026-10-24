---
name: text_to_image_lora_sampler_clip_423
type: Text To Image
frequency: 4
level: weak
coverage: 0.9475
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, DisTorchPurgeVRAMV2, EmptyLatentImage, EmptySD3LatentImage, GetImageSize, INTConstant, KSampler, Krea2EditGroundedEncode, Krea2EditModelPatch, LayerMask: PersonMaskUltra V2, LayerUtility: CropByMask V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, LoadImage, LoraLoaderModelOnly, RHHiddenNodes, SaveImage, SeedVR2Conditioning, SeedVR2Preprocess, SimpleMath+, UNETLoader, VAEDecode, VAEDecodeTiled, VAEEncodeTiled, VAELoader, easy imageConcat, easy imageRemBg, 图像缩放V2_孤海]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/一键生成角色三视图加特写加全表情 Krea2人物资产图分镜图设定图 IP资产批量产出_2108972379169968129.json, 图片生成/文生图/Krea2人物角色设定图IP设计资产分镜特写图生图处理工具_2101722895599886338.json, 图片生成/文生图/Krea2人物角色设定图生成IP设计必备分镜三视图四视图特写图_2100638373655437314.json, 图片生成/文生图/人物角色设定图炸裂生成！IP设计必备！Krea2生成人物资产图分镜三视图四视图特写图可随机可自己写_2098405585346715649.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_423

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/一键生成角色三视图加特写加全表情 Krea2人物资产图分镜图设定图 IP资产批量产出_2108972379169968129.json、图片生成/文生图/Krea2人物角色设定图IP设计资产分镜特写图生图处理工具_2101722895599886338.json、图片生成/文生图/Krea2人物角色设定图生成IP设计必备分镜三视图四视图特写图_2100638373655437314.json、图片生成/文生图/人物角色设定图炸裂生成！IP设计必备！Krea2生成人物资产图分镜三视图四视图特写图可随机可自己写_2098405585346715649.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：95%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DisTorchPurgeVRAMV2`
- `EmptyLatentImage`
- `EmptySD3LatentImage`
- `GetImageSize`
- `INTConstant`
- `KSampler`
- `Krea2EditGroundedEncode`
- `Krea2EditModelPatch`
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
- `SimpleMath+`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAEEncodeTiled`
- `VAELoader`
- `easy imageConcat`
- `easy imageRemBg`
- `图像缩放V2_孤海`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 3/4 个有
- `CR Text Input Switch (4 way)` —— 3/4 个有
- `ColorMatchPro` —— 3/4 个有
- `Float` —— 3/4 个有
- `FluxKontextMultiReferenceLatentMethod` —— 3/4 个有
- `ImageUpscaleWithModel` —— 3/4 个有
- `Int` —— 3/4 个有
- `JjkText` —— 3/4 个有
- `Krea2OstrisEditModelPatch` —— 3/4 个有
- `Krea2T-Enhancer-Advanced` —— 3/4 个有
- `ShowText|pysssss` —— 3/4 个有
- `TextEncodeKrea2OstrisEdit` —— 3/4 个有
- `UpscaleModelLoader` —— 3/4 个有
- `llama_cpp_instruct_adv` —— 3/4 个有
- `llama_cpp_model_loader` —— 3/4 个有
- `llama_cpp_parameters` —— 3/4 个有
- `solarL_SaveImagesToZip` —— 3/4 个有
- `ttN text7BOX_concat` —— 3/4 个有
- `孤海注释` —— 3/4 个有
- `DapaoBatchImageGrid` —— 1/4 个有
- `DapaoImagePadDirectionNode` —— 1/4 个有
- `PainterFluxImageEdit` —— 1/4 个有
- `ShunjingAIShade` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 10 | 4 | 53% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 4.5 | 4 | 58% |
| 采样算法 | er_sde | - | 4 | 75% |
| 调度器 | beta | - | 4 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 80 | 80 - 1024 | 4 | 0% |
| 高度 | 80 | 80 - 1024 | 4 | 0% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 14/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 10，4 个样本
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 4.5，4 个样本
- 采样算法 最常用 er_sde，4 个样本，一致性 75%
- 调度器 最常用 beta，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 1024，4 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 1024，4 个样本，取值分散，一致性仅 0%
- 高发问题（14/4 个样本）：Steps较低可能导致细节不足
