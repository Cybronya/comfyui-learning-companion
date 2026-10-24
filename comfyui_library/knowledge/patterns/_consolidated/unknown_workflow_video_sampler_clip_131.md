---
name: unknown_workflow_video_sampler_clip_131
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.4984
common_nodes: [Any2ListNode, Audio Duration (mtb), AudioEncoderEncode, AudioEncoderLoader, AudioSeparation, CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, ColorMatch, Float, GetNode, ImageFromBatch, Int, KSampler, LoadAudio, LoadImage, ModelPatchLoader, PainterAudioCut, PreviewAny, SetNode, SimpleMath+, Text, VAEDecode, VAELoader, VHS_VideoCombine, WanInfiniteTalkToVideo, easy batchAnything, easy forLoopEnd, easy forLoopStart, easy indexAnything, easy lengthAnything, easy promptLine, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/克隆自己_克隆他人声音做数字人长视频（官流稳定版）_2026533442996932609.json, 视频生成/图生视频/图生对口型-rh-全自动循环-数字人-模板_2019209695591927810.json, 视频生成/图生视频/高质量图片对口型数字人（电商、带货、短剧等实用场景）_2036376532473614337.json, 视频生成/文生视频/图生对口型-全自动循环-数字人-模板_2039982412008005633.json, 视频生成/文生视频/图生对口型-全自动循环-数字人-模板_2065338337707253762.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_131

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/克隆自己_克隆他人声音做数字人长视频（官流稳定版）_2026533442996932609.json、视频生成/图生视频/图生对口型-rh-全自动循环-数字人-模板_2019209695591927810.json、视频生成/图生视频/高质量图片对口型数字人（电商、带货、短剧等实用场景）_2036376532473614337.json、视频生成/文生视频/图生对口型-全自动循环-数字人-模板_2039982412008005633.json、视频生成/文生视频/图生对口型-全自动循环-数字人-模板_2065338337707253762.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：50%

## 共有节点

全部 5 个 workflow 都包含：
- `Any2ListNode`
- `Audio Duration (mtb)`
- `AudioEncoderEncode`
- `AudioEncoderLoader`
- `AudioSeparation`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `ColorMatch`
- `Float`
- `GetNode`
- `ImageFromBatch`
- `Int`
- `KSampler`
- `LoadAudio`
- `LoadImage`
- `ModelPatchLoader`
- `PainterAudioCut`
- `PreviewAny`
- `SetNode`
- `SimpleMath+`
- `Text`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanInfiniteTalkToVideo`
- `easy batchAnything`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy indexAnything`
- `easy lengthAnything`
- `easy promptLine`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `AudioCrop` —— 4/5 个有
- `ImageResizeKJv2` —— 3/5 个有
- `LoraLoaderModelOnly` —— 3/5 个有
- `UNETLoader` —— 3/5 个有
- `DiffusionModelLoaderKJ` —— 2/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/5 个有
- `CR Prompt Text` —— 1/5 个有
- `FB_Qwen3TTSVoiceClone` —— 1/5 个有
- `ImpactSwitch` —— 1/5 个有
- `PreviewAudio` —— 1/5 个有
- `VHS_AudioToVHSAudio` —— 1/5 个有
- `VHS_LoadVideo` —— 1/5 个有
- `VHS_VHSAudioToAudio` —— 1/5 个有
- `WhisperSTT` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
