---
name: unknown_workflow_video_sampler_clip_88
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.926
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, KSamplerAdvanced, LTX2SamplingPreviewOverride, LTX2_NAG, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAEEncode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVCropGuides, LTXVSeparateAVLatent, LoadAudio, PainterAudioCut, PainterFrameExtractor, PainterLTX2Vomni, PathchSageAttentionKJ, SetLatentNoiseMask, SolidMask, VAEDecodeTiled, VHS_VideoCombine, VHS_VideoInfoLoaded, easy cleanGpuUsed, easy seed]
problems: []
missing: []
members: [图片生成/图生图/LTX2.3+数字人配音工作流（给无声视频配音-文生语音） (1)_2084448637416988673.json, 数字人/数字人/9.11对口型_2098359939495448577.json, 数字人/数字人/LTX2.3 数字人配音工作流（给无声视频配音-文生语音）_2080558057649692674.json, 数字人/数字人/绘画小子ltx配音工作流（支持自定义音频以及文生音频）_2079545782264492034.json, 音频生成/音频生成/Bernini视频配音好助手-绘画小子LTX2.3配音-超强一致性支持自定义音频以及文生音频_视频对口型）_2082730525239889921.json, 音频生成/音频生成/LTX2.3 数字人配音工作流（给无声视频配音-文生语音）_2079759741563260931.json, 音频生成/音频生成/LTX2.3 数字人配音工作流（给无声视频配音-文生语音）_2080235822560931841.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_88

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/LTX2.3+数字人配音工作流（给无声视频配音-文生语音） (1)_2084448637416988673.json、数字人/数字人/9.11对口型_2098359939495448577.json、数字人/数字人/LTX2.3 数字人配音工作流（给无声视频配音-文生语音）_2080558057649692674.json、数字人/数字人/绘画小子ltx配音工作流（支持自定义音频以及文生音频）_2079545782264492034.json、音频生成/音频生成/Bernini视频配音好助手-绘画小子LTX2.3配音-超强一致性支持自定义音频以及文生音频_视频对口型）_2082730525239889921.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 7 个 workflow 都包含：
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
- `VHS_VideoCombine`
- `VHS_VideoInfoLoaded`
- `easy cleanGpuUsed`
- `easy seed`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 6/7 个有
- `VHS_LoadVideoFFmpeg` —— 6/7 个有
- `CR Text` —— 5/7 个有
- `LoraLoaderModelOnly` —— 5/7 个有
- `Label (rgthree)` —— 4/7 个有
- `AudioToFPS` —— 1/7 个有
- `ComfySwitchNode` —— 1/7 个有
- `GetNode` —— 1/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/7 个有
- `MathExpression|pysssss` —— 1/7 个有
- `ModelPatchTorchSettings` —— 1/7 个有
- `PrimitiveBoolean` —— 1/7 个有
- `SetNode` —— 1/7 个有
- `VHS_LoadVideo` —— 1/7 个有
- `easy convertAnything` —— 1/7 个有
- `easy imageSize` —— 1/7 个有
- `easy int` —— 1/7 个有
- `easy showAnything` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 7 | 100% |
| Prompt 约束强度(CFG) | 9 | 9 - 9 | 7 | 100% |
| 采样算法 | 1 | 1 - 1 | 7 | 100% |
| 调度器 | euler | - | 7 | 100% |
| 重绘幅度 | linear_quadratic | - | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，7 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 9，观测区间 9 - 9，7 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，7 个样本，一致性 100%
- 重绘幅度 最常用 linear_quadratic，7 个样本，一致性 100%
