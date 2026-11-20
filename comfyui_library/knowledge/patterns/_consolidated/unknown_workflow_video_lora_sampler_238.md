---
name: unknown_workflow_video_lora_sampler_238
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.553333
common_nodes: [Audio Duration (mtb), AudioEncoderEncode, AudioEncoderLoader, CLIPLoader, CLIPTextEncode, ImageFromBatch, ImageResizeKJv2, KSampler, LatentConcat, LatentCut, LoadAudio, LoadImage, LoraLoaderModelOnly, MathExpression|pysssss, ModelSamplingSD3, PrimitiveInt, SimpleMath+, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanSoundImageToVideo, WanSoundImageToVideoExtend, easy forLoopEnd, easy forLoopStart]
problems: [Steps较低可能导致细节不足]
missing: []
members: [数字人/数字人/Wan2.2 S2V 数字人对口型(说话唱歌（支持人、动物）)_2019347338757672961.json, 数字人/数字人/Wan2.2+S2V+数字人对口型(说话唱歌（支持人、动物）)_2019749940704055298.json, 数字人/数字人/video_wan2_2_14B_S2V 视频对口型+姿势控制_1976126547759378434.json, 视频生成/图生视频/WAN22 S2V视频唱歌说话不限时长_1987362777876598785.json, 视频生成/图生视频/video_wan2_2_14B_s2 姿势控制_1966889832326762497.json, 视频生成/图生视频/video_wan2_2_14B_s2v无视音频长度一键生成 根据音频长度去生成视频 林耀_2014761356595040257.json, 视频生成/图生视频/video_wan2_2_14B_s2v无视音频长度一键生成_1966794167441666049.json, 视频生成/图生视频/超强视频wan22唱歌说话不限时长_1969716858024849409.json, 音频生成/音频生成/数字人音频_文本驱动 wan2.2 S2V 数字人对口型 说话唱歌 带音色模仿 支持动物Q版 卡通_2004430918775435265.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_238

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（数字人/数字人/Wan2.2 S2V 数字人对口型(说话唱歌（支持人、动物）)_2019347338757672961.json、数字人/数字人/Wan2.2+S2V+数字人对口型(说话唱歌（支持人、动物）)_2019749940704055298.json、数字人/数字人/video_wan2_2_14B_S2V 视频对口型+姿势控制_1976126547759378434.json、视频生成/图生视频/WAN22 S2V视频唱歌说话不限时长_1987362777876598785.json、视频生成/图生视频/video_wan2_2_14B_s2 姿势控制_1966889832326762497.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：55%

## 共有节点

全部 9 个 workflow 都包含：
- `Audio Duration (mtb)`
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
- `SimpleMath+`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanSoundImageToVideo`
- `WanSoundImageToVideoExtend`
- `easy forLoopEnd`
- `easy forLoopStart`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 6/9 个有
- `PrimitiveFloat` —— 6/9 个有
- `SetNode` —— 6/9 个有
- `easy showAnything` —— 6/9 个有
- `INTConstant` —— 5/9 个有
- `Primitive integer [Crystools]` —— 3/9 个有
- `AIO_Preprocessor` —— 2/9 个有
- `GetImageSizeAndCount` —— 2/9 个有
- `VHS_LoadVideo` —— 2/9 个有
- `AudioCrop` —— 1/9 个有
- `AudioSeparation` —— 1/9 个有
- `Bjornulf_ShowInt` —— 1/9 个有
- `ImageConcatMulti` —— 1/9 个有
- `Int` —— 1/9 个有
- `PreviewImage` —— 1/9 个有
- `VHS_SelectImages` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 8 - 10 | 9 | 90% |
| Prompt 约束强度(CFG) | 6 | 1 - 6 | 9 | 46% |
| 采样算法 | uni_pc | - | 9 | 100% |
| 调度器 | simple | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 8 - 10，9 个样本，取值集中（一致性 90%）
- Prompt 约束强度(CFG) 中位数 6，观测区间 1 - 6，9 个样本，取值分散，一致性仅 46%
- 采样算法 最常用 uni_pc，9 个样本，一致性 100%
- 调度器 最常用 simple，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 高发问题（6/9 个样本）：Steps较低可能导致细节不足
