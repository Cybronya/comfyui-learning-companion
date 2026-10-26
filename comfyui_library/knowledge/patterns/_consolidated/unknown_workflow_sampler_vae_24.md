---
name: unknown_workflow_sampler_vae_24
type: Unknown Workflow
frequency: 13
level: weak
coverage: 0.888538
common_nodes: [CFGGuider, ComfyMathExpression, CreateVideo, EmptyLTXVLatentVideo, ImageResizeKJv2, KSamplerSelect, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVSeparateAVLatent, LoadImage, PrimitiveInt, RandomNoise, ResizeImagesByLongerEdge, SamplerCustomAdvanced, SaveVideo, VAEDecodeTiled]
problems: []
missing: []
members: [图片生成/文生图/LTX2.3 多图控制 提示词分段中继流_2073319635222618113.json, 视频生成/图生视频/LTX2.3 prompt relay 提示词分段控制流_2052341800647569410.json, 视频生成/图生视频/LTX2.3 首中尾3帧转场特效+手动提示词_2039999501695459329.json, 视频生成/图生视频/LTX2.3 首尾帧转场特效+手动提示词_2039363002973032450.json, 视频生成/图生视频/LTX2.3-图生视频三采样+自动提示词_2040690570988883969.json, 视频生成/图生视频/LTX2.3-图生视频（KJ版） 图生视频 音画同步 万能图生视频 优化加速版_2031244973215064065.json, 视频生成/图生视频/LTX2.3-图生视频（KJ版）_2031018191203340289.json, 视频生成/图生视频/LTX2.3-多图视频生成（首尾帧）_2040716663120732161.json, 视频生成/图生视频/LTX2.3-首中尾帧视频+Qwen3.5自动提示词_2037900927323082754.json, 视频生成/图生视频/LTX2.3-首尾帧超级转场（transition）_2037157386359672834.json, 视频生成/图生视频/LTX2.3-首尾帧超级转场（transition）_2037707002851364865.json, 视频生成/图生视频/LTX2.3最强首尾帧声画同步_2037742707522670593.json, 视频生成/图生视频/万象AI+LTX2.3 首中尾3帧转场特效+去字幕lora+自动提示词优化版_2040976928861069314.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_vae_24

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/文生图/LTX2.3 多图控制 提示词分段中继流_2073319635222618113.json、视频生成/图生视频/LTX2.3 prompt relay 提示词分段控制流_2052341800647569410.json、视频生成/图生视频/LTX2.3 首中尾3帧转场特效+手动提示词_2039999501695459329.json、视频生成/图生视频/LTX2.3 首尾帧转场特效+手动提示词_2039363002973032450.json、视频生成/图生视频/LTX2.3-图生视频三采样+自动提示词_2040690570988883969.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：89%

## 共有节点

全部 13 个 workflow 都包含：
- `CFGGuider`
- `ComfyMathExpression`
- `CreateVideo`
- `EmptyLTXVLatentVideo`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `PrimitiveInt`
- `RandomNoise`
- `ResizeImagesByLongerEdge`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `VAEDecodeTiled`

**可变部分**（部分 workflow 才有）：
- `DualCLIPLoader` —— 12/13 个有
- `LTXVImgToVideoInplace` —— 12/13 个有
- `UNETLoader` —— 12/13 个有
- `VAELoaderKJ` —— 12/13 个有
- `CLIPTextEncode` —— 11/13 个有
- `LTXVLatentUpsampler` —— 11/13 个有
- `LTXVPreprocess` —— 11/13 个有
- `LatentUpscaleModelLoader` —— 11/13 个有
- `ManualSigmas` —— 11/13 个有
- `SimpleMath+` —— 11/13 个有
- `LoraLoaderModelOnly` —— 10/13 个有
- `LTXVAddGuideMulti` —— 8/13 个有
- `ShowText|pysssss` —— 8/13 个有
- `Text` —— 6/13 个有
- `easy cleanGpuUsed` —— 5/13 个有
- `llama_cpp_instruct_adv` —— 5/13 个有
- `llama_cpp_model_loader` —— 5/13 个有
- `RH_LLMAPI_Pro_Node` —— 4/13 个有
- `AspectRatio` —— 3/13 个有
- `BasicScheduler` —— 2/13 个有
- `ConditioningZeroOut` —— 2/13 个有
- `Fast Groups Bypasser (rgthree)` —— 2/13 个有
- `ImageConcatMulti` —— 2/13 个有
- `ImageSizeInfo` —— 2/13 个有
- `PrimitiveFloat` —— 2/13 个有
- `PrimitiveStringMultiline` —— 2/13 个有
- `PromptRelayEncodeTimeline` —— 2/13 个有
- `easy showAnything` —— 2/13 个有
- `llama_cpp_unload_model` —— 2/13 个有
- `CR Prompt Text` —— 1/13 个有
- `CheckpointLoaderSimple` —— 1/13 个有
- `Int` —— 1/13 个有
- `LTXAVTextEncoderLoader` —— 1/13 个有
- `LTXVAudioVAELoader` —— 1/13 个有
- `LTXVImgToVideoInplaceKJ` —— 1/13 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 601 | 13 | 6% |
| 高度 | 25 | 25 - 25 | 13 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 601，13 个样本，取值分散，一致性仅 6%
- 高度 中位数 25，观测区间 25 - 25，13 个样本，取值集中（一致性 100%）
