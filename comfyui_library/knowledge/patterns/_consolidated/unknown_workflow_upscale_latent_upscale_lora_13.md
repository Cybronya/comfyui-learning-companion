---
name: unknown_workflow_upscale_latent_upscale_lora_13
type: Unknown Workflow
frequency: 15
level: strong
coverage: 0.880533
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, CreateVideo, EmptyImage, EmptyLTXVLatentVideo, GetImageSize, ImageScaleBy, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVLatentUpsampler, LTXVScheduler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoraLoaderModelOnly, RandomNoise, SamplerCustomAdvanced, SaveVideo]
problems: [Steps较低可能导致细节不足, 发现KSampler但没有VAEDecode]
missing: []
members: [视频生成/图生视频/超好用🔥氛围感长镜头-图生视频-自动提示词-直出1K_2053661040004612097.json, 视频生成/图生视频/超长时间15秒图生视频 LTX2.3+Wan2.7首尾帧+图生视频+虚拟数字人美女模特_2064175660364550145.json, 视频生成/图生视频/高质量图生视频High-Quality Image-to-Video Generation_2093165338220392450.json, 视频生成/文生视频/LTX-2.3-文生视频_2030171248226996226.json, 视频生成/文生视频/LTX-2文生视频工作流_2008796662071824386.json, 视频生成/文生视频/LTX-2文生视频工作流_2009245499412455426.json, 视频生成/文生视频/LTX-2文生视频提示词优化版_2009586018684510210.json, 视频生成/文生视频/LTX2.3 15秒图生视频 氛围感长镜头 自动提示词 高清1K 舒缓的节奏，平和的运镜_2053275385588142082.json, 视频生成/文生视频/LTX2.3 超长时间15秒图生视频 氛围感长镜头 自动提示词 高清1K 舒缓的节奏，平和的运镜_2053284080829116417.json, 视频生成/文生视频/LTX2.3+Wan2.7首尾帧 图生视频+虚拟美女模特 +超长时间15秒图生视频_2058802888926908417.json, 视频生成/文生视频/LTX2.3-全自动提示词-文生视频_2031218445026594817.json, 视频生成/文生视频/LTX2.3-全自动提示词-文生视频_2070775557209546753.json, 视频生成/文生视频/LTX2.3_Wan2.7+超长时间15秒图生视频   首尾帧图生视频_2054066272861736962.json, 视频生成/文生视频/LTX2.3_Wan2.7首尾帧+图生视频 超长时间15秒图生视频_2054073713494118402.json, 视频生成/文生视频/LTX2.3图生视频 优化升级版 全自动提示词  模块化调优版_2054362110859194369.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_13

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（视频生成/图生视频/超好用🔥氛围感长镜头-图生视频-自动提示词-直出1K_2053661040004612097.json、视频生成/图生视频/超长时间15秒图生视频 LTX2.3+Wan2.7首尾帧+图生视频+虚拟数字人美女模特_2064175660364550145.json、视频生成/图生视频/高质量图生视频High-Quality Image-to-Video Generation_2093165338220392450.json、视频生成/文生视频/LTX-2.3-文生视频_2030171248226996226.json、视频生成/文生视频/LTX-2文生视频工作流_2008796662071824386.json…）

- **类型**：Unknown Workflow
- **样本数**：15
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 15 个 workflow 都包含：
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
- `LTXVLatentUpsampler`
- `LTXVScheduler`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`

**可变部分**（部分 workflow 才有）：
- `PrimitiveInt` —— 14/15 个有
- `VAEDecode` —— 13/15 个有
- `KSampler` —— 12/15 个有
- `CR Prompt Text` —— 11/15 个有
- `RH_LLMAPI_Pro_Node` —— 11/15 个有
- `easy int` —— 11/15 个有
- `easy showAnything` —— 11/15 个有
- `Int` —— 10/15 个有
- `LTXVImgToVideoInplace` —— 9/15 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 9/15 个有
- `LoadImage` —— 9/15 个有
- `MathExpression|pysssss` —— 9/15 个有
- `easy float` —— 9/15 个有
- `PrimitiveFloat` —— 6/15 个有
- `VAEDecodeTiled` —— 6/15 个有
- `Fast Groups Bypasser (rgthree)` —— 5/15 个有
- `PreviewAny` —— 4/15 个有
- `RH_AlibabaWan27ImageToVideo` —— 4/15 个有
- `DualCLIPLoader` —— 3/15 个有
- `ManualSigmas` —— 3/15 个有
- `SimpleMath+` —— 3/15 个有
- `TextGenerateLTX2Prompt` —— 3/15 个有
- `CM_IntToFloat` —— 2/15 个有
- `Label (rgthree)` —— 2/15 个有
- `LTXVPreprocess` —— 1/15 个有
- `LayerUtility: PurgeVRAM V2` —— 1/15 个有
- `ResizeImageMaskNode` —— 1/15 个有
- `ResizeImagesByLongerEdge` —— 1/15 个有
- `Textbox` —— 1/15 个有
- `llama_cpp_instruct_adv` —— 1/15 个有
- `llama_cpp_model_loader` —— 1/15 个有
- `llama_cpp_parameters` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 12 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 12 | 100% |
| 采样算法 | euler | - | 12 | 100% |
| 调度器 | simple | - | 12 | 100% |
| 重绘幅度 | 0.35 | 0.35 - 0.4 | 12 | 94% |
| 宽度 | 97 | 97 - 97 | 15 | 100% |
| 高度 | 25 | 25 - 25 | 15 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 12/15 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |
| 发现KSampler但没有VAEDecode | 1/15 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，12 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，12 个样本，一致性 100%
- 调度器 最常用 simple，12 个样本，一致性 100%
- 重绘幅度 中位数 0.35，观测区间 0.35 - 0.4，12 个样本，取值集中（一致性 94%）
- 宽度 中位数 97，观测区间 97 - 97，15 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，15 个样本，取值集中（一致性 100%）
- 高发问题（12/15 个样本）：Steps较低可能导致细节不足
