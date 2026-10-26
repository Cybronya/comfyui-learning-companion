---
name: unknown_workflow_upscale_latent_upscale_lora_4
type: Unknown Workflow
frequency: 24
level: strong
coverage: 0.875125
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, CreateVideo, EmptyImage, EmptyLTXVLatentVideo, GetImageSize, ImageScaleBy, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVLatentUpsampler, LTXVScheduler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoraLoaderModelOnly, PrimitiveInt, RandomNoise, SamplerCustomAdvanced, SaveVideo]
problems: [Steps较低可能导致细节不足, 发现KSampler但没有VAEDecode]
missing: []
members: [视频生成/图生视频/超好用🔥氛围感长镜头-图生视频-自动提示词-直出1K_2053661040004612097.json, 视频生成/图生视频/超强图生视频  LTX2.3  最强开源_2046525999055114241.json, 视频生成/图生视频/超强开源模型 LTX2.3  图生视频 视频生成_2038160903216041986.json, 视频生成/图生视频/超长时间15秒图生视频 LTX2.3+Wan2.7首尾帧+图生视频+虚拟数字人美女模特_2064175660364550145.json, 视频生成/图生视频/马年视频_2052301410447970305.json, 视频生成/图生视频/高质量图生视频High-Quality Image-to-Video Generation_2093165338220392450.json, 视频生成/文生视频/LTX-2.3  文生视频 MV视频_2037159958583709697.json, 视频生成/文生视频/LTX-2.3-T2V-文生音视频_2029816055798964226.json, 视频生成/文生视频/LTX-2.3-图生视频_文生视频_2030340655863570434.json, 视频生成/文生视频/LTX-2.3-文生视频 长视频_2032729674383626241.json, 视频生成/文生视频/LTX2.3 15秒图生视频 氛围感长镜头 自动提示词 高清1K 舒缓的节奏，平和的运镜_2053275385588142082.json, 视频生成/文生视频/LTX2.3 文生视频 v1.1+VBVR_2030533262598213634.json, 视频生成/文生视频/LTX2.3 文生视频_2029978568398213122.json, 视频生成/文生视频/LTX2.3 文生视频工作流_2029878986880327681.json, 视频生成/文生视频/LTX2.3 文生视频工作流_2031938415188516866.json, 视频生成/文生视频/LTX2.3 超长时间15秒图生视频 氛围感长镜头 自动提示词 高清1K 舒缓的节奏，平和的运镜_2053284080829116417.json, 视频生成/文生视频/LTX2.3+Wan2.7首尾帧 图生视频+虚拟美女模特 +超长时间15秒图生视频_2058802888926908417.json, 视频生成/文生视频/LTX2.3-全自动提示词-文生视频_2031218445026594817.json, 视频生成/文生视频/LTX2.3-全自动提示词-文生视频_2070775557209546753.json, 视频生成/文生视频/LTX2.3_Wan2.7+超长时间15秒图生视频   首尾帧图生视频_2054066272861736962.json, 视频生成/文生视频/LTX2.3_Wan2.7首尾帧+图生视频 超长时间15秒图生视频_2054073713494118402.json, 视频生成/文生视频/LTX2.3图生视频 优化升级版 全自动提示词  模块化调优版_2054362110859194369.json, 视频生成/文生视频/LTX2.3图生视频—最佳效果_2062858202403926018.json, 视频生成/文生视频/双采样高质量图生视频 LTX2.3-单镜头可扩写提示词 高度遵从 运镜+动作+自动扩写 -高质量1K_2057269109406126081.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_4

> 由 `engine/knowledge_consolidation` 从 24 个 workflow 归纳得出（视频生成/图生视频/超好用🔥氛围感长镜头-图生视频-自动提示词-直出1K_2053661040004612097.json、视频生成/图生视频/超强图生视频  LTX2.3  最强开源_2046525999055114241.json、视频生成/图生视频/超强开源模型 LTX2.3  图生视频 视频生成_2038160903216041986.json、视频生成/图生视频/超长时间15秒图生视频 LTX2.3+Wan2.7首尾帧+图生视频+虚拟数字人美女模特_2064175660364550145.json、视频生成/图生视频/马年视频_2052301410447970305.json…）

- **类型**：Unknown Workflow
- **样本数**：24
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 24 个 workflow 都包含：
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
- `PrimitiveInt`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`

**可变部分**（部分 workflow 才有）：
- `KSampler` —— 23/24 个有
- `VAEDecode` —— 23/24 个有
- `LTXVImgToVideoInplace` —— 15/24 个有
- `LoadImage` —— 15/24 个有
- `PreviewAny` —— 15/24 个有
- `TextGenerateLTX2Prompt` —— 15/24 个有
- `DualCLIPLoader` —— 14/24 个有
- `CR Prompt Text` —— 13/24 个有
- `RH_LLMAPI_Pro_Node` —— 12/24 个有
- `easy int` —— 12/24 个有
- `easy showAnything` —— 12/24 个有
- `Int` —— 11/24 个有
- `PrimitiveFloat` —— 11/24 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 10/24 个有
- `MathExpression|pysssss` —— 10/24 个有
- `VAEDecodeTiled` —— 10/24 个有
- `easy float` —— 10/24 个有
- `Fast Groups Bypasser (rgthree)` —— 6/24 个有
- `LTXVPreprocess` —— 6/24 个有
- `ResizeImageMaskNode` —— 6/24 个有
- `ResizeImagesByLongerEdge` —— 6/24 个有
- `RH_AlibabaWan27ImageToVideo` —— 4/24 个有
- `SimpleMath+` —— 3/24 个有
- `CM_IntToFloat` —— 2/24 个有
- `Text` —— 2/24 个有
- `ManualSigmas` —— 1/24 个有
- `intToFloat _O` —— 1/24 个有
- `llama_cpp_instruct_adv` —— 1/24 个有
- `llama_cpp_model_loader` —— 1/24 个有
- `llama_cpp_parameters` —— 1/24 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 23 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 23 | 100% |
| 采样算法 | euler | - | 23 | 100% |
| 调度器 | simple | - | 23 | 100% |
| 重绘幅度 | 0.35 | 0.25 - 0.4 | 23 | 91% |
| 宽度 | 97 | 97 - 97 | 24 | 100% |
| 高度 | 25 | 25 - 25 | 24 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 24/24 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |
| 发现KSampler但没有VAEDecode | 1/24 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，23 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，23 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，23 个样本，一致性 100%
- 调度器 最常用 simple，23 个样本，一致性 100%
- 重绘幅度 中位数 0.35，观测区间 0.25 - 0.4，23 个样本，取值集中（一致性 91%）
- 宽度 中位数 97，观测区间 97 - 97，24 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，24 个样本，取值集中（一致性 100%）
- 高发问题（24/24 个样本）：Steps较低可能导致细节不足
