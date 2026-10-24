---
name: unknown_workflow_lora_sampler_clip_160
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.955
common_nodes: [CFGGuider, CLIPTextEncode, CreateVideo, EmptyLTXVLatentVideo, INTConstant, KSamplerSelect, LTXAVTextEncoderLoader, LTXAddVideoICLoRAGuide, LTXICLoRALoaderModelOnly, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVSeparateAVLatent, LiconMSR, LoadImage, LowVRAMCheckpointLoader, ManualSigmas, RandomNoise, SamplerCustomAdvanced, SaveVideo, VAEDecode]
problems: []
missing: []
members: [视频生成/图生视频/LTX2.3 MSR+BestFaceID一致性增强_2075527517234094082.json, 视频生成/图生视频/LTX2.3 MSR+BestFaceID面部一致增强_2074817349152235521.json, 视频生成/图生视频/LTX2.3 MSR-V2-BestFaceID多参考视频_2077979272010096641.json, 视频生成/图生视频/Licon-MSR生成视频参考工作流_2061975400108093442.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_160

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/LTX2.3 MSR+BestFaceID一致性增强_2075527517234094082.json、视频生成/图生视频/LTX2.3 MSR+BestFaceID面部一致增强_2074817349152235521.json、视频生成/图生视频/LTX2.3 MSR-V2-BestFaceID多参考视频_2077979272010096641.json、视频生成/图生视频/Licon-MSR生成视频参考工作流_2061975400108093442.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CreateVideo`
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
- `SaveVideo`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `CropFace` —— 3/4 个有
- `LTXIdentityOverlapConditioning` —— 3/4 个有
- `LoraLoaderModelOnly` —— 3/4 个有
- `PreviewAny` —— 3/4 个有
- `RH_LLMAPI_NODE` —— 3/4 个有
- `SplitStringByDelimiter` —— 3/4 个有
- `StringConcatenate` —— 3/4 个有
- `StringReplace` —— 3/4 个有
- `TTP_text_mix` —— 3/4 个有
- `TextGenerate` —— 3/4 个有
- `TextInput_` —— 3/4 个有
- `LTX2_NAG` —— 1/4 个有
- `LTXVAddGuideMulti` —— 1/4 个有
- `PromptRelayEncode` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 241 | 145 - 241 | 4 | 81% |
| 高度 | 50 | 24 - 50 | 4 | 74% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 241，观测区间 145 - 241，4 个样本，取值集中（一致性 81%）
- 高度 中位数 50，观测区间 24 - 50，4 个样本
