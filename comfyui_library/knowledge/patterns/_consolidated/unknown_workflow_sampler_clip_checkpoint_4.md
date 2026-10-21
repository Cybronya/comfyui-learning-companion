---
name: unknown_workflow_sampler_clip_checkpoint_4
type: Unknown Workflow
frequency: 12
level: strong
coverage: 0.874167
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, ComfyMathExpression, EmptyLTXVLatentVideo, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVPreprocess, LTXVSeparateAVLatent, ManualSigmas, PrimitiveInt, RandomNoise, ResizeImageMaskNode, SamplerCustomAdvanced, VAEDecodeTiled]
problems: []
missing: []
members: [视频生成/图生视频/2070029598238269442.json, 视频生成/图生视频/2053338009554169857.json, 视频生成/图生视频/2064734105044082689.json, 视频生成/图生视频/2062486746893471745.json, 视频生成/图生视频/2062515403225649154.json, 视频生成/图生视频/2033190788460453889.json, 视频生成/图生视频/2033053099966865410.json, 视频生成/图生视频/2070025882282061825.json, 视频生成/图生视频/2064635916139982850.json, 视频生成/文生视频/LTX-2.3-Text to Video-workflow_2034124938138882049.json, 视频生成/文生视频/LTX-2.3生成Logo展示视频_2030526628283027457.json, 视频生成/文生视频/LTX-2.3生成电影公司厂标视频_2030534215535693825.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_checkpoint_4

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（视频生成/图生视频/2070029598238269442.json、视频生成/图生视频/2053338009554169857.json、视频生成/图生视频/2064734105044082689.json、视频生成/图生视频/2062486746893471745.json、视频生成/图生视频/2062515403225649154.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 12 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ComfyMathExpression`
- `EmptyLTXVLatentVideo`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `ManualSigmas`
- `PrimitiveInt`
- `RandomNoise`
- `ResizeImageMaskNode`
- `SamplerCustomAdvanced`
- `VAEDecodeTiled`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 11/12 个有
- `LoraLoaderModelOnly` —— 11/12 个有
- `CreateVideo` —— 10/12 个有
- `SaveVideo` —— 10/12 个有
- `KSamplerSelect` —— 7/12 个有
- `LTXVAddGuide` —— 7/12 个有
- `LTXVLatentUpsampler` —— 7/12 个有
- `LatentUpscaleModelLoader` —— 7/12 个有
- `SamplerEulerAncestral` —— 7/12 个有
- `CR Text` —— 6/12 个有
- `GetImageSize` —— 6/12 个有
- `LTXVImgToVideoInplace` —— 5/12 个有
- `PrimitiveBoolean` —— 5/12 个有
- `PrimitiveStringMultiline` —— 5/12 个有
- `ResizeImagesByLongerEdge` —— 5/12 个有
- `ModelPatchTorchSettings` —— 4/12 个有
- `PathchSageAttentionKJ` —— 4/12 个有
- `RH_LLMAPI_Pro_Node` —— 4/12 个有
- `easy showAnything` —— 4/12 个有
- `CR Text Replace` —— 2/12 个有
- `ConcatTextOfUtils` —— 2/12 个有
- `LTXVChunkFeedForward` —— 2/12 个有
- `Label (rgthree)` —— 2/12 个有
- `VHS_VideoCombine` —— 2/12 个有
- `孤海注释` —— 2/12 个有
- `EmptyImage` —— 1/12 个有
- `FlashVSRInitPipe` —— 1/12 个有
- `FlashVSRNodeAdv` —— 1/12 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/12 个有
- `LoadVideo` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 12 | 100% |
| 高度 | 25 | 25 - 25 | 12 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，12 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，12 个样本，取值集中（一致性 100%）
