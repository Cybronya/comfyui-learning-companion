---
name: unknown_workflow_video_lora_sampler_24
type: Unknown Workflow
frequency: 28
level: strong
coverage: 0.775107
common_nodes: [BasicScheduler, DualCLIPLoader, EmptyLTXVLatentVideo, KSamplerSelect, LTX2SamplingPreviewOverride, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVImgToVideoInplaceKJ, LTXVPreprocess, LTXVSeparateAVLatent, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, PathchSageAttentionKJ, SamplerCustom, VAEDecode, VAELoaderKJ, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/2053376234775687170.json, 视频生成/图生视频/2053287053370118146.json, 视频生成/图生视频/2053287557496098818.json, 视频生成/图生视频/2053292180520878081.json, 视频生成/图生视频/2051826547308417026.json, 视频生成/图生视频/2054471149064597506.json, 视频生成/图生视频/2054525634252165121.json, 视频生成/图生视频/2070413005359243266.json, 视频生成/图生视频/2054480431743021058.json, 视频生成/图生视频/2054510424275595265.json, 视频生成/图生视频/2055122108715413506.json, 视频生成/图生视频/Ltx2.3 Prompt Relay Smart + VBVR 390K单图参考精准控制图生视频_2104521975828934658.json, 视频生成/图生视频/2053633709424820226.json, 视频生成/图生视频/2052624355913420802.json, 视频生成/图生视频/2058542604932968449.json, 视频生成/图生视频/2054244112395710465.json, 视频生成/图生视频/2072098418612326401.json, 视频生成/图生视频/2054758964251897857.json, 视频生成/图生视频/2054743040564178946.json, 视频生成/图生视频/2054742077061246978.json, 视频生成/图生视频/2052684073478434818.json, 视频生成/图生视频/2059634224981958657.json, 视频生成/图生视频/2055899428757753858.json, 视频生成/图生视频/2051845619093909505.json, 视频生成/图生视频/2052580214886154241.json, 视频生成/图生视频/2053103007134429186.json, 视频生成/图生视频/2047231171125317633.json, 视频生成/图生视频/2052683608971849729.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_24

> 由 `engine/knowledge_consolidation` 从 28 个 workflow 归纳得出（视频生成/图生视频/2053376234775687170.json、视频生成/图生视频/2053287053370118146.json、视频生成/图生视频/2053287557496098818.json、视频生成/图生视频/2053292180520878081.json、视频生成/图生视频/2051826547308417026.json…）

- **类型**：Unknown Workflow
- **样本数**：28
- **可信度**：强结论
- **平均知识覆盖**：78%

## 共有节点

全部 28 个 workflow 都包含：
- `BasicScheduler`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `KSamplerSelect`
- `LTX2SamplingPreviewOverride`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoInplaceKJ`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PathchSageAttentionKJ`
- `SamplerCustom`
- `VAEDecode`
- `VAELoaderKJ`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 27/28 个有
- `GetNode` —— 27/28 个有
- `PreviewImage` —— 27/28 个有
- `SetNode` —— 27/28 个有
- `VisualizeSigmasKJ` —— 27/28 个有
- `UNETLoader` —— 26/28 个有
- `ConditioningZeroOut` —— 25/28 个有
- `PromptRelaySmartEncode` —— 20/28 个有
- `JWInteger` —— 19/28 个有
- `Int` —— 9/28 个有
- `SimpleMath+` —— 9/28 个有
- `CLIPTextEncode` —— 8/28 个有
- `PromptRelayEncode` —— 7/28 个有
- `easy showAnything` —— 7/28 个有
- `RH_LLMAPI_Pro_Node` —— 5/28 个有
- `Float` —— 3/28 个有
- `CheckpointLoaderSimple` —— 2/28 个有
- `easy seed` —— 2/28 个有
- `DF_Integer` —— 1/28 个有
- `Float to Int` —— 1/28 个有
- `MathExpression|pysssss` —— 1/28 个有
- `PrimitiveBoolean` —— 1/28 个有
- `PrimitiveFloat` —— 1/28 个有
- `easy getNode` —— 1/28 个有
- `easy ifElse` —— 1/28 个有
- `easy positive` —— 1/28 个有
- `easy setNode` —— 1/28 个有
- `ttN float` —— 1/28 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 489 | 489 - 489 | 28 | 100% |
| 高度 | 25 | 25 - 30 | 28 | 96% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 489，观测区间 489 - 489，28 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 30，28 个样本，取值集中（一致性 96%）
