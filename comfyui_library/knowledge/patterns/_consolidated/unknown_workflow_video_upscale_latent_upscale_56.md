---
name: unknown_workflow_video_upscale_latent_upscale_56
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.892429
common_nodes: [CFGGuider, CLIPTextEncode, ComfyMathExpression, DualCLIPLoader, EmptyLTXVLatentVideo, ImageResizeKJv2, KSamplerSelect, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, LoraLoaderModelOnly, ManualSigmas, PrimitiveInt, RandomNoise, ResizeImagesByLongerEdge, SamplerCustomAdvanced, UNETLoader, VAEDecodeTiled, VAELoaderKJ, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/LTX2_3-图生视频V6（参考生成版）_2037865194449281026.json, 视频生成/图生视频/Ltx2.3 PromptRelaySmart(Timeline)_2054921122281467905.json, 视频生成/图生视频/Ltx2.3 PromptRelaySmart动作提示词控制_2054919936321040385.json, 视频生成/图生视频/Ltx2.3 再进化OmniNFT 画质-音质双提升！_2058534614507024386.json, 视频生成/图生视频/Ltx2.3 自用优化版 首尾帧_2063969520473165826.json, 视频生成/图生视频/Ltx2.3 自用优化版 首尾帧_2073707066895724546.json, 视频生成/图生视频/Ltx2.3 首尾帧变装+转场_2048728329137688578.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_56

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/LTX2_3-图生视频V6（参考生成版）_2037865194449281026.json、视频生成/图生视频/Ltx2.3 PromptRelaySmart(Timeline)_2054921122281467905.json、视频生成/图生视频/Ltx2.3 PromptRelaySmart动作提示词控制_2054919936321040385.json、视频生成/图生视频/Ltx2.3 再进化OmniNFT 画质-音质双提升！_2058534614507024386.json、视频生成/图生视频/Ltx2.3 自用优化版 首尾帧_2063969520473165826.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 7 个 workflow 都包含：
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
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PrimitiveInt`
- `RandomNoise`
- `ResizeImagesByLongerEdge`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoaderKJ`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LTX2_NAG` —— 6/7 个有
- `PrimitiveStringMultiline` —— 5/7 个有
- `LTXVChunkFeedForward` —— 4/7 个有
- `LTXVImgToVideoInplace` —— 4/7 个有
- `LayerUtility: PurgeVRAM` —— 4/7 个有
- `ModelPatchTorchSettings` —— 4/7 个有
- `PathchSageAttentionKJ` —— 4/7 个有
- `ResizeImageMaskNode` —— 4/7 个有
- `ImageStitch` —— 3/7 个有
- `LTXVFirstLastFrameControl_TTP` —— 3/7 个有
- `SimpleMath+` —— 3/7 个有
- `easy showAnything` —— 3/7 个有
- `llama_cpp_instruct_adv` —— 3/7 个有
- `llama_cpp_model_loader` —— 3/7 个有
- `llama_cpp_parameters` —— 3/7 个有
- `LTXTiledSampler` —— 2/7 个有
- `PromptRelaySmartEncode` —— 2/7 个有
- `INTConstant` —— 1/7 个有
- `ImageAddMulti` —— 1/7 个有
- `LTXVAddGuideMulti` —— 1/7 个有
- `LTXVImgToVideoConditionOnly` —— 1/7 个有
- `PromptRelayEncodeTimeline` —— 1/7 个有
- `easy ifElse` —— 1/7 个有
- `easy imageRemBg` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 7 | 100% |
| 高度 | 25 | 25 - 44 | 7 | 72% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，7 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 44，7 个样本
