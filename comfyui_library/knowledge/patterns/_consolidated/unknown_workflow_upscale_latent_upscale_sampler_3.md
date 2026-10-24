---
name: unknown_workflow_upscale_latent_upscale_sampler_3
type: Unknown Workflow
frequency: 15
level: strong
coverage: 0.903333
common_nodes: [CFGGuider, CLIPTextEncode, ComfyMathExpression, CreateVideo, EmptyLTXVLatentVideo, KSamplerSelect, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, ManualSigmas, PrimitiveInt, RandomNoise, SamplerCustomAdvanced, SaveVideo, VAEDecodeTiled, VAELoaderKJ]
problems: []
missing: []
members: [图片生成/图生图/LTX2.3首尾帧转场特效+Qwen3.5提示词优化_2064269147021864961.json, 图片生成/文生图/2030683389325479937.json, 图片生成/文生图/2031372826086739970.json, 图片生成/文生图/ltx2.3 文生视频图生视频_2031751863044939777.json, 视频生成/图生视频/LTX2.3 首中尾3帧转场特效+手动提示词_2039999501695459329.json, 视频生成/图生视频/LTX2.3 首尾帧动态海报+Qwen3.5自动提示词_2039365637025304577.json, 视频生成/图生视频/LTX2.3 首尾帧视频特效+Qwen3.5自动提示词_2038953510800199682.json, 视频生成/图生视频/LTX2.3 首尾帧转场特效+Qwen3.5自动提示词_2039330537847922689.json, 视频生成/图生视频/LTX2.3 首尾帧转场特效+手动提示词_2039363002973032450.json, 视频生成/图生视频/LTX2.3-图生视频三采样+自动提示词_2040690570988883969.json, 视频生成/图生视频/LTX2.3-图生视频（KJ版） 图生视频 音画同步 万能图生视频 优化加速版_2031244973215064065.json, 视频生成/图生视频/LTX2.3-图生视频（KJ版）_2031018191203340289.json, 视频生成/图生视频/LTX2.3-多图视频生成（首尾帧）_2040716663120732161.json, 视频生成/图生视频/LTX2.3-首尾帧超级转场+Qwen3.5自动提示词_2037880867695108098.json, 视频生成/图生视频/ltx2.3 文生视频图生视频_2054757610527707137.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_sampler_3

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（图片生成/图生图/LTX2.3首尾帧转场特效+Qwen3.5提示词优化_2064269147021864961.json、图片生成/文生图/2030683389325479937.json、图片生成/文生图/2031372826086739970.json、图片生成/文生图/ltx2.3 文生视频图生视频_2031751863044939777.json、视频生成/图生视频/LTX2.3 首中尾3帧转场特效+手动提示词_2039999501695459329.json…）

- **类型**：Unknown Workflow
- **样本数**：15
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 15 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `CreateVideo`
- `EmptyLTXVLatentVideo`
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
- `PrimitiveInt`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `VAEDecodeTiled`
- `VAELoaderKJ`

**可变部分**（部分 workflow 才有）：
- `DualCLIPLoader` —— 14/15 个有
- `UNETLoader` —— 14/15 个有
- `ImageResizeKJv2` —— 13/15 个有
- `ResizeImagesByLongerEdge` —— 13/15 个有
- `SimpleMath+` —— 13/15 个有
- `LoraLoaderModelOnly` —— 11/15 个有
- `ShowText|pysssss` —— 10/15 个有
- `easy cleanGpuUsed` —— 10/15 个有
- `llama_cpp_instruct_adv` —— 10/15 个有
- `llama_cpp_model_loader` —— 10/15 个有
- `LTXVAddGuideMulti` —— 8/15 个有
- `Text` —— 7/15 个有
- `AspectRatio` —— 6/15 个有
- `PrimitiveStringMultiline` —— 6/15 个有
- `ImageConcanate` —— 5/15 个有
- `PrimitiveBoolean` —— 4/15 个有
- `BasicScheduler` —— 2/15 个有
- `Int` —— 2/15 个有
- `LTX2_NAG` —— 2/15 个有
- `ModelSamplingSD3` —— 2/15 个有
- `ResizeImageMaskNode` —— 2/15 个有
- `VisualizeSigmasKJ` —— 2/15 个有
- `easy showAnything` —— 2/15 个有
- `llama_cpp_unload_model` —— 2/15 个有
- `DualCLIPLoaderGGUF` —— 1/15 个有
- `Fast Groups Bypasser (rgthree)` —— 1/15 个有
- `ImageConcatMulti` —— 1/15 个有
- `UnetLoaderGGUF` —— 1/15 个有
- `Vignette` —— 1/15 个有
- `llama_cpp_parameters` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 15 | 100% |
| 高度 | 25 | 25 - 25 | 15 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，15 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，15 个样本，取值集中（一致性 100%）
