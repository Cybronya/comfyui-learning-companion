---
name: unknown_workflow_upscale_latent_upscale_lora_15
type: Unknown Workflow
frequency: 14
level: strong
coverage: 0.885071
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, CreateVideo, EmptyImage, EmptyLTXVLatentVideo, GetImageSize, ImageScaleBy, KSampler, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVLatentUpsampler, LTXVScheduler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoraLoaderModelOnly, PrimitiveInt, RandomNoise, SamplerCustomAdvanced, SaveVideo, VAEDecode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/2053661040004612097.json, 视频生成/图生视频/2064175660364550145.json, 视频生成/图生视频/高质量图生视频High-Quality Image-to-Video Generation_2093165338220392450.json, 视频生成/文生视频/LTX2.3 15秒图生视频 氛围感长镜头 自动提示词 高清1K 舒缓的节奏，平和的运镜_2053275385588142082.json, 视频生成/文生视频/LTX2.3 超长时间15秒图生视频 氛围感长镜头 自动提示词 高清1K 舒缓的节奏，平和的运镜_2053284080829116417.json, 视频生成/文生视频/LTX2.3+Wan2.7首尾帧 图生视频+虚拟美女模特 +超长时间15秒图生视频_2058802888926908417.json, 视频生成/文生视频/LTX2.3-全自动提示词-文生视频_2031218445026594817.json, 视频生成/文生视频/LTX2.3-全自动提示词-文生视频_2070775557209546753.json, 视频生成/文生视频/LTX2.3-文生视频_2066069178989240321.json, 视频生成/文生视频/LTX2.3_Wan2.7+超长时间15秒图生视频   首尾帧图生视频_2054066272861736962.json, 视频生成/文生视频/LTX2.3_Wan2.7首尾帧+图生视频 超长时间15秒图生视频_2054073713494118402.json, 视频生成/文生视频/LTX2.3图生视频 优化升级版 全自动提示词  模块化调优版_2054362110859194369.json, 视频生成/文生视频/LTX2.3图生视频—最佳效果_2062858202403926018.json, 视频生成/文生视频/双采样高质量图生视频 LTX2.3-单镜头可扩写提示词 高度遵从 运镜+动作+自动扩写 -高质量1K_2057269109406126081.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_15

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（视频生成/图生视频/2053661040004612097.json、视频生成/图生视频/2064175660364550145.json、视频生成/图生视频/高质量图生视频High-Quality Image-to-Video Generation_2093165338220392450.json、视频生成/文生视频/LTX2.3 15秒图生视频 氛围感长镜头 自动提示词 高清1K 舒缓的节奏，平和的运镜_2053275385588142082.json、视频生成/文生视频/LTX2.3 超长时间15秒图生视频 氛围感长镜头 自动提示词 高清1K 舒缓的节奏，平和的运镜_2053284080829116417.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 14 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `CreateVideo`
- `EmptyImage`
- `EmptyLTXVLatentVideo`
- `GetImageSize`
- `ImageScaleBy`
- `KSampler`
- `KSamplerSelect`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVLatentUpsampler`
- `LTXVScheduler`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoraLoaderModelOnly`
- `PrimitiveInt`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 12/14 个有
- `easy int` —— 12/14 个有
- `easy showAnything` —— 12/14 个有
- `Int` —— 11/14 个有
- `LTXVImgToVideoInplace` —— 11/14 个有
- `LoadImage` —— 11/14 个有
- `RH_LLMAPI_Pro_Node` —— 11/14 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 10/14 个有
- `MathExpression|pysssss` —— 10/14 个有
- `easy float` —— 10/14 个有
- `Fast Groups Bypasser (rgthree)` —— 6/14 个有
- `DualCLIPLoader` —— 5/14 个有
- `PreviewAny` —— 5/14 个有
- `TextGenerateLTX2Prompt` —— 5/14 个有
- `PrimitiveFloat` —— 4/14 个有
- `RH_AlibabaWan27ImageToVideo` —— 4/14 个有
- `SimpleMath+` —— 3/14 个有
- `VAEDecodeTiled` —— 3/14 个有
- `CM_IntToFloat` —— 2/14 个有
- `LTXVPreprocess` —— 2/14 个有
- `ResizeImageMaskNode` —— 2/14 个有
- `ResizeImagesByLongerEdge` —— 2/14 个有
- `Seed (rgthree)` —— 1/14 个有
- `intToFloat _O` —— 1/14 个有
- `llama_cpp_instruct_adv` —— 1/14 个有
- `llama_cpp_model_loader` —— 1/14 个有
- `llama_cpp_parameters` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 14 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 14 | 100% |
| 采样算法 | euler | - | 14 | 100% |
| 调度器 | simple | - | 14 | 100% |
| 重绘幅度 | 0.35 | 0.25 - 0.4 | 14 | 90% |
| 宽度 | 97 | 97 - 97 | 14 | 100% |
| 高度 | 25 | 25 - 25 | 14 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 14/14 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，14 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，14 个样本，一致性 100%
- 调度器 最常用 simple，14 个样本，一致性 100%
- 重绘幅度 中位数 0.35，观测区间 0.25 - 0.4，14 个样本，取值集中（一致性 90%）
- 宽度 中位数 97，观测区间 97 - 97，14 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，14 个样本，取值集中（一致性 100%）
- 高发问题（14/14 个样本）：Steps较低可能导致细节不足
