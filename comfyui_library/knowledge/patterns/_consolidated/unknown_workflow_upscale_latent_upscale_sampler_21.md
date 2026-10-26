---
name: unknown_workflow_upscale_latent_upscale_sampler_21
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.843
common_nodes: [CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLTXVLatentVideo, KSamplerSelect, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVLatentUpsampler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, ManualSigmas, PrimitiveInt, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecodeTiled, VAELoader, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/LTX-2.5-I2V+双采样加速视频生成_2096206827863232514.json, 视频生成/图生视频/LTX2.5-图生视频_2087515101900402690.json, 视频生成/图生视频/LTX2.5图生视频 -自动扩写提示词-高质量直出1K_2087739505318129665.json, 视频生成/文生视频/LTX2.5文生视频-自动扩写提示词-高质量直出1K_2087739530110660610.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_sampler_21

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/LTX-2.5-I2V+双采样加速视频生成_2096206827863232514.json、视频生成/图生视频/LTX2.5-图生视频_2087515101900402690.json、视频生成/图生视频/LTX2.5图生视频 -自动扩写提示词-高质量直出1K_2087739505318129665.json、视频生成/文生视频/LTX2.5文生视频-自动扩写提示词-高质量直出1K_2087739530110660610.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLTXVLatentVideo`
- `KSamplerSelect`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVEmptyLatentAudio`
- `LTXVLatentUpsampler`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `ManualSigmas`
- `PrimitiveInt`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 3/4 个有
- `LTXVDualCFGGuider` —— 3/4 个有
- `LTXVImgToVideoInplace` —— 3/4 个有
- `LTXVPreprocess` —— 3/4 个有
- `LoadImage` —— 3/4 个有
- `RH_LLMAPI_Pro_Node` —— 3/4 个有
- `CreateVideo` —— 2/4 个有
- `PrimitiveBoolean` —— 2/4 个有
- `ResizeImageMaskNode` —— 2/4 个有
- `SaveVideo` —— 2/4 个有
- `ShellAgentPluginOutputText` —— 2/4 个有
- `VHS_VideoCombine` —— 2/4 个有
- `CFGGuider` —— 1/4 个有
- `CR Text` —— 1/4 个有
- `EmptyImage` —— 1/4 个有
- `GetImageSize` —— 1/4 个有
- `ImageResizeKJv2` —— 1/4 个有
- `ImageScaleBy` —— 1/4 个有
- `LTXVCropGuides` —— 1/4 个有
- `LoraLoaderModelOnly` —— 1/4 个有
- `ModelAttentionBackend` —— 1/4 个有
- `PrimitiveFloat` —— 1/4 个有
- `TextGenerateLTX2Prompt` —— 1/4 个有

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
