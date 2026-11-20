---
name: unknown_workflow_video_upscale_latent_upscale_111
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.619333
common_nodes: [CFGGuider, CLIPTextEncode, DualCLIPLoader, EmptyLTXVLatentVideo, GetImageSize, ImageResizeKJv2, KSamplerSelect, LTXAddVideoICLoRAGuide, LTXICLoRALoaderModelOnly, LTXTiledSampler, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVLatentUpsamplerTiled, LTXVSeparateAVLatent, LatentUpscaleModelLoader, ManualSigmas, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecodeTiled, VAELoaderKJ, VHS_LoadVideo, VHS_VideoCombine]
problems: []
missing: []
members: [平台全量/电商视频编辑更换拍摄角度 Ltx2.3 CrossView_2079148058566283266.json, 视频生成/图生视频/LTX-2.3_ICLoRA_crossview_2076951479637864450.json, 视频生成/图生视频/LTXIC视频生成 二次元_2079022514478608385.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_111

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/电商视频编辑更换拍摄角度 Ltx2.3 CrossView_2079148058566283266.json、视频生成/图生视频/LTX-2.3_ICLoRA_crossview_2076951479637864450.json、视频生成/图生视频/LTXIC视频生成 二次元_2079022514478608385.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：62%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `GetImageSize`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `LTXAddVideoICLoRAGuide`
- `LTXICLoRALoaderModelOnly`
- `LTXTiledSampler`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVLatentUpsamplerTiled`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `ManualSigmas`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoaderKJ`
- `VHS_LoadVideo`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 2/3 个有
- `INTConstant` —— 2/3 个有
- `SetNode` —— 2/3 个有
- `SimpleMath+` —— 2/3 个有
- `VHS_VideoInfo` —— 2/3 个有
- `CM_IntToFloat` —— 1/3 个有
- `JjkText` —— 1/3 个有
- `MathExpression|pysssss` —— 1/3 个有
- `PreviewAny` —— 1/3 个有
- `easy int` —— 1/3 个有
- `easy showAnything` —— 1/3 个有

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
