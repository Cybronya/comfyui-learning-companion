---
name: unknown_workflow_video_lora_sampler_462
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.474
common_nodes: [AudioCrop, AudioEncoderEncode, AudioEncoderLoader, AudioSeparation, CFGNorm, CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, ConditioningZeroOut, EmptySD3LatentImage, Evaluate Integers, FluxKontextMultiReferenceLatentMethod, GetNode, INTConstant, ImageBatch, ImageFromBatch, ImageResizeKJv2, JjkText, KSampler, LayerUtility: PurgeVRAM, LoadAudio, LoadImage, LoraLoaderModelOnly, ModelPatchLoader, ModelPatchTorchSettings, ModelSamplingAuraFlow, ModelSamplingSD3, PathchSageAttentionKJ, PreviewImage, PrimitiveInt, SetNode, SimpleMath+, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanInfiniteTalkToVideo, easy cleanGpuUsed, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/人物对口型V3加速版！_2039986432743317505.json, 视频生成/图生视频/Ai女友对口型60秒版！InfiniteTalkV3升级！B站艾橘溪_2018195510116491266.json, 视频生成/文生视频/图生视频超长60秒  Ai女友对口型 InfiniteTalk 升级版_2059436711733719042.json, 视频生成/文生视频/指定人物动作 全能图生视频新版 超长时间视频生成_2061322291950211073.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_462

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/人物对口型V3加速版！_2039986432743317505.json、视频生成/图生视频/Ai女友对口型60秒版！InfiniteTalkV3升级！B站艾橘溪_2018195510116491266.json、视频生成/文生视频/图生视频超长60秒  Ai女友对口型 InfiniteTalk 升级版_2059436711733719042.json、视频生成/文生视频/指定人物动作 全能图生视频新版 超长时间视频生成_2061322291950211073.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：47%

## 共有节点

全部 4 个 workflow 都包含：
- `AudioCrop`
- `AudioEncoderEncode`
- `AudioEncoderLoader`
- `AudioSeparation`
- `CFGNorm`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `ConditioningZeroOut`
- `EmptySD3LatentImage`
- `Evaluate Integers`
- `FluxKontextMultiReferenceLatentMethod`
- `GetNode`
- `INTConstant`
- `ImageBatch`
- `ImageFromBatch`
- `ImageResizeKJv2`
- `JjkText`
- `KSampler`
- `LayerUtility: PurgeVRAM`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelPatchLoader`
- `ModelPatchTorchSettings`
- `ModelSamplingAuraFlow`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `PreviewImage`
- `PrimitiveInt`
- `SetNode`
- `SimpleMath+`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanInfiniteTalkToVideo`
- `easy cleanGpuUsed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 2/4 个有
- `RH_RhartVideoGImageToVideo` —— 1/4 个有
- `SaveVideo` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | beta | - | 4 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 44/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 beta，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（44/4 个样本）：Steps较低可能导致细节不足
