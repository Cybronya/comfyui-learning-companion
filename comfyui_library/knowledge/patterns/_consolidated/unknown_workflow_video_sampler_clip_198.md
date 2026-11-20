---
name: unknown_workflow_video_sampler_clip_198
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.698333
common_nodes: [BasicScheduler, CFGGuider, CLIPTextEncode, DualCLIPLoader, EmptyLTXVLatentVideo, GetNode, INTConstant, ImageResizeKJv2, JoinStrings, KSamplerSelect, LTX2SamplingPreviewOverride, LTX2_NAG, LTXVAudioVAEEncode, LTXVConcatAVLatent, LTXVConditioning, LTXVImgToVideoInplaceKJ, LTXVPreprocess, LTXVSeparateAVLatent, LoadImage, ModelSamplingSD3, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, SamplerCustomAdvanced, SetLatentNoiseMask, SetNode, SolidMask, TrimAudioDuration, UNETLoader, VAEDecode, VAELoader, VAELoaderKJ, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/LTX2.3数字人对口型-16比9多机位成片版_2115832422628683777.json, 视频生成/图生视频/LTX2.3数字人对口型-16比9多机位成片版_2116022840418983938.json, 音频生成/音频生成/【原生 LTX 2.3】数字人说话 _ 唱歌工作流｜图 + 音一键驱动，人物零变形_2047015575972483074.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_198

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/LTX2.3数字人对口型-16比9多机位成片版_2115832422628683777.json、视频生成/图生视频/LTX2.3数字人对口型-16比9多机位成片版_2116022840418983938.json、音频生成/音频生成/【原生 LTX 2.3】数字人说话 _ 唱歌工作流｜图 + 音一键驱动，人物零变形_2047015575972483074.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：70%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicScheduler`
- `CFGGuider`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `INTConstant`
- `ImageResizeKJv2`
- `JoinStrings`
- `KSamplerSelect`
- `LTX2SamplingPreviewOverride`
- `LTX2_NAG`
- `LTXVAudioVAEEncode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVImgToVideoInplaceKJ`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `ModelSamplingSD3`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SetLatentNoiseMask`
- `SetNode`
- `SolidMask`
- `TrimAudioDuration`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VAELoaderKJ`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `ImageBatch` —— 2/3 个有
- `ImageFromBatch` —— 2/3 个有
- `LTX2AttentionTunerPatch` —— 2/3 个有
- `PathchSageAttentionKJ` —— 2/3 个有
- `VHS_LoadAudioUpload` —— 2/3 个有
- `LatentUpscaleModelLoader` —— 1/3 个有
- `LoadAudio` —— 1/3 个有
- `SimpleCalculatorKJ` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
