---
name: unknown_workflow_video_lora_sampler_556
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.45775
common_nodes: [CFGGuider, CLIPTextEncode, EmptyLTXVLatentVideo, GetNode, KSamplerSelect, LTXAVTextEncoderLoader, LTXAddVideoICLoRAGuide, LTXICLoRALoaderModelOnly, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVSeparateAVLatent, LiconMSR, LoadImage, ManualSigmas, RandomNoise, SamplerCustomAdvanced, SetNode, SimpleMath+, VAEDecode, VHS_VideoCombine, easy imageRemBg]
problems: []
missing: []
members: [视频生成/图生视频/LTX2.3 MSR v2全能参考自定义音频_2079011118076481538.json, 视频生成/图生视频/MSR v2全能参考_2079026510954057729.json, 视频生成/图生视频/（测试中）LTX2.3-MSR多参考图+音频参考_2082504671247298561.json, 视频生成/文生视频/LTX2.3全能参考_2066712542273163265.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_556

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/LTX2.3 MSR v2全能参考自定义音频_2079011118076481538.json、视频生成/图生视频/MSR v2全能参考_2079026510954057729.json、视频生成/图生视频/（测试中）LTX2.3-MSR多参考图+音频参考_2082504671247298561.json、视频生成/文生视频/LTX2.3全能参考_2066712542273163265.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：46%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `KSamplerSelect`
- `LTXAVTextEncoderLoader`
- `LTXAddVideoICLoRAGuide`
- `LTXICLoRALoaderModelOnly`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVSeparateAVLatent`
- `LiconMSR`
- `LoadImage`
- `ManualSigmas`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SetNode`
- `SimpleMath+`
- `VAEDecode`
- `VHS_VideoCombine`
- `easy imageRemBg`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 3/4 个有
- `ComfyMathExpression` —— 3/4 个有
- `Fast Groups Bypasser (rgthree)` —— 3/4 个有
- `INTConstant` —— 3/4 个有
- `PromptRelayEncode` —— 3/4 个有
- `ShowAnything|Mie` —— 3/4 个有
- `UNETLoader` —— 3/4 个有
- `VAELoaderKJ` —— 3/4 个有
- `LTXVAudioVAEEncode` —— 2/4 个有
- `LTXVEmptyLatentAudio` —— 2/4 个有
- `LoadAudio` —— 2/4 个有
- `SetLatentNoiseMask` —— 2/4 个有
- `SolidMask` —— 2/4 个有
- `Float` —— 1/4 个有
- `Int` —— 1/4 个有
- `LTXVAudioVAELoader` —— 1/4 个有
- `Label (rgthree)` —— 1/4 个有
- `LowVRAMCheckpointLoader` —— 1/4 个有
- `PreviewAudio` —— 1/4 个有
- `TTResolutionSelector` —— 1/4 个有
- `Text` —— 1/4 个有
- `TrimAudioDuration` —— 1/4 个有
- `easy cleanGpuUsed` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 145 | - | 2 | 100% |
| 高度 | 24 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 145，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 24，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
