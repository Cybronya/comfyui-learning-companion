---
name: unknown_workflow_upscale_latent_upscale_sampler_6
type: Unknown Workflow
frequency: 12
level: strong
coverage: 0.894333
common_nodes: [CFGGuider, CLIPTextEncode, ComfyMathExpression, EmptyLTXVLatentVideo, KSamplerSelect, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, ManualSigmas, PrimitiveInt, RandomNoise, SamplerCustomAdvanced, VAEDecodeTiled, VAELoaderKJ]
problems: []
missing: []
members: [图片生成/图生图/LTX2.3首尾帧转场特效+Qwen3.5提示词优化_2064269147021864961.json, 图片生成/文生图/2030683389325479937.json, 图片生成/文生图/2031372826086739970.json, 图片生成/文生图/ltx2.3 文生视频图生视频_2031751863044939777.json, 数字人/数字人/ltx2.3 文生视频图生视频_2057281402378477569.json, 视频生成/图生视频/LTX2.3 首尾帧动态海报+Qwen3.5自动提示词_2039365637025304577.json, 视频生成/图生视频/LTX2.3 首尾帧视频特效+Qwen3.5自动提示词_2038953510800199682.json, 视频生成/图生视频/LTX2.3 首尾帧转场特效+Qwen3.5自动提示词_2039330537847922689.json, 视频生成/图生视频/LTX2.3-首尾帧超级转场+Qwen3.5自动提示词_2037880867695108098.json, 视频生成/图生视频/LTX2.3-首尾帧转场+Qwen3.5反推【测试版】_2038548270510776322.json, 视频生成/图生视频/ltx2.3 文生视频图生视频_2054757610527707137.json, 视频生成/文生视频/LTX2.3-GGUF-手动提示词版_2034561004020961282.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_sampler_6

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/LTX2.3首尾帧转场特效+Qwen3.5提示词优化_2064269147021864961.json、图片生成/文生图/2030683389325479937.json、图片生成/文生图/2031372826086739970.json、图片生成/文生图/ltx2.3 文生视频图生视频_2031751863044939777.json、数字人/数字人/ltx2.3 文生视频图生视频_2057281402378477569.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 12 个 workflow 都包含：
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
- `VAEDecodeTiled`
- `VAELoaderKJ`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 11/12 个有
- `SaveVideo` —— 11/12 个有
- `DualCLIPLoader` —— 10/12 个有
- `UNETLoader` —— 10/12 个有
- `ImageResizeKJv2` —— 9/12 个有
- `LoraLoaderModelOnly` —— 9/12 个有
- `ResizeImagesByLongerEdge` —— 9/12 个有
- `SimpleMath+` —— 9/12 个有
- `ShowText|pysssss` —— 8/12 个有
- `easy cleanGpuUsed` —— 8/12 个有
- `llama_cpp_instruct_adv` —— 8/12 个有
- `llama_cpp_model_loader` —— 8/12 个有
- `ImageConcanate` —— 6/12 个有
- `LTXVAddGuideMulti` —— 6/12 个有
- `PrimitiveBoolean` —— 6/12 个有
- `PrimitiveStringMultiline` —— 6/12 个有
- `Text` —— 6/12 个有
- `AspectRatio` —— 4/12 个有
- `BasicScheduler` —— 3/12 个有
- `Int` —— 3/12 个有
- `LTX2_NAG` —— 3/12 个有
- `ModelSamplingSD3` —— 3/12 个有
- `ResizeImageMaskNode` —— 3/12 个有
- `VisualizeSigmasKJ` —— 3/12 个有
- `easy showAnything` —— 3/12 个有
- `DualCLIPLoaderGGUF` —— 2/12 个有
- `UnetLoaderGGUF` —— 2/12 个有
- `Vignette` —— 2/12 个有
- `llama_cpp_parameters` —— 2/12 个有
- `SaveImage` —— 1/12 个有
- `SaveVideoRGBA` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 12 | 100% |
| 高度 | 25 | 25 - 25 | 12 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，12 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，12 个样本，取值集中（一致性 100%）
