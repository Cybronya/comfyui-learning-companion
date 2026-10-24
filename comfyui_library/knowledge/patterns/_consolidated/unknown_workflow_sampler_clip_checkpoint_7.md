---
name: unknown_workflow_sampler_clip_checkpoint_7
type: Unknown Workflow
frequency: 10
level: strong
coverage: 0.8194
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, EmptyLTXVLatentVideo, LTXAVTextEncoderLoader, LTXVAddGuide, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVPreprocess, LTXVSeparateAVLatent, LoadImage, ManualSigmas, RandomNoise, ResizeImageMaskNode, SamplerCustomAdvanced, SamplerEulerAncestral, VAEDecodeTiled]
problems: []
missing: []
members: [视频生成/图生视频/LTX2.3 首尾帧双图生视频（官流）_2070029598238269442.json, 视频生成/图生视频/LTX2.3首尾帧图生视频_2053338009554169857.json, 视频生成/图生视频/LTX2.3首尾帧生视频（官流）_2064734105044082689.json, 视频生成/图生视频/danotebook-ltx2.3-ff2v_2062486746893471745.json, 视频生成/图生视频/danotebook-ltx2.3-flf2v_2062515403225649154.json, 视频生成/图生视频/首尾帧ltx2_3_style_transition_面部加强_自动提示词_2070025882282061825.json, 视频生成/图生视频/首尾帧ltx2_3_style_transition自动提示词_2064635916139982850.json, 视频生成/图生视频/首尾帧生视频（解禁模型）：LTX2.3 Sulphur_2064603463413223426.json, 视频生成/文生视频/四步引导+首尾帧ltx2_3_style_transition+全节点注释_2057837235214577666.json, 视频生成/文生视频/首尾帧ltx2_3_style_transition+全节点注释_2055806950063001602.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_checkpoint_7

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/LTX2.3 首尾帧双图生视频（官流）_2070029598238269442.json、视频生成/图生视频/LTX2.3首尾帧图生视频_2053338009554169857.json、视频生成/图生视频/LTX2.3首尾帧生视频（官流）_2064734105044082689.json、视频生成/图生视频/danotebook-ltx2.3-ff2v_2062486746893471745.json、视频生成/图生视频/danotebook-ltx2.3-flf2v_2062515403225649154.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 10 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLTXVLatentVideo`
- `LTXAVTextEncoderLoader`
- `LTXVAddGuide`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `ManualSigmas`
- `RandomNoise`
- `ResizeImageMaskNode`
- `SamplerCustomAdvanced`
- `SamplerEulerAncestral`
- `VAEDecodeTiled`

**可变部分**（部分 workflow 才有）：
- `ComfyMathExpression` —— 9/10 个有
- `LoraLoaderModelOnly` —— 9/10 个有
- `PrimitiveInt` —— 9/10 个有
- `GetImageSize` —— 8/10 个有
- `CreateVideo` —— 7/10 个有
- `SaveVideo` —— 7/10 个有
- `ModelPatchTorchSettings` —— 5/10 个有
- `PathchSageAttentionKJ` —— 5/10 个有
- `CR Text` —— 3/10 个有
- `VHS_VideoCombine` —— 3/10 个有
- `ConcatTextOfUtils` —— 2/10 个有
- `KSamplerSelect` —— 2/10 个有
- `LTXVChunkFeedForward` —— 2/10 个有
- `LTXVLatentUpsampler` —— 2/10 个有
- `LatentUpscaleModelLoader` —— 2/10 个有
- `RH_LLMAPI_Pro_Node` —— 2/10 个有
- `easy showAnything` —— 2/10 个有
- `孤海注释` —— 2/10 个有
- `FlashVSRInitPipe` —— 1/10 个有
- `FlashVSRNodeAdv` —— 1/10 个有
- `LoadVideo` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 201 | 10 | 71% |
| 高度 | 25 | 25 - 25 | 10 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 201，10 个样本
- 高度 中位数 25，观测区间 25 - 25，10 个样本，取值集中（一致性 100%）
