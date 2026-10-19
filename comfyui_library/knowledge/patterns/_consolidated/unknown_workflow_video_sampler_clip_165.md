---
name: unknown_workflow_video_sampler_clip_165
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.946
common_nodes: [Audio Duration, AudioEncoderEncode, AudioEncoderLoader, CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, ComfyMathExpression, DiffusionModelLoaderKJ, GetImageSize, ImageBatch, ImageFromBatch, ImageResizeKJ, KSampler, LoadImage, ModelPatchLoader, PreviewAudio, VAEDecode, VAELoader, VHS_VideoCombine, WanInfiniteTalkToVideo, easy forLoopEnd, easy forLoopStart, easy int, easy mathInt]
problems: [Steps较低可能导致细节不足]
missing: []
members: [数字人/数字人/数字人-文本驱动-无限时长-InfiniTetalk版_2108502688081207298.json, 视频生成/图生视频/数字人-声音克隆-无限时长-InfiniTetalk版_2109547310756745218.json, 视频生成/图生视频/数字人-音频驱动-无限时长-InfiniTetalk版_2109520566653898753.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_165

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（数字人/数字人/数字人-文本驱动-无限时长-InfiniTetalk版_2108502688081207298.json、视频生成/图生视频/数字人-声音克隆-无限时长-InfiniTetalk版_2109547310756745218.json、视频生成/图生视频/数字人-音频驱动-无限时长-InfiniTetalk版_2109520566653898753.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：95%

## 共有节点

全部 3 个 workflow 都包含：
- `Audio Duration`
- `AudioEncoderEncode`
- `AudioEncoderLoader`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `ComfyMathExpression`
- `DiffusionModelLoaderKJ`
- `GetImageSize`
- `ImageBatch`
- `ImageFromBatch`
- `ImageResizeKJ`
- `KSampler`
- `LoadImage`
- `ModelPatchLoader`
- `PreviewAudio`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanInfiniteTalkToVideo`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy int`
- `easy mathInt`

**可变部分**（部分 workflow 才有）：
- `LoadAudio` —— 2/3 个有
- `PrimitiveStringMultiline` —— 2/3 个有
- `SaveAudio` —— 2/3 个有
- `AudioSeparation` —— 1/3 个有
- `FB_Qwen3TTSVoiceClone` —— 1/3 个有
- `FB_Qwen3TTSVoiceDesign` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（6/3 个样本）：Steps较低可能导致细节不足
