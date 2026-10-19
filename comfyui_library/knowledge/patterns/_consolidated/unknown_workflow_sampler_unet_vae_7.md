---
name: unknown_workflow_sampler_unet_vae_7
type: Unknown Workflow
frequency: 22
level: strong
coverage: 0.792591
common_nodes: [BasicScheduler, DualCLIPLoader, EmptyLTXVLatentVideo, KSamplerSelect, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVImgToVideoInplaceKJ, LTXVPreprocess, LTXVSeparateAVLatent, LoadImage, PathchSageAttentionKJ, SamplerCustom, UNETLoader, VAEDecode, VAELoaderKJ, VisualizeSigmasKJ]
problems: []
missing: []
members: [视频生成/图生视频/2051154231129853954.json, 视频生成/图生视频/2059461166333775873.json, 视频生成/图生视频/2052193823329144834.json, 视频生成/图生视频/2067967750336761858.json, 视频生成/图生视频/2055229065958830081.json, 视频生成/图生视频/2049641151925370882.json, 视频生成/图生视频/2046944174850711553.json, 视频生成/图生视频/2056555868510056450.json, 视频生成/图生视频/2056616678716436482.json, 视频生成/图生视频/2081629704880222209.json, 视频生成/图生视频/2082003174491250690.json, 视频生成/图生视频/图生长视频Ltx2.3+细化多镜头长时间+KJ版+图生视频时间分段剪辑++逻辑控制PromptRe_2084109762710560769.json, 视频生成/图生视频/图生长视频Ltx2.3+细化多镜头长时间+KJ版+图生视频时间分段剪辑++逻辑控制PromptRe_2088511791516184578.json, 视频生成/图生视频/图生长视频Ltx2.3+细化多镜头长时间+KJ版+图生视频时间分段剪辑++逻辑控制PromptRe_2094974574181048322.json, 视频生成/图生视频/2056612468230807553.json, 视频生成/图生视频/2060459576042020865.json, 视频生成/图生视频/2059113705333415938.json, 视频生成/图生视频/2059459156813377538.json, 视频生成/图生视频/2059406752063512578.json, 视频生成/图生视频/2057108864734154754.json, 视频生成/图生视频/2057108922590388226.json, 视频生成/图生视频/2057109059437948929.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_7

> 由 `engine/knowledge_consolidation` 从 22 个 workflow 归纳得出（视频生成/图生视频/2051154231129853954.json、视频生成/图生视频/2059461166333775873.json、视频生成/图生视频/2052193823329144834.json、视频生成/图生视频/2067967750336761858.json、视频生成/图生视频/2055229065958830081.json…）

- **类型**：Unknown Workflow
- **样本数**：22
- **可信度**：强结论
- **平均知识覆盖**：79%

## 共有节点

全部 22 个 workflow 都包含：
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
- `VisualizeSigmasKJ`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 21/22 个有
- `GetNode` —— 21/22 个有
- `LTX2SamplingPreviewOverride` —— 21/22 个有
- `LoraLoaderModelOnly` —— 21/22 个有
- `PreviewImage` —— 21/22 个有
- `SetNode` —— 21/22 个有
- `VHS_VideoCombine` —— 21/22 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 17/22 个有
- `PromptRelayEncode` —— 17/22 个有
- `CR Prompt Text` —— 16/22 个有
- `JWInteger` —— 16/22 个有
- `PromptRelayEncodeTimeline` —— 5/22 个有
- `CLIPTextEncode` —— 1/22 个有
- `CM_IntToFloat` —— 1/22 个有
- `ComfyNumberConvert` —— 1/22 个有
- `CreateVideo` —— 1/22 个有
- `LTX2_NAG` —— 1/22 个有
- `Label (rgthree)` —— 1/22 个有
- `LoadAudio` —— 1/22 个有
- `PrimitiveFloat` —— 1/22 个有
- `SaveVideo` —— 1/22 个有
- `SimpleMath+` —— 1/22 个有
- `Text` —— 1/22 个有
- `easy mathInt` —— 1/22 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 489 | 241 - 489 | 22 | 87% |
| 高度 | 25 | 24 - 30 | 22 | 96% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 489，观测区间 241 - 489，22 个样本，取值集中（一致性 87%）
- 高度 中位数 25，观测区间 24 - 30，22 个样本，取值集中（一致性 96%）
