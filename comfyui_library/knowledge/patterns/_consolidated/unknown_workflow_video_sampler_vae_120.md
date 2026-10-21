---
name: unknown_workflow_video_sampler_vae_120
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.52875
common_nodes: [BasicScheduler, CR Float To Integer, ConditioningZeroOut, DualCLIPLoader, EmptyLTXVLatentVideo, GetImageSize, GetNode, KSamplerSelect, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVImgToVideoInplaceKJ, LTXVPreprocess, LTXVSeparateAVLatent, LoadImage, MathExpression|pysssss, PathchSageAttentionKJ, PreviewImage, PrimitiveFloat, PrimitiveInt, ResizeImageMaskNode, SamplerCustom, SetNode, VAEDecode, VAELoader, VHS_VideoCombine, VisualizeSigmasKJ, easy cleanGpuUsed, easy clearCacheAll]
problems: []
missing: []
members: [视频生成/图生视频/2059201415213568002.json, 视频生成/文生视频/LTX2.3 Product Commercial LoRA 商业广告视频生成_2074728813149380610.json, 视频生成/文生视频/LTX2.3 PromptRelay Timeline 动漫视频生成工作流_2052005691182858242.json, 视频生成/文生视频/LTX2.3_PromptRelay+DramaBoxTTS 音画同步视频生成工作流_2056252444816003074.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_120

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/2059201415213568002.json、视频生成/文生视频/LTX2.3 Product Commercial LoRA 商业广告视频生成_2074728813149380610.json、视频生成/文生视频/LTX2.3 PromptRelay Timeline 动漫视频生成工作流_2052005691182858242.json、视频生成/文生视频/LTX2.3_PromptRelay+DramaBoxTTS 音画同步视频生成工作流_2056252444816003074.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：53%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicScheduler`
- `CR Float To Integer`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `GetImageSize`
- `GetNode`
- `KSamplerSelect`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVImgToVideoInplaceKJ`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `MathExpression|pysssss`
- `PathchSageAttentionKJ`
- `PreviewImage`
- `PrimitiveFloat`
- `PrimitiveInt`
- `ResizeImageMaskNode`
- `SamplerCustom`
- `SetNode`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `VisualizeSigmasKJ`
- `easy cleanGpuUsed`
- `easy clearCacheAll`

**可变部分**（部分 workflow 才有）：
- `Any Switch (rgthree)` —— 3/4 个有
- `LTXVAudioVAEEncode` —— 3/4 个有
- `LTXVAudioVAELoader` —— 3/4 个有
- `LTXVEmptyLatentAudio` —— 3/4 个有
- `PromptRelayEncode` —— 3/4 个有
- `SetLatentNoiseMask` —— 3/4 个有
- `SolidMask` —— 3/4 个有
- `UnetLoaderGGUF` —— 3/4 个有
- `CLIPTextEncode` —— 2/4 个有
- `CheckpointLoaderSimple` —— 2/4 个有
- `LTX2SamplingPreviewOverride` —— 2/4 个有
- `LoadImageFromPath` —— 2/4 个有
- `LoraLoaderModelOnly` —— 2/4 个有
- `PrimitiveStringMultiline` —— 2/4 个有
- `UNETLoader` —— 2/4 个有
- `VHS_LoadAudio` —— 2/4 个有
- `AILab_QwenVL_Advanced` —— 1/4 个有
- `Any To Any` —— 1/4 个有
- `Audio Duration (mtb)` —— 1/4 个有
- `CFGGuider` —— 1/4 个有
- `DramaBoxLoader` —— 1/4 个有
- `DramaBoxTTS` —— 1/4 个有
- `DramaBoxVoiceClone` —— 1/4 个有
- `ImageScaleToMaxDimension` —— 1/4 个有
- `LTX2_NAG` —— 1/4 个有
- `LTXVLoopingSampler` —— 1/4 个有
- `LTXVSpatioTemporalTiledVAEDecode` —— 1/4 个有
- `Load Lora` —— 1/4 个有
- `LoadAudio` —— 1/4 个有
- `LoraLoader` —— 1/4 个有
- `ManualSigmas` —— 1/4 个有
- `Power Lora Loader (rgthree)` —— 1/4 个有
- `PreviewAudio` —— 1/4 个有
- `PromptRelayEncodeTimeline` —— 1/4 个有
- `RandomNoise` —— 1/4 个有
- `ShowText|pysssss` —— 1/4 个有
- `StringReplace` —— 1/4 个有
- `VAEEncodeTiled` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 505 | 505 - 505 | 3 | 100% |
| 高度 | 25 | 25 - 25 | 3 | 100% |
| LoRA 模型强度 | 0.9 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 505，观测区间 505 - 505，3 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，3 个样本，取值集中（一致性 100%）
