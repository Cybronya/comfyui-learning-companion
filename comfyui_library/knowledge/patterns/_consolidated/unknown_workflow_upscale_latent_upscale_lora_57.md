---
name: unknown_workflow_upscale_latent_upscale_lora_57
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.896333
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, EmptyImage, EmptyLTXVLatentVideo, GetImageSize, ImageScaleBy, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVLatentUpsampler, LTXVPreprocess, LTXVScheduler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, LoraLoaderModelOnly, ManualSigmas, PrimitiveInt, RandomNoise, ResizeImagesByLongerEdge, SamplerCustomAdvanced, VAEDecode]
problems: []
missing: []
members: [视频生成/图生视频/【Supermate 稳定版2】ltx2单图原音驱动工作流_2012047557043687425.json, 视频生成/图生视频/【Supermate】优化LTX-2 图生视频 （Plus会员版）_2008554221829885954.json, 视频生成/图生视频/【加速】LTX2.0 图生视频工作流_2017478785842548737.json, 视频生成/图生视频/【老金驿站】LTX2-19B一镜聚焦工作流_2014309275279036418.json, 视频生成/图生视频/图生视频--LTX_2_首尾帧工作流_2057285774952980482.json, 视频生成/图生视频/大凯辰光 LTX-2 首尾帧工作流PLus版在线工作流_2009604954146742273.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_57

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/【Supermate 稳定版2】ltx2单图原音驱动工作流_2012047557043687425.json、视频生成/图生视频/【Supermate】优化LTX-2 图生视频 （Plus会员版）_2008554221829885954.json、视频生成/图生视频/【加速】LTX2.0 图生视频工作流_2017478785842548737.json、视频生成/图生视频/【老金驿站】LTX2-19B一镜聚焦工作流_2014309275279036418.json、视频生成/图生视频/图生视频--LTX_2_首尾帧工作流_2057285774952980482.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 6 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyImage`
- `EmptyLTXVLatentVideo`
- `GetImageSize`
- `ImageScaleBy`
- `KSamplerSelect`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVScheduler`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PrimitiveInt`
- `RandomNoise`
- `ResizeImagesByLongerEdge`
- `SamplerCustomAdvanced`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `ImageResizeKJv2` —— 4/6 个有
- `LTXVImgToVideoInplace` —— 4/6 个有
- `easy cleanGpuUsed` —— 4/6 个有
- `CreateVideo` —— 3/6 个有
- `MemoryCleaner` —— 3/6 个有
- `SaveVideo` —— 3/6 个有
- `VHS_VideoCombine` —— 3/6 个有
- `BetaSamplingScheduler` —— 2/6 个有
- `LTXVFirstLastFrameControl_TTP` —— 2/6 个有
- `Any To String (mtb)` —— 1/6 个有
- `CR Prompt Text` —— 1/6 个有
- `INTConstant` —— 1/6 个有
- `PreviewImage` —— 1/6 个有
- `Qwen3_VQA` —— 1/6 个有
- `Resize` —— 1/6 个有
- `SaveImage` —— 1/6 个有
- `ShowText|pysssss` —— 1/6 个有
- `SmartImageConcat` —— 1/6 个有
- `Textbox` —— 1/6 个有
- `easy promptConcat` —— 1/6 个有
- `easy seed` —— 1/6 个有
- `easy textSwitch` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 6 | 100% |
| 高度 | 25 | 25 - 25 | 6 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，6 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，6 个样本，取值集中（一致性 100%）
