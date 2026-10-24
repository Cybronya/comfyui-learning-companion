---
name: unknown_workflow_video_sampler_clip_68
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.853556
common_nodes: [BasicScheduler, CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, EmptyLTXVLatentVideo, ImageResizeKJv2, KSamplerSelect, LTX2SamplingPreviewOverride, LTX2_NAG, LTXVConditioning, LTXVPreprocess, LoadImage, ModelSamplingSD3, SamplerCustom, UNETLoader, VAEDecode, VAELoader, VAELoaderKJ, VHS_VideoCombine, VisualizeSigmasKJ]
problems: []
missing: []
members: [视频生成/图生视频/YJ-LTX2.3-图生视频_2060617208614703105.json, 视频生成/图生视频/电商图生15秒视频 指定配音 Ltx2.3_2042797388833755137.json, 视频生成/图生视频/电商多图生15秒视频 保持人物一致性  Ltx2.3_2042139178611253249.json, 视频生成/图生视频/电商数字人图生15秒视频 指定说话音频 Ltx2.3_2043889875862163457.json, 视频生成/图生视频/空白工作流_2072161079689572354.json, 视频生成/图生视频/音画同步图生视频 LTX2.3图生视频KJ优化版_2032301702237392897.json, 视频生成/文生视频/LTX2.3-亲子对话-文生视频工作流--搞笑视频_2083450669406711809.json, 视频生成/文生视频/LTX2.3图生视频-KJ版-参数化_2069425308750671874.json, 视频生成/文生视频/LTX2.3图生视频KJ优化版_2034072375746105345.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_68

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/YJ-LTX2.3-图生视频_2060617208614703105.json、视频生成/图生视频/电商图生15秒视频 指定配音 Ltx2.3_2042797388833755137.json、视频生成/图生视频/电商多图生15秒视频 保持人物一致性  Ltx2.3_2042139178611253249.json、视频生成/图生视频/电商数字人图生15秒视频 指定说话音频 Ltx2.3_2043889875862163457.json、视频生成/图生视频/空白工作流_2072161079689572354.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 9 个 workflow 都包含：
- `BasicScheduler`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `LTX2SamplingPreviewOverride`
- `LTX2_NAG`
- `LTXVConditioning`
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
- `Int` —— 8/9 个有
- `LTXVAudioVAEDecode` —— 8/9 个有
- `LTXVConcatAVLatent` —— 8/9 个有
- `LTXVEmptyLatentAudio` —— 8/9 个有
- `LTXVImgToVideoInplaceKJ` —— 8/9 个有
- `LTXVSeparateAVLatent` —— 8/9 个有
- `PrimitiveInt` —— 8/9 个有
- `SimpleMath+` —— 5/9 个有
- `DF_Int_to_Float` —— 4/9 个有
- `JjkText` —— 4/9 个有
- `LoraLoaderModelOnly` —— 4/9 个有
- `MathExpression|pysssss` —— 4/9 个有
- `PathchSageAttentionKJ` —— 4/9 个有
- `AILab_QwenVL_Advanced` —— 3/9 个有
- `GetNode` —— 3/9 个有
- `ImageFromBatch+` —— 3/9 个有
- `SetNode` —— 3/9 个有
- `ShowText|pysssss` —— 3/9 个有
- `StringFunction|pysssss` —— 3/9 个有
- `CR Text` —— 2/9 个有
- `easy positive` —— 2/9 个有
- `LTXVAudioVAEEncode` —— 1/9 个有
- `LTXVImgToVideoConditionOnly` —— 1/9 个有
- `LoadAudio` —— 1/9 个有
- `PrimitiveBoolean` —— 1/9 个有
- `SetLatentNoiseMask` —— 1/9 个有
- `SolidMask` —— 1/9 个有
- `VRAMReserver` —— 1/9 个有
- `easy getNode` —— 1/9 个有
- `easy setNode` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 305 | 8 | 40% |
| 高度 | 25 | 24 - 25 | 8 | 98% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 305，8 个样本，取值分散，一致性仅 40%
- 高度 中位数 25，观测区间 24 - 25，8 个样本，取值集中（一致性 98%）
