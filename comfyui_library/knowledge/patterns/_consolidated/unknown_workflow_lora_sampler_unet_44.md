---
name: unknown_workflow_lora_sampler_unet_44
type: Unknown Workflow
frequency: 12
level: strong
coverage: 0.771667
common_nodes: [BasicScheduler, ConditioningZeroOut, DualCLIPLoader, EmptyLTXVLatentVideo, GetNode, KSamplerSelect, LTX2SamplingPreviewOverride, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVImgToVideoInplaceKJ, LTXVPreprocess, LTXVSeparateAVLatent, LoadImage, LoraLoaderModelOnly, PathchSageAttentionKJ, SamplerCustom, SetNode, UNETLoader, VAEDecode, VAELoaderKJ, VisualizeSigmasKJ]
problems: []
missing: []
members: [视频生成/图生视频/阿良绘】火辣版_ Dasiwa V2+Prompt Relay视频生成_2056368932285665281.json, 视频生成/图生视频/（方案2）Ltx2.3多镜头时间+逻辑控制PromptRelay+VBVR（KJ版）V2_2046813828544995329.json, 视频生成/图生视频/（自用）N版 Ltx2.3 Dasiwa V2+Prompt Relay精准图生视频_2054515717713743873.json, 视频生成/图生视频/（自用）N版Ltx2.3 Sulphur2 + VBVR 390K单图参考精准控制极速版_2054915878034132994.json, 视频生成/文生视频/LTX2.3多镜头时间+逻辑控制PromptRelay+VBVR（KJ版）图文生视频_2047557904437350401.json, 视频生成/文生视频/LTX2.3多镜头时间+逻辑控制PromptRelay+VBVR（KJ版）图文生视频_2068645053744115713.json, 视频生成/文生视频/Ltx2.3+细化多镜头长时间 KJ版 图生视频时间分段剪辑++逻辑控制PromptRelay+VB_2052194763788570626.json, 视频生成/文生视频/Ltx2.3细化多镜头长时间+KJ版+时间分段剪辑+逻辑控制PromptRe图生视频_2055523539997995010.json, 视频生成/文生视频/Ltx2.3（单图）PromptRelayEncode(Timeline)_2059942776380420097.json, 视频生成/文生视频/ltx2.3生视频工作流_2055117729442607106.json, 视频生成/文生视频/一键图生长视频Ltx2.5+细化多镜头长时间+图生视频时间分段剪辑+逻辑控制_2089903343618584577.json, 视频生成/文生视频/图生长视频Ltx2.3+细化多镜头长时间+KJ版+图生视频时间分段剪辑++逻辑控制PromptRe_2055128924383924225.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_44

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（视频生成/图生视频/阿良绘】火辣版_ Dasiwa V2+Prompt Relay视频生成_2056368932285665281.json、视频生成/图生视频/（方案2）Ltx2.3多镜头时间+逻辑控制PromptRelay+VBVR（KJ版）V2_2046813828544995329.json、视频生成/图生视频/（自用）N版 Ltx2.3 Dasiwa V2+Prompt Relay精准图生视频_2054515717713743873.json、视频生成/图生视频/（自用）N版Ltx2.3 Sulphur2 + VBVR 390K单图参考精准控制极速版_2054915878034132994.json、视频生成/文生视频/LTX2.3多镜头时间+逻辑控制PromptRelay+VBVR（KJ版）图文生视频_2047557904437350401.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：77%

## 共有节点

全部 12 个 workflow 都包含：
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
- `LoraLoaderModelOnly`
- `PathchSageAttentionKJ`
- `SamplerCustom`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAELoaderKJ`
- `VisualizeSigmasKJ`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageScaleByAspectRatio V2` —— 11/12 个有
- `CR Prompt Text` —— 10/12 个有
- `JWInteger` —— 10/12 个有
- `PreviewImage` —— 10/12 个有
- `VHS_VideoCombine` —— 9/12 个有
- `PromptRelayEncode` —— 7/12 个有
- `DuckHideNode` —— 3/12 个有
- `PromptRelaySmartEncode` —— 3/12 个有
- `SaveImage` —— 3/12 个有
- `TT_img_enc` —— 3/12 个有
- `TT_img_enc_v2` —— 3/12 个有
- `PromptRelayEncodeTimeline` —— 2/12 个有
- `Float` —— 1/12 个有
- `Float to Int` —— 1/12 个有
- `Int` —— 1/12 个有
- `easy getNode` —— 1/12 个有
- `easy setNode` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 489 | 361 - 489 | 12 | 93% |
| 高度 | 25 | 25 - 25 | 12 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 489，观测区间 361 - 489，12 个样本，取值集中（一致性 93%）
- 高度 中位数 25，观测区间 25 - 25，12 个样本，取值集中（一致性 100%）
