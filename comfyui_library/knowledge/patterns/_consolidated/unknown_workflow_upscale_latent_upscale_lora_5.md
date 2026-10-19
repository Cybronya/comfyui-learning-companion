---
name: unknown_workflow_upscale_latent_upscale_lora_5
type: Unknown Workflow
frequency: 23
level: strong
coverage: 0.905087
common_nodes: [CFGGuider, CLIPTextEncode, EmptyImage, EmptyLTXVLatentVideo, GetImageSize, ImageScaleBy, KSamplerSelect, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVLatentUpsampler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoraLoaderModelOnly, ManualSigmas, PrimitiveFloat, PrimitiveInt, RandomNoise, SamplerCustomAdvanced, VAEDecodeTiled]
problems: []
missing: []
members: [视频生成/图生视频/2072859139281342465.json, 视频生成/文生视频/LTX-2 文生视频官方版_2008956000639918082.json, 视频生成/文生视频/LTX-2 文生视频官方版_2073297832060211201.json, 视频生成/文生视频/LTX-2 文生视频运镜控制_2073298030320775169.json, 视频生成/文生视频/LTX2 文生视频_2008738820421853186.json, 视频生成/文生视频/LTX2 文生视频原版_2008509004686823425.json, 视频生成/文生视频/LTX2.0文生视频_2008728323093962754.json, 视频生成/文生视频/LTX2.0文生视频_2021110563987791873.json, 视频生成/文生视频/LTX2.3文生视频 ai提示词优化增强版 提示词ai优化版文生视频_2029978716578779138.json, 视频生成/文生视频/LTX2.3文生视频_2059534082203283458.json, 视频生成/文生视频/LTX2.3文生视频_2065077242186788866.json, 视频生成/文生视频/LTX2.3文生视频_2072522403787399169.json, 视频生成/文生视频/LTX2.3文生视频【优化版3】_2056732469243760641.json, 视频生成/文生视频/LTX2.3文生视频【优化版】_2029959325606744066.json, 视频生成/文生视频/LTX2.3文生视频【优化版】_2056288371739287553.json, 视频生成/文生视频/LTX2.3文生视频【优化版】_2071227330307125249.json, 视频生成/文生视频/LTX2.3文生视频【切镜头优化版4】_2065674485692461057.json, 视频生成/文生视频/LTX2.3文生视频【切镜头优化版4】_2066698425961369602.json, 视频生成/文生视频/LTX2.3文生视频【切镜头优化版4】_2071506679061106690.json, 视频生成/文生视频/LTX2.3文生视频【切镜头优化版4】_2071853403160014850.json, 视频生成/文生视频/LTX2.3文生视频【切镜头优化版】_2066428134618124289.json, 视频生成/文生视频/LTX2.3文生视频【根据时间写剧情】_2067564577201672194.json, 视频生成/文生视频/LTX2.3文生视频： ai提示词优化增强版 提示词ai优化版文生视频工作流_2030140893503692802.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_5

> 由 `engine/knowledge_consolidation` 从 23 个 workflow 归纳得出（视频生成/图生视频/2072859139281342465.json、视频生成/文生视频/LTX-2 文生视频官方版_2008956000639918082.json、视频生成/文生视频/LTX-2 文生视频官方版_2073297832060211201.json、视频生成/文生视频/LTX-2 文生视频运镜控制_2073298030320775169.json、视频生成/文生视频/LTX2 文生视频_2008738820421853186.json…）

- **类型**：Unknown Workflow
- **样本数**：23
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 23 个 workflow 都包含：
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
- `LTXVEmptyLatentAudio`
- `LTXVLatentUpsampler`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PrimitiveFloat`
- `PrimitiveInt`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `VAEDecodeTiled`

**可变部分**（部分 workflow 才有）：
- `LTXVScheduler` —— 21/23 个有
- `easy cleanGpuUsed` —— 21/23 个有
- `CR Text` —— 18/23 个有
- `Int` —— 18/23 个有
- `PIP_IntegerCalculator` —— 18/23 个有
- `VHS_VideoCombine` —— 18/23 个有
- `VRAMReserver` —— 18/23 个有
- `easy convertAnything` —— 18/23 个有
- `CheckpointLoaderSimple` —— 14/23 个有
- `DualCLIPLoader` —— 14/23 个有
- `LTX2_NAG` —— 14/23 个有
- `LTXAVTextEncoderLoader` —— 14/23 个有
- `LTXVAudioVAELoader` —— 14/23 个有
- `UNETLoader` —— 14/23 个有
- `VAELoaderKJ` —— 14/23 个有
- `CreateVideo` —— 13/23 个有
- `LTXVCropGuides` —— 13/23 个有
- `SaveVideo` —— 13/23 个有
- `CR String To Combo` —— 10/23 个有
- `CR Text Concatenate` —— 10/23 个有
- `Display Any (rgthree)` —— 10/23 个有
- `ImpactSwitch` —— 10/23 个有
- `LTXICLoRALoaderModelOnly` —— 10/23 个有
- `RH_LLMAPI_NODE` —— 10/23 个有
- `ttN concat` —— 10/23 个有
- `BasicScheduler` —— 9/23 个有
- `SaveAudio` —— 9/23 个有
- `LTXVChunkFeedForward` —— 4/23 个有
- `TextNode` —— 2/23 个有
- `VideoSizePresetNode` —— 2/23 个有
- `Fast Groups Muter (rgthree)` —— 1/23 个有
- `ImpactStringSelector` —— 1/23 个有
- `ModelscopeApiTextGenerationNode` —— 1/23 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 121 | 97 - 121 | 23 | 91% |
| 高度 | 25 | 25 - 25 | 23 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 121，观测区间 97 - 121，23 个样本，取值集中（一致性 91%）
- 高度 中位数 25，观测区间 25 - 25，23 个样本，取值集中（一致性 100%）
