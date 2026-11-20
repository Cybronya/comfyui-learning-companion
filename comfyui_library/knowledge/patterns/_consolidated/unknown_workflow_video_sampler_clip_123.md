---
name: unknown_workflow_video_sampler_clip_123
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.9414
common_nodes: [Audio Duration (mtb), AudioCrop, AudioEncoderEncode, AudioEncoderLoader, CLIPLoader, CLIPTextEncode, CR Text, ColorMatch, ImageFromBatch+, ImageResizeKJv2, KSamplerAdvanced, LoadAudio, LoadImage, ModelPatchLoader, ModelSamplingSD3, PainterAI2V, PainterAudioCut, PathchSageAttentionKJ, SimpleMath+, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [数字人/数字人/InfiniteTalk首尾帧数字人_2017590671816790018.json, 数字人/数字人/InfiniteTalk首尾帧数字人（Plus运行）_2018507855774621697.json, 数字人/数字人/Wan2.2 InfiniTetalk首尾帧数字人_2018231987617669122.json, 视频生成/图生视频/最新InfiniteTalk首尾帧图片数字人_2018160114842210306.json, 视频生成/图生视频/🐔首尾帧+infinitetalk对口型 极简使用流🐔_2018158671607369730.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_123

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（数字人/数字人/InfiniteTalk首尾帧数字人_2017590671816790018.json、数字人/数字人/InfiniteTalk首尾帧数字人（Plus运行）_2018507855774621697.json、数字人/数字人/Wan2.2 InfiniTetalk首尾帧数字人_2018231987617669122.json、视频生成/图生视频/最新InfiniteTalk首尾帧图片数字人_2018160114842210306.json、视频生成/图生视频/🐔首尾帧+infinitetalk对口型 极简使用流🐔_2018158671607369730.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：94%

## 共有节点

全部 5 个 workflow 都包含：
- `Audio Duration (mtb)`
- `AudioCrop`
- `AudioEncoderEncode`
- `AudioEncoderLoader`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `ColorMatch`
- `ImageFromBatch+`
- `ImageResizeKJv2`
- `KSamplerAdvanced`
- `LoadAudio`
- `LoadImage`
- `ModelPatchLoader`
- `ModelSamplingSD3`
- `PainterAI2V`
- `PainterAudioCut`
- `PathchSageAttentionKJ`
- `SimpleMath+`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `AudioBeforeAfterSilence` —— 4/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/5 个有
- `RunningHub Deepcleaner` —— 4/5 个有
- `easy showAnything` —— 3/5 个有
- `DapaoImageAspectRatioResizeNode` —— 1/5 个有
- `ImpactInt` —— 1/5 个有
- `Note Plus (mtb)` —— 1/5 个有
- `easy int` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 5 | 100% |
| Prompt 约束强度(CFG) | 4 | 4 - 4 | 5 | 100% |
| 采样算法 | 1 | 1 - 1 | 5 | 100% |
| 调度器 | euler | - | 5 | 100% |
| 重绘幅度 | simple | - | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，5 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 4，5 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，5 个样本，一致性 100%
- 重绘幅度 最常用 simple，5 个样本，一致性 100%
