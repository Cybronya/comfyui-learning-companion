---
name: unknown_workflow_video_upscale_latent_upscale_91
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.944
common_nodes: [CFGGuider, CLIPTextEncode, DualCLIPLoaderGGUF, EmptyLTXVLatentVideo, INTConstant, KSamplerSelect, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, ManualSigmas, PrimitiveInt, RandomNoise, SamplerCustomAdvanced, UnetLoaderGGUF, VAEDecodeTiled, VAELoader, VHS_VideoCombine, easy cleanGpuUsed]
problems: []
missing: []
members: [视频生成/图生视频/LTX-2音视频同步生成_GGUF量化版-8G显卡可超快运行放大版图生视频 (二次优化)_2012162728634359809.json, 视频生成/图生视频/WH（首尾帧）_LTX-2_GGUF量化8G超快运行放大版图生视频_2013139812877864961.json, 视频生成/图生视频/【GGUF量化版】ltx-2音视频高清图生视频音频同步生成数字人漫画短视频生成5秒3分钟完成_2012200191926996993.json, 视频生成/文生视频/LTX-2.3+GGUF量化版生视频_2033507189314297858.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_91

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/LTX-2音视频同步生成_GGUF量化版-8G显卡可超快运行放大版图生视频 (二次优化)_2012162728634359809.json、视频生成/图生视频/WH（首尾帧）_LTX-2_GGUF量化8G超快运行放大版图生视频_2013139812877864961.json、视频生成/图生视频/【GGUF量化版】ltx-2音视频高清图生视频音频同步生成数字人漫画短视频生成5秒3分钟完成_2012200191926996993.json、视频生成/文生视频/LTX-2.3+GGUF量化版生视频_2033507189314297858.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：94%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `DualCLIPLoaderGGUF`
- `EmptyLTXVLatentVideo`
- `INTConstant`
- `KSamplerSelect`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVEmptyLatentAudio`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadImage`
- `ManualSigmas`
- `PrimitiveInt`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UnetLoaderGGUF`
- `VAEDecodeTiled`
- `VAELoader`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `JWInteger` —— 3/4 个有
- `LTXVAudioVAELoader` —— 3/4 个有
- `LTXVCropGuides` —— 3/4 个有
- `LTXVScheduler` —— 3/4 个有
- `Label (rgthree)` —— 3/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/4 个有
- `LTXVImgToVideoInplace` —— 2/4 个有
- `LoraLoaderModelOnly` —— 2/4 个有
- `PathchSageAttentionKJ` —— 2/4 个有
- `CR Prompt Text` —— 1/4 个有
- `CR Text` —— 1/4 个有
- `ComfyMathExpression` —— 1/4 个有
- `Fast Groups Bypasser (rgthree)` —— 1/4 个有
- `ImageResizeKJv2` —— 1/4 个有
- `LTXVFirstLastFrameControl_TTP` —— 1/4 个有
- `LTXVImgToVideoConditionOnly` —— 1/4 个有
- `PrimitiveBoolean` —— 1/4 个有
- `VAELoaderKJ` —— 1/4 个有

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
