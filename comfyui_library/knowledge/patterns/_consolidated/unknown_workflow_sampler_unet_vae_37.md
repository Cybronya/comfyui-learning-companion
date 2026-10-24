---
name: unknown_workflow_sampler_unet_vae_37
type: Unknown Workflow
frequency: 16
level: strong
coverage: 0.788438
common_nodes: [BasicScheduler, DualCLIPLoader, EmptyLTXVLatentVideo, KSamplerSelect, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVImgToVideoInplaceKJ, LTXVPreprocess, LTXVSeparateAVLatent, LoadImage, PathchSageAttentionKJ, SamplerCustom, UNETLoader, VAEDecode, VAELoaderKJ]
problems: []
missing: []
members: [视频生成/图生视频/prompt_relay_ltx23_2067967750336761858.json, 视频生成/图生视频/prompt_relay_ltx23_timeline_2055229065958830081.json, 视频生成/图生视频/【Supermate】LTX2.3精控提示词时间线prompt_relay_timeline_2049641151925370882.json, 视频生成/图生视频/单图多镜头prompt_relay_ltx23_提示词中继，分段提示词，视频符合物理逻辑_2052988468854312962.json, 视频生成/图生视频/测试图生视频_2059113705333415938.json, 视频生成/图生视频/空白工作流_2059459156813377538.json, 视频生成/图生视频/视频生成-音画同步_2059406752063512578.json, 视频生成/图生视频/超强的LTX2.3——图生视频_2057108864734154754.json, 视频生成/图生视频/超强的LTX2.3——图生视频_2057108922590388226.json, 视频生成/图生视频/超强的LTX2.3——图生视频_2057109059437948929.json, 视频生成/文生视频/LTX2.3多镜头时间+逻辑控制PromptRelay+VBVR（KJ版）图文生视频_2047557904437350401.json, 视频生成/文生视频/LTX2.3多镜头时间+逻辑控制PromptRelay+VBVR（KJ版）图文生视频_2068645053744115713.json, 视频生成/文生视频/Ltx2.3+细化多镜头长时间 KJ版 图生视频时间分段剪辑++逻辑控制PromptRelay+VB_2052194763788570626.json, 视频生成/文生视频/Ltx2.3细化多镜头长时间+KJ版+时间分段剪辑+逻辑控制PromptRe图生视频_2055523539997995010.json, 视频生成/文生视频/一键图生长视频Ltx2.5+细化多镜头长时间+图生视频时间分段剪辑+逻辑控制_2089903343618584577.json, 视频生成/文生视频/图生长视频Ltx2.3+细化多镜头长时间+KJ版+图生视频时间分段剪辑++逻辑控制PromptRe_2055128924383924225.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_37

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（视频生成/图生视频/prompt_relay_ltx23_2067967750336761858.json、视频生成/图生视频/prompt_relay_ltx23_timeline_2055229065958830081.json、视频生成/图生视频/【Supermate】LTX2.3精控提示词时间线prompt_relay_timeline_2049641151925370882.json、视频生成/图生视频/单图多镜头prompt_relay_ltx23_提示词中继，分段提示词，视频符合物理逻辑_2052988468854312962.json、视频生成/图生视频/测试图生视频_2059113705333415938.json…）

- **类型**：Unknown Workflow
- **样本数**：16
- **可信度**：强结论
- **平均知识覆盖**：79%

## 共有节点

全部 16 个 workflow 都包含：
- `BasicScheduler`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `KSamplerSelect`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoInplaceKJ`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `PathchSageAttentionKJ`
- `SamplerCustom`
- `UNETLoader`
- `VAEDecode`
- `VAELoaderKJ`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 15/16 个有
- `GetNode` —— 15/16 个有
- `LTX2SamplingPreviewOverride` —— 15/16 个有
- `PreviewImage` —— 15/16 个有
- `SetNode` —— 15/16 个有
- `VisualizeSigmasKJ` —— 15/16 个有
- `LoraLoaderModelOnly` —— 14/16 个有
- `VHS_VideoCombine` —— 14/16 个有
- `CR Prompt Text` —— 12/16 个有
- `JWInteger` —— 12/16 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 12/16 个有
- `PromptRelayEncode` —— 12/16 个有
- `PromptRelayEncodeTimeline` —— 4/16 个有
- `CLIPTextEncode` —— 2/16 个有
- `CreateVideo` —— 2/16 个有
- `LTX2_NAG` —— 2/16 个有
- `SaveVideo` —— 2/16 个有
- `ComfyNumberConvert` —— 1/16 个有
- `ConditioningCombine` —— 1/16 个有
- `Label (rgthree)` —— 1/16 个有
- `PrimitiveFloat` —— 1/16 个有
- `VHS_LoadVideo` —— 1/16 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 489 | 129 - 489 | 16 | 76% |
| 高度 | 25 | 25 - 30 | 16 | 95% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 489，观测区间 129 - 489，16 个样本
- 高度 中位数 25，观测区间 25 - 30，16 个样本，取值集中（一致性 95%）
