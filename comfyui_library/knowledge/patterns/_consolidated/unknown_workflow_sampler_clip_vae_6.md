---
name: unknown_workflow_sampler_clip_vae_6
type: Unknown Workflow
frequency: 16
level: strong
coverage: 0.858062
common_nodes: [CLIPTextEncode, ComfyMathExpression, EmptyLTXVLatentVideo, KSamplerSelect, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVImgToVideoInplace, LTXVSeparateAVLatent, LoadImage, ManualSigmas, PrimitiveInt, PrimitiveStringMultiline, RandomNoise, ResizeImageMaskNode, SamplerCustomAdvanced, VAEDecodeTiled]
problems: []
missing: []
members: [视频生成/图生视频/LTX25单图生视频二_2101996495485624321.json, 视频生成/图生视频/LTX25单图生视频第一版_2101966214657564674.json, 视频生成/图生视频/LTX_2.5_图生视频_2090673250572521473.json, 视频生成/图生视频/Ltx2.5图生视频-极速版-高质量-自动扩写提示词_2089690744842969089.json, 视频生成/图生视频/ltx2.5图文生视频_2111289590802903041.json, 视频生成/图生视频/ltx2.5图生视频_2087607964956979202.json, 视频生成/图生视频/video_ltx2_3_FLframe_latent_guide_2031027294181003266.json, 视频生成/图生视频/video_ltx2_3_FLframe_latent_injection_2031010048406720514.json, 视频生成/图生视频/video_ltx2_3_FLframe_latent_injection_2058784933593837570.json, 视频生成/图生视频/video_ltx2_3_FLframe_transition_multi_guide_2036368754602414082.json, 视频生成/图生视频/video_ltx2_3_FLframe_transition_video_inplace_2036749082479304706.json, 视频生成/图生视频/video_ltx2_3_FMLframe_latent_injection1_2031034395125096450.json, 视频生成/图生视频/video_ltx2_5_i2v-comfyui_2087443808706457602.json, 视频生成/图生视频/video_ltx2_5_i2v_2087366084356820993.json, 视频生成/图生视频/本地开源免费，漫剧短镜头3_2057838055628828673.json, 视频生成/图生视频/本地开源免费，真人短镜头3_2058240849422675970.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_6

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（视频生成/图生视频/LTX25单图生视频二_2101996495485624321.json、视频生成/图生视频/LTX25单图生视频第一版_2101966214657564674.json、视频生成/图生视频/LTX_2.5_图生视频_2090673250572521473.json、视频生成/图生视频/Ltx2.5图生视频-极速版-高质量-自动扩写提示词_2089690744842969089.json、视频生成/图生视频/ltx2.5图文生视频_2111289590802903041.json…）

- **类型**：Unknown Workflow
- **样本数**：16
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 16 个 workflow 都包含：
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLTXVLatentVideo`
- `KSamplerSelect`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoInplace`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `ManualSigmas`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResizeImageMaskNode`
- `SamplerCustomAdvanced`
- `VAEDecodeTiled`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 15/16 个有
- `LTXVPreprocess` —— 15/16 个有
- `PrimitiveBoolean` —— 15/16 个有
- `LTXVLatentUpsampler` —— 14/16 个有
- `LatentUpscaleModelLoader` —— 14/16 个有
- `UNETLoader` —— 14/16 个有
- `SaveVideo` —— 13/16 个有
- `VAELoader` —— 10/16 个有
- `CFGGuider` —— 8/16 个有
- `CLIPLoader` —— 8/16 个有
- `DualCLIPLoader` —— 8/16 个有
- `ImageResizeKJv2` —— 8/16 个有
- `LTXVCropGuides` —— 8/16 个有
- `LTXVDualCFGGuider` —— 8/16 个有
- `ResizeImagesByLongerEdge` —— 8/16 个有
- `ResolutionSelector` —— 8/16 个有
- `TextGenerateLTX2Prompt` —— 8/16 个有
- `VAELoaderKJ` —— 8/16 个有
- `ComfySwitchNode` —— 7/16 个有
- `PreviewAny` —— 6/16 个有
- `LTXVImgToVideoInplaceKJ` —— 4/16 个有
- `LoraLoaderModelOnly` —— 4/16 个有
- `VHS_VideoCombine` —— 3/16 个有
- `EnhancedLoadDiffusionModel` —— 2/16 个有
- `LTXVAddGuideMulti` —— 2/16 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/16 个有
- `StringConcatenate` —— 2/16 个有
- `easy indexAnything` —— 2/16 个有
- `JjkText` —— 1/16 个有
- `LTX2AttentionTunerPatch` —— 1/16 个有
- `LoadAudio` —— 1/16 个有
- `PathchSageAttentionKJ` —— 1/16 个有
- `PreviewImage` —— 1/16 个有
- `PurgeVRAM_UTK` —— 1/16 个有
- `Switch` —— 1/16 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 16 | 100% |
| 高度 | 25 | 24 - 25 | 16 | 99% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，16 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 24 - 25，16 个样本，取值集中（一致性 99%）
