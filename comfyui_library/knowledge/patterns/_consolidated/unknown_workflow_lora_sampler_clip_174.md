---
name: unknown_workflow_lora_sampler_clip_174
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.689667
common_nodes: [BasicScheduler, CFGGuider, CLIPTextEncode, CM_FloatToInt, DiffusionModelLoaderKJ, DualCLIPLoaderGGUF, EmptyLTXVLatentVideo, Float, GetNode, INTConstant, ImageResizeKJv2, KSamplerSelect, LTX2_NAG, LTXVAudioVAEEncode, LTXVConcatAVLatent, LTXVConditioning, LTXVSeparateAVLatent, LoadImage, LoraLoaderModelOnly, PreviewAudio, PreviewImage, RandomNoise, SamplerCustomAdvanced, SetLatentNoiseMask, SetNode, SimpleMath+, SolidMask, VAEDecodeTiled, VAELoaderKJ, VHS_LoadAudioUpload, VisualizeSigmasKJ, easy showAnything]
problems: []
missing: []
members: [图片生成/反推提示词/78singsong_2052695235456712706.json, 视频生成/图生视频/LTX2.3极速超级数字人图生视频_2061333260944367617.json, 视频生成/图生视频/LTX2.3极速超级数字人首尾帧生视频_2061445369535483905.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_174

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/反推提示词/78singsong_2052695235456712706.json、视频生成/图生视频/LTX2.3极速超级数字人图生视频_2061333260944367617.json、视频生成/图生视频/LTX2.3极速超级数字人首尾帧生视频_2061445369535483905.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：69%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicScheduler`
- `CFGGuider`
- `CLIPTextEncode`
- `CM_FloatToInt`
- `DiffusionModelLoaderKJ`
- `DualCLIPLoaderGGUF`
- `EmptyLTXVLatentVideo`
- `Float`
- `GetNode`
- `INTConstant`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `LTX2_NAG`
- `LTXVAudioVAEEncode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewAudio`
- `PreviewImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SetLatentNoiseMask`
- `SetNode`
- `SimpleMath+`
- `SolidMask`
- `VAEDecodeTiled`
- `VAELoaderKJ`
- `VHS_LoadAudioUpload`
- `VisualizeSigmasKJ`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `LTXVImgToVideoInplace` —— 2/3 个有
- `PrimitiveBoolean` —— 2/3 个有
- `VHS_SelectImages` —— 2/3 个有
- `VHS_VideoCombine` —— 2/3 个有
- `CM_IntToFloat` —— 1/3 个有
- `CreateVideo` —— 1/3 个有
- `LTXVAddGuideMulti` —— 1/3 个有
- `LTXVCropGuides` —— 1/3 个有
- `RTXVideoSuperResolution` —— 1/3 个有
- `SaveVideo` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
