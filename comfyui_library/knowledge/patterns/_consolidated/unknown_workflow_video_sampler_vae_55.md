---
name: unknown_workflow_video_sampler_vae_55
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.724125
common_nodes: [BasicScheduler, ConditioningZeroOut, DualCLIPLoader, EmptyLTXVLatentVideo, GetNode, KSamplerSelect, LTX2SamplingPreviewOverride, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVImgToVideoInplaceKJ, LTXVSeparateAVLatent, PreviewImage, SamplerCustom, SetNode, VAEDecode, VAELoaderKJ, VHS_VideoCombine, VisualizeSigmasKJ]
problems: []
missing: []
members: [图片生成/图生图/🎉老许Gary：LTX2.3丝滑长镜头运镜丨PromptRelay_VLM_2047365125039984641.json, 视频生成/图生视频/LTX2.3 Prompt时间戳控制视频生成_2050810161220071425.json, 视频生成/图生视频/LTX2.3-prompt_relay_simple(单图、多图)_2055227152429273089.json, 视频生成/图生视频/LTX2.3丝滑长镜头运镜_2047475119030800385.json, 视频生成/图生视频/LTX2.3更高的遵从度-提示词对应连续动作_2046925023830614018.json, 视频生成/图生视频/LTX2.3美女摇摆！LTX2.3图生视频！_2050454214081556481.json, 视频生成/图生视频/LTX2.3美女爆破！LTX2.3图生视频！_2050514926795538434.json, 视频生成/文生视频/LTX2.3_PromptRelay_VLM 高级工作流_2047601506693685249.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_55

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/🎉老许Gary：LTX2.3丝滑长镜头运镜丨PromptRelay_VLM_2047365125039984641.json、视频生成/图生视频/LTX2.3 Prompt时间戳控制视频生成_2050810161220071425.json、视频生成/图生视频/LTX2.3-prompt_relay_simple(单图、多图)_2055227152429273089.json、视频生成/图生视频/LTX2.3丝滑长镜头运镜_2047475119030800385.json、视频生成/图生视频/LTX2.3更高的遵从度-提示词对应连续动作_2046925023830614018.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：72%

## 共有节点

全部 8 个 workflow 都包含：
- `BasicScheduler`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `KSamplerSelect`
- `LTX2SamplingPreviewOverride`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoInplaceKJ`
- `LTXVSeparateAVLatent`
- `PreviewImage`
- `SamplerCustom`
- `SetNode`
- `VAEDecode`
- `VAELoaderKJ`
- `VHS_VideoCombine`
- `VisualizeSigmasKJ`

**可变部分**（部分 workflow 才有）：
- `LTXVPreprocess` —— 7/8 个有
- `LoadImage` —— 7/8 个有
- `LoraLoaderModelOnly` —— 7/8 个有
- `PathchSageAttentionKJ` —— 6/8 个有
- `PromptRelayEncode` —— 6/8 个有
- `MathExpression|pysssss` —— 5/8 个有
- `PrimitiveInt` —— 5/8 个有
- `UNETLoader` —— 5/8 个有
- `CR Float To Integer` —— 3/8 个有
- `CheckpointLoaderSimple` —— 3/8 个有
- `PrimitiveFloat` —— 3/8 个有
- `PrimitiveStringMultiline` —— 3/8 个有
- `ShowText|pysssss` —— 3/8 个有
- `StringReplace` —— 3/8 个有
- `AILab_QwenVL_Advanced` —— 2/8 个有
- `CR Text` —— 2/8 个有
- `INTConstant` —— 2/8 个有
- `ImageResizeKJv2` —— 2/8 个有
- `PromptRelayEncodeTimeline` —— 2/8 个有
- `ttN float` —— 2/8 个有
- `AILab_QwenVL` —— 1/8 个有
- `Int` —— 1/8 个有
- `MultiImageLoader` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 465 | 305 - 505 | 8 | 79% |
| 高度 | 25 | 25 - 50 | 8 | 65% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 465，观测区间 305 - 505，8 个样本
- 高度 中位数 25，观测区间 25 - 50，8 个样本
