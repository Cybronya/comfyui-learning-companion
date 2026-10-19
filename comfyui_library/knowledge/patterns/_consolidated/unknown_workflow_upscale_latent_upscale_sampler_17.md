---
name: unknown_workflow_upscale_latent_upscale_sampler_17
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.81375
common_nodes: [CLIPLoader, CLIPTextEncode, ComfyMathExpression, ComfySwitchNode, CreateVideo, EmptyLTXVLatentVideo, KSamplerSelect, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVDualCFGGuider, LTXVEmptyLatentAudio, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, ManualSigmas, PreviewAny, PrimitiveBoolean, PrimitiveInt, PrimitiveStringMultiline, RandomNoise, ResizeImageMaskNode, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecodeTiled, VAELoader, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters]
problems: []
missing: []
members: [视频生成/图生视频/LTX2.5音画精准匹配+图生视频+尾帧提取+无限时长_2089012468189323266.json, 视频生成/文生视频/LTX2.5 图生视频_2087377269655425025.json, 视频生成/文生视频/LTX2.5 文生视频_2087431075462213634.json, 视频生成/文生视频/LTX2.5音画精准匹配+图生视频+尾帧提取+无限时长_2092080500621004801.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_sampler_17

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/LTX2.5音画精准匹配+图生视频+尾帧提取+无限时长_2089012468189323266.json、视频生成/文生视频/LTX2.5 图生视频_2087377269655425025.json、视频生成/文生视频/LTX2.5 文生视频_2087431075462213634.json、视频生成/文生视频/LTX2.5音画精准匹配+图生视频+尾帧提取+无限时长_2092080500621004801.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `ComfySwitchNode`
- `CreateVideo`
- `EmptyLTXVLatentVideo`
- `KSamplerSelect`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVDualCFGGuider`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadImage`
- `ManualSigmas`
- `PreviewAny`
- `PrimitiveBoolean`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResizeImageMaskNode`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoader`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`

**可变部分**（部分 workflow 才有）：
- `CLIPVisionEncode` —— 2/4 个有
- `CLIPVisionLoader` —— 2/4 个有
- `DisTorchPurgeVRAMV2` —— 2/4 个有
- `Fast Groups Muter (rgthree)` —— 2/4 个有
- `GetVideoComponents` —— 2/4 个有
- `ImageFromBatch+` —— 2/4 个有
- `ImageSizeAndBatchSize` —— 2/4 个有
- `LoadVideo` —— 2/4 个有
- `PreviewImage` —— 2/4 个有
- `RIFE VFI` —— 2/4 个有
- `TextGenerateLTX2Prompt` —— 2/4 个有
- `VHS_VideoCombine` —— 2/4 个有
- `孤海注释` —— 1/4 个有

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
