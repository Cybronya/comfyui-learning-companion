---
name: unknown_workflow_video_lora_sampler_666
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.81675
common_nodes: [CLIPTextEncode, DualCLIPLoader, EmptyLTXVLatentVideo, KSamplerAdvanced, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVCropGuides, LTXVSeparateAVLatent, LayerUtility: PurgeVRAM V2, LoraLoaderModelOnly, PainterFrameExtractor, PainterLTX2Vomni, PrimitiveInt, PrimitiveStringMultiline, PromptRelayEncode, RIFEInterpolation, SimpleMath+, UNETLoader, VAEDecodeTiled, VAELoaderKJ, VHS_GetImageCount, VHS_VideoCombine]
problems: []
missing: []
members: [平台全量/LTX2.3 视频配音_2080277383072014337.json, 平台全量/Ltx2.3视频配音+自定义音频_2080289592082784257.json, 视频生成/图生视频/Bernini + LTX2.3 参考生视频+自定义音频_2079522335211745282.json, 视频生成/图生视频/Bernini + LTX2.3 参考生视频_2079543216025726977.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_666

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（平台全量/LTX2.3 视频配音_2080277383072014337.json、平台全量/Ltx2.3视频配音+自定义音频_2080289592082784257.json、视频生成/图生视频/Bernini + LTX2.3 参考生视频+自定义音频_2079522335211745282.json、视频生成/图生视频/Bernini + LTX2.3 参考生视频_2079543216025726977.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `KSamplerAdvanced`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVCropGuides`
- `LTXVSeparateAVLatent`
- `LayerUtility: PurgeVRAM V2`
- `LoraLoaderModelOnly`
- `PainterFrameExtractor`
- `PainterLTX2Vomni`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `PromptRelayEncode`
- `RIFEInterpolation`
- `SimpleMath+`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoaderKJ`
- `VHS_GetImageCount`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `BasicScheduler` —— 2/4 个有
- `BerniniConditioning` —— 2/4 个有
- `CLIPLoader` —— 2/4 个有
- `Fast Groups Bypasser (rgthree)` —— 2/4 个有
- `KSamplerSelect` —— 2/4 个有
- `LTXVAudioVAEEncode` —— 2/4 个有
- `LTXVEmptyLatentAudio` —— 2/4 个有
- `LoadAudio` —— 2/4 个有
- `LoadImage` —— 2/4 个有
- `MelBandRoFormerModelLoader` —— 2/4 个有
- `MelBandRoFormerSampler` —— 2/4 个有
- `PrimitiveFloat` —— 2/4 个有
- `SamplerCustom` —— 2/4 个有
- `SetLatentNoiseMask` —— 2/4 个有
- `SimpleComparison+` —— 2/4 个有
- `SolidMask` —— 2/4 个有
- `SplitSigmas` —— 2/4 个有
- `TrimAudioDuration` —— 2/4 个有
- `VAELoader` —— 2/4 个有
- `VHS_LoadVideo` —— 2/4 个有
- `VHS_VideoInfo` —— 2/4 个有
- `easy ifElse` —— 2/4 个有
- `easy promptConcat` —— 2/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 4 | 75% |
| Prompt 约束强度(CFG) | 9 | 9 - 9 | 4 | 100% |
| 采样算法 | 1 | 1 - 1 | 4 | 100% |
| 调度器 | euler | - | 4 | 100% |
| 重绘幅度 | linear_quadratic | - | 4 | 100% |
| 宽度 | 1 | - | 2 | 100% |
| 高度 | 30 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，4 个样本，一致性 75%
- Prompt 约束强度(CFG) 中位数 9，观测区间 9 - 9，4 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，4 个样本，一致性 100%
- 重绘幅度 最常用 linear_quadratic，4 个样本，一致性 100%
- 宽度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 30，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
