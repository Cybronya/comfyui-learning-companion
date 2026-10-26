---
name: unknown_workflow_video_lora_sampler_963
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.733
common_nodes: [Audio Cut (mtb), AudioConcat, CFGNorm, CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CM_IntToFloat, CR Text Concatenate, ConditioningZeroOut, DWPreprocessor, EmptySD3LatentImage, GetImageRangeFromBatch, GetNode, GetRandomIntegerInRange, ImageBatchMulti, ImageResizeKJv2, Int, Int2String, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, ModelSamplingSD3, MuyeTextEditOutput, PathchSageAttentionKJ, PixelPerfectResolution, PreviewImage, SetNode, SimpleMath+, Text, TextEncodeQwenImageEditPlus, TrimVideoLatent, UNETLoader, VAEDecode, VAELoader, VHS_DuplicateImages, VHS_GetImageCount, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfoLoaded, WanAnimateToVideo, easy cleanGpuUsed, easy imageSize, easy seed]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/兵哥定制-图生视频（自动检测+人物替换+长视频）_1988577815270440962.json, 视频生成/图生视频/兵哥定制（动作迁移）_1988227122856681474.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_963

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/兵哥定制-图生视频（自动检测+人物替换+长视频）_1988577815270440962.json、视频生成/图生视频/兵哥定制（动作迁移）_1988227122856681474.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：73%

## 共有节点

全部 2 个 workflow 都包含：
- `Audio Cut (mtb)`
- `AudioConcat`
- `CFGNorm`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CM_IntToFloat`
- `CR Text Concatenate`
- `ConditioningZeroOut`
- `DWPreprocessor`
- `EmptySD3LatentImage`
- `GetImageRangeFromBatch`
- `GetNode`
- `GetRandomIntegerInRange`
- `ImageBatchMulti`
- `ImageResizeKJv2`
- `Int`
- `Int2String`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `ModelSamplingSD3`
- `MuyeTextEditOutput`
- `PathchSageAttentionKJ`
- `PixelPerfectResolution`
- `PreviewImage`
- `SetNode`
- `SimpleMath+`
- `Text`
- `TextEncodeQwenImageEditPlus`
- `TrimVideoLatent`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_DuplicateImages`
- `VHS_GetImageCount`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfoLoaded`
- `WanAnimateToVideo`
- `easy cleanGpuUsed`
- `easy imageSize`
- `easy seed`

**可变部分**（部分 workflow 才有）：
- `BlockifyMask` —— 1/2 个有
- `CreateVideo` —— 1/2 个有
- `DrawMaskOnImage` —— 1/2 个有
- `FaceMaskFromPoseKeypoints` —— 1/2 个有
- `GrowMask` —— 1/2 个有
- `ImageCropByMaskAndResize` —— 1/2 个有
- `LayerMask: SegformerB2ClothesUltra` —— 1/2 个有
- `RHHiddenNodes` —— 1/2 个有
- `RH_LLMAPI_Pro_Node` —— 1/2 个有
- `RunningHub ThinkSound` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 7 | - | 2 | 86% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | er_sde | - | 2 | 50% |
| 调度器 | beta | - | 2 | 50% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 12/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 7，样本不足，未给区间，2 个样本，取值集中（一致性 86%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，2 个样本，一致性 50%
- 调度器 最常用 beta，2 个样本，一致性 50%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（12/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
