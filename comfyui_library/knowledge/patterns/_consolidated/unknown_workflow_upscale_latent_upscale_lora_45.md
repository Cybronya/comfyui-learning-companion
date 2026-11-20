---
name: unknown_workflow_upscale_latent_upscale_lora_45
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.893
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, CreateVideo, EmptyLTXVLatentVideo, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVLatentUpsampler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoraLoaderModelOnly, RandomNoise, SamplerCustomAdvanced, SaveVideo]
problems: [Steps较低可能导致细节不足, 发现KSampler但没有VAEDecode]
missing: []
members: [视频生成/图生视频/LTX 2.3 自动生成播客视频_2044772850472591362.json, 视频生成/图生视频/LTX-2 文生视频 ComfyUI官方流_2008477289973030914.json, 视频生成/图生视频/LTX-2 音画同步训练lora多种搭建方式工作流（防音频过拟合）_2012140284192235522.json, 视频生成/图生视频/LTX-2.3-图生视频_2030196782323474433.json, 视频生成/图生视频/LTX-2图生视频工作流_2008838542486671361.json, 视频生成/图生视频/LTX-2图生视频工作流_2009242619980812289.json, 视频生成/图生视频/LTX-2高动态图生视频工作流_2009601705482129409.json, 视频生成/图生视频/LTX2.3图生视频_2029943442415034369.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_45

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/LTX 2.3 自动生成播客视频_2044772850472591362.json、视频生成/图生视频/LTX-2 文生视频 ComfyUI官方流_2008477289973030914.json、视频生成/图生视频/LTX-2 音画同步训练lora多种搭建方式工作流（防音频过拟合）_2012140284192235522.json、视频生成/图生视频/LTX-2.3-图生视频_2030196782323474433.json、视频生成/图生视频/LTX-2图生视频工作流_2008838542486671361.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 8 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `CreateVideo`
- `EmptyLTXVLatentVideo`
- `KSamplerSelect`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVLatentUpsampler`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`

**可变部分**（部分 workflow 才有）：
- `EmptyImage` —— 7/8 个有
- `GetImageSize` —— 7/8 个有
- `ImageScaleBy` —— 7/8 个有
- `LTXVScheduler` —— 7/8 个有
- `PrimitiveInt` —— 7/8 个有
- `LTXVImgToVideoInplace` —— 6/8 个有
- `LTXVPreprocess` —— 6/8 个有
- `LoadImage` —— 6/8 个有
- `ManualSigmas` —— 6/8 个有
- `ResizeImagesByLongerEdge` —— 5/8 个有
- `VAEDecode` —— 5/8 个有
- `PrimitiveFloat` —— 4/8 个有
- `VAEDecodeTiled` —— 4/8 个有
- `ImageResizeKJv2` —— 3/8 个有
- `KSampler` —— 2/8 个有
- `Label (rgthree)` —— 2/8 个有
- `PreviewAny` —— 2/8 个有
- `RH_LLMAPI_Pro_Node` —— 2/8 个有
- `easy cleanGpuUsed` —— 2/8 个有
- `BasicScheduler` —— 1/8 个有
- `CM_FloatToInt` —— 1/8 个有
- `Float to Int` —— 1/8 个有
- `Int` —— 1/8 个有
- `JWStringReplace` —— 1/8 个有
- `LTXVSpatioTemporalTiledVAEDecode` —— 1/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/8 个有
- `PrimitiveStringMultiline` —— 1/8 个有
- `RH_LLMAPI_NODE` —— 1/8 个有
- `ResizeImageMaskNode` —— 1/8 个有
- `RunningHub Deepcleaner` —— 1/8 个有
- `SimpleMath+` —— 1/8 个有
- `Text _O` —— 1/8 个有
- `TextInput_` —— 1/8 个有
- `Textbox` —— 1/8 个有
- `easy showAnything` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 8 | 100% |
| 高度 | 25 | 25 - 25 | 8 | 100% |
| 采样步数 | 4 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 0.335 | - | 2 | 96% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |
| 发现KSampler但没有VAEDecode | 1/8 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，8 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，8 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 0.335，样本不足，未给区间，2 个样本，取值集中（一致性 96%）
