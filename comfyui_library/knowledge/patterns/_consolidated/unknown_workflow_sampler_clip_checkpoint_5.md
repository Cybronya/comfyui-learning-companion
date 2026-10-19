---
name: unknown_workflow_sampler_clip_checkpoint_5
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.795875
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, EmptyLTXVLatentVideo, GetImageSize, LTXAVTextEncoderLoader, LTXVAddGuide, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVPreprocess, LTXVSeparateAVLatent, LoadImage, ManualSigmas, RandomNoise, ResizeImageMaskNode, SamplerCustomAdvanced, SamplerEulerAncestral, VAEDecodeTiled]
problems: []
missing: []
members: [视频生成/图生视频/2070029598238269442.json, 视频生成/图生视频/2053338009554169857.json, 视频生成/图生视频/2064734105044082689.json, 视频生成/图生视频/2070025882282061825.json, 视频生成/图生视频/2064635916139982850.json, 视频生成/图生视频/2064603463413223426.json, 视频生成/文生视频/四步引导+首尾帧ltx2_3_style_transition+全节点注释_2057837235214577666.json, 视频生成/文生视频/首尾帧ltx2_3_style_transition+全节点注释_2055806950063001602.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_checkpoint_5

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/2070029598238269442.json、视频生成/图生视频/2053338009554169857.json、视频生成/图生视频/2064734105044082689.json、视频生成/图生视频/2070025882282061825.json、视频生成/图生视频/2064635916139982850.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：80%

## 共有节点

全部 8 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLTXVLatentVideo`
- `GetImageSize`
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
- `ComfyMathExpression` —— 7/8 个有
- `LoraLoaderModelOnly` —— 7/8 个有
- `PrimitiveInt` —— 7/8 个有
- `CreateVideo` —— 5/8 个有
- `ModelPatchTorchSettings` —— 5/8 个有
- `PathchSageAttentionKJ` —— 5/8 个有
- `SaveVideo` —— 5/8 个有
- `CR Text` —— 3/8 个有
- `VHS_VideoCombine` —— 3/8 个有
- `ConcatTextOfUtils` —— 2/8 个有
- `LTXVChunkFeedForward` —— 2/8 个有
- `RH_LLMAPI_Pro_Node` —— 2/8 个有
- `easy showAnything` —— 2/8 个有
- `孤海注释` —— 2/8 个有
- `FlashVSRInitPipe` —— 1/8 个有
- `FlashVSRNodeAdv` —— 1/8 个有
- `LoadVideo` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 201 | 8 | 69% |
| 高度 | 25 | 25 - 25 | 8 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 201，8 个样本
- 高度 中位数 25，观测区间 25 - 25，8 个样本，取值集中（一致性 100%）
