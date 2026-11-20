---
name: unknown_workflow_video_lora_sampler_715
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.45525
common_nodes: [CFGGuider, CLIPTextEncode, EmptyLTXVLatentVideo, GetNode, KSamplerSelect, LTXAVTextEncoderLoader, LTXAddVideoICLoRAGuide, LTXICLoRALoaderModelOnly, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVSeparateAVLatent, LiconMSR, LoadImage, ManualSigmas, PromptRelayEncode, RandomNoise, SamplerCustomAdvanced, SetNode, SimpleMath+, UNETLoader, VAEDecode, VAELoaderKJ, VHS_VideoCombine, easy imageRemBg]
problems: []
missing: []
members: [视频生成/图生视频/AI代码侠土豆-LTX2.3-MSR多参考图V2+音频参考_2080190771210313729.json, 视频生成/图生视频/LTX2.3 MSR v2全能参考自定义音频_2079011118076481538.json, 视频生成/图生视频/MSR v2全能参考_2079026510954057729.json, 视频生成/图生视频/（测试中）LTX2.3-MSR多参考图+音频参考_2082504671247298561.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_715

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/AI代码侠土豆-LTX2.3-MSR多参考图V2+音频参考_2080190771210313729.json、视频生成/图生视频/LTX2.3 MSR v2全能参考自定义音频_2079011118076481538.json、视频生成/图生视频/MSR v2全能参考_2079026510954057729.json、视频生成/图生视频/（测试中）LTX2.3-MSR多参考图+音频参考_2082504671247298561.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
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
- `PromptRelayEncode`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SetNode`
- `SimpleMath+`
- `UNETLoader`
- `VAEDecode`
- `VAELoaderKJ`
- `VHS_VideoCombine`
- `easy imageRemBg`

**可变部分**（部分 workflow 才有）：
- `LTXVAudioVAEEncode` —— 3/4 个有
- `LoadAudio` —— 3/4 个有
- `SetLatentNoiseMask` —— 3/4 个有
- `SolidMask` —— 3/4 个有
- `CR Text` —— 2/4 个有
- `ComfyMathExpression` —— 2/4 个有
- `Fast Groups Bypasser (rgthree)` —— 2/4 个有
- `Float` —— 2/4 个有
- `INTConstant` —— 2/4 个有
- `Int` —— 2/4 个有
- `Label (rgthree)` —— 2/4 个有
- `PreviewAudio` —— 2/4 个有
- `ShowAnything|Mie` —— 2/4 个有
- `TTResolutionSelector` —— 2/4 个有
- `Text` —— 2/4 个有
- `easy cleanGpuUsed` —— 2/4 个有
- `LTXVEmptyLatentAudio` —— 1/4 个有
- `TrimAudioDuration` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 145 | - | 1 | 100% |
| 高度 | 24 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
