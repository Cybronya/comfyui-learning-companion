---
name: unknown_workflow_video_sampler_vae_83
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.709167
common_nodes: [BasicScheduler, ConditioningZeroOut, DualCLIPLoader, EmptyLTXVLatentVideo, GetNode, KSamplerSelect, LTX2SamplingPreviewOverride, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVImgToVideoInplaceKJ, LTXVPreprocess, LTXVSeparateAVLatent, LoadImage, PreviewImage, PrimitiveInt, SamplerCustom, SetNode, VAEDecode, VAELoaderKJ, VHS_VideoCombine, VisualizeSigmasKJ]
problems: []
missing: []
members: [图片生成/图生图/🎉老许Gary：LTX2.3丝滑长镜头运镜丨PromptRelay_VLM_2047365125039984641.json, 视频生成/图生视频/LTX2.3丝滑长镜头运镜_2047475119030800385.json, 视频生成/图生视频/LTX2.3美女摇摆！LTX2.3图生视频！_2050454214081556481.json, 视频生成/图生视频/LTX2.3美女爆破！LTX2.3图生视频！_2050514926795538434.json, 视频生成/图生视频/重大进步_连贯动作长视频生成(Prompt_relay_ltx2.3)_2046880656696807426.json, 视频生成/文生视频/LTX2.3_PromptRelay_VLM 高级工作流_2047601506693685249.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_83

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/🎉老许Gary：LTX2.3丝滑长镜头运镜丨PromptRelay_VLM_2047365125039984641.json、视频生成/图生视频/LTX2.3丝滑长镜头运镜_2047475119030800385.json、视频生成/图生视频/LTX2.3美女摇摆！LTX2.3图生视频！_2050454214081556481.json、视频生成/图生视频/LTX2.3美女爆破！LTX2.3图生视频！_2050514926795538434.json、视频生成/图生视频/重大进步_连贯动作长视频生成(Prompt_relay_ltx2.3)_2046880656696807426.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：71%

## 共有节点

全部 6 个 workflow 都包含：
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
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `PreviewImage`
- `PrimitiveInt`
- `SamplerCustom`
- `SetNode`
- `VAEDecode`
- `VAELoaderKJ`
- `VHS_VideoCombine`
- `VisualizeSigmasKJ`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 5/6 个有
- `MathExpression|pysssss` —— 5/6 个有
- `PathchSageAttentionKJ` —— 4/6 个有
- `PrimitiveStringMultiline` —— 4/6 个有
- `PromptRelayEncode` —— 4/6 个有
- `StringReplace` —— 4/6 个有
- `CR Float To Integer` —— 3/6 个有
- `CheckpointLoaderSimple` —— 3/6 个有
- `PrimitiveFloat` —— 3/6 个有
- `ShowText|pysssss` —— 3/6 个有
- `UNETLoader` —— 3/6 个有
- `AILab_QwenVL_Advanced` —— 2/6 个有
- `CR Text` —— 2/6 个有
- `INTConstant` —— 2/6 个有
- `ImageResizeKJv2` —— 2/6 个有
- `PromptRelayEncodeTimeline` —— 2/6 个有
- `ttN float` —— 2/6 个有
- `AILab_QwenVL` —— 1/6 个有
- `PreviewAny` —— 1/6 个有
- `PrimitiveString` —— 1/6 个有
- `RH_LLMAPI_NODE` —— 1/6 个有
- `RH_Translator` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 405 | 241 - 505 | 6 | 71% |
| 高度 | 25 | 25 - 50 | 6 | 65% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 405，观测区间 241 - 505，6 个样本
- 高度 中位数 25，观测区间 25 - 50，6 个样本
