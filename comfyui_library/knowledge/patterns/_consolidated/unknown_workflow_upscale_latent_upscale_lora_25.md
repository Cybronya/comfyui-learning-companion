---
name: unknown_workflow_upscale_latent_upscale_lora_25
type: Unknown Workflow
frequency: 11
level: strong
coverage: 0.687727
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, EmptyImage, EmptyLTXVLatentVideo, GetImageSize, ImageScaleBy, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVLatentUpsampler, LTXVPreprocess, LTXVScheduler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, LoraLoaderModelOnly, RandomNoise, SamplerCustomAdvanced]
problems: [Steps较低可能导致细节不足, 发现KSampler但没有VAEDecode]
missing: []
members: [视频生成/图生视频/2012334757446684674.json, 视频生成/图生视频/2019749362657660929.json, 视频生成/图生视频/2016324555433840641.json, 视频生成/图生视频/2073298883534483458.json, 视频生成/图生视频/2013159959533461506.json, 视频生成/图生视频/2030196782323474433.json, 视频生成/图生视频/2011039306126725122.json, 视频生成/图生视频/2011355814191177729.json, 视频生成/图生视频/2011038713081499649.json, 视频生成/图生视频/2009647759535644673.json, 视频生成/图生视频/2011496236766994433.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_25

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/2012334757446684674.json、视频生成/图生视频/2019749362657660929.json、视频生成/图生视频/2016324555433840641.json、视频生成/图生视频/2073298883534483458.json、视频生成/图生视频/2013159959533461506.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：69%

## 共有节点

全部 11 个 workflow 都包含：
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
- `ManualSigmas` —— 10/11 个有
- `VAEDecodeTiled` —— 10/11 个有
- `ShowText|pysssss` —— 9/11 个有
- `easy showAnything` —— 9/11 个有
- `Int` —— 8/11 个有
- `JoinStrings` —— 8/11 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 8/11 个有
- `PrimitiveInt` —— 8/11 个有
- `Qwen3_VQA` —— 8/11 个有
- `TextInput_` —— 8/11 个有
- `VHS_VideoCombine` —— 8/11 个有
- `Fast Groups Bypasser (rgthree)` —— 7/11 个有
- `PreviewImage` —— 7/11 个有
- `ImageConcatMulti` —— 6/11 个有
- `LTXVFirstLastFrameControl_TTP` —— 6/11 个有
- `LTXVImgToVideoInplace` —— 5/11 个有
- `VRAMReserver` —— 5/11 个有
- `LayerUtility: PurgeVRAM V2` —— 4/11 个有
- `MemoryCleaner` —— 4/11 个有
- `ResizeImagesByLongerEdge` —— 4/11 个有
- `easy cleanGpuUsed` —— 4/11 个有
- `CreateVideo` —— 3/11 个有
- `ImageResizeKJv2` —— 3/11 个有
- `SaveVideo` —— 3/11 个有
- `PrimitiveFloat` —— 2/11 个有
- `SimpleMath+` —— 2/11 个有
- `FloatConstant` —— 1/11 个有
- `INTConstant` —— 1/11 个有
- `JWInteger` —— 1/11 个有
- `KSampler` —— 1/11 个有
- `LTXVMiddleFrame_TTP` —— 1/11 个有
- `LTXVSpatioTemporalTiledVAEDecode` —— 1/11 个有
- `RH_LLMAPI_Pro_Node` —— 1/11 个有
- `ShellAgentPluginOutputText` —— 1/11 个有
- `Text` —— 1/11 个有
- `VAEDecode` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 121 | 11 | 91% |
| 高度 | 25 | 25 - 25 | 11 | 100% |
| 采样步数 | 4 | - | 1 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 1 | 100% |
| 采样算法 | euler | - | 1 | 100% |
| 调度器 | simple | - | 1 | 100% |
| 重绘幅度 | 0.32 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |
| 发现KSampler但没有VAEDecode | 1/11 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 121，11 个样本，取值集中（一致性 91%）
- 高度 中位数 25，观测区间 25 - 25，11 个样本，取值集中（一致性 100%）
