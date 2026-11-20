---
name: unknown_workflow_video_lora_sampler_834
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.7425
common_nodes: [BasicScheduler, BerniniConditioning, CLIPLoader, CLIPTextEncode, DualCLIPLoader, EmptyLTXVLatentVideo, Fast Groups Bypasser (rgthree), KSamplerAdvanced, KSamplerSelect, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVCropGuides, LTXVSeparateAVLatent, LayerUtility: PurgeVRAM V2, LoadImage, LoraLoaderModelOnly, PainterFrameExtractor, PainterLTX2Vomni, PrimitiveFloat, PrimitiveInt, PrimitiveStringMultiline, PromptRelayEncode, RIFEInterpolation, SamplerCustom, SimpleComparison+, SimpleMath+, SplitSigmas, UNETLoader, VAEDecodeTiled, VAELoader, VAELoaderKJ, VHS_GetImageCount, VHS_VideoCombine, easy ifElse, easy promptConcat]
problems: []
missing: []
members: [视频生成/图生视频/Bernini + LTX2.3 参考生视频+自定义音频_2079522335211745282.json, 视频生成/图生视频/Bernini + LTX2.3 参考生视频_2079543216025726977.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_834

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/Bernini + LTX2.3 参考生视频+自定义音频_2079522335211745282.json、视频生成/图生视频/Bernini + LTX2.3 参考生视频_2079543216025726977.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：74%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicScheduler`
- `BerniniConditioning`
- `CLIPLoader`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `Fast Groups Bypasser (rgthree)`
- `KSamplerAdvanced`
- `KSamplerSelect`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVCropGuides`
- `LTXVSeparateAVLatent`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PainterFrameExtractor`
- `PainterLTX2Vomni`
- `PrimitiveFloat`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `PromptRelayEncode`
- `RIFEInterpolation`
- `SamplerCustom`
- `SimpleComparison+`
- `SimpleMath+`
- `SplitSigmas`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoader`
- `VAELoaderKJ`
- `VHS_GetImageCount`
- `VHS_VideoCombine`
- `easy ifElse`
- `easy promptConcat`

**可变部分**（部分 workflow 才有）：
- `LTXVAudioVAEEncode` —— 1/2 个有
- `LTXVEmptyLatentAudio` —— 1/2 个有
- `LoadAudio` —— 1/2 个有
- `MelBandRoFormerModelLoader` —— 1/2 个有
- `MelBandRoFormerSampler` —— 1/2 个有
- `SetLatentNoiseMask` —— 1/2 个有
- `SolidMask` —— 1/2 个有
- `TrimAudioDuration` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 2 | 50% |
| Prompt 约束强度(CFG) | 9 | - | 2 | 100% |
| 采样算法 | 1 | - | 2 | 100% |
| 调度器 | euler | - | 2 | 100% |
| 重绘幅度 | linear_quadratic | - | 2 | 100% |
| 宽度 | 1 | - | 1 | 100% |
| 高度 | 30 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，2 个样本，一致性 50%
- Prompt 约束强度(CFG) 中位数 9，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，2 个样本，一致性 100%
- 重绘幅度 最常用 linear_quadratic，2 个样本，一致性 100%
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
