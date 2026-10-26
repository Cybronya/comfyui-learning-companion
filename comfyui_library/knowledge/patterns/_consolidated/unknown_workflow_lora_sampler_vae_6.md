---
name: unknown_workflow_lora_sampler_vae_6
type: Unknown Workflow
frequency: 9
level: strong
coverage: 0.668556
common_nodes: [BlockifyMask, CLIPLoader, ClothesSegment, DrawMaskOnImage, Florence2ModelLoader, Florence2Run, GetNode, KSampler, LayerUtility: ImageBlend, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, Mask Fill Holes, MaskPreview+, PreviewImage, RMBG, SDPoseOODLoader, SDPoseOODProcessor, SaveImage, SetNode, ToBinaryMask, VAEDecode, YOLOModelLoader, easy ifElse, easy isMaskEmpty]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/FireRed Edit  1.1最强人物替换（适合二创）---不偏色，无偏移，平替全能图片V1_2029890668960681985.json, 图片生成/图生图/Qwen edit 2511最强人物替换（适合二创）---不偏色，无偏移，平替全能图片V1_2005835574374268930.json, 图片生成/图生图/Qwen角色替换_2012168849222799361.json, 图片生成/图生图/【推荐】最强二创-多人角色替换、人物迁移，不改背景（圈哪迁移哪）_2008559004934475777.json, 图片生成/图生图/二创人物替换_2111096798566772737.json, 图片生成/图生图/多人角色替换、人物迁移，不改背景_2006172580859875330.json, 图片生成/图生图/多人角色替换、人物迁移，不改背景_2008011759189237762.json, 图片生成/图生图/最强二创-多人角色替换、人物迁移，不改背景_2010644275884724226.json, 图片生成/图生图/最强二创-多人角色替换、人物迁移，不改背景_2010766623031955458.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_vae_6

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/FireRed Edit  1.1最强人物替换（适合二创）---不偏色，无偏移，平替全能图片V1_2029890668960681985.json、图片生成/图生图/Qwen edit 2511最强人物替换（适合二创）---不偏色，无偏移，平替全能图片V1_2005835574374268930.json、图片生成/图生图/Qwen角色替换_2012168849222799361.json、图片生成/图生图/【推荐】最强二创-多人角色替换、人物迁移，不改背景（圈哪迁移哪）_2008559004934475777.json、图片生成/图生图/二创人物替换_2111096798566772737.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：67%

## 共有节点

全部 9 个 workflow 都包含：
- `BlockifyMask`
- `CLIPLoader`
- `ClothesSegment`
- `DrawMaskOnImage`
- `Florence2ModelLoader`
- `Florence2Run`
- `GetNode`
- `KSampler`
- `LayerUtility: ImageBlend`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `Mask Fill Holes`
- `MaskPreview+`
- `PreviewImage`
- `RMBG`
- `SDPoseOODLoader`
- `SDPoseOODProcessor`
- `SaveImage`
- `SetNode`
- `ToBinaryMask`
- `VAEDecode`
- `YOLOModelLoader`
- `easy ifElse`
- `easy isMaskEmpty`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 8/9 个有
- `Fast Groups Muter (rgthree)` —— 8/9 个有
- `MaskToImage` —— 8/9 个有
- `UNETLoader` —— 8/9 个有
- `VAELoader` —— 8/9 个有
- `ConditioningZeroOut` —— 7/9 个有
- `TextEncodeQwenImageEditPlusAdvance_lrzjason` —— 7/9 个有
- `CFGNorm` —— 6/9 个有
- `Image Comparer (rgthree)` —— 6/9 个有
- `ModelSamplingAuraFlow` —— 6/9 个有
- `UnetLoaderGGUF` —— 6/9 个有
- `GetImageSize+` —— 3/9 个有
- `SeedVR2LoadDiTModel` —— 3/9 个有
- `SeedVR2LoadVAEModel` —— 3/9 个有
- `SeedVR2VideoUpscaler` —— 3/9 个有
- `EmptyLatentImage` —— 2/9 个有
- `LayerUtility: ImageReel` —— 2/9 个有
- `LayerUtility: ImageReelComposit` —— 2/9 个有
- `Sa2VANodeTpl` —— 2/9 个有
- `TextEncodeQwenImageEditPlus` —— 2/9 个有
- `CheckpointLoaderSimple` —— 1/9 个有
- `ImageResize+` —— 1/9 个有
- `ImageScaleBy` —— 1/9 个有
- `ImageUpscaleWithModel` —— 1/9 个有
- `Int` —— 1/9 个有
- `KOOK_ImageCompression` —— 1/9 个有
- `PatchSageAttention` —— 1/9 个有
- `PrimitiveFloat` —— 1/9 个有
- `PrimitiveInt` —— 1/9 个有
- `PrimitiveString` —— 1/9 个有
- `PrimitiveStringMultiline` —— 1/9 个有
- `String` —— 1/9 个有
- `TTP_Image_Assy` —— 1/9 个有
- `TTP_Image_Tile_Batch` —— 1/9 个有
- `TTP_Tile_image_size` —— 1/9 个有
- `TorchCompileModelQwenImage` —— 1/9 个有
- `UpscaleModelLoader` —— 1/9 个有
- `easy showAnything` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | - | 2 | 100% |
| 高度 | 512 | - | 2 | 100% |
| 采样步数 | 6 | 4 - 8 | 9 | 69% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | euler | - | 9 | 78% |
| 调度器 | beta57 | - | 9 | 89% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 15/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 512，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 512，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 6，观测区间 4 - 8，9 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，9 个样本，一致性 78%
- 调度器 最常用 beta57，9 个样本，一致性 89%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 高发问题（15/9 个样本）：Steps较低可能导致细节不足
