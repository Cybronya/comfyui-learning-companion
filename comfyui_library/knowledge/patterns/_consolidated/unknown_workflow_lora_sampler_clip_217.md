---
name: unknown_workflow_lora_sampler_clip_217
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.883667
common_nodes: [CFGGuider, CLIPTextEncode, EmptyLTXVLatentVideo, KSamplerSelect, LTXAVTextEncoderLoader, LTXAddVideoICLoRAGuide, LTXICLoRALoaderModelOnly, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVSeparateAVLatent, LiconMSR, LoadImage, LowVRAMCheckpointLoader, ManualSigmas, RandomNoise, SamplerCustomAdvanced, VAEDecode]
problems: []
missing: []
members: [视频生成/图生视频/电商多图参考生视频 保持人物一致性 Ltx2.3 MSRV2_2078769207956819970.json, 视频生成/图生视频/（高帧率）Ltx2.3 Licon-MSR全能参考生视频正式版V1_2063444223206191106.json, 视频生成/文生视频/LTX 2.3_MSR（多参图生视频）_2080284714388246530.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_217

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/电商多图参考生视频 保持人物一致性 Ltx2.3 MSRV2_2078769207956819970.json、视频生成/图生视频/（高帧率）Ltx2.3 Licon-MSR全能参考生视频正式版V1_2063444223206191106.json、视频生成/文生视频/LTX 2.3_MSR（多参图生视频）_2080284714388246530.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `EmptyLTXVLatentVideo`
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
- `INTConstant` —— 2/3 个有
- `LTX2_NAG` —— 2/3 个有
- `PromptRelayEncode` —— 2/3 个有
- `VHS_VideoCombine` —— 2/3 个有
- `CM_FloatToInt` —— 1/3 个有
- `CR Prompt Text` —— 1/3 个有
- `CreateVideo` —— 1/3 个有
- `FloatConstant` —— 1/3 个有
- `GetNode` —— 1/3 个有
- `ImageScale` —— 1/3 个有
- `JjkText` —— 1/3 个有
- `MathExpression|pysssss` —— 1/3 个有
- `SaveVideo` —— 1/3 个有
- `SetNode` —— 1/3 个有
- `SimpleMath+` —— 1/3 个有
- `easy int` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 241 | 97 - 241 | 3 | 65% |
| 高度 | 50 | 25 - 50 | 3 | 72% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 241，观测区间 97 - 241，3 个样本
- 高度 中位数 50，观测区间 25 - 50，3 个样本
