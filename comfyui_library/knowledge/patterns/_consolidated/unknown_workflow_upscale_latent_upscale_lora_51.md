---
name: unknown_workflow_upscale_latent_upscale_lora_51
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.714429
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, EmptyImage, EmptyLTXVLatentVideo, GetImageSize, ImageScaleBy, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVLatentUpsampler, LTXVPreprocess, LTXVScheduler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, LoraLoaderModelOnly, RandomNoise, SamplerCustomAdvanced]
problems: []
missing: []
members: [视频生成/图生视频/LH-DMT-LTX2.0-006.首尾帧生视频-音画同步_2012334757446684674.json, 视频生成/图生视频/LH-DMT-LTX2.0-006.首尾帧生视频-音画同步_2019749362657660929.json, 视频生成/图生视频/LH-DMT-LTX2.0-007.LTX2.0-图生视频（优化版）全自动反推提示词_2016324555433840641.json, 视频生成/图生视频/LTX-2 图生视频高动态版_2073298883534483458.json, 视频生成/图生视频/LTX-2 极速图生视频_2010303270488641537.json, 视频生成/图生视频/LTX-2 高质量图生视频  电影镜头动画 可智能反推提示词 真实摄影_2013159959533461506.json, 视频生成/图生视频/LTX2.3-图生视频升级版（自动提示词）_2030630367857741826.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_51

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/LH-DMT-LTX2.0-006.首尾帧生视频-音画同步_2012334757446684674.json、视频生成/图生视频/LH-DMT-LTX2.0-006.首尾帧生视频-音画同步_2019749362657660929.json、视频生成/图生视频/LH-DMT-LTX2.0-007.LTX2.0-图生视频（优化版）全自动反推提示词_2016324555433840641.json、视频生成/图生视频/LTX-2 图生视频高动态版_2073298883534483458.json、视频生成/图生视频/LTX-2 极速图生视频_2010303270488641537.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：71%

## 共有节点

全部 7 个 workflow 都包含：
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
- `RandomNoise`
- `SamplerCustomAdvanced`

**可变部分**（部分 workflow 才有）：
- `ManualSigmas` —— 6/7 个有
- `VAEDecodeTiled` —— 6/7 个有
- `easy cleanGpuUsed` —— 6/7 个有
- `Int` —— 5/7 个有
- `LTXVImgToVideoInplace` —— 5/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/7 个有
- `ShowText|pysssss` —— 5/7 个有
- `PrimitiveInt` —— 4/7 个有
- `VHS_VideoCombine` —— 4/7 个有
- `easy showAnything` —— 4/7 个有
- `CreateVideo` —— 3/7 个有
- `Fast Groups Bypasser (rgthree)` —— 3/7 个有
- `JoinStrings` —— 3/7 个有
- `LayerUtility: PurgeVRAM V2` —— 3/7 个有
- `PreviewImage` —— 3/7 个有
- `Qwen3_VQA` —— 3/7 个有
- `ResizeImagesByLongerEdge` —— 3/7 个有
- `SaveVideo` —— 3/7 个有
- `SimpleMath+` —— 3/7 个有
- `TextInput_` —— 3/7 个有
- `ImageConcatMulti` —— 2/7 个有
- `ImageResizeKJv2` —— 2/7 个有
- `LTXVFirstLastFrameControl_TTP` —— 2/7 个有
- `PrimitiveFloat` —— 2/7 个有
- `Text` —— 2/7 个有
- `GetNode` —— 1/7 个有
- `INTConstant` —— 1/7 个有
- `JWInteger` —— 1/7 个有
- `LTXVSpatioTemporalTiledVAEDecode` —— 1/7 个有
- `RH_LLMAPI_Pro_Node` —— 1/7 个有
- `SetNode` —— 1/7 个有
- `VAEDecode` —— 1/7 个有
- `llama_cpp_instruct_adv` —— 1/7 个有
- `llama_cpp_model_loader` —— 1/7 个有
- `llama_cpp_unload_model` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 121 | 7 | 90% |
| 高度 | 25 | 25 - 25 | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 121，7 个样本，取值集中（一致性 90%）
- 高度 中位数 25，观测区间 25 - 25，7 个样本，取值集中（一致性 100%）
