---
name: unknown_workflow_video_upscale_latent_upscale_65
type: Unknown Workflow
frequency: 6
level: weak
coverage: 0.708667
common_nodes: [CFGGuider, CLIPTextEncode, DualCLIPLoader, EmptyLTXVLatentVideo, INTConstant, KSamplerSelect, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVLatentUpsampler, LTXVPreprocess, LTXVScheduler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, ManualSigmas, RandomNoise, ResizeImagesByLongerEdge, SamplerCustomAdvanced, UNETLoader, VAEDecodeTiled, VAELoader, VAELoaderKJ, VHS_VideoCombine]
problems: []
missing: []
members: [平台全量/Ltx 2.3_IC_LORA_3DReal_2075511261936308225.json, 视频生成/图生视频/LTX 2.3 四图首尾帧_2041823999381999617.json, 视频生成/图生视频/LTX 2.3双人分镜视频生成_2059165088854138882.json, 视频生成/图生视频/LTX-2.3_-_I2V_Short-Story_PromptRelay四图视频制作_2050871854566518786.json, 视频生成/图生视频/LTX2首尾帧工作流_2016770696625524737.json, 视频生成/文生视频/LTX 2.3 多图首尾帧_2032460701406601217.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_65

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（平台全量/Ltx 2.3_IC_LORA_3DReal_2075511261936308225.json、视频生成/图生视频/LTX 2.3 四图首尾帧_2041823999381999617.json、视频生成/图生视频/LTX 2.3双人分镜视频生成_2059165088854138882.json、视频生成/图生视频/LTX-2.3_-_I2V_Short-Story_PromptRelay四图视频制作_2050871854566518786.json、视频生成/图生视频/LTX2首尾帧工作流_2016770696625524737.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：71%

## 共有节点

全部 6 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `INTConstant`
- `KSamplerSelect`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVEmptyLatentAudio`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVScheduler`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadImage`
- `ManualSigmas`
- `RandomNoise`
- `ResizeImagesByLongerEdge`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoader`
- `VAELoaderKJ`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `GetImageSize` —— 5/6 个有
- `ImageResizeKJv2` —— 5/6 个有
- `LTXVChunkFeedForward` —— 5/6 个有
- `LTXVCropGuides` —— 5/6 个有
- `LTXVImgToVideoInplace` —— 5/6 个有
- `LoraLoaderModelOnly` —— 5/6 个有
- `PrimitiveFloat` —— 5/6 个有
- `LTX2SamplingPreviewOverride` —— 4/6 个有
- `LTX2_NAG` —— 4/6 个有
- `LTXVAddGuideMulti` —— 4/6 个有
- `GetNode` —— 3/6 个有
- `ImageScaleBy` —— 3/6 个有
- `ResizeImageMaskNode` —— 3/6 个有
- `SetNode` —— 3/6 个有
- `SimpleCalculatorKJ` —— 3/6 个有
- `DualCLIPLoaderGGUF` —— 2/6 个有
- `Fast Groups Bypasser (rgthree)` —— 2/6 个有
- `ImageConcatMulti` —— 2/6 个有
- `LTX2AudioLatentNormalizingSampling` —— 2/6 个有
- `PathchSageAttentionKJ` —— 2/6 个有
- `PromptRelayEncodeTimeline` —— 2/6 个有
- `UnetLoaderGGUF` —— 2/6 个有
- `CM_IntToFloat` —— 1/6 个有
- `ComfyMathExpression` —— 1/6 个有
- `Context (rgthree)` —— 1/6 个有
- `Context Switch (rgthree)` —— 1/6 个有
- `LTX2AttentionTunerPatch` —— 1/6 个有
- `LTX2MemoryEfficientSageAttentionPatch` —— 1/6 个有
- `LTXAddVideoICLoRAGuideAdvanced` —— 1/6 个有
- `LTXICLoRALoaderModelOnly` —— 1/6 个有
- `MathExpression|pysssss` —— 1/6 个有
- `PreviewAudio` —— 1/6 个有
- `PrimitiveInt` —— 1/6 个有
- `SimpleMath+` —— 1/6 个有
- `VAEDecode` —— 1/6 个有
- `VHS_LoadVideo` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 51 - 721 | 6 | 0% |
| 高度 | 25 | 24 - 25 | 6 | 98% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 51 - 721，6 个样本，取值分散，一致性仅 0%
- 高度 中位数 25，观测区间 24 - 25，6 个样本，取值集中（一致性 98%）
