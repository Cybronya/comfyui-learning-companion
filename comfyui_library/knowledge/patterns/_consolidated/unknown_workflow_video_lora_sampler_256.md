---
name: unknown_workflow_video_lora_sampler_256
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.9095
common_nodes: [AILab_QwenVL, BasicScheduler, BerniniConditioning, CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, GetNode, INTConstant, ImageResizeKJv2, ImageScaleDownToSize, ImageScaleToMaxDimension, JjkText, KSamplerSelect, LTXVAudioVAEDecode, LTXVAudioVideoMask, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVSeparateAVLatent, LayerUtility: PurgeVRAM, LoadImage, LoraLoaderModelOnly, ManualSigmas, PathchSageAttentionKJ, RIFE VFI, RandomNoise, SamplerCustom, SamplerCustomAdvanced, Seed, SetNode, SimpleMath+, SplitSigmas, UNETLoader, VAEDecode, VAEEncodeTiled, VAELoader, VAELoaderKJ, VHS_VideoCombine, easy positive]
problems: []
missing: []
members: [视频生成/图生视频/2074480608352493569.json, 视频生成/图生视频/2074489565452267522.json, 视频生成/图生视频/Bernini R2V多图参考+图生视频+音效生成！KJ版！_2107040499428319233.json, 视频生成/图生视频/Bernini R2V多图参考+图生视频+音效生成！KJ版！_2107086497366237186.json, 视频生成/图生视频/2074313627301146626.json, 视频生成/图生视频/2074666900642156545.json, 视频生成/图生视频/2081637298290122753.json, 视频生成/图生视频/2074654211740094466.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_256

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/2074480608352493569.json、视频生成/图生视频/2074489565452267522.json、视频生成/图生视频/Bernini R2V多图参考+图生视频+音效生成！KJ版！_2107040499428319233.json、视频生成/图生视频/Bernini R2V多图参考+图生视频+音效生成！KJ版！_2107086497366237186.json、视频生成/图生视频/2074313627301146626.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 8 个 workflow 都包含：
- `AILab_QwenVL`
- `BasicScheduler`
- `BerniniConditioning`
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `GetNode`
- `INTConstant`
- `ImageResizeKJv2`
- `ImageScaleDownToSize`
- `ImageScaleToMaxDimension`
- `JjkText`
- `KSamplerSelect`
- `LTXVAudioVAEDecode`
- `LTXVAudioVideoMask`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVEmptyLatentAudio`
- `LTXVSeparateAVLatent`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PathchSageAttentionKJ`
- `RIFE VFI`
- `RandomNoise`
- `SamplerCustom`
- `SamplerCustomAdvanced`
- `Seed`
- `SetNode`
- `SimpleMath+`
- `SplitSigmas`
- `UNETLoader`
- `VAEDecode`
- `VAEEncodeTiled`
- `VAELoader`
- `VAELoaderKJ`
- `VHS_VideoCombine`
- `easy positive`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 129 | 129 - 129 | 8 | 100% |
| 高度 | 24 | 24 - 24 | 8 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 129，观测区间 129 - 129，8 个样本，取值集中（一致性 100%）
- 高度 中位数 24，观测区间 24 - 24，8 个样本，取值集中（一致性 100%）
