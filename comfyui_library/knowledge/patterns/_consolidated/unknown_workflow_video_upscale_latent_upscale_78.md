---
name: unknown_workflow_video_upscale_latent_upscale_78
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.4898
common_nodes: [Anything Everywhere, CFGGuider, CLIPTextEncode, ComfyMathExpression, DualCLIPLoader, EmptyLTXVLatentVideo, GetNode, KSamplerSelect, LTX2_NAG, LTXVAudioVAEDecode, LTXVChunkFeedForward, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, ManualSigmas, MathExpression|pysssss, ModelPatchTorchSettings, PathchSageAttentionKJ, PrimitiveBoolean, PrimitiveInt, RandomNoise, SamplerCustomAdvanced, SetNode, VAEDecodeTiled, VAELoaderKJ, VHS_VideoCombine, easy cleanGpuUsed]
problems: []
missing: []
members: [视频生成/图生视频/LTX2.3+首尾帧gguf_2037924833685671937.json, 视频生成/文生视频/LTX2.3 单图&文生视频_2035556553025134594.json, 视频生成/文生视频/LTX2.3 生长视频版-18秒视频16分钟生成-单图&文生视频-加强版_2035746141073051650.json, 视频生成/文生视频/LTX2.3 生长视频版-30秒视频8分半钟生成-首尾帧双图&文生视频-加强版_2035952445355986945.json, 视频生成/文生视频/LTX2.3 生长视频版-50秒视频15分钟生成-首中尾帧三图&文生视频-加强版_2036052171002748929.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_78

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/LTX2.3+首尾帧gguf_2037924833685671937.json、视频生成/文生视频/LTX2.3 单图&文生视频_2035556553025134594.json、视频生成/文生视频/LTX2.3 生长视频版-18秒视频16分钟生成-单图&文生视频-加强版_2035746141073051650.json、视频生成/文生视频/LTX2.3 生长视频版-30秒视频8分半钟生成-首尾帧双图&文生视频-加强版_2035952445355986945.json、视频生成/文生视频/LTX2.3 生长视频版-50秒视频15分钟生成-首中尾帧三图&文生视频-加强版_2036052171002748929.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：49%

## 共有节点

全部 5 个 workflow 都包含：
- `Anything Everywhere`
- `CFGGuider`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `KSamplerSelect`
- `LTX2_NAG`
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
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `ManualSigmas`
- `MathExpression|pysssss`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `PrimitiveBoolean`
- `PrimitiveInt`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SetNode`
- `VAEDecodeTiled`
- `VAELoaderKJ`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 4/5 个有
- `ShowText|pysssss` —— 4/5 个有
- `UNETLoader` —— 4/5 个有
- `llama_cpp_instruct_adv` —— 4/5 个有
- `llama_cpp_model_loader` —— 4/5 个有
- `LTXVImgToVideoInplaceKJ` —— 3/5 个有
- `WujiCleaner` —— 3/5 个有
- `easy imageConcat` —— 2/5 个有
- `UnetLoaderGGUF` —— 1/5 个有
- `VRAMReserver` —— 1/5 个有

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
