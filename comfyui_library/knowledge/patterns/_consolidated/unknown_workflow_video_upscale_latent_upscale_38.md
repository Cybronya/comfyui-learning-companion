---
name: unknown_workflow_video_upscale_latent_upscale_38
type: Unknown Workflow
frequency: 10
level: strong
coverage: 0.7248
common_nodes: [CFGGuider, CLIPTextEncode, EmptyLTXVLatentVideo, INTConstant, KSamplerSelect, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVLatentUpsampler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, ManualSigmas, RandomNoise, SamplerCustomAdvanced, SolidMask, Text Multiline, VAEDecodeTiled, VAELoaderKJ, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/LTX2.3-三帧MV音乐视频_2037924916380573698.json, 视频生成/图生视频/LTX2.3-多帧MV视频【简易版】_2035021083685953537.json, 视频生成/图生视频/LTX2.3声音+图片（MV 音乐数字人）_2031678223054016514.json, 视频生成/图生视频/LTX2.3声音+图片（MV 音乐数字人）_2033338918136975362.json, 视频生成/图生视频/LTX2.3多图引导生成工作流_2031935763281092609.json, 视频生成/文生视频/LTX2.3-AIO-Lite版视频工作流_2034809834549288962.json, 视频生成/文生视频/LTX2.3-AIO-低显存版视频工作流_2037429372935737346.json, 视频生成/文生视频/LTX2.3-AIO视频工作流_2032019073520902145.json, 视频生成/文生视频/LTX2.3-AIO视频工作流_V2（无字幕版）_2050758511885332481.json, 视频生成/文生视频/LTX2.3长视频生成（PromptRelay增强）_2049157702005297154.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_38

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/LTX2.3-三帧MV音乐视频_2037924916380573698.json、视频生成/图生视频/LTX2.3-多帧MV视频【简易版】_2035021083685953537.json、视频生成/图生视频/LTX2.3声音+图片（MV 音乐数字人）_2031678223054016514.json、视频生成/图生视频/LTX2.3声音+图片（MV 音乐数字人）_2033338918136975362.json、视频生成/图生视频/LTX2.3多图引导生成工作流_2031935763281092609.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：72%

## 共有节点

全部 10 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `EmptyLTXVLatentVideo`
- `INTConstant`
- `KSamplerSelect`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVLatentUpsampler`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadImage`
- `ManualSigmas`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SolidMask`
- `Text Multiline`
- `VAEDecodeTiled`
- `VAELoaderKJ`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `DualCLIPLoader` —— 9/10 个有
- `GetNode` —— 9/10 个有
- `LTXVAudioVAEEncode` —— 9/10 个有
- `LTXVPreprocess` —— 9/10 个有
- `LoadAudio` —— 9/10 个有
- `PrimitiveBoolean` —— 9/10 个有
- `ResizeImageMaskNode` —— 9/10 个有
- `ResizeImagesByLongerEdge` —— 9/10 个有
- `SetLatentNoiseMask` —— 9/10 个有
- `SetNode` —— 9/10 个有
- `TrimAudioDuration` —— 9/10 个有
- `UNETLoader` —— 9/10 个有
- `easy showAnything` —— 9/10 个有
- `PrimitiveInt` —— 8/10 个有
- `ComfyMathExpression` —— 7/10 个有
- `LTXVImgToVideoInplaceKJ` —— 7/10 个有
- `PathchSageAttentionKJ` —— 7/10 个有
- `Switch any [Crystools]` —— 7/10 个有
- `Fast Groups Bypasser (rgthree)` —— 6/10 个有
- `LoraLoaderModelOnly` —— 6/10 个有
- `PreviewAny` —— 6/10 个有
- `CM_IntToFloat` —— 4/10 个有
- `llama_cpp_instruct_adv` —— 4/10 个有
- `llama_cpp_model_loader` —— 4/10 个有
- `LTXVImgToVideoConditionOnly` —— 3/10 个有
- `LTXVImgToVideoInplace` —— 3/10 个有
- `Lora Loader Stack (rgthree)` —— 3/10 个有
- `RIFEInterpolation` —— 3/10 个有
- `RTXVideoSuperResolution` —— 3/10 个有
- `TextGenerateLTX2Prompt` —— 3/10 个有
- `math_calculate` —— 3/10 个有
- `CM_FloatToInt` —— 2/10 个有
- `LTX2_NAG` —— 2/10 个有
- `PlaySound|pysssss` —— 2/10 个有
- `PrimitiveFloat` —— 2/10 个有
- `PromptRelayEncodeTimeline` —— 2/10 个有
- `VAEDecode` —— 2/10 个有
- `easy anythingIndexSwitch` —— 2/10 个有
- `1hew_AnySwitchSelect` —— 1/10 个有
- `DualCLIPLoaderGGUF` —— 1/10 个有
- `FrameSelector` —— 1/10 个有
- `ImageResizeKJv2` —— 1/10 个有
- `ImpactFloat` —— 1/10 个有
- `LTXVAddGuideMulti` —— 1/10 个有
- `LTXVChunkFeedForward` —— 1/10 个有
- `LTXVScheduler` —— 1/10 个有
- `PainterVRAM` —— 1/10 个有
- `PrimitiveStringMultiline` —— 1/10 个有
- `UnetLoaderGGUF` —— 1/10 个有
- `VRAM_Debug` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 10 | 100% |
| 高度 | 25 | 25 - 25 | 10 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，10 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，10 个样本，取值集中（一致性 100%）
