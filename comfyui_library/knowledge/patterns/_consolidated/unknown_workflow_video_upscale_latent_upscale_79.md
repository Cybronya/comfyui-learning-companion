---
name: unknown_workflow_video_upscale_latent_upscale_79
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.7808
common_nodes: [CFGGuider, CLIPTextEncode, ComfyMathExpression, DualCLIPLoader, EmptyLTXVLatentVideo, ImageResizeKJv2, Int, KSamplerSelect, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, ManualSigmas, RandomNoise, ResizeImagesByLongerEdge, SamplerCustomAdvanced, SimpleMath+, UNETLoader, VAEDecodeTiled, VAELoaderKJ, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/LTX2.3-i2v-kijai-三段式采样-细节更丰富-自动提示词_2040449259794866177.json, 视频生成/图生视频/LTX2.3-i2v-kijai-三段式采样-细节更丰富_2041694294079184898.json, 视频生成/图生视频/LTX2.3-transition-lora-丝滑转场-首尾帧视频-自动提示词_2037153504921391105.json, 视频生成/图生视频/LTX2.3-数字人-电商带货-首中尾帧转场特效-去字幕lora-自动提示词优化版_2051128498395336706.json, 视频生成/图生视频/Qwen3.5+LTX2.3-transition-lora-丝滑转场-首尾帧视频-自动提示词_2063264536383287297.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_79

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/LTX2.3-i2v-kijai-三段式采样-细节更丰富-自动提示词_2040449259794866177.json、视频生成/图生视频/LTX2.3-i2v-kijai-三段式采样-细节更丰富_2041694294079184898.json、视频生成/图生视频/LTX2.3-transition-lora-丝滑转场-首尾帧视频-自动提示词_2037153504921391105.json、视频生成/图生视频/LTX2.3-数字人-电商带货-首中尾帧转场特效-去字幕lora-自动提示词优化版_2051128498395336706.json、视频生成/图生视频/Qwen3.5+LTX2.3-transition-lora-丝滑转场-首尾帧视频-自动提示词_2063264536383287297.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：78%

## 共有节点

全部 5 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `ImageResizeKJv2`
- `Int`
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
- `LoadImage`
- `ManualSigmas`
- `RandomNoise`
- `ResizeImagesByLongerEdge`
- `SamplerCustomAdvanced`
- `SimpleMath+`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoaderKJ`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `CustomAddLabel` —— 4/5 个有
- `PrimitiveStringMultiline` —— 4/5 个有
- `easy showAnything` —— 4/5 个有
- `CreateVideo` —— 3/5 个有
- `LTXVAddGuideMulti` —— 3/5 个有
- `LoraLoaderModelOnly` —— 3/5 个有
- `RH_LLMAPI_Pro_Node` —— 3/5 个有
- `TTResolutionSelector` —— 3/5 个有
- `GetNode` —— 2/5 个有
- `JWFloat` —— 2/5 个有
- `JjkText` —— 2/5 个有
- `LoraLoader` —— 2/5 个有
- `PreviewImage` —— 2/5 个有
- `PrimitiveBoolean` —— 2/5 个有
- `ResizeImageMaskNode` —— 2/5 个有
- `SetNode` —— 2/5 个有
- `llama_cpp_instruct_adv` —— 2/5 个有
- `llama_cpp_model_loader` —— 2/5 个有
- `llama_cpp_parameters` —— 2/5 个有
- `Dapao_LlamaCaption` —— 1/5 个有
- `Dapao_LlamaCaptionOptions` —— 1/5 个有
- `GetVideoComponents` —— 1/5 个有
- `MultiTextConcatenate` —— 1/5 个有
- `RH_Utils` —— 1/5 个有
- `RegexReplace` —— 1/5 个有
- `ShowText` —— 1/5 个有
- `Text` —— 1/5 个有
- `ttN concat` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 5 | 100% |
| 高度 | 25 | 25 - 25 | 5 | 100% |
| LoRA 模型强度 | 1 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，5 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，5 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
