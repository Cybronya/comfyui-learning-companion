---
name: unknown_workflow_upscale_latent_upscale_sampler_23
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.7875
common_nodes: [CFGGuider, CLIPTextEncode, ComfyMathExpression, EmptyLTXVLatentVideo, KSamplerSelect, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVLatentUpsampler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, ManualSigmas, RandomNoise, SamplerCustomAdvanced, VAEDecodeTiled, VAELoaderKJ]
problems: []
missing: []
members: [视频生成/文生视频/LTX2.3 文生_图生视频 KJ版_2030578285100408833.json, 视频生成/文生视频/LTX2.3-GGUF-手动提示词版_2034561004020961282.json, 视频生成/文生视频/LTX2.3-文生视频三采样+自动提示词_2040703381571899393.json, 视频生成/文生视频/LTX2.3_IT2V_Qwen3.5自动提示词_图文生视频(图文合优化并版)_2038990216597344257.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_sampler_23

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/文生视频/LTX2.3 文生_图生视频 KJ版_2030578285100408833.json、视频生成/文生视频/LTX2.3-GGUF-手动提示词版_2034561004020961282.json、视频生成/文生视频/LTX2.3-文生视频三采样+自动提示词_2040703381571899393.json、视频生成/文生视频/LTX2.3_IT2V_Qwen3.5自动提示词_图文生视频(图文合优化并版)_2038990216597344257.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：79%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `ComfyMathExpression`
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
- `RandomNoise`
- `SamplerCustomAdvanced`
- `VAEDecodeTiled`
- `VAELoaderKJ`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 3/4 个有
- `DualCLIPLoader` —— 3/4 个有
- `LTXVImgToVideoInplace` —— 3/4 个有
- `LTXVPreprocess` —— 3/4 个有
- `LoadImage` —— 3/4 个有
- `PrimitiveBoolean` —— 3/4 个有
- `PrimitiveInt` —— 3/4 个有
- `PrimitiveStringMultiline` —— 3/4 个有
- `ResizeImageMaskNode` —— 3/4 个有
- `ResizeImagesByLongerEdge` —— 3/4 个有
- `SaveVideo` —— 3/4 个有
- `ShowText|pysssss` —— 3/4 个有
- `UNETLoader` —— 3/4 个有
- `llama_cpp_instruct_adv` —— 3/4 个有
- `llama_cpp_model_loader` —— 3/4 个有
- `LoraLoaderModelOnly` —— 2/4 个有
- `easy cleanGpuUsed` —— 2/4 个有
- `CR Prompt Text` —— 1/4 个有
- `DualCLIPLoaderGGUF` —— 1/4 个有
- `EmptyImage` —— 1/4 个有
- `FloatConstant` —— 1/4 个有
- `GetImageSize` —— 1/4 个有
- `GetNode` —— 1/4 个有
- `INTConstant` —— 1/4 个有
- `JoinStrings` —— 1/4 个有
- `LTX2SamplingPreviewOverride` —— 1/4 个有
- `LTX2_NAG` —— 1/4 个有
- `MathExpression|pysssss` —— 1/4 个有
- `PainterVRAM` —— 1/4 个有
- `SetNode` —— 1/4 个有
- `SigmasPreview` —— 1/4 个有
- `SimpleMath+` —— 1/4 个有
- `Text` —— 1/4 个有
- `UnetLoaderGGUF` —— 1/4 个有
- `VAELoader` —— 1/4 个有
- `VHS_VideoCombine` —— 1/4 个有
- `llama_cpp_parameters` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 4 | 100% |
| 高度 | 25 | 25 - 25 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，4 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，4 个样本，取值集中（一致性 100%）
