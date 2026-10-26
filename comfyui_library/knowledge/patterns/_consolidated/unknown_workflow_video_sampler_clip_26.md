---
name: unknown_workflow_video_sampler_clip_26
type: Unknown Workflow
frequency: 16
level: moderate
coverage: 0.795
common_nodes: [BasicScheduler, CLIPTextEncode, DualCLIPLoader, EmptyLTXVLatentVideo, ImageResizeKJv2, KSamplerSelect, LTX2SamplingPreviewOverride, LTX2_NAG, LTXVConditioning, LTXVImgToVideoInplaceKJ, LTXVPreprocess, LoadImage, ModelSamplingSD3, SamplerCustom, UNETLoader, VAEDecode, VAELoader, VAELoaderKJ, VHS_VideoCombine, VisualizeSigmasKJ]
problems: []
missing: []
members: [视频生成/图生视频/YJ-LTX2.3-图生视频_2060617208614703105.json, 视频生成/图生视频/电商图生15秒视频 指定配音 Ltx2.3_2042797388833755137.json, 视频生成/图生视频/电商多图生15秒视频 保持人物一致性  Ltx2.3_2042139178611253249.json, 视频生成/图生视频/电商数字人图生15秒视频 指定说话音频 Ltx2.3_2043889875862163457.json, 视频生成/图生视频/空白工作流_2072161079689572354.json, 视频生成/文生视频/LTX2.3图生视频-KJ版-参数化_2069425308750671874.json, 视频生成/文生视频/LTX2.3图生视频KJ优化版_2034072375746105345.json, 视频生成/文生视频/LTX2.3图生视频_2071785997519646721.json, 视频生成/文生视频/LTX2.3图生视频_KJ版_参数化_2059632348878163969.json, 视频生成/文生视频/LTX2.3图生视频音画同步KJ优化版图片加文字直出视频短剧电商带货视频工作流_2103808377213247489.json, 视频生成/文生视频/LTX2.3文生视频KJ版 音画同步+提示词润色_2070637012666900482.json, 视频生成/文生视频/LTX2.3极速版 图生视频优化加速版  数字人说话唱歌对口型 音画同步 KJ优化版_2034796660177506306.json, 视频生成/文生视频/双人_单人视频 LTX2.3 数字人对话！图生视频音画同步 KJ优化版！单人也可以说话！_2080101375643574273.json, 视频生成/文生视频/双人_多人视频 LTX2.3+双人_单人对话+极速生视频+KJ优化版+图生视频音画同步_2059151115840741377.json, 视频生成/文生视频/双人对话图生视频音画同步优化版！_2064924344870072322.json, 视频生成/文生视频/图生视频音画同步_2060240885446692865.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_26

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（视频生成/图生视频/YJ-LTX2.3-图生视频_2060617208614703105.json、视频生成/图生视频/电商图生15秒视频 指定配音 Ltx2.3_2042797388833755137.json、视频生成/图生视频/电商多图生15秒视频 保持人物一致性  Ltx2.3_2042139178611253249.json、视频生成/图生视频/电商数字人图生15秒视频 指定说话音频 Ltx2.3_2043889875862163457.json、视频生成/图生视频/空白工作流_2072161079689572354.json…）

- **类型**：Unknown Workflow
- **样本数**：16
- **可信度**：中等可信
- **平均知识覆盖**：80%

## 共有节点

全部 16 个 workflow 都包含：
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `LTX2SamplingPreviewOverride`
- `LTX2_NAG`
- `LTXVConditioning`
- `LTXVImgToVideoInplaceKJ`
- `LTXVPreprocess`
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
- `LTXVAudioVAEDecode` —— 15/16 个有
- `LTXVConcatAVLatent` —— 15/16 个有
- `LTXVEmptyLatentAudio` —— 15/16 个有
- `LTXVSeparateAVLatent` —— 15/16 个有
- `Int` —— 14/16 个有
- `PrimitiveInt` —— 14/16 个有
- `ConditioningZeroOut` —— 12/16 个有
- `JjkText` —— 12/16 个有
- `SimpleMath+` —— 11/16 个有
- `AILab_QwenVL_Advanced` —— 10/16 个有
- `ShowText|pysssss` —— 10/16 个有
- `StringFunction|pysssss` —— 10/16 个有
- `DF_Int_to_Float` —— 9/16 个有
- `GetNode` —— 9/16 个有
- `SetNode` —— 9/16 个有
- `PathchSageAttentionKJ` —— 8/16 个有
- `easy positive` —— 8/16 个有
- `LayerUtility: BooleanOperatorV2` —— 7/16 个有
- `LayerUtility: If ` —— 7/16 个有
- `LayerUtility: NumberCalculatorV2` —— 7/16 个有
- `LoraLoaderModelOnly` —— 7/16 个有
- `MathExpression|pysssss` —— 5/16 个有
- `JoinStrings` —— 4/16 个有
- `PrimitiveStringMultiline` —— 4/16 个有
- `CR Text` —— 3/16 个有
- `ImageFromBatch+` —— 3/16 个有
- `LTXVAudioVAEEncode` —— 1/16 个有
- `LoadAudio` —— 1/16 个有
- `SaveImage` —— 1/16 个有
- `SetLatentNoiseMask` —— 1/16 个有
- `SolidMask` —— 1/16 个有
- `TT_img_enc` —— 1/16 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 305 | 97 - 305 | 15 | 50% |
| 高度 | 24 | 24 - 25 | 15 | 98% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 305，观测区间 97 - 305，15 个样本
- 高度 中位数 24，观测区间 24 - 25，15 个样本，取值集中（一致性 98%）
