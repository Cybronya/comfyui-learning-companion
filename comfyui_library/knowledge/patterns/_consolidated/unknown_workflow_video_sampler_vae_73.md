---
name: unknown_workflow_video_sampler_vae_73
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.770714
common_nodes: [BasicScheduler, ConditioningZeroOut, DualCLIPLoader, EmptyLTXVLatentVideo, KSamplerSelect, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVImgToVideoInplaceKJ, LTXVSeparateAVLatent, PathchSageAttentionKJ, PreviewImage, SamplerCustom, VAEDecode, VAELoaderKJ, VHS_VideoCombine, VisualizeSigmasKJ]
problems: []
missing: []
members: [视频生成/图生视频/LTX2.3 GGUF promptrelay 时序长效_2047485702841049089.json, 视频生成/图生视频/LTX2.3 Prompt时间戳控制视频生成_2050810161220071425.json, 视频生成/图生视频/LTX2.3-prompt_relay_simple(单图、多图)_2055227152429273089.json, 视频生成/图生视频/LTX2.3更高的遵从度-提示词对应连续动作_2046925023830614018.json, 视频生成/图生视频/ltx2.3 中继节点_2051154231129853954.json, 视频生成/图生视频/ltx2.3_prompt_relay_kj版_2059461166333775873.json, 视频生成/图生视频/本地开源免费，漫剧运镜长镜头1_2060459576042020865.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_73

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/LTX2.3 GGUF promptrelay 时序长效_2047485702841049089.json、视频生成/图生视频/LTX2.3 Prompt时间戳控制视频生成_2050810161220071425.json、视频生成/图生视频/LTX2.3-prompt_relay_simple(单图、多图)_2055227152429273089.json、视频生成/图生视频/LTX2.3更高的遵从度-提示词对应连续动作_2046925023830614018.json、视频生成/图生视频/ltx2.3 中继节点_2051154231129853954.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：77%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicScheduler`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `KSamplerSelect`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoInplaceKJ`
- `LTXVSeparateAVLatent`
- `PathchSageAttentionKJ`
- `PreviewImage`
- `SamplerCustom`
- `VAEDecode`
- `VAELoaderKJ`
- `VHS_VideoCombine`
- `VisualizeSigmasKJ`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 6/7 个有
- `LTX2SamplingPreviewOverride` —— 6/7 个有
- `LTXVPreprocess` —— 6/7 个有
- `LoadImage` —— 6/7 个有
- `LoraLoaderModelOnly` —— 6/7 个有
- `SetNode` —— 6/7 个有
- `UNETLoader` —— 6/7 个有
- `PromptRelayEncode` —— 5/7 个有
- `LoadAudio` —— 2/7 个有
- `PromptRelayEncodeTimeline` —— 2/7 个有
- `AudioCrop` —— 1/7 个有
- `INTConstant` —— 1/7 个有
- `Int` —— 1/7 个有
- `LTXVAudioVAEEncode` —— 1/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/7 个有
- `MultiImageLoader` —— 1/7 个有
- `SetLatentNoiseMask` —— 1/7 个有
- `SolidMask` —— 1/7 个有
- `Text` —— 1/7 个有
- `UnetLoaderGGUF` —— 1/7 个有
- `easy cleanGpuUsed` —— 1/7 个有
- `easy ifElse` —— 1/7 个有
- `easy mathInt` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 441 | 313 - 489 | 7 | 85% |
| 高度 | 25 | 24 - 25 | 7 | 99% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 441，观测区间 313 - 489，7 个样本，取值集中（一致性 85%）
- 高度 中位数 25，观测区间 24 - 25，7 个样本，取值集中（一致性 99%）
