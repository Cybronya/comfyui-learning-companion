---
name: unknown_workflow_video_sampler_clip_60
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.7466
common_nodes: [BasicScheduler, CLIPTextEncode, DualCLIPLoader, EmptyLTXVLatentVideo, ImageResizeKJv2, KSamplerSelect, LTX2SamplingPreviewOverride, LTX2_NAG, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVImgToVideoInplaceKJ, LTXVPreprocess, LTXVSeparateAVLatent, LoadImage, ModelSamplingSD3, SamplerCustom, UNETLoader, VAEDecode, VAELoader, VAELoaderKJ, VHS_VideoCombine, VisualizeSigmasKJ]
problems: []
missing: []
members: [视频生成/文生视频/LTX2.3图生视频_2071785997519646721.json, 视频生成/文生视频/LTX2.3图生视频_KJ版_参数化_2059632348878163969.json, 视频生成/文生视频/LTX2.3图生视频音画同步KJ优化版图片加文字直出视频短剧电商带货视频工作流_2103808377213247489.json, 视频生成/文生视频/LTX2.3文生视频KJ版 音画同步+提示词润色_2070637012666900482.json, 视频生成/文生视频/LTX2.3极速版 图生视频优化加速版  数字人说话唱歌对口型 音画同步 KJ优化版_2034796660177506306.json, 视频生成/文生视频/双人_单人视频 LTX2.3 数字人对话！图生视频音画同步 KJ优化版！单人也可以说话！_2080101375643574273.json, 视频生成/文生视频/双人_多人视频 LTX2.3+双人_单人对话+极速生视频+KJ优化版+图生视频音画同步_2059151115840741377.json, 视频生成/文生视频/双人对话图生视频音画同步优化版！_2064924344870072322.json, 视频生成/文生视频/图生视频优化加速版 LTX2.3 数字人说话唱歌对口型  音画同步 KJ优化版_2034441938631401474.json, 视频生成/文生视频/图生视频音画同步_2060240885446692865.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_60

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/文生视频/LTX2.3图生视频_2071785997519646721.json、视频生成/文生视频/LTX2.3图生视频_KJ版_参数化_2059632348878163969.json、视频生成/文生视频/LTX2.3图生视频音画同步KJ优化版图片加文字直出视频短剧电商带货视频工作流_2103808377213247489.json、视频生成/文生视频/LTX2.3文生视频KJ版 音画同步+提示词润色_2070637012666900482.json、视频生成/文生视频/LTX2.3极速版 图生视频优化加速版  数字人说话唱歌对口型 音画同步 KJ优化版_2034796660177506306.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：75%

## 共有节点

全部 10 个 workflow 都包含：
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `LTX2SamplingPreviewOverride`
- `LTX2_NAG`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoInplaceKJ`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `ModelSamplingSD3`
- `SamplerCustom`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VAELoaderKJ`
- `VHS_VideoCombine`
- `VisualizeSigmasKJ`

**可变部分**（部分 workflow 才有）：
- `AILab_QwenVL_Advanced` —— 9/10 个有
- `Int` —— 9/10 个有
- `JjkText` —— 9/10 个有
- `PrimitiveInt` —— 9/10 个有
- `ShowText|pysssss` —— 9/10 个有
- `SimpleMath+` —— 9/10 个有
- `StringFunction|pysssss` —— 9/10 个有
- `DF_Int_to_Float` —— 8/10 个有
- `GetNode` —— 8/10 个有
- `LayerUtility: BooleanOperatorV2` —— 8/10 个有
- `LayerUtility: If ` —— 8/10 个有
- `LayerUtility: NumberCalculatorV2` —— 8/10 个有
- `SetNode` —— 8/10 个有
- `easy positive` —— 8/10 个有
- `PathchSageAttentionKJ` —— 7/10 个有
- `ConditioningZeroOut` —— 6/10 个有
- `JoinStrings` —— 4/10 个有
- `LoraLoaderModelOnly` —— 4/10 个有
- `PrimitiveStringMultiline` —— 4/10 个有
- `CR Text` —— 1/10 个有
- `MathExpression|pysssss` —— 1/10 个有
- `SaveImage` —— 1/10 个有
- `TT_img_enc` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 305 | 97 - 305 | 10 | 68% |
| 高度 | 24 | 24 - 25 | 10 | 98% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 305，观测区间 97 - 305，10 个样本
- 高度 中位数 24，观测区间 24 - 25，10 个样本，取值集中（一致性 98%）
