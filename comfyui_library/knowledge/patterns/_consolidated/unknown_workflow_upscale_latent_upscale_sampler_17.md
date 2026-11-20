---
name: unknown_workflow_upscale_latent_upscale_sampler_17
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.968429
common_nodes: [CLIPLoader, CLIPTextEncode, CreateVideo, KSamplerSelect, LTXVConcatAVLatent, LTXVConditioning, LTXVDualCFGGuider, LTXVLatentUpsampler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, ManualSigmas, RandomNoise, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecodeTiled, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/LTX2.5目前最好的商业级数字人_2091907655366434818.json, 平台全量/ltx25-video-upscale-x2_2092893876892819457.json, 平台全量/ltx25-video-upscale-xx_2092905955867582465.json, 数字人/数字人/LTX2.5导演台_audio_2104762505347297281.json, 数字人/数字人/LTX2.5目前最好的商业级数字人_2071844871547211778.json, 视频生成/图生视频/LTX2.5导演台2.5剪辑台_2092197444435140610.json, 视频生成/文生视频/LTX2.5导演台_no_audio_2104764554013138946.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_sampler_17

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/LTX2.5目前最好的商业级数字人_2091907655366434818.json、平台全量/ltx25-video-upscale-x2_2092893876892819457.json、平台全量/ltx25-video-upscale-xx_2092905955867582465.json、数字人/数字人/LTX2.5导演台_audio_2104762505347297281.json、数字人/数字人/LTX2.5目前最好的商业级数字人_2071844871547211778.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CreateVideo`
- `KSamplerSelect`
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
- `LTX2_NAG` —— 5/7 个有
- `LTXDirector` —— 5/7 个有
- `LTXDirectorCropGuides` —— 5/7 个有
- `LTXDirectorGuide` —— 5/7 个有
- `LTXVAudioVAEDecode` —— 5/7 个有
- `LoadVideoUI` —— 3/7 个有
- `GetVideoComponents` —— 2/7 个有
- `LTXVAudioVAEEncode` —— 2/7 个有
- `LoadVideo` —— 2/7 个有
- `VAEEncode` —— 2/7 个有
- `ImageScale` —— 1/7 个有
- `孤海注释` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
