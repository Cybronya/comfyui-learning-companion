---
name: unknown_workflow_upscale_latent_upscale_sampler_6
type: Unknown Workflow
frequency: 12
level: strong
coverage: 0.88275
common_nodes: [CLIPLoader, CLIPTextEncode, KSamplerSelect, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVDualCFGGuider, LTXVLatentUpsampler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, ManualSigmas, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecodeTiled, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/LTX2.5目前最好的商业级数字人_2091907655366434818.json, 数字人/数字人/LTX2.5导演台_audio_2104762505347297281.json, 数字人/数字人/LTX2.5目前最好的商业级数字人_2071844871547211778.json, 视频生成/图生视频/LTX2.5导演台2.5剪辑台_2092197444435140610.json, 视频生成/文生视频/LTX2.5导演台_no_audio_2104764554013138946.json, 视频生成/文生视频/LTX2.5超精简文生视频480P只要1分钟【推荐新手试用】​_2087423274367143937.json, 视频生成/文生视频/Y-video_ltx2_5_t2v_2087478473655939074.json, 视频生成/文生视频/ltx2.5_t2v文生视频_2091808540783636482.json, 视频生成/文生视频/video_ltx2_5_t2v_2087405148887928833.json, 视频生成/文生视频/【开源】LTX2.5 文生视频_2087436423283695618.json, 视频生成/文生视频/极速 文生视频 LTX2.5 音画同出_2087530875780157441.json, 视频生成/文生视频/阿清的LTX2.5文-图生视频_2090758573637849089.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_sampler_6

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/LTX2.5目前最好的商业级数字人_2091907655366434818.json、数字人/数字人/LTX2.5导演台_audio_2104762505347297281.json、数字人/数字人/LTX2.5目前最好的商业级数字人_2071844871547211778.json、视频生成/图生视频/LTX2.5导演台2.5剪辑台_2092197444435140610.json、视频生成/文生视频/LTX2.5导演台_no_audio_2104764554013138946.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSamplerSelect`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVDualCFGGuider`
- `LTXVLatentUpsampler`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `ManualSigmas`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 10/12 个有
- `SaveVideo` —— 10/12 个有
- `ComfyMathExpression` —— 7/12 个有
- `EmptyLTXVLatentVideo` —— 7/12 个有
- `LTXVEmptyLatentAudio` —— 7/12 个有
- `PrimitiveInt` —— 7/12 个有
- `ResolutionSelector` —— 7/12 个有
- `PrimitiveStringMultiline` —— 6/12 个有
- `LTX2_NAG` —— 5/12 个有
- `LTXDirector` —— 5/12 个有
- `LTXDirectorCropGuides` —— 5/12 个有
- `LTXDirectorGuide` —— 5/12 个有
- `PrimitiveBoolean` —— 5/12 个有
- `ComfySwitchNode` —— 4/12 个有
- `PreviewAny` —— 4/12 个有
- `TextGenerateLTX2Prompt` —— 4/12 个有
- `LoadVideoUI` —— 3/12 个有
- `LoadImage` —— 2/12 个有
- `VHS_VideoCombine` —— 2/12 个有
- `LTXVImgToVideoInplace` —— 1/12 个有
- `LTXVPreprocess` —— 1/12 个有
- `MuyeTextEditOutput` —— 1/12 个有
- `ResizeImageMaskNode` —— 1/12 个有
- `Text` —— 1/12 个有
- `孤海注释` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 7 | 100% |
| 高度 | 25 | 25 - 25 | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，7 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，7 个样本，取值集中（一致性 100%）
