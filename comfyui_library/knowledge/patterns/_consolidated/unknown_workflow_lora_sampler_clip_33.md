---
name: unknown_workflow_lora_sampler_clip_33
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.478
common_nodes: [AudioEncoderEncode, AudioEncoderLoader, CLIPLoader, CLIPTextEncode, ImageFromBatch, ImageResizeKJv2, KSampler, LatentConcat, LatentCut, LoadAudio, LoadImage, LoraLoaderModelOnly, MathExpression|pysssss, ModelSamplingSD3, PrimitiveInt, UNETLoader, VAEDecode, VAELoader, WanSoundImageToVideo, WanSoundImageToVideoExtend, easy forLoopEnd, easy forLoopStart]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/1987362777876598785.json, 视频生成/图生视频/1966889832326762497.json, 视频生成/图生视频/2014761356595040257.json, 视频生成/图生视频/1966794167441666049.json, 视频生成/图生视频/2059625088659582978.json, 视频生成/图生视频/1969716858024849409.json, 音频生成/音频生成/数字人音频_文本驱动 wan2.2 S2V 数字人对口型 说话唱歌 带音色模仿 支持动物Q版 卡通_2004430918775435265.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_33

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/1987362777876598785.json、视频生成/图生视频/1966889832326762497.json、视频生成/图生视频/2014761356595040257.json、视频生成/图生视频/1966794167441666049.json、视频生成/图生视频/2059625088659582978.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：48%

## 共有节点

全部 7 个 workflow 都包含：
- `AudioEncoderEncode`
- `AudioEncoderLoader`
- `CLIPLoader`
- `CLIPTextEncode`
- `ImageFromBatch`
- `ImageResizeKJv2`
- `KSampler`
- `LatentConcat`
- `LatentCut`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MathExpression|pysssss`
- `ModelSamplingSD3`
- `PrimitiveInt`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `WanSoundImageToVideo`
- `WanSoundImageToVideoExtend`
- `easy forLoopEnd`
- `easy forLoopStart`

**可变部分**（部分 workflow 才有）：
- `Audio Duration (mtb)` —— 6/7 个有
- `GetNode` —— 6/7 个有
- `INTConstant` —— 6/7 个有
- `SetNode` —— 6/7 个有
- `SimpleMath+` —— 6/7 个有
- `VHS_VideoCombine` —— 6/7 个有
- `PrimitiveFloat` —— 5/7 个有
- `easy showAnything` —— 5/7 个有
- `AIO_Preprocessor` —— 1/7 个有
- `CreateVideo` —— 1/7 个有
- `GetImageSizeAndCount` —— 1/7 个有
- `PreviewAny` —— 1/7 个有
- `Primitive integer [Crystools]` —— 1/7 个有
- `SaveVideo` —— 1/7 个有
- `VHS_LoadVideo` —— 1/7 个有
- `Video Slice` —— 1/7 个有
- `easy float` —— 1/7 个有
- `easy seed` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 4 - 10 | 7 | 76% |
| Prompt 约束强度(CFG) | 6 | 1 - 6 | 7 | 51% |
| 采样算法 | uni_pc | - | 7 | 100% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 4 - 10，7 个样本
- Prompt 约束强度(CFG) 中位数 6，观测区间 1 - 6，7 个样本
- 采样算法 最常用 uni_pc，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（4/7 个样本）：Steps较低可能导致细节不足
