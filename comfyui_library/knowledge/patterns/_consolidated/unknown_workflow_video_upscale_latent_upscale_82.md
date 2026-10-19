---
name: unknown_workflow_video_upscale_latent_upscale_82
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.8686
common_nodes: [CFGGuider, CLIPTextEncode, ComfyMathExpression, DualCLIPLoader, EmptyLTXVLatentVideo, KSamplerSelect, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVLatentUpsampler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, ManualSigmas, PrimitiveInt, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecodeTiled, VAELoaderKJ, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/文生视频/LTX2.3 文生_图生视频 KJ版_2030578285100408833.json, 视频生成/文生视频/LTX2.3 自用版 T2V_2063969490962042881.json, 视频生成/文生视频/LTX2.3图生视频（自动提示词）工作流_2030929565035536385.json, 视频生成/文生视频/LTX2.3文生视频（自动提示词）工作流_2031313603197935618.json, 视频生成/文生视频/LTX2.3音图生视频工作流_2031546661310308354.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_82

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/文生视频/LTX2.3 文生_图生视频 KJ版_2030578285100408833.json、视频生成/文生视频/LTX2.3 自用版 T2V_2063969490962042881.json、视频生成/文生视频/LTX2.3图生视频（自动提示词）工作流_2030929565035536385.json、视频生成/文生视频/LTX2.3文生视频（自动提示词）工作流_2031313603197935618.json、视频生成/文生视频/LTX2.3音图生视频工作流_2031546661310308354.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 5 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `KSamplerSelect`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVLatentUpsampler`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `ManualSigmas`
- `PrimitiveInt`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoaderKJ`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 4/5 个有
- `LTXVImgToVideoInplace` —— 3/5 个有
- `LTXVPreprocess` —— 3/5 个有
- `LoadImage` —— 3/5 个有
- `PathchSageAttentionKJ` —— 3/5 个有
- `PrimitiveBoolean` —— 3/5 个有
- `RIFEInterpolation` —— 3/5 个有
- `ResizeImagesByLongerEdge` —— 3/5 个有
- `easy showAnything` —— 3/5 个有
- `Int` —— 2/5 个有
- `MuyeTextEditOutput` —— 2/5 个有
- `PreviewAny` —— 2/5 个有
- `PrimitiveStringMultiline` —— 2/5 个有
- `ResizeImageMaskNode` —— 2/5 个有
- `llama_cpp_instruct_adv` —— 2/5 个有
- `llama_cpp_model_loader` —— 2/5 个有
- `BasicScheduler` —— 1/5 个有
- `INTConstant` —— 1/5 个有
- `LTX2_NAG` —— 1/5 个有
- `LTXTiledSampler` —— 1/5 个有
- `LTXVAudioVAEEncode` —— 1/5 个有
- `LayerUtility: PurgeVRAM` —— 1/5 个有
- `LoadAudio` —— 1/5 个有
- `PromptRelayEncode` —— 1/5 个有
- `Resize` —— 1/5 个有
- `SetLatentNoiseMask` —— 1/5 个有
- `SimpleMath+` —— 1/5 个有
- `SolidMask` —— 1/5 个有
- `Text Multiline` —— 1/5 个有
- `TrimAudioDuration` —— 1/5 个有
- `easy anythingIndexSwitch` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 5 | 100% |
| 高度 | 25 | 25 - 25 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，5 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，5 个样本，取值集中（一致性 100%）
