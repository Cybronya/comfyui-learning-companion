---
name: unknown_workflow_video_sampler_clip_164
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.988
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, KSamplerAdvanced, LTX2SamplingPreviewOverride, LTX2_NAG, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAEEncode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVCropGuides, LTXVSeparateAVLatent, LoadAudio, PainterAudioCut, PainterFrameExtractor, PainterLTX2Vomni, PathchSageAttentionKJ, SetLatentNoiseMask, SolidMask, VAEDecodeTiled, VHS_LoadVideoFFmpeg, VHS_VideoCombine, VHS_VideoInfoLoaded, easy cleanGpuUsed, easy seed]
problems: []
missing: []
members: [数字人/数字人/9.11对口型_2098359939495448577.json, 音频生成/音频生成/LTX2.3 数字人配音工作流（给无声视频配音-文生语音）_2079759741563260931.json, 音频生成/音频生成/LTX2.3 数字人配音工作流（给无声视频配音-文生语音）_2080235822560931841.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_164

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（数字人/数字人/9.11对口型_2098359939495448577.json、音频生成/音频生成/LTX2.3 数字人配音工作流（给无声视频配音-文生语音）_2079759741563260931.json、音频生成/音频生成/LTX2.3 数字人配音工作流（给无声视频配音-文生语音）_2080235822560931841.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：99%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `KSamplerAdvanced`
- `LTX2SamplingPreviewOverride`
- `LTX2_NAG`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAEEncode`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVCropGuides`
- `LTXVSeparateAVLatent`
- `LoadAudio`
- `PainterAudioCut`
- `PainterFrameExtractor`
- `PainterLTX2Vomni`
- `PathchSageAttentionKJ`
- `SetLatentNoiseMask`
- `SolidMask`
- `VAEDecodeTiled`
- `VHS_LoadVideoFFmpeg`
- `VHS_VideoCombine`
- `VHS_VideoInfoLoaded`
- `easy cleanGpuUsed`
- `easy seed`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 2/3 个有
- `Label (rgthree)` —— 2/3 个有
- `LoadImage` —— 2/3 个有
- `LoraLoaderModelOnly` —— 2/3 个有
- `AudioToFPS` —— 1/3 个有
- `easy showAnything` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 3 | 100% |
| Prompt 约束强度(CFG) | 9 | 9 - 9 | 3 | 100% |
| 采样算法 | 1 | 1 - 1 | 3 | 100% |
| 调度器 | euler | - | 3 | 100% |
| 重绘幅度 | linear_quadratic | - | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，3 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 9，观测区间 9 - 9，3 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，3 个样本，一致性 100%
- 重绘幅度 最常用 linear_quadratic，3 个样本，一致性 100%
