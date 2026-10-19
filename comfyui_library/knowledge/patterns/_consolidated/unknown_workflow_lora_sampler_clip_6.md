---
name: unknown_workflow_lora_sampler_clip_6
type: Unknown Workflow
frequency: 16
level: moderate
coverage: 0.745938
common_nodes: [CFGGuider, CLIPTextEncode, EmptyLTXVLatentVideo, INTConstant, KSamplerSelect, LTXAVTextEncoderLoader, LTXAddVideoICLoRAGuide, LTXICLoRALoaderModelOnly, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVSeparateAVLatent, LiconMSR, LoadImage, LowVRAMCheckpointLoader, ManualSigmas, RandomNoise, SamplerCustomAdvanced, VAEDecode]
problems: []
missing: []
members: [视频生成/图生视频/2064287550000422914.json, 视频生成/图生视频/2064563859888885761.json, 视频生成/图生视频/GS-ltx2.3_msr_v2多参图生视频_2087382666709659650.json, 视频生成/图生视频/2079038691699412993.json, 视频生成/图生视频/2066734260651913217.json, 视频生成/图生视频/2077298487875694594.json, 视频生成/图生视频/2079024443669696513.json, 视频生成/图生视频/2078737111863353346.json, 视频生成/图生视频/2081916685078061057.json, 视频生成/图生视频/LTX2.3 MSR V2 (多主体参考) 图生视频_2083493730379722754.json, 视频生成/图生视频/2066907383061901313.json, 视频生成/图生视频/2072516302538887169.json, 视频生成/图生视频/2063611075953778689.json, 视频生成/图生视频/2072510726874427393.json, 视频生成/图生视频/2073281065932046336.json, 视频生成/图生视频/2064168475052036098.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_6

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（视频生成/图生视频/2064287550000422914.json、视频生成/图生视频/2064563859888885761.json、视频生成/图生视频/GS-ltx2.3_msr_v2多参图生视频_2087382666709659650.json、视频生成/图生视频/2079038691699412993.json、视频生成/图生视频/2066734260651913217.json…）

- **类型**：Unknown Workflow
- **样本数**：16
- **可信度**：中等可信
- **平均知识覆盖**：75%

## 共有节点

全部 16 个 workflow 都包含：
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
- `CreateVideo` —— 12/16 个有
- `SaveVideo` —— 12/16 个有
- `GetNode` —— 8/16 个有
- `LTX2_NAG` —— 8/16 个有
- `PromptRelayEncode` —— 8/16 个有
- `SetNode` —— 8/16 个有
- `LoraLoaderModelOnly` —— 7/16 个有
- `CR Text` —— 6/16 个有
- `MathExpression|pysssss` —— 6/16 个有
- `CR Float To Integer` —— 5/16 个有
- `CR Text Concatenate` —— 5/16 个有
- `CR Value` —— 5/16 个有
- `FloatConstant` —— 5/16 个有
- `PreviewAny` —— 5/16 个有
- `RH_LLMAPI_NODE` —— 5/16 个有
- `SimpleMath+` —— 5/16 个有
- `VHS_VideoCombine` —— 5/16 个有
- `easy boolean` —— 5/16 个有
- `easy convertAnything` —— 5/16 个有
- `LTXVSetAudioRefTokens` —— 4/16 个有
- `CR Prompt Text` —— 3/16 个有
- `ComfyMathExpression` —— 3/16 个有
- `LTXVAddGuideMulti` —— 1/16 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/16 个有
- `LoadVideo` —— 1/16 个有
- `PreviewImage` —— 1/16 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 241 | 145 - 241 | 16 | 83% |
| 高度 | 24 | 24 - 50 | 16 | 64% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 241，观测区间 145 - 241，16 个样本，取值集中（一致性 83%）
- 高度 中位数 24，观测区间 24 - 50，16 个样本
