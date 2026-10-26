---
name: unknown_workflow_sampler_clip_unet_40
type: Unknown Workflow
frequency: 18
level: strong
coverage: 0.836444
common_nodes: [CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLTXVLatentVideo, KSamplerSelect, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVDualCFGGuider, LTXVEmptyLatentAudio, LTXVSeparateAVLatent, ManualSigmas, PrimitiveInt, RandomNoise, SamplerCustomAdvanced, TextGenerateLTX2Prompt, UNETLoader, VAEDecodeTiled, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/LTX25单图生视频二_2101996495485624321.json, 视频生成/图生视频/LTX25单图生视频第一版_2101966214657564674.json, 视频生成/图生视频/LTX_2.5_图生视频_2090673250572521473.json, 视频生成/图生视频/Ltx2.5图生视频-极速版-高质量-自动扩写提示词_2089690744842969089.json, 视频生成/图生视频/ltx2.5图文生视频_2111289590802903041.json, 视频生成/图生视频/ltx2.5图生视频_2087607964956979202.json, 视频生成/图生视频/video_ltx2_5_i2v-comfyui_2087443808706457602.json, 视频生成/图生视频/video_ltx2_5_i2v_2087366084356820993.json, 视频生成/图生视频/【开源】LTX2.5 图生视频_2087455802314547201.json, 视频生成/图生视频/图生视频  极速  LTX2.5 音画同出_2087530924060798978.json, 视频生成/图生视频/极速图生视频音画同出   LTX2.5_2095738668177780738.json, 视频生成/文生视频/A-8 LTX-2.5 文生视频（T2V）· 音画同步生成_2087369134014291970.json, 视频生成/文生视频/A-8_LTX-2.5_文生视频T2V·_音画同步生成_2104390729396211714.json, 视频生成/文生视频/LTX-2.5 文生视频_2089155568840830977.json, 视频生成/文生视频/LTX-2.5_文生视频T2V·_音画同步生成_2102690657440718849.json, 视频生成/文生视频/LTX-2.5_文生视频T2V·_音画同步生成_2104492526324510722.json, 视频生成/文生视频/LTX2.5 二采高清（图生+文生视频）_2087733249475956738.json, 视频生成/文生视频/LTX2.5 视频生成 I 提示词强化_2087468290628214785.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_40

> 由 `engine/knowledge_consolidation` 从 18 个 workflow 归纳得出（视频生成/图生视频/LTX25单图生视频二_2101996495485624321.json、视频生成/图生视频/LTX25单图生视频第一版_2101966214657564674.json、视频生成/图生视频/LTX_2.5_图生视频_2090673250572521473.json、视频生成/图生视频/Ltx2.5图生视频-极速版-高质量-自动扩写提示词_2089690744842969089.json、视频生成/图生视频/ltx2.5图文生视频_2111289590802903041.json…）

- **类型**：Unknown Workflow
- **样本数**：18
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 18 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLTXVLatentVideo`
- `KSamplerSelect`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVDualCFGGuider`
- `LTXVEmptyLatentAudio`
- `LTXVSeparateAVLatent`
- `ManualSigmas`
- `PrimitiveInt`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `TextGenerateLTX2Prompt`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ComfySwitchNode` —— 17/18 个有
- `PrimitiveBoolean` —— 17/18 个有
- `PrimitiveStringMultiline` —— 17/18 个有
- `ResolutionSelector` —— 17/18 个有
- `LTXVLatentUpsampler` —— 16/18 个有
- `LatentUpscaleModelLoader` —— 16/18 个有
- `PreviewAny` —— 15/18 个有
- `CreateVideo` —— 14/18 个有
- `SaveVideo` —— 14/18 个有
- `LTXVImgToVideoInplace` —— 13/18 个有
- `LoadImage` —— 13/18 个有
- `ResizeImageMaskNode` —— 13/18 个有
- `LTXVPreprocess` —— 12/18 个有
- `VHS_VideoCombine` —— 9/18 个有
- `ImageFromBatch` —— 5/18 个有
- `SaveAudio` —— 5/18 个有
- `SaveImage` —— 5/18 个有
- `ImageResizeKJv2` —— 2/18 个有
- `PurgeVRAM_UTK` —— 2/18 个有
- `StringConcatenate` —— 2/18 个有
- `JjkText` —— 1/18 个有
- `LTX2AttentionTunerPatch` —— 1/18 个有
- `PathchSageAttentionKJ` —— 1/18 个有
- `Text` —— 1/18 个有
- `easy cleanGpuUsed` —— 1/18 个有
- `easy showAnything` —— 1/18 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 18 | 100% |
| 高度 | 25 | 24 - 25 | 18 | 99% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，18 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 24 - 25，18 个样本，取值集中（一致性 99%）
