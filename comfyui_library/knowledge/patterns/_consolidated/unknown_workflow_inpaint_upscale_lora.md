---
name: unknown_workflow_inpaint_upscale_lora
type: Unknown Workflow
frequency: 11
level: strong
coverage: 0.813091
common_nodes: [CLIPLoader, CLIPTextEncode, Easy_QwenEdit2509, Fast Groups Muter (rgthree), FluxKontextImageScale, Image Comparer (rgthree), ImageScaleRestore_UTK, InpaintModelConditioning, InvertMask, JDCN_StringToList, KSampler, KSamplerAdvanced, LayerMask: LoadSegmentAnythingModels, LayerMask: SegmentAnythingUltra V3, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, ProcessString, PurgeVRAM_UTK, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAELoader, easy int]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Cosplay任何角色 写真集  操作简单 效果炸裂_2030281063553044481.json, 图片生成/图生图/Cosplay任何角色 写真集  操作简单 效果炸裂_2033182117735178241.json, 图片生成/图生图/Cosplay任何角色+写真集（一张动漫角色参考图和模特图）_2028391084245655554.json, 图片生成/图生图/Cosplay任何角色+写真集（一张动漫角色参考图和模特图）_2028763464965033986.json, 图片生成/图生图/Cosplay任何角色（一张动漫角色参考图和模特图）_2028691099979620354.json, 图片生成/图生图/Cosplay换装+高清放大+写真集生成_2083144135560749057.json, 图片生成/图生图/真人Cosplay动漫角色+写真集_2052278858170290178.json, 图片生成/图生图/真人Cosplay动漫角色+写真集_2064877205381009410.json, 图片生成/图生图/真人Cosplay动漫角色+写真集_2064891194680897538.json, 图片生成/图生图/真人Cosplay动漫角色+写真集_2064898800380112897.json, 图片生成/图生图/真人Cosplay动漫角色+写真集_2065353159706497025.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_upscale_lora

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/Cosplay任何角色 写真集  操作简单 效果炸裂_2030281063553044481.json、图片生成/图生图/Cosplay任何角色 写真集  操作简单 效果炸裂_2033182117735178241.json、图片生成/图生图/Cosplay任何角色+写真集（一张动漫角色参考图和模特图）_2028391084245655554.json、图片生成/图生图/Cosplay任何角色+写真集（一张动漫角色参考图和模特图）_2028763464965033986.json、图片生成/图生图/Cosplay任何角色（一张动漫角色参考图和模特图）_2028691099979620354.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `Easy_QwenEdit2509`
- `Fast Groups Muter (rgthree)`
- `FluxKontextImageScale`
- `Image Comparer (rgthree)`
- `ImageScaleRestore_UTK`
- `InpaintModelConditioning`
- `InvertMask`
- `JDCN_StringToList`
- `KSampler`
- `KSamplerAdvanced`
- `LayerMask: LoadSegmentAnythingModels`
- `LayerMask: SegmentAnythingUltra V3`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `ProcessString`
- `PurgeVRAM_UTK`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `CFGNorm` —— 10/11 个有
- `CR Prompt Text` —— 10/11 个有
- `GetNode` —— 10/11 个有
- `LayerUtility: PurgeVRAM` —— 10/11 个有
- `RunningHub Deepcleaner` —— 10/11 个有
- `Seed (rgthree)` —— 10/11 个有
- `SetNode` —— 10/11 个有
- `Text Concatenate` —— 10/11 个有
- `Int` —— 1/11 个有
- `PreviewImage` —— 1/11 个有
- `TT_img_enc_v2` —— 1/11 个有
- `Text` —— 1/11 个有
- `TwoWaySwitch` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 11 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 11 | 100% |
| 采样算法 | res_2m | - | 11 | 100% |
| 调度器 | sgm_uniform | - | 11 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 22/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，11 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_2m，11 个样本，一致性 100%
- 调度器 最常用 sgm_uniform，11 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 高发问题（22/11 个样本）：Steps较低可能导致细节不足
