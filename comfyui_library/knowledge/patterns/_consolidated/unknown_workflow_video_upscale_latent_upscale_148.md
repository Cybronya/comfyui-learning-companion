---
name: unknown_workflow_video_upscale_latent_upscale_148
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.862
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, ComfyMathExpression, Fast Groups Bypasser (rgthree), ImageResizeKJv2, Int, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAELoader, LTXVConditioning, LTXVEmptyLatentAudio, LatentUpscaleModelLoader, LoadImage, LoraLoaderModelOnly, PrimitiveFloat, PrimitiveInt, PrimitiveStringMultiline, RHHiddenNodes, RandomNoise, ResizeImagesByLongerEdge, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/多图参考-4宫格-LTX2.3图生视频音画同步_2059942996799479809.json, 视频生成/图生视频/首尾帧-图生视频ltx2.3稳定版-3-15秒_2046426362579259394.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_148

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/多图参考-4宫格-LTX2.3图生视频音画同步_2059942996799479809.json、视频生成/图生视频/首尾帧-图生视频ltx2.3稳定版-3-15秒_2046426362579259394.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：86%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ComfyMathExpression`
- `Fast Groups Bypasser (rgthree)`
- `ImageResizeKJv2`
- `Int`
- `KSamplerSelect`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAELoader`
- `LTXVConditioning`
- `LTXVEmptyLatentAudio`
- `LatentUpscaleModelLoader`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PrimitiveFloat`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `RHHiddenNodes`
- `RandomNoise`
- `ResizeImagesByLongerEdge`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `ImageFromBatch+` —— 1/2 个有
- `ImageTile+` —— 1/2 个有
- `LTXVPreprocess` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1 | - | 2 | 100% |
| 高度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
