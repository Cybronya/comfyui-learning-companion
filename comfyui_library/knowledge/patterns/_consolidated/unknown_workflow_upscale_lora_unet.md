---
name: unknown_workflow_upscale_lora_unet
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.924545
common_nodes: [CLIPLoader, GetImageSize, GrowMaskWithBlur, LayerFilter: FilmV2, LayerMask: PersonMaskUltra V2, LayerUtility: CropByMask V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, LayerUtility: RestoreCropBox, LoadImage, LoraLoaderModelOnly, PrimitiveInt, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAELoader, ZML_ImageSelectorNode, easy imageConcat, easy imageRemBg]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/FluxKlein换背景场景+换装+换头可选_2073696319495032833.json, 图片生成/图生图/FluxKlein换背景场景+换装+换头可选_2115263448992010241.json, 图片生成/图生图/FluxKlein换背景场景+换装+换头可选_2115275619759120386.json, 图片生成/图生图/FluxKlein换背景场景+换装！换头可选，自然无痕！_2096043363530272770.json, 图片生成/图生图/FluxKlein换背景场景+换装！换头可选，自然无痕！_2096158027081666561.json, 图片生成/图生图/千问QWEN 姿态姿势迁移 换背景场景人像写真 摆Pose复刻_2082768842199232514.json, 图片生成/图生图/千问QWEN姿态姿势迁移换背景场景人像写真_“不会摆姿势？把别人的满分姿势偷过来，人换成你自己！”_2081762175454113793.json, 图片生成/图生图/土味自拍_到_国际超模_！商用级别！克莱因FluxKlein换背景场景+换装！换头可选，自然无痕！_2111077121601916929.json, 图片生成/图生图/景绝了，姿势废了？_救命稻草来了！商用级别Klein换姿势换姿态迁移姿势迁移姿势复制_2091497635218804738.json, 平台全量/“不会摆姿势？那就把别人的满分姿势偷过来换成自己！”千问Qwen换姿势姿态迁移一键换装换人换头换背景_2077228233992527873.json, 平台全量/你还不会摆姿势吗？朋友圈人均旅拍大片了！_商用级别！FluxKlein姿势复制姿态迁移换装脸换背景_2081767163718889474.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_unet

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/FluxKlein换背景场景+换装+换头可选_2073696319495032833.json、图片生成/图生图/FluxKlein换背景场景+换装+换头可选_2115263448992010241.json、图片生成/图生图/FluxKlein换背景场景+换装+换头可选_2115275619759120386.json、图片生成/图生图/FluxKlein换背景场景+换装！换头可选，自然无痕！_2096043363530272770.json、图片生成/图生图/FluxKlein换背景场景+换装！换头可选，自然无痕！_2096158027081666561.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPLoader`
- `GetImageSize`
- `GrowMaskWithBlur`
- `LayerFilter: FilmV2`
- `LayerMask: PersonMaskUltra V2`
- `LayerUtility: CropByMask V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM V2`
- `LayerUtility: RestoreCropBox`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PrimitiveInt`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `UNETLoader`
- `VAELoader`
- `ZML_ImageSelectorNode`
- `easy imageConcat`
- `easy imageRemBg`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 8/11 个有
- `KSampler` —— 8/11 个有
- `LayerColor: Exposure` —— 8/11 个有
- `PainterFluxImageEdit` —— 8/11 个有
- `RHHiddenNodes` —— 8/11 个有
- `VAEDecode` —— 8/11 个有
- `PreviewImage` —— 7/11 个有
- `CR Text` —— 6/11 个有
- `Image Comparer (rgthree)` —— 6/11 个有
- `ImageColorMatchAdobe+` —— 6/11 个有
- `ImageScale` —— 6/11 个有
- `CR Text Concatenate` —— 5/11 个有
- `easy showAnything` —— 5/11 个有
- `DWPreprocessor` —— 4/11 个有
- `Dapao_LlamaCaption` —— 4/11 个有
- `FaceAnalysisModels` —— 3/11 个有
- `FaceEmbedDistance` —— 3/11 个有
- `QwenImageIntegratedKSampler` —— 3/11 个有
- `easy seed` —— 2/11 个有
- `DepthAnythingV2Preprocessor` —— 1/11 个有
- `LayerFilter: GaussianBlur` —— 1/11 个有
- `RandomPromptSelector` —— 1/11 个有
- `ShowText|pysssss` —— 1/11 个有
- `llama_cpp_instruct_adv` —— 1/11 个有
- `llama_cpp_model_loader` —— 1/11 个有
- `llama_cpp_parameters` —— 1/11 个有
- `孤海外补画板按方向` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 5 | 4 - 6 | 8 | 80% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 11 | 100% |
| 采样算法 | euler | - | 11 | 73% |
| 调度器 | simple | - | 11 | 73% |
| 重绘幅度 | 1 | 1 - 8.46849e+14 | 11 | 0% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 23/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 5，观测区间 4 - 6，8 个样本，取值集中（一致性 80%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，11 个样本，一致性 73%
- 调度器 最常用 simple，11 个样本，一致性 73%
- 重绘幅度 中位数 1，观测区间 1 - 8.46849e+14，11 个样本，取值分散，一致性仅 0%
- 风险：重绘幅度 观测到 8.46849e+14，超出安全上限 1（denoise 接近 1.0 时接近重新生成，初始潜空间影响被抹平）
- 高发问题（23/11 个样本）：Steps较低可能导致细节不足
