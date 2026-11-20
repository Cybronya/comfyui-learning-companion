---
name: unknown_workflow_video_sampler_clip_229
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8155
common_nodes: [BlurImageFast, CFGGuider, CLIPLoader, CLIPTextEncode, CheckpointLoaderSimple, EmptyLTXVLatentVideo, FloatConstant, FloatToSigmas, ImageResizeKJ, ImpactSwitch, JWInteger, KSamplerSelect, LTXVAddGuide, LTXVConditioning, LTXVCropGuides, LTXVPreprocess, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, LoadImage, PreviewImage, RH_Captioner, RandomNoise, SamplerCustomAdvanced, ShowText|pysssss, StringConstantMultiline, StringToFloatList, Text Concatenate, Text Multiline, VAEDecode, VHS_VideoCombine]
problems: []
missing: []
members: [平台全量/LTX超稳定超级加速高一致性图生视频_1917745318803210241.json, 视频生成/图生视频/LTXV 0.9.6超稳定超级加速高一致性图生视频V3(修正保存和模式2问题)_1914329665732050945.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_229

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/LTX超稳定超级加速高一致性图生视频_1917745318803210241.json、视频生成/图生视频/LTXV 0.9.6超稳定超级加速高一致性图生视频V3(修正保存和模式2问题)_1914329665732050945.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：82%

## 共有节点

全部 2 个 workflow 都包含：
- `BlurImageFast`
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLTXVLatentVideo`
- `FloatConstant`
- `FloatToSigmas`
- `ImageResizeKJ`
- `ImpactSwitch`
- `JWInteger`
- `KSamplerSelect`
- `LTXVAddGuide`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVPreprocess`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `PreviewImage`
- `RH_Captioner`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `ShowText|pysssss`
- `StringConstantMultiline`
- `StringToFloatList`
- `Text Concatenate`
- `Text Multiline`
- `VAEDecode`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 1/2 个有
- `Note Plus (mtb)` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
