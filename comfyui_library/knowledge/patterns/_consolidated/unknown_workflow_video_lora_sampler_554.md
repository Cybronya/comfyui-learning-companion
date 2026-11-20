---
name: unknown_workflow_video_lora_sampler_554
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.806
common_nodes: [CLIPTextEncode, CR Text, CheckpointLoaderSimple, KSamplerAdvanced, LTX2SamplingPreviewOverride, LTX2_NAG, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAEEncode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVCropGuides, LTXVSeparateAVLatent, LoadAudio, LoraLoaderModelOnly, PainterAudioCut, PainterFrameExtractor, PainterLTX2Vomni, PathchSageAttentionKJ, SetLatentNoiseMask, SolidMask, VAEDecodeTiled, VHS_VideoCombine, VHS_VideoInfoLoaded, easy cleanGpuUsed, easy seed]
problems: []
missing: []
members: [图片生成/图生图/LTX2.3+数字人配音工作流（给无声视频配音-文生语音） (1)_2084448637416988673.json, 平台全量/LTX2.3 无声视频配音_2080113557957599233.json, 平台全量/LTX2.3+数字人配音工作流（给无声视频配音-文生语音） (3)_2089174777041866754.json, 平台全量/国际版Bernini视频LTX2.3配音-超强一致性支持自定义音频以及文生音频_视频对口型）_2084097789818138625.json, 音频生成/音频生成/Bernini视频配音好助手-绘画小子LTX2.3配音-超强一致性支持自定义音频以及文生音频_视频对口型）_2082730525239889921.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_554

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/LTX2.3+数字人配音工作流（给无声视频配音-文生语音） (1)_2084448637416988673.json、平台全量/LTX2.3 无声视频配音_2080113557957599233.json、平台全量/LTX2.3+数字人配音工作流（给无声视频配音-文生语音） (3)_2089174777041866754.json、平台全量/国际版Bernini视频LTX2.3配音-超强一致性支持自定义音频以及文生音频_视频对口型）_2084097789818138625.json、音频生成/音频生成/Bernini视频配音好助手-绘画小子LTX2.3配音-超强一致性支持自定义音频以及文生音频_视频对口型）_2082730525239889921.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPTextEncode`
- `CR Text`
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
- `LoraLoaderModelOnly`
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
- `LoadImage` —— 4/5 个有
- `Label (rgthree)` —— 3/5 个有
- `VHS_LoadVideoFFmpeg` —— 3/5 个有
- `ComfySwitchNode` —— 2/5 个有
- `GetNode` —— 2/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/5 个有
- `MathExpression|pysssss` —— 2/5 个有
- `ModelPatchTorchSettings` —— 2/5 个有
- `PrimitiveBoolean` —— 2/5 个有
- `SetNode` —— 2/5 个有
- `VHS_LoadVideo` —— 2/5 个有
- `easy convertAnything` —— 2/5 个有
- `easy imageSize` —— 2/5 个有
- `easy int` —— 2/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 5 | 100% |
| Prompt 约束强度(CFG) | 9 | 9 - 9 | 5 | 100% |
| 采样算法 | 1 | 1 - 1 | 5 | 100% |
| 调度器 | euler | - | 5 | 100% |
| 重绘幅度 | linear_quadratic | - | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，5 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 9，观测区间 9 - 9，5 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，5 个样本，一致性 100%
- 重绘幅度 最常用 linear_quadratic，5 个样本，一致性 100%
