---
name: unknown_workflow_video_lora_sampler_441
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.9442
common_nodes: [AudioEncoderEncode, AudioEncoderLoader, AudioInfo, AudioTrim, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, Evaluate Integers, ImageBatch, ImageFromBatch, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, LoadImage, LoraLoaderModelOnly, MelBandRoFormerModelLoader, MelBandRoFormerSampler, ModelPatchLoader, ModelPatchTorchSettings, PathchSageAttentionKJ, PreviewAudio, Text Multiline, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanInfiniteTalkToVideo, easy forLoopEnd, easy forLoopStart, easy int, easy mathInt, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/反推提示词/110本地生活探店数字人生成_2063575509426069505.json, 数字人/数字人/InfiniteTalk 官版自循环版无质量劣化问题_2019211461448441857.json, 数字人/数字人/InfiniteTalk-ComfyUI官版数字人MV_2019097656231989249.json, 视频生成/图生视频/本地生活探店数字人生成_2046426953556692994.json, 视频生成/图生视频/本地生活数字人_2046186407764434945.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_441

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/反推提示词/110本地生活探店数字人生成_2063575509426069505.json、数字人/数字人/InfiniteTalk 官版自循环版无质量劣化问题_2019211461448441857.json、数字人/数字人/InfiniteTalk-ComfyUI官版数字人MV_2019097656231989249.json、视频生成/图生视频/本地生活探店数字人生成_2046426953556692994.json、视频生成/图生视频/本地生活数字人_2046186407764434945.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：94%

## 共有节点

全部 5 个 workflow 都包含：
- `AudioEncoderEncode`
- `AudioEncoderLoader`
- `AudioInfo`
- `AudioTrim`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `Evaluate Integers`
- `ImageBatch`
- `ImageFromBatch`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler`
- `ModelPatchLoader`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `PreviewAudio`
- `Text Multiline`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanInfiniteTalkToVideo`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy int`
- `easy mathInt`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `Apply Whisper` —— 3/5 个有
- `CR Text Replace` —— 3/5 个有
- `JWFloat` —— 3/5 个有
- `PurgeVRAM_UTK` —— 3/5 个有
- `Qwen3TTSModelLoader` —— 3/5 个有
- `Qwen3TTSVoiceClone` —— 3/5 个有
- `Qwen3_VQA` —— 3/5 个有
- `RH_LLMAPI_Pro_Node` —— 3/5 个有
- `Text` —— 3/5 个有
- `TextConcatenate` —— 3/5 个有
- `VHS_LoadVideo` —— 3/5 个有
- `Fast Bypasser (rgthree)` —— 2/5 个有
- `Mute / Bypass Repeater (rgthree)` —— 2/5 个有
- `CR Text` —— 1/5 个有
- `CreateVideo` —— 1/5 个有
- `GetImageSize` —— 1/5 个有
- `ImageBatchMulti` —— 1/5 个有
- `Int` —— 1/5 个有
- `LayerUtility: TextJoin` —— 1/5 个有
- `MathExpression|pysssss` —— 1/5 个有
- `RH_LLMAPI_NODE` —— 1/5 个有
- `SaveVideo` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 3 | 3 - 4 | 5 | 86% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | normal | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 3，观测区间 3 - 4，5 个样本，取值集中（一致性 86%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 normal，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（10/5 个样本）：Steps较低可能导致细节不足
