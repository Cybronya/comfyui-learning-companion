---
name: unknown_workflow_upscale_latent_upscale_sampler_12
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.894125
common_nodes: [CFGGuider, CLIPTextEncode, ComfyMathExpression, DualCLIPLoader, EmptyLTXVLatentVideo, KSamplerSelect, LTXVAudioVAEDecode, LTXVChunkFeedForward, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, ManualSigmas, ModelPatchTorchSettings, PathchSageAttentionKJ, PrimitiveInt, RandomNoise, ResizeImagesByLongerEdge, SamplerCustomAdvanced, UNETLoader, VAEDecodeTiled, VAELoaderKJ]
problems: []
missing: []
members: [视频生成/图生视频/LTX2_3-图生视频 (V5版，切镜人物保持相对一致)_2037403697717714946.json, 视频生成/图生视频/LTX2_3-图生视频V6（参考生成版）_2037865194449281026.json, 视频生成/图生视频/Ltx2.3 PromptRelaySmart(Timeline)_2054921122281467905.json, 视频生成/图生视频/Ltx2.3 PromptRelaySmart动作提示词控制_2054919936321040385.json, 视频生成/图生视频/Ltx2.3 再进化OmniNFT 画质-音质双提升！_2058534614507024386.json, 视频生成/图生视频/aidir-LTX 2.3  首中尾三图+多图_2069594232695902209.json, 视频生成/图生视频/最新LTX2.3 1.1模型 _ 三图-首中尾帧 极速版_2048705684543381506.json, 视频生成/文生视频/LTX 2.3  首中尾三图+多图_2035272794954539010.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_sampler_12

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/LTX2_3-图生视频 (V5版，切镜人物保持相对一致)_2037403697717714946.json、视频生成/图生视频/LTX2_3-图生视频V6（参考生成版）_2037865194449281026.json、视频生成/图生视频/Ltx2.3 PromptRelaySmart(Timeline)_2054921122281467905.json、视频生成/图生视频/Ltx2.3 PromptRelaySmart动作提示词控制_2054919936321040385.json、视频生成/图生视频/Ltx2.3 再进化OmniNFT 画质-音质双提升！_2058534614507024386.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 8 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `KSamplerSelect`
- `LTXVAudioVAEDecode`
- `LTXVChunkFeedForward`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadImage`
- `ManualSigmas`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `PrimitiveInt`
- `RandomNoise`
- `ResizeImagesByLongerEdge`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoaderKJ`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 7/8 个有
- `PrimitiveStringMultiline` —— 6/8 个有
- `VHS_VideoCombine` —— 6/8 个有
- `LTX2_NAG` —— 5/8 个有
- `ResizeImageMaskNode` —— 5/8 个有
- `INTConstant` —— 4/8 个有
- `ImageResizeKJv2` —— 4/8 个有
- `CreateVideo` —— 3/8 个有
- `FloatConstant` —— 3/8 个有
- `LTXVImgToVideoInplaceKJ` —— 3/8 个有
- `RH_LLMAPI_Pro_Node` —— 3/8 个有
- `VAELoader` —— 3/8 个有
- `easy showAnything` —— 3/8 个有
- `Label (rgthree)` —— 2/8 个有
- `LayerUtility: PurgeVRAM` —— 2/8 个有
- `PrimitiveBoolean` —— 2/8 个有
- `PromptRelaySmartEncode` —— 2/8 个有
- `SaveVideo` —— 2/8 个有
- `SimpleCalculatorKJ` —— 2/8 个有
- `easy ifElse` —— 2/8 个有
- `easy imageScaleDown` —— 2/8 个有
- `ImageAddMulti` —— 1/8 个有
- `LTXAddVideoICLoRAGuideAdvanced` —— 1/8 个有
- `LTXICLoRALoaderModelOnly` —— 1/8 个有
- `LTXVAddGuideMulti` —— 1/8 个有
- `PromptRelayEncodeTimeline` —— 1/8 个有
- `SimpleMath+` —— 1/8 个有
- `easy imageRemBg` —— 1/8 个有
- `孤海图像缩放按像素` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 8 | 100% |
| 高度 | 25 | 25 - 44 | 8 | 71% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，8 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 44，8 个样本
