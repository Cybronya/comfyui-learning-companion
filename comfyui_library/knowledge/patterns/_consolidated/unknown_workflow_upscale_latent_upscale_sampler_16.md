---
name: unknown_workflow_upscale_latent_upscale_sampler_16
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.9722
common_nodes: [CLIPLoader, CLIPTextEncode, CreateVideo, KSamplerSelect, LTX2_NAG, LTXDirector, LTXDirectorCropGuides, LTXDirectorGuide, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVDualCFGGuider, LTXVLatentUpsampler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, ManualSigmas, RandomNoise, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecodeTiled, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/LTX2.5目前最好的商业级数字人_2091907655366434818.json, 数字人/数字人/LTX2.5导演台_audio_2104762505347297281.json, 数字人/数字人/LTX2.5目前最好的商业级数字人_2071844871547211778.json, 视频生成/图生视频/LTX2.5导演台2.5剪辑台_2092197444435140610.json, 视频生成/文生视频/LTX2.5导演台_no_audio_2104764554013138946.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_sampler_16

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/LTX2.5目前最好的商业级数字人_2091907655366434818.json、数字人/数字人/LTX2.5导演台_audio_2104762505347297281.json、数字人/数字人/LTX2.5目前最好的商业级数字人_2071844871547211778.json、视频生成/图生视频/LTX2.5导演台2.5剪辑台_2092197444435140610.json、视频生成/文生视频/LTX2.5导演台_no_audio_2104764554013138946.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CreateVideo`
- `KSamplerSelect`
- `LTX2_NAG`
- `LTXDirector`
- `LTXDirectorCropGuides`
- `LTXDirectorGuide`
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
- `SaveVideo`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadVideoUI` —— 3/5 个有
- `孤海注释` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
