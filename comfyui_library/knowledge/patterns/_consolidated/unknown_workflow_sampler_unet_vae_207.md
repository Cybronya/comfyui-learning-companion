---
name: unknown_workflow_sampler_unet_vae_207
type: Unknown Workflow
frequency: 5
level: weak
coverage: 0.856
common_nodes: [CFGGuider, ComfyMathExpression, CreateVideo, DualCLIPLoader, EmptyLTXVLatentVideo, ImageResizeKJv2, KSamplerSelect, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVSeparateAVLatent, LoadImage, PrimitiveInt, RandomNoise, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecodeTiled, VAELoaderKJ]
problems: []
missing: []
members: [图片生成/文生图/LTX2.3 多图控制 提示词分段中继流_2073319635222618113.json, 视频生成/图生视频/LTX2.3 prompt relay 提示词分段控制流_2052341800647569410.json, 视频生成/图生视频/万象AI+LTX2.3 首中尾3帧转场特效+去字幕lora+自动提示词优化版_2040976928861069314.json, 视频生成/文生视频/LTX2.3-多宫格生视频-画质感人-v2_2038941376720674817.json, 视频生成/文生视频/LTX2.3-多宫格生视频-画质感人_2038650134229159937.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_207

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/LTX2.3 多图控制 提示词分段中继流_2073319635222618113.json、视频生成/图生视频/LTX2.3 prompt relay 提示词分段控制流_2052341800647569410.json、视频生成/图生视频/万象AI+LTX2.3 首中尾3帧转场特效+去字幕lora+自动提示词优化版_2040976928861069314.json、视频生成/文生视频/LTX2.3-多宫格生视频-画质感人-v2_2038941376720674817.json、视频生成/文生视频/LTX2.3-多宫格生视频-画质感人_2038650134229159937.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：86%

## 共有节点

全部 5 个 workflow 都包含：
- `CFGGuider`
- `ComfyMathExpression`
- `CreateVideo`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `PrimitiveInt`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoaderKJ`

**可变部分**（部分 workflow 才有）：
- `LTXVAddGuideMulti` —— 4/5 个有
- `LTXVImgToVideoInplace` —— 4/5 个有
- `easy showAnything` —— 4/5 个有
- `CLIPTextEncode` —— 3/5 个有
- `Int` —— 3/5 个有
- `LTXVLatentUpsampler` —— 3/5 个有
- `LTXVPreprocess` —— 3/5 个有
- `LatentUpscaleModelLoader` —— 3/5 个有
- `LoraLoaderModelOnly` —— 3/5 个有
- `ManualSigmas` —— 3/5 个有
- `RH_LLMAPI_Pro_Node` —— 3/5 个有
- `ResizeImagesByLongerEdge` —— 3/5 个有
- `SimpleMath+` —— 3/5 个有
- `BasicScheduler` —— 2/5 个有
- `ConditioningZeroOut` —— 2/5 个有
- `GuHaiAutoImageSplit` —— 2/5 个有
- `ImageFromBatch` —— 2/5 个有
- `PrimitiveFloat` —— 2/5 个有
- `PromptRelayEncodeTimeline` —— 2/5 个有
- `QZ_ResolutionPreset` —— 2/5 个有
- `SaveImage` —— 2/5 个有
- `AspectRatio` —— 1/5 个有
- `CR Prompt Text` —— 1/5 个有
- `ConcatTextOfUtils` —— 1/5 个有
- `Fast Groups Bypasser (rgthree)` —— 1/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 601 | 5 | 10% |
| 高度 | 25 | 25 - 25 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 601，5 个样本，取值分散，一致性仅 10%
- 高度 中位数 25，观测区间 25 - 25，5 个样本，取值集中（一致性 100%）
