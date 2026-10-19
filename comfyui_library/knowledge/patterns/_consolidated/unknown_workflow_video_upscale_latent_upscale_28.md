---
name: unknown_workflow_video_upscale_latent_upscale_28
type: Unknown Workflow
frequency: 13
level: strong
coverage: 0.957385
common_nodes: [CFGGuider, CLIPTextEncode, DualCLIPLoader, EmptyImage, EmptyLTXVLatentVideo, ImageScaleBy, KSamplerSelect, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, ManualSigmas, PathchSageAttentionKJ, RandomNoise, ResizeImagesByLongerEdge, SamplerCustomAdvanced, ShowText|pysssss, SimpleMath+, UNETLoader, VAEDecode, VAELoaderKJ, VHS_VideoCombine, easy imageSize, easy int, easy mathInt]
problems: []
missing: []
members: [视频生成/图生视频/2054550521217855489.json, 视频生成/图生视频/2054554418292502529.json, 视频生成/图生视频/2063043864067399681.json, 视频生成/图生视频/2063157785164083202.json, 视频生成/图生视频/2062774620129939457.json, 视频生成/图生视频/2062869219989086209.json, 视频生成/图生视频/2062051326342815746.json, 视频生成/图生视频/2063144368743206913.json, 视频生成/图生视频/2053064469290463233.json, 视频生成/图生视频/2063911577220378625.json, 视频生成/图生视频/2063914876237602818.json, 视频生成/图生视频/2063429400057704450.json, 视频生成/文生视频/LTX-2.3 Singularity正式优化版（图生视频、首尾帧）优化版_2070498825197940737.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_28

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（视频生成/图生视频/2054550521217855489.json、视频生成/图生视频/2054554418292502529.json、视频生成/图生视频/2063043864067399681.json、视频生成/图生视频/2063157785164083202.json、视频生成/图生视频/2062774620129939457.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：强结论
- **平均知识覆盖**：96%

## 共有节点

全部 13 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyImage`
- `EmptyLTXVLatentVideo`
- `ImageScaleBy`
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
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `ManualSigmas`
- `PathchSageAttentionKJ`
- `RandomNoise`
- `ResizeImagesByLongerEdge`
- `SamplerCustomAdvanced`
- `ShowText|pysssss`
- `SimpleMath+`
- `UNETLoader`
- `VAEDecode`
- `VAELoaderKJ`
- `VHS_VideoCombine`
- `easy imageSize`
- `easy int`
- `easy mathInt`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 12/13 个有
- `CR Text` —— 10/13 个有
- `Fast Groups Muter (rgthree)` —— 10/13 个有
- `LTXVImgToVideoInplaceKJ` —— 10/13 个有
- `RH_LLMAPI_Pro_Node` —— 10/13 个有
- `Dapao_LlamaChat` —— 9/13 个有
- `easy showAnything` —— 7/13 个有
- `CR Prompt Text` —— 5/13 个有
- `llama_cpp_instruct_adv` —— 3/13 个有
- `llama_cpp_model_loader` —— 3/13 个有
- `llama_cpp_parameters` —— 3/13 个有
- `FlashVSRNode` —— 1/13 个有
- `LoraLoaderBlockWeight //Inspire` —— 1/13 个有
- `easy clearCacheAll` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 361 | 361 - 361 | 13 | 100% |
| 高度 | 24 | 24 - 24 | 13 | 100% |
| LoRA 模型强度 | LTX 2.3 - Pixar CGI Toon Style().safetensors | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 361，观测区间 361 - 361，13 个样本，取值集中（一致性 100%）
- 高度 中位数 24，观测区间 24 - 24，13 个样本，取值集中（一致性 100%）
