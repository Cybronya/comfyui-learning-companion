---
name: unknown_workflow_upscale_latent_upscale_sampler_22
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.837667
common_nodes: [AudioConcat, CFGGuider, CLIPTextEncode, ComfyMathExpression, CreateVideo, DualCLIPLoader, EmptyLTXVLatentVideo, GetNode, INTConstant, KSamplerSelect, LTXVAudioVAEDecode, LTXVAudioVAEEncode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadAudio, LoadImage, ManualSigmas, NormalizeAudioLoudness, PreviewAudio, PrimitiveBoolean, PrimitiveInt, RandomNoise, ResizeImageMaskNode, ResizeImagesByLongerEdge, SamplerCustomAdvanced, SaveVideo, SetNode, SimpleMath+, TrimAudioDuration, UNETLoader, VAEDecodeTiled, VAELoaderKJ]
problems: []
missing: []
members: [视频生成/图生视频/ltx 2.3 中文无字幕_流畅清晰加强版（写实）_2063909819664388098.json, 视频生成/文生视频/ltx 2.3 中文无字幕_流畅清晰加强版（写实）_2062083287601995777.json, 视频生成/文生视频/图生视频LTX2.3_kijai_fp8_2043785559667122178.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_sampler_22

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/ltx 2.3 中文无字幕_流畅清晰加强版（写实）_2063909819664388098.json、视频生成/文生视频/ltx 2.3 中文无字幕_流畅清晰加强版（写实）_2062083287601995777.json、视频生成/文生视频/图生视频LTX2.3_kijai_fp8_2043785559667122178.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 3 个 workflow 都包含：
- `AudioConcat`
- `CFGGuider`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `CreateVideo`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `INTConstant`
- `KSamplerSelect`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAEEncode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadAudio`
- `LoadImage`
- `ManualSigmas`
- `NormalizeAudioLoudness`
- `PreviewAudio`
- `PrimitiveBoolean`
- `PrimitiveInt`
- `RandomNoise`
- `ResizeImageMaskNode`
- `ResizeImagesByLongerEdge`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `SetNode`
- `SimpleMath+`
- `TrimAudioDuration`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoaderKJ`

**可变部分**（部分 workflow 才有）：
- `ImageScaleByAspectRatio_UTK` —— 2/3 个有
- `LTXFaceDetector` —— 2/3 个有
- `LTXICLoRALoaderModelOnly` —— 2/3 个有
- `LTXLikenessGuide` —— 2/3 个有
- `PromptRelayEncodeTimeline` —— 2/3 个有
- `Prompt_Text` —— 2/3 个有
- `Text Multiline` —— 2/3 个有
- `PrimitiveStringMultiline` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 3 | 100% |
| 高度 | 25 | 25 - 25 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，3 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，3 个样本，取值集中（一致性 100%）
