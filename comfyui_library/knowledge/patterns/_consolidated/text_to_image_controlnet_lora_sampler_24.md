---
name: text_to_image_controlnet_lora_sampler_24
type: Text To Image
frequency: 2
level: weak
coverage: 0.881
common_nodes: [AIO_Preprocessor, CLIPLoader, CLIPTextEncode, CompressImages, ConditioningZeroOut, EmptyLatentImage, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoraLoaderModelOnly, ModelPatchLoader, PlaySound|pysssss, PreviewImage, QwenImageDiffsynthControlnet, RHBatchImages:, RHExtractImage, RHUploadZip, RH_Captioner, Text, TextConcatenate_UTK, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy batchAnything, easy cleanGpuUsed, easy forLoopEnd, easy forLoopStart, easy imageCount, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/印花裂变_2041114944355180546.json, 图片生成/图生图/印花裂变合并版_2041728791302643714.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_lora_sampler_24

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/印花裂变_2041114944355180546.json、图片生成/图生图/印花裂变合并版_2041728791302643714.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：88%

## 共有节点

全部 2 个 workflow 都包含：
- `AIO_Preprocessor`
- `CLIPLoader`
- `CLIPTextEncode`
- `CompressImages`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoraLoaderModelOnly`
- `ModelPatchLoader`
- `PlaySound|pysssss`
- `PreviewImage`
- `QwenImageDiffsynthControlnet`
- `RHBatchImages:`
- `RHExtractImage`
- `RHUploadZip`
- `RH_Captioner`
- `Text`
- `TextConcatenate_UTK`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy batchAnything`
- `easy cleanGpuUsed`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy imageCount`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `BiRefNetRMBG` —— 1/2 个有
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `FlashVSR_SM_KSampler` —— 1/2 个有
- `FlashVSR_SM_Model` —— 1/2 个有
- `GetImageRangeFromBatch` —— 1/2 个有
- `GetImageSize` —— 1/2 个有
- `ImageScaleBy` —— 1/2 个有
- `JWInteger` —— 1/2 个有
- `RMBG` —— 1/2 个有
- `SaveImage` —— 1/2 个有
- `Switch` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | FlowMatchEulerDiscreteScheduler | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |
| 宽度 | 800 | - | 2 | 100% |
| 高度 | 800 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 FlowMatchEulerDiscreteScheduler，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 800，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 800，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
