---
name: image_to_image_video_lora_sampler_13
type: Image To Image
frequency: 3
level: moderate
coverage: 0.827
common_nodes: [CFGNorm, CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CR Text Replace, ConditioningZeroOut, Fast Groups Bypasser (rgthree), GetImageSizeAndCount, GetNode, ImageFromBatch, ImageFromBatch+, JWInteger, KSampler, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, LoadAudio, LoadImage, LoraLoaderModelOnly, MathExpression|pysssss, ModelPatchTorchSettings, ModelSamplingAuraFlow, ModelSamplingSD3, Mute / Bypass Relay (rgthree), Mute / Bypass Repeater (rgthree), PathchSageAttentionKJ, PrimitiveStringMultiline, ProcessString, Qwen3_VQA, QwenVisionNode, SaveImage, SetNode, Text Multiline, TextEncodeQwenImageEditPlusAdvance_lrzjason, UNETLoader, VAEDecode, VAEEncode, VAELoader, VHS_VideoCombine, WanImageToVideo, easy batchAnything, easy imageBatchToImageList, easy imageListToImageBatch, easy promptLine, easy showAnything, wanBlockSwap]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/一键直出，美女写真套图视频_1984872507406761986.json, 视频生成/图生视频/写真套图视频一键生成_1984890760073986049.json, 视频生成/图生视频/美女写真套图视频一键直出_1983727908047003650.json]
source: knowledge_consolidation
---

# image_to_image_video_lora_sampler_13

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/一键直出，美女写真套图视频_1984872507406761986.json、视频生成/图生视频/写真套图视频一键生成_1984890760073986049.json、视频生成/图生视频/美女写真套图视频一键直出_1983727908047003650.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CR Text Replace`
- `ConditioningZeroOut`
- `Fast Groups Bypasser (rgthree)`
- `GetImageSizeAndCount`
- `GetNode`
- `ImageFromBatch`
- `ImageFromBatch+`
- `JWInteger`
- `KSampler`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM V2`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MathExpression|pysssss`
- `ModelPatchTorchSettings`
- `ModelSamplingAuraFlow`
- `ModelSamplingSD3`
- `Mute / Bypass Relay (rgthree)`
- `Mute / Bypass Repeater (rgthree)`
- `PathchSageAttentionKJ`
- `PrimitiveStringMultiline`
- `ProcessString`
- `Qwen3_VQA`
- `QwenVisionNode`
- `SaveImage`
- `SetNode`
- `Text Multiline`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanImageToVideo`
- `easy batchAnything`
- `easy imageBatchToImageList`
- `easy imageListToImageBatch`
- `easy promptLine`
- `easy showAnything`
- `wanBlockSwap`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 8 | 3 | 1% |
| 采样算法 | euler | - | 3 | 67% |
| 调度器 | beta57 | - | 3 | 67% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 8，3 个样本，取值分散，一致性仅 1%
- 采样算法 最常用 euler，3 个样本，一致性 67%
- 调度器 最常用 beta57，3 个样本，一致性 67%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
