---
name: unknown_workflow_lora_sampler_clip_184
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.921
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, ComfyMathExpression, CreateVideo, EmptyLTXVLatentVideo, GemmaAPITextEncode, GetVideoComponents, KSamplerSelect, LTXAVTextEncoderLoader, LTXAddVideoICLoRAGuide, LTXFloatToInt, LTXICLoRALoaderModelOnly, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVSeparateAVLatent, LTXVTiledVAEDecode, LoadVideo, LoraLoaderModelOnly, ManualSigmas, PrimitiveString, RandomNoise, SamplerCustomAdvanced, SaveVideo]
problems: []
missing: []
members: [图片生成/图生图/LTX2.3动作迁移优化_2083394351262158850.json, 视频生成/图生视频/LTX2.3人物动作迁移（视频）_2083198650917941249.json, 音频生成/音频生成/LTX-2.3_ICLoRA_Lipdub V2V 口型同步工作流_2054609608710344705.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_184

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/LTX2.3动作迁移优化_2083394351262158850.json、视频生成/图生视频/LTX2.3人物动作迁移（视频）_2083198650917941249.json、音频生成/音频生成/LTX-2.3_ICLoRA_Lipdub V2V 口型同步工作流_2054609608710344705.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ComfyMathExpression`
- `CreateVideo`
- `EmptyLTXVLatentVideo`
- `GemmaAPITextEncode`
- `GetVideoComponents`
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
- `LTXVEmptyLatentAudio`
- `LTXVSeparateAVLatent`
- `LTXVTiledVAEDecode`
- `LoadVideo`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PrimitiveString`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`

**可变部分**（部分 workflow 才有）：
- `CannyEdgePreprocessor` —— 2/3 个有
- `DWPreprocessor` —— 2/3 个有
- `GetImageSize` —— 2/3 个有
- `ImageScale` —— 2/3 个有
- `ImageToMask` —— 2/3 个有
- `LTXVDilateVideoMask` —— 2/3 个有
- `LTXVImgToVideoConditionOnly` —— 2/3 个有
- `LTXVLaplacianPyramidBlend` —— 2/3 个有
- `LoadImage` —— 2/3 个有
- `MaskToImage` —— 2/3 个有
- `PrimitiveBoolean` —— 2/3 个有
- `SimpleMath+` —— 2/3 个有
- `GetImageSizeAndCount` —— 1/3 个有
- `LTXVAudioVAEEncode` —— 1/3 个有
- `LTXVLatentUpsampler` —— 1/3 个有
- `LTXVSetAudioRefTokens` —— 1/3 个有
- `LatentUpscaleModelLoader` —— 1/3 个有
- `ResizeImageMaskNode` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 3 | 100% |
| 高度 | 25 | 25 - 25 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，3 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，3 个样本，取值集中（一致性 100%）
