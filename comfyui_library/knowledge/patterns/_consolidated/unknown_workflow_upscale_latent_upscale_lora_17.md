---
name: unknown_workflow_upscale_latent_upscale_lora_17
type: Unknown Workflow
frequency: 14
level: strong
coverage: 0.832286
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, ComfyMathExpression, CreateVideo, EmptyLTXVLatentVideo, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVLatentUpsampler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoraLoaderModelOnly, ManualSigmas, PrimitiveBoolean, PrimitiveInt, PrimitiveStringMultiline, RandomNoise, SamplerCustomAdvanced, SaveVideo, VAEDecodeTiled]
problems: []
missing: []
members: [视频生成/文生视频/LTX2.3  文生视频 优化版_2030871574055755778.json, 视频生成/文生视频/LTX2.3 t2v 2.5D 奶油风格文生视频_2055255391927324673.json, 视频生成/文生视频/LTX2.3 t2v 丝滑过度转场+变身效果_2037115919574507522.json, 视频生成/文生视频/LTX2.3 t2v 优化版 提升画面质量 减少卡顿 减少崩坏_2042604394591559682.json, 视频生成/文生视频/LTX2.3 t2v 优化版 提升画面质量 减少卡顿 减少崩坏_2048010064992145409.json, 视频生成/文生视频/LTX2.3 t2v 优化版_2030584532939841538.json, 视频生成/文生视频/LTX2.3 图生视频ComfyUI工作流【非导演工作台】_2066741149947219969.json, 视频生成/文生视频/LTX2.3 文生_图生视频 官方版_2030578306432634882.json, 视频生成/文生视频/LTX2.3-文生视频，智能提示词优化_2031263174128836610.json, 视频生成/文生视频/LTX2.3图生&文生视频_2031683201361518593.json, 视频生成/文生视频/LTX2.3文生_图生视频 AI真人短剧工作流_2053318411618398209.json, 视频生成/文生视频/LTX2.3文生_图生视频 AI真人短剧工作流_2054136644139266049.json, 视频生成/文生视频/LTX2.3文生_图生视频_2055972165740179457.json, 视频生成/文生视频/【LTX2.3官方工作流优化】文生视频+图生视频_含提示词扩写模板_2033142799469649922.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_17

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（视频生成/文生视频/LTX2.3  文生视频 优化版_2030871574055755778.json、视频生成/文生视频/LTX2.3 t2v 2.5D 奶油风格文生视频_2055255391927324673.json、视频生成/文生视频/LTX2.3 t2v 丝滑过度转场+变身效果_2037115919574507522.json、视频生成/文生视频/LTX2.3 t2v 优化版 提升画面质量 减少卡顿 减少崩坏_2042604394591559682.json、视频生成/文生视频/LTX2.3 t2v 优化版 提升画面质量 减少卡顿 减少崩坏_2048010064992145409.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 14 个 workflow 都包含：
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
- `PrimitiveBoolean`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `VAEDecodeTiled`

**可变部分**（部分 workflow 才有）：
- `LTXVImgToVideoInplace` —— 8/14 个有
- `LTXVPreprocess` —— 8/14 个有
- `LoadImage` —— 8/14 个有
- `ResizeImageMaskNode` —— 8/14 个有
- `ResizeImagesByLongerEdge` —— 8/14 个有
- `Fast Groups Bypasser (rgthree)` —— 6/14 个有
- `LTX2_NAG` —— 6/14 个有
- `easy showAnything` —— 6/14 个有
- `RH_LLMAPI_Pro_Node` —— 5/14 个有
- `llama_cpp_instruct_adv` —— 5/14 个有
- `llama_cpp_model_loader` —— 5/14 个有
- `llama_cpp_parameters` —— 5/14 个有
- `DeepTranslatorTextNode` —— 3/14 个有
- `GetNode` —— 2/14 个有
- `SetNode` —— 2/14 个有
- `LayerUtility: PurgeVRAM V2` —— 1/14 个有
- `PlaySound|pysssss` —— 1/14 个有
- `Qwen3_VQA` —— 1/14 个有
- `TTResolutionSelector` —— 1/14 个有
- `Text` —— 1/14 个有
- `TextConcatenator` —— 1/14 个有
- `easy ifElse` —— 1/14 个有
- `ttN text` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 14 | 100% |
| 高度 | 25 | 25 - 25 | 14 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，14 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，14 个样本，取值集中（一致性 100%）
