---
name: unknown_workflow_upscale_latent_upscale_sampler_21
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.8915
common_nodes: [CFGGuider, CLIPTextEncode, ComfyMathExpression, EmptyLTXVLatentVideo, KSamplerSelect, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, ManualSigmas, PrimitiveBoolean, PrimitiveInt, RandomNoise, ResizeImagesByLongerEdge, SamplerCustomAdvanced]
problems: []
missing: []
members: [视频生成/图生视频/本地开源免费，漫剧短镜头3_2057838055628828673.json, 视频生成/图生视频/本地开源免费，真人短镜头3_2058240849422675970.json, 视频生成/文生视频/LTX 2.3 -22b IC-LoRA Cameraman_v2 视频工作流_2053468262532435970.json, 视频生成/文生视频/LTX2.3 文生_图生视频 KJ版_2030578285100408833.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_sampler_21

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/本地开源免费，漫剧短镜头3_2057838055628828673.json、视频生成/图生视频/本地开源免费，真人短镜头3_2058240849422675970.json、视频生成/文生视频/LTX 2.3 -22b IC-LoRA Cameraman_v2 视频工作流_2053468262532435970.json、视频生成/文生视频/LTX2.3 文生_图生视频 KJ版_2030578285100408833.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLTXVLatentVideo`
- `KSamplerSelect`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadImage`
- `ManualSigmas`
- `PrimitiveBoolean`
- `PrimitiveInt`
- `RandomNoise`
- `ResizeImagesByLongerEdge`
- `SamplerCustomAdvanced`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 3/4 个有
- `DualCLIPLoader` —— 3/4 个有
- `LoraLoaderModelOnly` —— 3/4 个有
- `PrimitiveStringMultiline` —— 3/4 个有
- `ResizeImageMaskNode` —— 3/4 个有
- `SaveVideo` —— 3/4 个有
- `VAEDecodeTiled` —— 3/4 个有
- `VAELoader` —— 3/4 个有
- `VAELoaderKJ` —— 3/4 个有
- `EnhancedLoadDiffusionModel` —— 2/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/4 个有
- `UNETLoader` —— 2/4 个有
- `easy indexAnything` —— 2/4 个有
- `ImageResizeKJv2` —— 1/4 个有
- `LTXAVTextEncoderLoader` —— 1/4 个有
- `LoadAudio` —— 1/4 个有
- `PreviewImage` —— 1/4 个有
- `Switch` —— 1/4 个有
- `VAEDecode` —— 1/4 个有
- `VHS_VideoCombine` —— 1/4 个有
- `easy cleanGpuUsed` —— 1/4 个有
- `easy clearCacheAll` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 4 | 100% |
| 高度 | 25 | 25 - 25 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，4 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，4 个样本，取值集中（一致性 100%）
