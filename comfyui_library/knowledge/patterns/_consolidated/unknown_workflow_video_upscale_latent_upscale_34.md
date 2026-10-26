---
name: unknown_workflow_video_upscale_latent_upscale_34
type: Unknown Workflow
frequency: 10
level: strong
coverage: 0.8139
common_nodes: [CFGGuider, CLIPTextEncode, ComfyMathExpression, DualCLIPLoader, EmptyLTXVLatentVideo, GetImageSize, GetNode, ImageResizeKJv2, ImageScaleToTotalPixels, KSamplerSelect, LTX2_NAG, LTXVAudioVAEEncode, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVImgToVideoInplace, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LayerUtility: PurgeVRAM V2, LoadAudio, LoadImage, LoraLoaderModelOnly, MelBandRoFormerModelLoader, MelBandRoFormerSampler, PreviewAudio, PrimitiveBoolean, PrimitiveInt, PrimitiveStringMultiline, RandomNoise, ResizeImagesByLongerEdge, SamplerCustomAdvanced, SetLatentNoiseMask, SetNode, SimpleMath+, SolidMask, SoundFlow_GetLength, TrimAudioDuration, UNETLoader, VAELoader, VAELoaderKJ, VHS_VideoCombine, easy int, easy showAnything]
problems: []
missing: []
members: [图片生成/文生图/LTX2.3数字人-(修仙传角色)_2064873985099255809.json, 数字人/数字人/LTX2.3数字人30S只要10分钟-(预置凡人修仙传角色)_2067452419683995650.json, 数字人/数字人/LTX2.3高动态数字人带一致性保持(预置凡人修仙传角色)_2064430603466010626.json, 视频生成/图生视频/30S图生视频 LTX2.3数字人 对口型 说话唱歌 30S只要10分钟 内置lora角色_2068875271280873474.json, 视频生成/图生视频/LTX2.3 动漫数字人特制版_2069018499376312322.json, 视频生成/图生视频/LTX2.3数字人30S只要10分钟-(小海豚老师教唱歌学员专用)_2069213658181365761.json, 视频生成/图生视频/图生视频-LTX2.3数字人30S只要10分钟_2068898654504706050.json, 视频生成/图生视频/图生视频-LTX2.3数字人30S只要10分钟_2069966527956344833.json, 视频生成/图生视频/图生视频-LTX2.3数字人30S只要10分钟_2075040945753640962.json, 视频生成/图生视频/图生视频-LTX2.3数字人30S只要10分钟_2095739123867938818.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_34

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/文生图/LTX2.3数字人-(修仙传角色)_2064873985099255809.json、数字人/数字人/LTX2.3数字人30S只要10分钟-(预置凡人修仙传角色)_2067452419683995650.json、数字人/数字人/LTX2.3高动态数字人带一致性保持(预置凡人修仙传角色)_2064430603466010626.json、视频生成/图生视频/30S图生视频 LTX2.3数字人 对口型 说话唱歌 30S只要10分钟 内置lora角色_2068875271280873474.json、视频生成/图生视频/LTX2.3 动漫数字人特制版_2069018499376312322.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 10 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `GetImageSize`
- `GetNode`
- `ImageResizeKJv2`
- `ImageScaleToTotalPixels`
- `KSamplerSelect`
- `LTX2_NAG`
- `LTXVAudioVAEEncode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoInplace`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LayerUtility: PurgeVRAM V2`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler`
- `PreviewAudio`
- `PrimitiveBoolean`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResizeImagesByLongerEdge`
- `SamplerCustomAdvanced`
- `SetLatentNoiseMask`
- `SetNode`
- `SimpleMath+`
- `SolidMask`
- `SoundFlow_GetLength`
- `TrimAudioDuration`
- `UNETLoader`
- `VAELoader`
- `VAELoaderKJ`
- `VHS_VideoCombine`
- `easy int`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CM_IntUnaryCondition` —— 9/10 个有
- `CR Prompt Text` —— 9/10 个有
- `CR String To Boolean` —— 9/10 个有
- `ImpactConditionalBranch` —— 9/10 个有
- `IndexTTS2Run` —— 9/10 个有
- `PrimitiveFloat` —— 9/10 个有
- `easy anythingIndexSwitch` —— 9/10 个有
- `BasicScheduler` —— 8/10 个有
- `JoinStrings` —— 8/10 个有
- `LTXVTiledVAEDecode` —— 8/10 个有
- `ModelSamplingSD3` —— 7/10 个有
- `JoinStringMulti` —— 2/10 个有
- `LTXVLatentUpsampler` —— 2/10 个有
- `LTXVScheduler` —— 2/10 个有
- `ManualSigmas` —— 2/10 个有
- `VAEDecode` —— 2/10 个有
- `ComfySwitchNode` —— 1/10 个有
- `Evaluate Strings` —— 1/10 个有
- `LTX2SamplingPreviewOverride` —— 1/10 个有
- `ResolutionSelector` —— 1/10 个有
- `ShowText|pysssss` —— 1/10 个有
- `easy float` —— 1/10 个有
- `llama_cpp_instruct_adv` —— 1/10 个有
- `llama_cpp_model_loader` —— 1/10 个有
- `llama_cpp_parameters` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 10 | 100% |
| 高度 | 25 | 25 - 25 | 10 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，10 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，10 个样本，取值集中（一致性 100%）
