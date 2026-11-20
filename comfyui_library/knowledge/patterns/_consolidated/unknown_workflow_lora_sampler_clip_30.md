---
name: unknown_workflow_lora_sampler_clip_30
type: Unknown Workflow
frequency: 13
level: moderate
coverage: 0.952
common_nodes: [CFGGuider, CLIPTextEncode, EmptyLTXVLatentVideo, INTConstant, KSamplerSelect, LTXAVTextEncoderLoader, LTXAddVideoICLoRAGuide, LTXICLoRALoaderModelOnly, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVSeparateAVLatent, LiconMSR, LoadImage, LowVRAMCheckpointLoader, ManualSigmas, RandomNoise, SamplerCustomAdvanced, VAEDecode]
problems: []
missing: []
members: [视频生成/图生视频/GS-ltx2.3_msr_v2多参图生视频_2087382666709659650.json, 视频生成/图生视频/LTX-2.3 MSR V2参考生视频（AI短剧漫剧一键生成）_2079038691699412993.json, 视频生成/图生视频/LTX-2.3-MSR_2066734260651913217.json, 视频生成/图生视频/LTX-2.3-MSR多图参考视频生成V2_2079024443669696513.json, 视频生成/图生视频/LTX-2.3_MSR V2模型多参生视频（一致性及音频优化）_2078737111863353346.json, 视频生成/图生视频/LTX-2.3_MSRV2单采版优化_2081916685078061057.json, 视频生成/图生视频/LTX-2.3_MSR_sample_workflow_V1_2063384595684483073.json, 视频生成/图生视频/LTX-2.3_MSR_多参考图生视频_2063553496401666050.json, 视频生成/图生视频/LTX2.3 Licon-MSR 多图参考正式版+反推提示词_2066036494720126978.json, 视频生成/图生视频/光锥实验室开源LTX-2.3_MSR多参生视频_2067788916261998594.json, 视频生成/图生视频/光锥实验室开源LTX-2.3_MSR多参生视频_2073325205451268097.json, 视频生成/文生视频/LTX2.3 Licon-MSR 多图参考正式版_2067553179402854402.json, 视频生成/文生视频/自动分镜-LTX-2.3-Licon-MSR-V2.0_2082802801167650818.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_30

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（视频生成/图生视频/GS-ltx2.3_msr_v2多参图生视频_2087382666709659650.json、视频生成/图生视频/LTX-2.3 MSR V2参考生视频（AI短剧漫剧一键生成）_2079038691699412993.json、视频生成/图生视频/LTX-2.3-MSR_2066734260651913217.json、视频生成/图生视频/LTX-2.3-MSR多图参考视频生成V2_2079024443669696513.json、视频生成/图生视频/LTX-2.3_MSR V2模型多参生视频（一致性及音频优化）_2078737111863353346.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 13 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `EmptyLTXVLatentVideo`
- `INTConstant`
- `KSamplerSelect`
- `LTXAVTextEncoderLoader`
- `LTXAddVideoICLoRAGuide`
- `LTXICLoRALoaderModelOnly`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVSeparateAVLatent`
- `LiconMSR`
- `LoadImage`
- `LowVRAMCheckpointLoader`
- `ManualSigmas`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 12/13 个有
- `SaveVideo` —— 12/13 个有
- `LTX2_NAG` —— 11/13 个有
- `PromptRelayEncode` —— 11/13 个有
- `CR Float To Integer` —— 6/13 个有
- `FloatConstant` —— 6/13 个有
- `LTXVSetAudioRefTokens` —— 6/13 个有
- `SimpleMath+` —— 6/13 个有
- `PrimitiveStringMultiline` —— 4/13 个有
- `CR Prompt Text` —— 3/13 个有
- `CR Text` —— 3/13 个有
- `CM_IntToFloat` —— 2/13 个有
- `ComfyMathExpression` —— 2/13 个有
- `LoraLoaderModelOnly` —— 2/13 个有
- `PreviewImage` —— 2/13 个有
- `SimpleCalculatorKJ` —— 2/13 个有
- `ComfySwitchNode` —— 1/13 个有
- `Fast Bypasser (rgthree)` —— 1/13 个有
- `ImageResizeKJv2` —— 1/13 个有
- `LTXVAddGuideMulti` —— 1/13 个有
- `LTXVPreprocess` —— 1/13 个有
- `LayerUtility: BooleanOperator` —— 1/13 个有
- `LoadVideo` —— 1/13 个有
- `PrimitiveBoolean` —— 1/13 个有
- `RH_LLMAPI_Pro_Node` —— 1/13 个有
- `Text Find and Replace` —— 1/13 个有
- `VHS_VideoCombine` —— 1/13 个有
- `easy showAnything` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 241 | 241 - 241 | 13 | 100% |
| 高度 | 50 | 24 - 50 | 13 | 68% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 241，观测区间 241 - 241，13 个样本，取值集中（一致性 100%）
- 高度 中位数 50，观测区间 24 - 50，13 个样本
