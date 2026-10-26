---
name: unknown_workflow_video_lora_sampler_812
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.5575
common_nodes: [CLIPVisionLoader, FlashVSR_SM_KSampler, FlashVSR_SM_Model, GetImageSizeAndCount, GetNode, GroundingDinoModelLoader (segment anything2), JjkText, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, MathExpression|pysssss, RH_LLMAPI_NODE, SDPoseOODLoader, SDPoseOODProcessor, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTeaCache, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVAELoader, YOLOModelLoader, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [数字人/数字人/海曳V1.0_2014146204921241601.json, 数字人/数字人/海曳V1.0【首帧版】_2014535976319721473.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_812

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（数字人/数字人/海曳V1.0_2014146204921241601.json、数字人/数字人/海曳V1.0【首帧版】_2014535976319721473.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：56%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPVisionLoader`
- `FlashVSR_SM_KSampler`
- `FlashVSR_SM_Model`
- `GetImageSizeAndCount`
- `GetNode`
- `GroundingDinoModelLoader (segment anything2)`
- `JjkText`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM V2`
- `MathExpression|pysssss`
- `RH_LLMAPI_NODE`
- `SDPoseOODLoader`
- `SDPoseOODProcessor`
- `SetNode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoAnimateEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTeaCache`
- `WanVideoTextEncodeCached`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `YOLOModelLoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CheckpointLoaderSimple` —— 1/2 个有
- `EmptyLatentImage` —— 1/2 个有
- `GetImageSize+` —— 1/2 个有
- `ImageFromBatch+` —— 1/2 个有
- `Int` —— 1/2 个有
- `KSampler` —— 1/2 个有
- `LoadImage` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `RHHiddenNodes` —— 1/2 个有
- `TextEncodeQwenImageEditPlus` —— 1/2 个有
- `VAEDecode` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 1.77872e+09 | - | 2 | 98% |
| Prompt 约束强度(CFG) | randomize | - | 2 | 100% |
| 采样算法 | 2 | - | 2 | 100% |
| 调度器 | 3.5 | - | 2 | 100% |
| 重绘幅度 | 11 | - | 2 | 100% |
| 宽度 | 832 | - | 1 | 100% |
| 高度 | 1248 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 1.77872e+09，样本不足，未给区间，2 个样本，取值集中（一致性 98%）
- Prompt 约束强度(CFG) 最常用 randomize，2 个样本，一致性 100%
- 采样算法 中位数 2，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 中位数 3.5，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 重绘幅度 中位数 11，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 风险：采样步数 观测到 1.80932e+09，超出安全上限 60（steps 偏高收益递减且显著增加耗时）
- 风险：重绘幅度 观测到 11，超出安全上限 1（denoise 接近 1.0 时接近重新生成，初始潜空间影响被抹平）
- 高发问题（1/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
