---
name: image_to_image_video_lora_sampler_8
type: Image To Image
frequency: 4
level: strong
coverage: 0.812
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CR Overlay Text, CR Text Replace, ConditioningZeroOut, GetImageSizeAndCount, GetNode, GetTextFromJson, ImageConcatMulti, ImageFromBatch, ImageScaleToTotalPixels, JWInteger, KSampler, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, LoadImage, LoadJsonFromText, LoraLoaderModelOnly, MathExpression|pysssss, ModelPatchTorchSettings, ModelSamplingSD3, PathchSageAttentionKJ, PreviewImage, SetNode, ShowText|pysssss, Text Concatenate, Text Multiline, TextEncodeQwenImageEditPlusAdvance_lrzjason, UNETLoader, VAEDecode, VAEEncode, VAELoader, VHS_VideoCombine, WanImageToVideo, easy imageBatchToImageList, easy imageListToImageBatch, easy promptLine, easy showAnything, wanBlockSwap]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/260105001-005.三宫格视频自动字幕_2008181646041817090.json, 视频生成/图生视频/260110005.三宫格视频自动字幕_2011257424702873602.json, 视频生成/图生视频/【视频版】Qwen-Edit 2509 三宫格写真（自动中英文字幕）_1983153646135353345.json, 视频生成/文生视频/超火三宫格玩法+视频版+自动添加字幕_2033065190819893250.json]
source: knowledge_consolidation
---

# image_to_image_video_lora_sampler_8

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/260105001-005.三宫格视频自动字幕_2008181646041817090.json、视频生成/图生视频/260110005.三宫格视频自动字幕_2011257424702873602.json、视频生成/图生视频/【视频版】Qwen-Edit 2509 三宫格写真（自动中英文字幕）_1983153646135353345.json、视频生成/文生视频/超火三宫格玩法+视频版+自动添加字幕_2033065190819893250.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CR Overlay Text`
- `CR Text Replace`
- `ConditioningZeroOut`
- `GetImageSizeAndCount`
- `GetNode`
- `GetTextFromJson`
- `ImageConcatMulti`
- `ImageFromBatch`
- `ImageScaleToTotalPixels`
- `JWInteger`
- `KSampler`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `LoadJsonFromText`
- `LoraLoaderModelOnly`
- `MathExpression|pysssss`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `PreviewImage`
- `SetNode`
- `ShowText|pysssss`
- `Text Concatenate`
- `Text Multiline`
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
- `RH_LLMAPI_NODE` —— 3/4 个有
- `ImpactMakeImageList` —— 2/4 个有
- `SDVM Image List Repeat` —— 2/4 个有
- `RHHiddenNodes` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 4 | 100% |
| Prompt 约束强度(CFG) | 8 | 8 - 8 | 4 | 100% |
| 采样算法 | 1 | 1 - 1 | 4 | 100% |
| 调度器 | euler_ancestral | - | 4 | 100% |
| 重绘幅度 | simple | - | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 最常用 fixed，4 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 8，观测区间 8 - 8，4 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler_ancestral，4 个样本，一致性 100%
- 重绘幅度 最常用 simple，4 个样本，一致性 100%
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
