---
name: unknown_workflow_video_lora_sampler_761
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.945
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, EmptyLTXVLatentVideo, ImageResizeKJv2, KSamplerSelect, LTXAVTextEncoderLoader, LTXAddVideoICLoRAGuide, LTXICLoRALoaderModelOnly, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVImgToVideoConditionOnly, LTXVPreprocess, LTXVSeparateAVLatent, LoadImage, LoraLoaderModelOnly, ManualSigmas, PrimitiveBoolean, RandomNoise, SDPoseOODLoader, SDPoseOODProcessor, SamplerCustomAdvanced, VAEDecodeTiled, VHS_LoadVideo, VHS_VideoCombine, YOLOModelLoader]
problems: []
missing: []
members: [视频生成/图生视频/2041045547859054594.json, 视频生成/图生视频/2036397493621104642.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_761

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/2041045547859054594.json、视频生成/图生视频/2036397493621104642.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：94%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLTXVLatentVideo`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `LTXAVTextEncoderLoader`
- `LTXAddVideoICLoRAGuide`
- `LTXICLoRALoaderModelOnly`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoConditionOnly`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PrimitiveBoolean`
- `RandomNoise`
- `SDPoseOODLoader`
- `SDPoseOODProcessor`
- `SamplerCustomAdvanced`
- `VAEDecodeTiled`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `YOLOModelLoader`

**可变部分**（部分 workflow 才有）：
- `CM_FloatToInt` —— 1/2 个有
- `CR Text` —— 1/2 个有
- `DWPreprocessor` —— 1/2 个有
- `GetImageSize` —— 1/2 个有
- `INTConstant` —— 1/2 个有
- `ImageConcanate` —— 1/2 个有
- `Int` —— 1/2 个有
- `LTXVChunkFeedForward` —— 1/2 个有
- `LatentUpscaleModelLoader` —— 1/2 个有
- `ModelPatchTorchSettings` —— 1/2 个有
- `PathchSageAttentionKJ` —— 1/2 个有
- `PixelPerfectResolution` —— 1/2 个有
- `PrimitiveFloat` —— 1/2 个有
- `PrimitiveInt` —— 1/2 个有
- `Text` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 109 | - | 2 | 89% |
| 高度 | 24 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 109，样本不足，未给区间，2 个样本，取值集中（一致性 89%）
- 高度 中位数 24，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
