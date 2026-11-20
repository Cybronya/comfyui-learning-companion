---
name: unknown_workflow_video_lora_sampler_921
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9665
common_nodes: [AudioCropProcessUTK, CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, EmptyLTXVLatentVideo, ImageSharpen, JWInteger, KSamplerSelect, LTXVAudioVAEEncode, LTXVChunkFeedForward, LTXVConcatAVLatent, LTXVConditioning, LTXVImgToVideoInplace, LTXVPreprocess, LTXVSeparateAVLatent, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, LoadAudio, LoadImage, LoraLoaderModelOnly, MathExpression|pysssss, PathchSageAttentionKJ, PrimitiveFloat, RH_LLMAPI_NODE, RH_LLMAPI_Pro_Node, RandomNoise, SamplerCustomAdvanced, SetLatentNoiseMask, SolidMask, TrimAudioDuration, VAEDecode, VAELoaderKJ, VHS_VideoCombine, easy float]
problems: []
missing: []
members: [视频生成/图生视频/ltx-2-数字人-Digital Human_2019699591033131009.json, 视频生成/图生视频/ltx2.3数字人-图生视频_2033035717600878594.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_921

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/ltx-2-数字人-Digital Human_2019699591033131009.json、视频生成/图生视频/ltx2.3数字人-图生视频_2033035717600878594.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：97%

## 共有节点

全部 2 个 workflow 都包含：
- `AudioCropProcessUTK`
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLTXVLatentVideo`
- `ImageSharpen`
- `JWInteger`
- `KSamplerSelect`
- `LTXVAudioVAEEncode`
- `LTXVChunkFeedForward`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVImgToVideoInplace`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM V2`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MathExpression|pysssss`
- `PathchSageAttentionKJ`
- `PrimitiveFloat`
- `RH_LLMAPI_NODE`
- `RH_LLMAPI_Pro_Node`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SetLatentNoiseMask`
- `SolidMask`
- `TrimAudioDuration`
- `VAEDecode`
- `VAELoaderKJ`
- `VHS_VideoCombine`
- `easy float`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 1/2 个有
- `CR Text Concatenate` —— 1/2 个有
- `DualCLIPLoader` —— 1/2 个有
- `LTXAVTextEncoderLoader` —— 1/2 个有
- `LTXVScheduler` —— 1/2 个有
- `LayerFilter: GaussianBlur` —— 1/2 个有
- `ManualSigmas` —— 1/2 个有
- `MelBandRoFormerModelLoader` —— 1/2 个有
- `MelBandRoFormerSampler` —— 1/2 个有
- `ModelPatchTorchSettings` —— 1/2 个有
- `PreviewAny` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
