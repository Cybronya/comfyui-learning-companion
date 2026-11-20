---
name: unknown_workflow_lora_sampler_clip_77
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.71125
common_nodes: [CFGGuider, CLIPTextEncode, CreateVideo, EmptyLTXVLatentVideo, INTConstant, KSamplerSelect, LTXAVTextEncoderLoader, LTXAddVideoICLoRAGuide, LTXICLoRALoaderModelOnly, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVSeparateAVLatent, LiconMSR, LoadImage, LoraLoaderModelOnly, LowVRAMCheckpointLoader, ManualSigmas, PreviewAny, RH_LLMAPI_NODE, RandomNoise, SamplerCustomAdvanced, SaveVideo, VAEDecode]
problems: []
missing: []
members: [视频生成/图生视频/LTX2.3 MSR+BestFaceID一致性增强_2075527517234094082.json, 视频生成/图生视频/LTX2.3 MSR+BestFaceID面部一致增强_2074817349152235521.json, 视频生成/图生视频/LTX2.3 MSR-V2-BestFaceID多参考视频_2077979272010096641.json, 视频生成/图生视频/LTX2.3-MSR图生视频 全局参考  提示词扩写自动优化 数字人说话唱歌_2072516302538887169.json, 视频生成/图生视频/LTX2.3-MSR图生视频V2【全局参考】_2063611075953778689.json, 视频生成/图生视频/LTX2.3-MSR图生视频【全局参考】_2072510726874427393.json, 视频生成/图生视频/LTX2.3-MSR图生视频【全局参考】_2073281065932046336.json, 视频生成/图生视频/LTX2.3-MSR图生视频【全局多图参考】_2064168475052036098.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_77

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/LTX2.3 MSR+BestFaceID一致性增强_2075527517234094082.json、视频生成/图生视频/LTX2.3 MSR+BestFaceID面部一致增强_2074817349152235521.json、视频生成/图生视频/LTX2.3 MSR-V2-BestFaceID多参考视频_2077979272010096641.json、视频生成/图生视频/LTX2.3-MSR图生视频 全局参考  提示词扩写自动优化 数字人说话唱歌_2072516302538887169.json、视频生成/图生视频/LTX2.3-MSR图生视频V2【全局参考】_2063611075953778689.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：71%

## 共有节点

全部 8 个 workflow 都包含：
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
- `LoraLoaderModelOnly`
- `LowVRAMCheckpointLoader`
- `ManualSigmas`
- `PreviewAny`
- `RH_LLMAPI_NODE`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 5/8 个有
- `CR Text Concatenate` —— 5/8 个有
- `CR Value` —— 5/8 个有
- `GetNode` —— 5/8 个有
- `MathExpression|pysssss` —— 5/8 个有
- `SetNode` —— 5/8 个有
- `easy boolean` —— 5/8 个有
- `easy convertAnything` —— 5/8 个有
- `CropFace` —— 3/8 个有
- `LTXIdentityOverlapConditioning` —— 3/8 个有
- `SplitStringByDelimiter` —— 3/8 个有
- `StringConcatenate` —— 3/8 个有
- `StringReplace` —— 3/8 个有
- `TTP_text_mix` —— 3/8 个有
- `TextGenerate` —— 3/8 个有
- `TextInput_` —— 3/8 个有
- `LTX2_NAG` —— 1/8 个有
- `PromptRelayEncode` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 241 | 241 - 241 | 8 | 100% |
| 高度 | 24 | 24 - 50 | 8 | 63% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 241，观测区间 241 - 241，8 个样本，取值集中（一致性 100%）
- 高度 中位数 24，观测区间 24 - 50，8 个样本
