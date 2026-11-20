---
name: unknown_workflow_upscale_latent_upscale_sampler_10
type: Unknown Workflow
frequency: 10
level: strong
coverage: 0.7541
common_nodes: [CFGGuider, CLIPTextEncode, ComfyMathExpression, DualCLIPLoader, EmptyLTXVLatentVideo, ImageResizeKJv2, KSamplerSelect, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, ManualSigmas, PrimitiveInt, RandomNoise, ResizeImagesByLongerEdge, SamplerCustomAdvanced, UNETLoader, VAEDecodeTiled, VAELoaderKJ]
problems: []
missing: []
members: [视频生成/图生视频/LTX23_i2v_pose_control_2076514549532024833.json, 视频生成/图生视频/video_ltx2_3_FLframe_latent_guide_2031027294181003266.json, 视频生成/图生视频/video_ltx2_3_FLframe_latent_injection_2031010048406720514.json, 视频生成/图生视频/video_ltx2_3_FLframe_latent_injection_2058784933593837570.json, 视频生成/图生视频/video_ltx2_3_FLframe_transition_multi_guide_2036368754602414082.json, 视频生成/图生视频/video_ltx2_3_FLframe_transition_video_inplace_2036749082479304706.json, 视频生成/图生视频/video_ltx2_3_FMLframe_latent_injection1_2031034395125096450.json, 视频生成/图生视频/video_ltx2_3_i2v_galaxyAce_2037940462845169665.json, 视频生成/图生视频/video_ltx2_3_i2v_kijai_three_stage_2039715377143353346.json, 视频生成/图生视频/video_ltx2_3_i2v_kijai_three_stage_2041087454286979073.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_sampler_10

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/LTX23_i2v_pose_control_2076514549532024833.json、视频生成/图生视频/video_ltx2_3_FLframe_latent_guide_2031027294181003266.json、视频生成/图生视频/video_ltx2_3_FLframe_latent_injection_2031010048406720514.json、视频生成/图生视频/video_ltx2_3_FLframe_latent_injection_2058784933593837570.json、视频生成/图生视频/video_ltx2_3_FLframe_transition_multi_guide_2036368754602414082.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：75%

## 共有节点

全部 10 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `ManualSigmas`
- `PrimitiveInt`
- `RandomNoise`
- `ResizeImagesByLongerEdge`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoaderKJ`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 9/10 个有
- `PrimitiveStringMultiline` —— 9/10 个有
- `CreateVideo` —— 7/10 个有
- `PrimitiveBoolean` —— 7/10 个有
- `ResizeImageMaskNode` —— 7/10 个有
- `SaveVideo` —— 5/10 个有
- `VHS_VideoCombine` —— 5/10 个有
- `LTXVImgToVideoInplaceKJ` —— 4/10 个有
- `LoraLoader` —— 4/10 个有
- `LoraLoaderModelOnly` —— 4/10 个有
- `PreviewImage` —— 4/10 个有
- `GetNode` —— 3/10 个有
- `SetNode` —— 3/10 个有
- `LTXVAddGuideMulti` —— 2/10 个有
- `LTX2_NAG` —— 1/10 个有
- `LTXAddVideoICLoRAGuide` —— 1/10 个有
- `LTXICLoRALoaderModelOnly` —— 1/10 个有
- `PathchSageAttentionKJ` —— 1/10 个有
- `RebatchImages` —— 1/10 个有
- `SDVN Load Image Url` —— 1/10 个有
- `SaveAudio` —— 1/10 个有
- `String` —— 1/10 个有
- `VHS_LoadVideo` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 10 | 100% |
| 高度 | 25 | 25 - 25 | 10 | 100% |
| LoRA 模型强度 | 1 | 0 - 1 | 4 | 42% |
| LoRA 文本强度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，10 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，10 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1，观测区间 0 - 1，4 个样本，取值分散，一致性仅 42%
- LoRA 文本强度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
