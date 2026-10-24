---
name: unknown_workflow_video_upscale_latent_upscale_8
type: Unknown Workflow
frequency: 23
level: strong
coverage: 0.950348
common_nodes: [CFGGuider, CLIPTextEncode, DualCLIPLoader, EmptyLTXVLatentVideo, GetImageSize, ImageResizeKJv2, KSamplerSelect, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, LoraLoaderModelOnly, ManualSigmas, PathchSageAttentionKJ, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoaderKJ, VHS_VideoCombine, easy compare, easy ifElse, easy imageSize, easy mathInt, easy positive, easy promptConcat]
problems: []
missing: []
members: [视频生成/图生视频/LTX2.3 -图生视频 超长时间 15s 电商服装模特带货短视频 优化版_2051526645630156801.json, 视频生成/图生视频/LTX2.3 图生视频_2054436042597511169.json, 视频生成/图生视频/LTX2.3 图生视频提示词自动优化版 26-05-07_2052323497153703938.json, 视频生成/图生视频/LTX2.3 漫剧短剧图生视频_2054756564090802178.json, 视频生成/图生视频/LTX2.3 漫剧短剧图生视频_2055141755422560257.json, 视频生成/图生视频/LTX2.3+图生视频_2054731485474770946.json, 视频生成/图生视频/LTX2.3+漫剧短剧图生视频LTX2.3_2058444144254742529.json, 视频生成/图生视频/LTX2.3+漫剧短剧图生视频_2057287117268676609.json, 视频生成/图生视频/LTX2.3+漫剧短剧图生视频_2058362218181386241.json, 视频生成/图生视频/LTX2.3+漫剧短剧图生视频_2058392205324275714.json, 视频生成/图生视频/LTX2.3+漫剧短剧图生视频_2058398311345909761.json, 视频生成/图生视频/LTX2.3+漫剧短剧图生视频_2058417532914196482.json, 视频生成/图生视频/LTX2.3+漫剧短剧图生视频_2058436523154034690.json, 视频生成/图生视频/LTX2.3+漫剧短剧图生视频_2058440251340840961.json, 视频生成/图生视频/LTX2.3+漫剧短剧图生视频_2058444261548453889.json, 视频生成/图生视频/LTX2.3+漫剧短剧图生视频_2058491686904487937.json, 视频生成/图生视频/LTX2.3+漫剧短剧图生视频_2067494155026255873.json, 视频生成/图生视频/ltx2.3-20s服装模特带货短视频-已解决字幕问题_2050955132552134658.json, 视频生成/图生视频/ltx2.3-qwen3-tts-服装模特带货短视频_2055109104980504577.json, 视频生成/图生视频/一键生成--LTX2.3 图生视频_2057346400337358850.json, 视频生成/图生视频/一键生成--LTX2.3 图生视频_2057635344086028289.json, 视频生成/文生视频/LTX2.3 图生视频提示词自动优化版_2071572188259512321.json, 视频生成/文生视频/LTX2.3+-图生视频+15s超长时间+电商服装模特带货短视频+优化版_2052915059373953025.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_8

> 由 `engine/knowledge_consolidation` 从 23 个 workflow 归纳得出（视频生成/图生视频/LTX2.3 -图生视频 超长时间 15s 电商服装模特带货短视频 优化版_2051526645630156801.json、视频生成/图生视频/LTX2.3 图生视频_2054436042597511169.json、视频生成/图生视频/LTX2.3 图生视频提示词自动优化版 26-05-07_2052323497153703938.json、视频生成/图生视频/LTX2.3 漫剧短剧图生视频_2054756564090802178.json、视频生成/图生视频/LTX2.3 漫剧短剧图生视频_2055141755422560257.json…）

- **类型**：Unknown Workflow
- **样本数**：23
- **可信度**：强结论
- **平均知识覆盖**：95%

## 共有节点

全部 23 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `GetImageSize`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsampler`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PathchSageAttentionKJ`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoaderKJ`
- `VHS_VideoCombine`
- `easy compare`
- `easy ifElse`
- `easy imageSize`
- `easy mathInt`
- `easy positive`
- `easy promptConcat`

**可变部分**（部分 workflow 才有）：
- `ImageConcanate` —— 22/23 个有
- `LTXVEmptyLatentAudio` —— 22/23 个有
- `LTXVPreprocess` —— 22/23 个有
- `ResizeImagesByLongerEdge` —— 22/23 个有
- `EmptyImage` —— 21/23 个有
- `ImageScaleBy` —— 21/23 个有
- `easy int` —— 21/23 个有
- `CR Text` —— 19/23 个有
- `Dapao_LlamaChat` —— 19/23 个有
- `SimpleMath+` —— 19/23 个有
- `AILab_QwenVL` —— 4/23 个有
- `PreviewImage` —— 4/23 个有
- `easy showAnything` —— 4/23 个有
- `PreviewAny` —— 2/23 个有
- `Seed (rgthree)` —— 2/23 个有
- `CM_FloatToInt` —— 1/23 个有
- `ExtractLinesByIndex` —— 1/23 个有
- `LTXVAudioVAEEncode` —— 1/23 个有
- `LayerUtility: TextImage V2` —— 1/23 个有
- `LoadAudio` —— 1/23 个有
- `Note Plus (mtb)` —— 1/23 个有
- `PreviewAudio` —— 1/23 个有
- `Qwen3TTSModelLoader` —— 1/23 个有
- `Qwen3TTSVoiceClone` —— 1/23 个有
- `SetLatentNoiseMask` —— 1/23 个有
- `SolidMask` —— 1/23 个有
- `SoundFlow_GetLength` —— 1/23 个有
- `easy cleanGpuUsed` —— 1/23 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 361 | 361 - 481 | 22 | 93% |
| 高度 | 24 | 24 - 24 | 22 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 361，观测区间 361 - 481，22 个样本，取值集中（一致性 93%）
- 高度 中位数 24，观测区间 24 - 24，22 个样本，取值集中（一致性 100%）
