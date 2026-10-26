---
name: text_to_image_upscale_latent_upscale_lora_10
type: Text To Image
frequency: 4
level: strong
coverage: 0.8445
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, CR String To Combo, CR Text, CR Text Concatenate, CheckpointLoaderSimple, Display Any (rgthree), DualCLIPLoader, EmptyImage, EmptyLTXVLatentVideo, EmptyLatentImage, GetImageSize, ImageScaleBy, ImpactSwitch, Int, JjkText, KSampler, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVLatentUpsampler, LTXVScheduler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoraLoaderModelOnly, ManualSigmas, PrimitiveInt, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeTiled, VAELoader, VAELoaderKJ, VRAMReserver, easy cleanGpuUsed, easy convertAnything, solarL_SaveImagesToZip, ttN concat]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/反推提示词/LTX2.3优化版文生视频，反推提示词加持出片更省心_2110464347188322305.json, 图片生成/反推提示词/LTX2.3文生视频优化版 提示词三选一处理生成工具_2113400928278769666.json, 视频生成/图生视频/LTX2.3图生视频蒸馏dev版｜提示词优化加持｜AI短视频短剧生成利器_2102618740818010113.json, 视频生成/文生视频/LTX2.3优化版文生视频，反推提示词加持出片更省心_2113461211319853057.json]
source: knowledge_consolidation
---

# text_to_image_upscale_latent_upscale_lora_10

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/反推提示词/LTX2.3优化版文生视频，反推提示词加持出片更省心_2110464347188322305.json、图片生成/反推提示词/LTX2.3文生视频优化版 提示词三选一处理生成工具_2113400928278769666.json、视频生成/图生视频/LTX2.3图生视频蒸馏dev版｜提示词优化加持｜AI短视频短剧生成利器_2102618740818010113.json、视频生成/文生视频/LTX2.3优化版文生视频，反推提示词加持出片更省心_2113461211319853057.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR String To Combo`
- `CR Text`
- `CR Text Concatenate`
- `CheckpointLoaderSimple`
- `Display Any (rgthree)`
- `DualCLIPLoader`
- `EmptyImage`
- `EmptyLTXVLatentVideo`
- `EmptyLatentImage`
- `GetImageSize`
- `ImageScaleBy`
- `ImpactSwitch`
- `Int`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVEmptyLatentAudio`
- `LTXVLatentUpsampler`
- `LTXVScheduler`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PrimitiveInt`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAELoader`
- `VAELoaderKJ`
- `VRAMReserver`
- `easy cleanGpuUsed`
- `easy convertAnything`
- `solarL_SaveImagesToZip`
- `ttN concat`

**可变部分**（部分 workflow 才有）：
- `LTX2_NAG` —— 3/4 个有
- `PIP_IntegerCalculator` —— 3/4 个有
- `PrimitiveFloat` —— 3/4 个有
- `RH_LLMAPI_NODE` —— 3/4 个有
- `SaveAudio` —— 3/4 个有
- `SaveImage` —— 3/4 个有
- `VHS_VideoCombine` —— 3/4 个有
- `孤海注释` —— 3/4 个有
- `Any To String (mtb)` —— 1/4 个有
- `CR Value` —— 1/4 个有
- `CreateVideo` —— 1/4 个有
- `Fast Groups Muter (rgthree)` —— 1/4 个有
- `GetNode` —— 1/4 个有
- `LTXVChunkFeedForward` —— 1/4 个有
- `LTXVCropGuides` —— 1/4 个有
- `LTXVImgToVideoInplace` —— 1/4 个有
- `LTXVPreprocess` —— 1/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/4 个有
- `LoadImage` —— 1/4 个有
- `MathExpression|pysssss` —— 1/4 个有
- `PreviewImage` —— 1/4 个有
- `ResizeImagesByLongerEdge` —— 1/4 个有
- `SaveVideo` —— 1/4 个有
- `SetNode` —— 1/4 个有
- `ShowText|pysssss` —— 1/4 个有
- `easy int` —— 1/4 个有
- `llama_cpp_instruct_adv` —— 1/4 个有
- `llama_cpp_model_loader` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 4 | 100% |
| 高度 | 80 | 80 - 80 | 4 | 100% |
| 采样步数 | 4 | 4 - 4 | 4 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 4 | 100% |
| 采样算法 | er_sde | - | 4 | 100% |
| 调度器 | beta | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，4 个样本，一致性 100%
- 调度器 最常用 beta，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
