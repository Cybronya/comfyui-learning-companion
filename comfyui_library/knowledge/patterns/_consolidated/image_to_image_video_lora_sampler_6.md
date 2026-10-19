---
name: image_to_image_video_lora_sampler_6
type: Image To Image
frequency: 5
level: moderate
coverage: 0.7788
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CR Overlay Text, ConditioningZeroOut, GetNode, ImageConcatMulti, ImageFromBatch, JWInteger, KSampler, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, LoadImage, LoraLoaderModelOnly, MathExpression|pysssss, ModelPatchTorchSettings, ModelSamplingSD3, PathchSageAttentionKJ, PreviewImage, SetNode, TextEncodeQwenImageEditPlusAdvance_lrzjason, UNETLoader, VAEDecode, VAEEncode, VAELoader, VHS_VideoCombine, WanImageToVideo, easy imageBatchToImageList, easy imageListToImageBatch, easy promptLine, easy showAnything, wanBlockSwap]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/2008181646041817090.json, 视频生成/图生视频/2011257424702873602.json, 视频生成/图生视频/1983153646135353345.json, 视频生成/图生视频/1983726049295015938.json, 视频生成/文生视频/超火三宫格玩法+视频版+自动添加字幕_2033065190819893250.json]
source: knowledge_consolidation
---

# image_to_image_video_lora_sampler_6

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/2008181646041817090.json、视频生成/图生视频/2011257424702873602.json、视频生成/图生视频/1983153646135353345.json、视频生成/图生视频/1983726049295015938.json、视频生成/文生视频/超火三宫格玩法+视频版+自动添加字幕_2033065190819893250.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：78%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CR Overlay Text`
- `ConditioningZeroOut`
- `GetNode`
- `ImageConcatMulti`
- `ImageFromBatch`
- `JWInteger`
- `KSampler`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MathExpression|pysssss`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `PreviewImage`
- `SetNode`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanImageToVideo`
- `easy imageBatchToImageList`
- `easy imageListToImageBatch`
- `easy promptLine`
- `easy showAnything`
- `wanBlockSwap`

**可变部分**（部分 workflow 才有）：
- `CR Text Replace` —— 4/5 个有
- `GetImageSizeAndCount` —— 4/5 个有
- `GetTextFromJson` —— 4/5 个有
- `ImageScaleToTotalPixels` —— 4/5 个有
- `LoadJsonFromText` —— 4/5 个有
- `RH_LLMAPI_NODE` —— 4/5 个有
- `ShowText|pysssss` —— 4/5 个有
- `Text Concatenate` —— 4/5 个有
- `Text Multiline` —— 4/5 个有
- `SDVM Image List Repeat` —— 3/5 个有
- `ImpactMakeImageList` —— 2/5 个有
- `CFGNorm` —— 1/5 个有
- `CR Prompt Text` —— 1/5 个有
- `DeepTranslatorTextNode` —— 1/5 个有
- `Float` —— 1/5 个有
- `ImageListToImageBatch` —— 1/5 个有
- `Int` —— 1/5 个有
- `JjkText` —— 1/5 个有
- `ModelSamplingAuraFlow` —— 1/5 个有
- `ProcessString` —— 1/5 个有
- `RHHiddenNodes` —— 1/5 个有
- `SaveImage` —— 1/5 个有
- `Text` —— 1/5 个有
- `TextEncodeQwenImageEditPlus` —— 1/5 个有
- `easy cleanGpuUsed` —— 1/5 个有
- `easy promptConcat` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 5 | 80% |
| Prompt 约束强度(CFG) | 8 | 1 - 8 | 5 | 58% |
| 采样算法 | 1 | 1 - 1 | 4 | 100% |
| 调度器 | euler_ancestral | - | 5 | 80% |
| 重绘幅度 | simple | - | 5 | 80% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 最常用 fixed，5 个样本，一致性 80%
- Prompt 约束强度(CFG) 中位数 8，观测区间 1 - 8，5 个样本
- 采样算法 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler_ancestral，5 个样本，一致性 80%
- 重绘幅度 最常用 simple，5 个样本，一致性 80%
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
