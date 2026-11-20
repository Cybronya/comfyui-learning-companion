---
name: unknown_workflow_video_upscale_latent_upscale_40
type: Unknown Workflow
frequency: 10
level: strong
coverage: 0.9335
common_nodes: [CFGGuider, CLIPTextEncode, CR Text, CR Text Concatenate, Display Any (rgthree), EmptyImage, EmptyLTXVLatentVideo, GetImageSize, ImageScaleBy, ImpactSwitch, Int, KSamplerSelect, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVLatentUpsampler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoraLoaderModelOnly, ManualSigmas, PIP_IntegerCalculator, PrimitiveFloat, PrimitiveInt, RH_LLMAPI_NODE, RandomNoise, SamplerCustomAdvanced, VAEDecodeTiled, VHS_VideoCombine, VRAMReserver, easy cleanGpuUsed, easy convertAnything, ttN concat]
problems: []
missing: []
members: [视频生成/文生视频/LTX2.0文生视频_2008728323093962754.json, 视频生成/文生视频/LTX2.0文生视频_2021110563987791873.json, 视频生成/文生视频/LTX2.3文生视频 ai提示词优化增强版 提示词ai优化版文生视频_2029978716578779138.json, 视频生成/文生视频/LTX2.3文生视频_2059534082203283458.json, 视频生成/文生视频/LTX2.3文生视频_2065077242186788866.json, 视频生成/文生视频/LTX2.3文生视频【优化版3】_2056732469243760641.json, 视频生成/文生视频/LTX2.3文生视频【优化版】_2029959325606744066.json, 视频生成/文生视频/LTX2.3文生视频【优化版】_2056288371739287553.json, 视频生成/文生视频/LTX2.3文生视频【优化版】_2071227330307125249.json, 视频生成/文生视频/LTX2.3文生视频： ai提示词优化增强版 提示词ai优化版文生视频工作流_2030140893503692802.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_40

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/文生视频/LTX2.0文生视频_2008728323093962754.json、视频生成/文生视频/LTX2.0文生视频_2021110563987791873.json、视频生成/文生视频/LTX2.3文生视频 ai提示词优化增强版 提示词ai优化版文生视频_2029978716578779138.json、视频生成/文生视频/LTX2.3文生视频_2059534082203283458.json、视频生成/文生视频/LTX2.3文生视频_2065077242186788866.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 10 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CR Text`
- `CR Text Concatenate`
- `Display Any (rgthree)`
- `EmptyImage`
- `EmptyLTXVLatentVideo`
- `GetImageSize`
- `ImageScaleBy`
- `ImpactSwitch`
- `Int`
- `KSamplerSelect`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVEmptyLatentAudio`
- `LTXVLatentUpsampler`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PIP_IntegerCalculator`
- `PrimitiveFloat`
- `PrimitiveInt`
- `RH_LLMAPI_NODE`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `VAEDecodeTiled`
- `VHS_VideoCombine`
- `VRAMReserver`
- `easy cleanGpuUsed`
- `easy convertAnything`
- `ttN concat`

**可变部分**（部分 workflow 才有）：
- `CR String To Combo` —— 9/10 个有
- `CheckpointLoaderSimple` —— 9/10 个有
- `LTXAVTextEncoderLoader` —— 9/10 个有
- `LTXVAudioVAELoader` —— 9/10 个有
- `SaveAudio` —— 9/10 个有
- `LTXVScheduler` —— 8/10 个有
- `DualCLIPLoader` —— 6/10 个有
- `LTX2_NAG` —— 6/10 个有
- `UNETLoader` —— 6/10 个有
- `VAELoaderKJ` —— 6/10 个有
- `LTXVChunkFeedForward` —— 4/10 个有
- `LTXICLoRALoaderModelOnly` —— 2/10 个有
- `TextNode` —— 2/10 个有
- `VideoSizePresetNode` —— 2/10 个有
- `BasicScheduler` —— 1/10 个有
- `Fast Groups Muter (rgthree)` —— 1/10 个有
- `ModelscopeApiTextGenerationNode` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 121 | 121 - 121 | 10 | 100% |
| 高度 | 25 | 25 - 25 | 10 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 121，观测区间 121 - 121，10 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，10 个样本，取值集中（一致性 100%）
