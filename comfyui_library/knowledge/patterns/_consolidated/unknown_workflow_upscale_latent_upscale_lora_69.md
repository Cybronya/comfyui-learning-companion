---
name: unknown_workflow_upscale_latent_upscale_lora_69
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.8906
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, CreateVideo, EmptyImage, EmptyLTXVLatentVideo, GetImageSize, ImageScaleBy, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocess, LTXVScheduler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, LoraLoaderModelOnly, PrimitiveInt, RandomNoise, ResizeImagesByLongerEdge, SamplerCustomAdvanced, SaveVideo, VAEDecode, easy cleanGpuUsed]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/【Supermate 稳定版2】ltx2单图原音驱动工作流_2012047557043687425.json, 视频生成/图生视频/【Supermate】LTX2.3单图视频(Gemma4））-还在调整_2048744630820278273.json, 视频生成/图生视频/【Supermate】LTX2.3单图视频(无反推）_2042871628979249154.json, 视频生成/图生视频/【Supermate】优化LTX-2 图生视频 （Plus会员版）_2008554221829885954.json, 视频生成/图生视频/【老金驿站】LTX2-19B一镜聚焦工作流_2014309275279036418.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_69

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/【Supermate 稳定版2】ltx2单图原音驱动工作流_2012047557043687425.json、视频生成/图生视频/【Supermate】LTX2.3单图视频(Gemma4））-还在调整_2048744630820278273.json、视频生成/图生视频/【Supermate】LTX2.3单图视频(无反推）_2042871628979249154.json、视频生成/图生视频/【Supermate】优化LTX-2 图生视频 （Plus会员版）_2008554221829885954.json、视频生成/图生视频/【老金驿站】LTX2-19B一镜聚焦工作流_2014309275279036418.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 5 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `CreateVideo`
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
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVScheduler`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PrimitiveInt`
- `RandomNoise`
- `ResizeImagesByLongerEdge`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `VAEDecode`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `ManualSigmas` —— 3/5 个有
- `ImageResizeKJv2` —— 2/5 个有
- `Int` —— 2/5 个有
- `KSampler` —— 2/5 个有
- `Label (rgthree)` —— 2/5 个有
- `PreviewAny` —— 2/5 个有
- `ResizeImageMaskNode` —— 2/5 个有
- `Text` —— 2/5 个有
- `easy saveText` —— 2/5 个有
- `easy showAnything` —— 2/5 个有
- `llama_cpp_instruct_adv` —— 2/5 个有
- `llama_cpp_model_loader` —— 2/5 个有
- `llama_cpp_parameters` —— 2/5 个有
- `CR Prompt Text` —— 1/5 个有
- `MemoryCleaner` —— 1/5 个有
- `PreviewImage` —— 1/5 个有
- `Resize` —— 1/5 个有
- `easy promptConcat` —— 1/5 个有
- `easy seed` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 5 | 100% |
| 高度 | 25 | 25 - 25 | 5 | 100% |
| 采样步数 | 4 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 0.35 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，5 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，5 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 0.35，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
