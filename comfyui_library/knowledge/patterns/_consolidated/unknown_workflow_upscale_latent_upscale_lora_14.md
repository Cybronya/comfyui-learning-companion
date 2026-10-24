---
name: unknown_workflow_upscale_latent_upscale_lora_14
type: Unknown Workflow
frequency: 14
level: strong
coverage: 0.884214
common_nodes: [CFGGuider, CLIPTextEncode, EmptyImage, EmptyLTXVLatentVideo, GetImageSize, ImageScaleBy, KSamplerSelect, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVLatentUpsampler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoraLoaderModelOnly, PrimitiveInt, RandomNoise, SamplerCustomAdvanced]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/LTX-2 蒸馏版 1080P_2073298682799288322.json, 图片生成/文生图/LTX2.3文生视频_2044769183031894018.json, 图片生成/文生图/LTXV2.0文生视频_2008915535752335362.json, 图片生成/文生图/LTX_2_首尾帧工作流 V1.0_2010216291981860866.json, 视频生成/图生视频/LTX-2 GGUF 12GB图生有声视频工作流-B站UP主@好奇漫步_2018342004555522049.json, 视频生成/图生视频/LTX-2 图生视频官方版_2073297592267657218.json, 视频生成/图生视频/LTX-2 图生视频高动态版_2073298883534483458.json, 视频生成/图生视频/LTX-2图生视频工作流_2008838542486671361.json, 视频生成/图生视频/LTX-2图生视频工作流_2009242619980812289.json, 视频生成/图生视频/LTX-2高动态图生视频工作流_2009601705482129409.json, 视频生成/图生视频/LTX2.3图生视频_2029943442415034369.json, 视频生成/图生视频/LTX2.3图生视频_2030295867214794753.json, 视频生成/图生视频/LTX2.3图生视频_2032301246597570562.json, 视频生成/图生视频/LTX2.3图生视频_2033385858308513793.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_14

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（图片生成/文生图/LTX-2 蒸馏版 1080P_2073298682799288322.json、图片生成/文生图/LTX2.3文生视频_2044769183031894018.json、图片生成/文生图/LTXV2.0文生视频_2008915535752335362.json、图片生成/文生图/LTX_2_首尾帧工作流 V1.0_2010216291981860866.json、视频生成/图生视频/LTX-2 GGUF 12GB图生有声视频工作流-B站UP主@好奇漫步_2018342004555522049.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 14 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `EmptyImage`
- `EmptyLTXVLatentVideo`
- `GetImageSize`
- `ImageScaleBy`
- `KSamplerSelect`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVLatentUpsampler`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoraLoaderModelOnly`
- `PrimitiveInt`
- `RandomNoise`
- `SamplerCustomAdvanced`

**可变部分**（部分 workflow 才有）：
- `CheckpointLoaderSimple` —— 13/14 个有
- `LTXAVTextEncoderLoader` —— 13/14 个有
- `LTXVAudioVAELoader` —— 13/14 个有
- `LTXVScheduler` —— 13/14 个有
- `CreateVideo` —— 12/14 个有
- `SaveVideo` —— 12/14 个有
- `LTXVPreprocess` —— 11/14 个有
- `LoadImage` —— 11/14 个有
- `ResizeImagesByLongerEdge` —— 11/14 个有
- `VAEDecode` —— 11/14 个有
- `LTXVImgToVideoInplace` —— 10/14 个有
- `ManualSigmas` —— 9/14 个有
- `PreviewAny` —— 6/14 个有
- `DualCLIPLoader` —— 5/14 个有
- `KSampler` —— 5/14 个有
- `VAEDecodeTiled` —— 5/14 个有
- `ImageResizeKJv2` —— 4/14 个有
- `PrimitiveFloat` —— 4/14 个有
- `ResizeImageMaskNode` —— 4/14 个有
- `TextGenerateLTX2Prompt` —— 4/14 个有
- `RH_LLMAPI_Pro_Node` —— 3/14 个有
- `easy cleanGpuUsed` —— 3/14 个有
- `Label (rgthree)` —— 2/14 个有
- `VHS_VideoCombine` —— 2/14 个有
- `AILab_QwenVL` —— 1/14 个有
- `BetaSamplingScheduler` —— 1/14 个有
- `CR Multiline Text` —— 1/14 个有
- `LTXVFirstLastFrameControl_TTP` —— 1/14 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/14 个有
- `LayerUtility: PurgeVRAM V2` —— 1/14 个有
- `MemoryCleaner` —— 1/14 个有
- `RunningHub Deepcleaner` —— 1/14 个有
- `Text _O` —— 1/14 个有
- `Textbox` —— 1/14 个有
- `UnetLoaderGGUF` —— 1/14 个有
- `VAELoaderKJ` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 14 | 100% |
| 高度 | 25 | 25 - 25 | 14 | 100% |
| 采样步数 | 4 | 4 - 4 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 0.35 | 0.35 - 0.4 | 5 | 94% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/14 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，14 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，14 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 0.35，观测区间 0.35 - 0.4，5 个样本，取值集中（一致性 94%）
