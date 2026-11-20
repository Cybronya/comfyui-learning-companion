---
name: unknown_workflow_upscale_latent_upscale_lora_30
type: Unknown Workflow
frequency: 10
level: strong
coverage: 0.8763
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, ComfyMathExpression, CreateVideo, EmptyLTXVLatentVideo, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVLatentUpsampler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoraLoaderModelOnly, ManualSigmas, RandomNoise, SamplerCustomAdvanced, SaveVideo, VAEDecodeTiled, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters]
problems: []
missing: []
members: [图片生成/图生图/酱板鸭视频生成器 一键生成多国语言酱板鸭视频 支持OpenClaw_2049510722668859394.json, 图片生成/文生图/LTX2.3-transition-lora-丝滑转场-i2v视频-自动提示词_2040078621276114946.json, 视频生成/图生视频/3.0最新图生视频 （懒人版）你提想法帮你实现_2066087069847482370.json, 视频生成/图生视频/LTX-2.3-图生视频-音画同步-输入主题-全自动提示词_2039704492752510977.json, 视频生成/图生视频/LTX-2.3-图生视频-音画同步-输入主题-全自动提示词_2039914050452201474.json, 视频生成/图生视频/LTX2.3-transition-lora-丝滑转场-i2v-多图-自动提示词_2040291923272933378.json, 视频生成/图生视频/ltx2.3 图生视频_2042446425367257089.json, 视频生成/图生视频/酱板鸭视频生成器 一键生成多国语言酱板鸭视频 支持OpenClaw_2049507628333670402.json, 视频生成/图生视频/酱板鸭视频生成器（LTX-2.3版）：一键生成多国语言对话的酱板鸭视频，支持OpenClaw调用！_2037239092089458690.json, 视频生成/文生视频/LTX2.3-transition-lora-丝滑转场-t2v视频-自动提示词_2040215269943021570.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_30

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/酱板鸭视频生成器 一键生成多国语言酱板鸭视频 支持OpenClaw_2049510722668859394.json、图片生成/文生图/LTX2.3-transition-lora-丝滑转场-i2v视频-自动提示词_2040078621276114946.json、视频生成/图生视频/3.0最新图生视频 （懒人版）你提想法帮你实现_2066087069847482370.json、视频生成/图生视频/LTX-2.3-图生视频-音画同步-输入主题-全自动提示词_2039704492752510977.json、视频生成/图生视频/LTX-2.3-图生视频-音画同步-输入主题-全自动提示词_2039914050452201474.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 10 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ComfyMathExpression`
- `CreateVideo`
- `EmptyLTXVLatentVideo`
- `KSamplerSelect`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVLatentUpsampler`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `VAEDecodeTiled`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`

**可变部分**（部分 workflow 才有）：
- `LTXVImgToVideoInplace` —— 9/10 个有
- `LTXVPreprocess` —— 9/10 个有
- `LoadImage` —— 9/10 个有
- `ResizeImagesByLongerEdge` —— 9/10 个有
- `PrimitiveBoolean` —— 8/10 个有
- `PrimitiveStringMultiline` —— 8/10 个有
- `ImageResizeKJv2` —— 7/10 个有
- `PreviewAny` —— 7/10 个有
- `PrimitiveInt` —— 7/10 个有
- `CustomAddLabel` —— 5/10 个有
- `Int` —— 5/10 个有
- `RH_Utils` —— 5/10 个有
- `TTResolutionSelector` —— 5/10 个有
- `SimpleMath+` —— 4/10 个有
- `JWFloat` —— 3/10 个有
- `LTX2_NAG` —— 3/10 个有
- `Label (rgthree)` —— 3/10 个有
- `ResizeImageMaskNode` —— 3/10 个有
- `StringReplace` —— 3/10 个有
- `string_util_StrConcat` —— 3/10 个有
- `ttN concat` —— 3/10 个有
- `CR Text` —— 2/10 个有
- `CR Text Concatenate` —— 2/10 个有
- `Evaluate Integers` —— 2/10 个有
- `JjkText` —— 2/10 个有
- `MultiTextConcatenate` —— 2/10 个有
- `SDVN Any Show` —— 2/10 个有
- `easy showAnything` —— 2/10 个有
- `ImageStitch` —— 1/10 个有
- `LTXVImgToVideoInplaceKJ` —— 1/10 个有
- `MathExpression|pysssss` —— 1/10 个有
- `ShowAnything|Mie` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 10 | 100% |
| 高度 | 25 | 25 - 25 | 10 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，10 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，10 个样本，取值集中（一致性 100%）
