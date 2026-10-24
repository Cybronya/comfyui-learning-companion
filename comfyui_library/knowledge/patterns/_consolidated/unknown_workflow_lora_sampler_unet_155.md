---
name: unknown_workflow_lora_sampler_unet_155
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.7792
common_nodes: [BasicScheduler, ConditioningZeroOut, DualCLIPLoader, EmptyLTXVLatentVideo, GetNode, JWInteger, KSamplerSelect, LTX2SamplingPreviewOverride, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVImgToVideoInplaceKJ, LTXVPreprocess, LTXVSeparateAVLatent, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, PathchSageAttentionKJ, SamplerCustom, SetNode, UNETLoader, VAEDecode, VAELoaderKJ, VisualizeSigmasKJ]
problems: []
missing: []
members: [视频生成/图生视频/阿良绘】火辣版_ Dasiwa V2+Prompt Relay视频生成_2056368932285665281.json, 视频生成/图生视频/（方案2）Ltx2.3多镜头时间+逻辑控制PromptRelay+VBVR（KJ版）V2_2046813828544995329.json, 视频生成/图生视频/（自用）N版 Ltx2.3 Dasiwa V2+Prompt Relay精准图生视频_2054515717713743873.json, 视频生成/图生视频/（自用）N版Ltx2.3 Sulphur2 + VBVR 390K单图参考精准控制极速版_2054915878034132994.json, 视频生成/文生视频/LTX2.3图生视频 -时间线分镜-PromptRelay-服装模特带货短视频_2055106849938132994.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_155

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/阿良绘】火辣版_ Dasiwa V2+Prompt Relay视频生成_2056368932285665281.json、视频生成/图生视频/（方案2）Ltx2.3多镜头时间+逻辑控制PromptRelay+VBVR（KJ版）V2_2046813828544995329.json、视频生成/图生视频/（自用）N版 Ltx2.3 Dasiwa V2+Prompt Relay精准图生视频_2054515717713743873.json、视频生成/图生视频/（自用）N版Ltx2.3 Sulphur2 + VBVR 390K单图参考精准控制极速版_2054915878034132994.json、视频生成/文生视频/LTX2.3图生视频 -时间线分镜-PromptRelay-服装模特带货短视频_2055106849938132994.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：78%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicScheduler`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `JWInteger`
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
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAELoaderKJ`
- `VisualizeSigmasKJ`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 4/5 个有
- `DuckHideNode` —— 3/5 个有
- `PromptRelaySmartEncode` —— 3/5 个有
- `SaveImage` —— 3/5 个有
- `TT_img_enc` —— 3/5 个有
- `TT_img_enc_v2` —— 3/5 个有
- `PreviewImage` —— 2/5 个有
- `VHS_VideoCombine` —— 2/5 个有
- `CM_IntToFloat` —— 1/5 个有
- `PreviewAny` —— 1/5 个有
- `PromptRelayEncode` —— 1/5 个有
- `PromptRelayEncodeTimeline` —— 1/5 个有
- `RH_LLMAPI_Pro_Node` —— 1/5 个有
- `RegexExtract` —— 1/5 个有
- `SimpleMath+` —— 1/5 个有
- `Text` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 489 | 489 - 489 | 5 | 100% |
| 高度 | 25 | 25 - 25 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 489，观测区间 489 - 489，5 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，5 个样本，取值集中（一致性 100%）
