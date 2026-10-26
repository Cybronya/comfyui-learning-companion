---
name: unknown_workflow_lora_sampler_clip_53
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.854778
common_nodes: [CFGGuider, CLIPTextEncode, CreateVideo, EmptyLTXVLatentVideo, INTConstant, KSamplerSelect, LTXAddVideoICLoRAGuide, LTXICLoRALoaderModelOnly, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVSeparateAVLatent, LiconMSR, LoadImage, ManualSigmas, RandomNoise, SamplerCustomAdvanced, SaveVideo, VAEDecode]
problems: []
missing: []
members: [视频生成/图生视频/LTX-2.3_MSR_sample_workflow_V1_2063384595684483073.json, 视频生成/图生视频/LTX-2.3_MSR_多参考图生视频_2063553496401666050.json, 视频生成/图生视频/LTX-2.3_小seedance2全能参考节点_2065439100508921858.json, 视频生成/图生视频/LTX2.3 Licon-MSR 多图参考正式版+反推提示词_2066036494720126978.json, 视频生成/图生视频/LTX2.3多图参考（小）Seedance 2.0_2067207518782316546.json, 视频生成/图生视频/aidir-LTX2.3多图参考（小）Seedance 2.0_2069617886041305089.json, 视频生成/图生视频/光锥实验室开源LTX-2.3_MSR多参生视频_2067788916261998594.json, 视频生成/图生视频/光锥实验室开源LTX-2.3_MSR多参生视频_2073325205451268097.json, 视频生成/文生视频/LTX2.3 Licon-MSR 多图参考正式版_2067553179402854402.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_53

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/LTX-2.3_MSR_sample_workflow_V1_2063384595684483073.json、视频生成/图生视频/LTX-2.3_MSR_多参考图生视频_2063553496401666050.json、视频生成/图生视频/LTX-2.3_小seedance2全能参考节点_2065439100508921858.json、视频生成/图生视频/LTX2.3 Licon-MSR 多图参考正式版+反推提示词_2066036494720126978.json、视频生成/图生视频/LTX2.3多图参考（小）Seedance 2.0_2067207518782316546.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 9 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CreateVideo`
- `EmptyLTXVLatentVideo`
- `INTConstant`
- `KSamplerSelect`
- `LTXAddVideoICLoRAGuide`
- `LTXICLoRALoaderModelOnly`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVSeparateAVLatent`
- `LiconMSR`
- `LoadImage`
- `ManualSigmas`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `LTXAVTextEncoderLoader` —— 6/9 个有
- `LTXVAudioVAELoader` —— 6/9 个有
- `LowVRAMCheckpointLoader` —— 6/9 个有
- `LTX2_NAG` —— 4/9 个有
- `PrimitiveStringMultiline` —— 4/9 个有
- `PromptRelayEncode` —— 4/9 个有
- `DualCLIPLoader` —— 3/9 个有
- `GetNode` —— 3/9 个有
- `SetNode` —— 3/9 个有
- `UNETLoader` —— 3/9 个有
- `VAELoader` —— 3/9 个有
- `CM_IntToFloat` —— 2/9 个有
- `ComfyMathExpression` —— 2/9 个有
- `LTXVSetAudioRefTokens` —— 2/9 个有
- `MuyeTextEditOutput` —— 2/9 个有
- `SimpleCalculatorKJ` —— 2/9 个有
- `AtSignCLIPTextEncode` —— 1/9 个有
- `CR Text` —— 1/9 个有
- `MultiIntFormula` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 241 | 97 - 241 | 9 | 80% |
| 高度 | 24 | 24 - 50 | 9 | 64% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 241，观测区间 97 - 241，9 个样本
- 高度 中位数 24，观测区间 24 - 50，9 个样本
