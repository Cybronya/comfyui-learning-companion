---
name: unknown_workflow_video_sampler_clip_21
type: Unknown Workflow
frequency: 19
level: strong
coverage: 0.367105
common_nodes: [Audio Duration (mtb), AudioEncoderEncode, AudioEncoderLoader, AudioSeparation, CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, DiffusionModelLoaderKJ, GetNode, ImageBatch, ImageFromBatch, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, LoadImage, MathExpression|pysssss, ModelPatchLoader, PreviewAny, PreviewAudio, PrimitiveFloat, SetNode, TextInput_, VAEDecode, VAELoader, VHS_VideoCombine, WanInfiniteTalkToVideo, easy indexAnything, easy int, easy promptLine, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [数字人/数字人/Fishaudio+单人InfiniteTalk官方版工作流东源自然数字人长视频_2033511522793693185.json, 数字人/数字人/InfiniteTalk （官方流）图片驱动、数字人单人对口型_2019726268798869506.json, 数字人/数字人/InfiniteTalk数字人_2065228820231311362.json, 数字人/数字人/Jian Wei 单人InfiniteTalk官方版工作流（无限流）_2037806085641347074.json, 数字人/数字人/三七—单人口播（sanqi）_2039235549533310978.json, 数字人/数字人/单人InfiniteTalk官方版工作流_2053384334404530178.json, 数字人/数字人/单人InfiniteTalk官方版工作流_2066423963697373186.json, 数字人/数字人/彭博坦InfiniteTalk工作流_2034945862035574785.json, 数字人/数字人/数字人44秒_2040243235951484930.json, 数字人/数字人/数字人对口型_2093326224767672322.json, 数字人/数字人/数字人直播60秒_2040007973870768130.json, 数字人/数字人/数字人视频创作20秒_2072599683289141249.json, 数字人/数字人/数字人（自循环）2.0_2052595077180076034.json, 数字人/数字人/数字人（自循环）_2052213475111387137.json, 视频生成/图生视频/单人InfiniteTalk官方版工作流 (1)_2058730777491369986.json, 视频生成/图生视频/单人InfiniteTalk官方版工作流_2054726545402548226.json, 视频生成/图生视频/单人InfiniteTalk官方版工作流_2056896899143262209.json, 视频生成/图生视频/单人InfiniteTalk官方版工作流_2059550534989864961.json, 视频生成/图生视频/单人InfiniteTalk官方版电商工作流_2071583964170641410.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_21

> 由 `engine/knowledge_consolidation` 从 19 个 workflow 归纳得出（数字人/数字人/Fishaudio+单人InfiniteTalk官方版工作流东源自然数字人长视频_2033511522793693185.json、数字人/数字人/InfiniteTalk （官方流）图片驱动、数字人单人对口型_2019726268798869506.json、数字人/数字人/InfiniteTalk数字人_2065228820231311362.json、数字人/数字人/Jian Wei 单人InfiniteTalk官方版工作流（无限流）_2037806085641347074.json、数字人/数字人/三七—单人口播（sanqi）_2039235549533310978.json…）

- **类型**：Unknown Workflow
- **样本数**：19
- **可信度**：强结论
- **平均知识覆盖**：37%

## 共有节点

全部 19 个 workflow 都包含：
- `Audio Duration (mtb)`
- `AudioEncoderEncode`
- `AudioEncoderLoader`
- `AudioSeparation`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `DiffusionModelLoaderKJ`
- `GetNode`
- `ImageBatch`
- `ImageFromBatch`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadAudio`
- `LoadImage`
- `MathExpression|pysssss`
- `ModelPatchLoader`
- `PreviewAny`
- `PreviewAudio`
- `PrimitiveFloat`
- `SetNode`
- `TextInput_`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanInfiniteTalkToVideo`
- `easy indexAnything`
- `easy int`
- `easy promptLine`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `Any2ListNode` —— 18/19 个有
- `AudioCrop` —— 18/19 个有
- `PreviewImage` —— 17/19 个有
- `CR Prompt Text` —— 3/19 个有
- `easy forLoopEnd` —— 3/19 个有
- `easy forLoopStart` —— 3/19 个有
- `Int` —— 2/19 个有
- `LongCatVoiceCloneTTS` —— 2/19 个有
- `NormalizeAudioLoudness` —— 2/19 个有
- `Qwen3ASRLoader` —— 2/19 个有
- `Qwen3ASRTranscribe` —— 2/19 个有
- `easy cleanGpuUsed` —— 2/19 个有
- `Any To String (mtb)` —— 1/19 个有
- `Audio To Text (mtb)` —— 1/19 个有
- `Bjornulf_ShowInt` —— 1/19 个有
- `Fast Groups Bypasser (rgthree)` —— 1/19 个有
- `FishS2VoiceCloneTTS` —— 1/19 个有
- `LayerUtility: PurgeVRAM` —— 1/19 个有
- `LayerUtility: PurgeVRAM V2` —— 1/19 个有
- `Load Whisper (mtb)` —— 1/19 个有
- `LoadVideo` —— 1/19 个有
- `PlaySound|pysssss` —— 1/19 个有
- `ShowText|pysssss` —— 1/19 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 19 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 19 | 100% |
| 采样算法 | euler | - | 19 | 100% |
| 调度器 | normal | - | 19 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 19 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 146/19 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，19 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，19 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，19 个样本，一致性 100%
- 调度器 最常用 normal，19 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，19 个样本，取值集中（一致性 100%）
- 高发问题（146/19 个样本）：Steps较低可能导致细节不足
