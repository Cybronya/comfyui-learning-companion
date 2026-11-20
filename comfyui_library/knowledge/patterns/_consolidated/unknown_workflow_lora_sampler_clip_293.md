---
name: unknown_workflow_lora_sampler_clip_293
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9555
common_nodes: [CFGGuider, CLIPTextEncode, CannyEdgePreprocessor, CheckpointLoaderSimple, ComfyMathExpression, CreateVideo, DWPreprocessor, EmptyLTXVLatentVideo, GemmaAPITextEncode, GetImageSize, GetVideoComponents, ImageScale, ImageToMask, KSamplerSelect, LTXAVTextEncoderLoader, LTXAddVideoICLoRAGuide, LTXFloatToInt, LTXICLoRALoaderModelOnly, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVDilateVideoMask, LTXVEmptyLatentAudio, LTXVImgToVideoConditionOnly, LTXVLaplacianPyramidBlend, LTXVSeparateAVLatent, LTXVTiledVAEDecode, LoadImage, LoadVideo, LoraLoaderModelOnly, ManualSigmas, MaskToImage, PrimitiveBoolean, PrimitiveString, RandomNoise, SamplerCustomAdvanced, SaveVideo, SimpleMath+]
problems: []
missing: []
members: [图片生成/图生图/LTX2.3动作迁移优化_2083394351262158850.json, 视频生成/图生视频/LTX2.3人物动作迁移（视频）_2083198650917941249.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_293

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/LTX2.3动作迁移优化_2083394351262158850.json、视频生成/图生视频/LTX2.3人物动作迁移（视频）_2083198650917941249.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：96%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CannyEdgePreprocessor`
- `CheckpointLoaderSimple`
- `ComfyMathExpression`
- `CreateVideo`
- `DWPreprocessor`
- `EmptyLTXVLatentVideo`
- `GemmaAPITextEncode`
- `GetImageSize`
- `GetVideoComponents`
- `ImageScale`
- `ImageToMask`
- `KSamplerSelect`
- `LTXAVTextEncoderLoader`
- `LTXAddVideoICLoRAGuide`
- `LTXFloatToInt`
- `LTXICLoRALoaderModelOnly`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVDilateVideoMask`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoConditionOnly`
- `LTXVLaplacianPyramidBlend`
- `LTXVSeparateAVLatent`
- `LTXVTiledVAEDecode`
- `LoadImage`
- `LoadVideo`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `MaskToImage`
- `PrimitiveBoolean`
- `PrimitiveString`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `SimpleMath+`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | - | 2 | 100% |
| 高度 | 25 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 25，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
