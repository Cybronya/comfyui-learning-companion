---
name: unknown_workflow_video_upscale_latent_upscale_26
type: Unknown Workflow
frequency: 13
level: strong
coverage: 0.443923
common_nodes: [BasicScheduler, CFGGuider, CLIPTextEncode, ComfyMathExpression, ComfySwitchNode, DualCLIPLoader, EmptyLTXVLatentVideo, GetImageSizeAndCount, GetNode, INTConstant, ImageResizeKJv2, KSamplerSelect, LTX2AttentionTunerPatch, LTX2SamplingPreviewOverride, LTX2_NAG, LTXAddVideoICLoRAGuide, LTXICLoRALoaderModelOnly, LTXVAudioVAEDecode, LTXVChunkFeedForward, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVLatentUpsampler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LiconMSR, LoadImage, LoraLoaderModelOnly, ManualSigmas, ModelSamplingSD3, PathchSageAttentionKJ, PrimitiveBoolean, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, SetNode, SimpleCalculatorKJ, UNETLoader, VAEDecode, VAELoader, VAELoaderKJ, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/33.LTX-2.3 多角色参考_2083954070502596610.json, 视频生成/图生视频/2068774393836302338.json, 视频生成/图生视频/2062011300338823170.json, 视频生成/图生视频/2063462550611779585.json, 视频生成/图生视频/2063467103675568130.json, 视频生成/图生视频/2063551335492050946.json, 视频生成/图生视频/2063834654762950658.json, 视频生成/图生视频/LTX2.3+MSR 多主体生视频_2083049154284187649.json, 视频生成/图生视频/2063649146149625858.json, 视频生成/图生视频/2068654333478129665.json, 视频生成/图生视频/数字人短剧剧情LTX2.3+MSR V2高动效，人物一致性，高质量视频制作_2082742613286932481.json, 视频生成/文生视频/LTX-2.3-MSR-多主体参考视频生成_2065248408478248962.json, 视频生成/文生视频/LTX2.3+MSR V2高动效，高人物一致，高质量视频制作_2081628938446655489.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_26

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（视频生成/图生视频/33.LTX-2.3 多角色参考_2083954070502596610.json、视频生成/图生视频/2068774393836302338.json、视频生成/图生视频/2062011300338823170.json、视频生成/图生视频/2063462550611779585.json、视频生成/图生视频/2063467103675568130.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：强结论
- **平均知识覆盖**：44%

## 共有节点

全部 13 个 workflow 都包含：
- `BasicScheduler`
- `CFGGuider`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `ComfySwitchNode`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `GetImageSizeAndCount`
- `GetNode`
- `INTConstant`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `LTX2AttentionTunerPatch`
- `LTX2SamplingPreviewOverride`
- `LTX2_NAG`
- `LTXAddVideoICLoRAGuide`
- `LTXICLoRALoaderModelOnly`
- `LTXVAudioVAEDecode`
- `LTXVChunkFeedForward`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVLatentUpsampler`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LiconMSR`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `PrimitiveBoolean`
- `PrimitiveFloat`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SetNode`
- `SimpleCalculatorKJ`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VAELoaderKJ`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 9/13 个有
- `ImageBatchMulti` —— 9/13 个有
- `LTXVAddGuideMulti` —— 9/13 个有
- `LTXVAddGuidesFromBatch` —— 9/13 个有
- `RMBG` —— 9/13 个有
- `SaveVideo` —— 9/13 个有
- `SeedGenerator` —— 9/13 个有
- `TextInput_` —— 5/13 个有
- `ComfyNumberConvert` —— 4/13 个有
- `LTX2MemoryEfficientSageAttentionPatch` —— 4/13 个有
- `PromptRelayEncode` —— 4/13 个有
- `FlashVSRInitPipe` —— 2/13 个有
- `FlashVSRNodeAdv` —— 2/13 个有
- `Label (rgthree)` —— 2/13 个有
- `PreviewAny` —— 2/13 个有
- `PromptRelayEncodeTimeline` —— 2/13 个有
- `RH_LLMAPI_NODE` —— 2/13 个有
- `TTP_text_mix` —— 2/13 个有
- `DualCLIPLoaderGGUF` —— 1/13 个有
- `Power Lora Loader (rgthree)` —— 1/13 个有
- `UnetLoaderGGUF` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 145 | 145 - 241 | 13 | 75% |
| 高度 | 24 | 24 - 24 | 13 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 145，观测区间 145 - 241，13 个样本
- 高度 中位数 24，观测区间 24 - 24，13 个样本，取值集中（一致性 100%）
