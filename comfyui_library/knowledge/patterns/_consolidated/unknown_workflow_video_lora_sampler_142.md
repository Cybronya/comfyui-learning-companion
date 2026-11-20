---
name: unknown_workflow_video_lora_sampler_142
type: Unknown Workflow
frequency: 13
level: strong
coverage: 0.823923
common_nodes: [Any Switch (rgthree), BasicGuider, CLIPLoader, ComfyMathExpression, Fast Groups Bypasser (rgthree), H3SigmaRefiner, LoadAudio, LoraLoaderBypassModelOnly, LoraLoaderModelOnly, MiniMaxH3AudioConditioningT8, MiniMaxH3DualClockSamplerT8, MiniMaxH3MemoryEfficientSageAttentionPatch, ModelAttentionBackend, PreviewAny, PrimitiveFloat, RH_Screenwriter, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SolAttnMiniMax, SoundFlow_GetLength, SoundFlow_TrimAudio, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine, WujiCleaner, WujiH3PromptEnhancer, ZML_IntegerFloatConverter]
problems: []
missing: []
members: [数字人/数字人/MiniMax-H3视频对口型数字人（视频生视频）_2096864802261000194.json, 数字人/数字人/（MV创作专用）MiniMax-H3开源 音频驱动对口型数字人_2114681829616865282.json, 数字人/数字人/（MV创作专用）MiniMax-H3开源 音频驱动对口型数字人_2114683930212388866.json, 视频生成/图生视频/MiniMax-H3音频驱动对口型数字人，MV创作专用_2091543791437176834.json, 视频生成/图生视频/MiniMax-H3音频驱动数字人，MV创作专用_2095437567507386370.json, 视频生成/图生视频/老照片修复Flux2-Klein+MiniMax-H3_2092469294427893762.json, 视频生成/图生视频/老照片修复Flux2-Klein+MiniMax-H3_2097160477880180738.json, 视频生成/图生视频/老照片修复Flux2-Klein+MiniMax-H3_2097500745795985409.json, 视频生成/图生视频/（MV创作专用）MiniMax-H3开源 音频驱动对口型数字人_2094370315370586113.json, 视频生成/图生视频/（MV创作专用）MiniMax-H3开源 音频驱动对口型数字人_2094387651045580802.json, 视频生成/图生视频/（MV创作专用）MiniMax-H3开源 音频驱动对口型数字人_2098028999967592450.json, 视频生成/文生视频/MiniMax-H3文生图生多参首尾帧多合一分镜视频制作_2092570315934228482.json, 视频生成/文生视频/老照片修复+MiniMax-H3动态视频_2092779312918392833.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_142

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（数字人/数字人/MiniMax-H3视频对口型数字人（视频生视频）_2096864802261000194.json、数字人/数字人/（MV创作专用）MiniMax-H3开源 音频驱动对口型数字人_2114681829616865282.json、数字人/数字人/（MV创作专用）MiniMax-H3开源 音频驱动对口型数字人_2114683930212388866.json、视频生成/图生视频/MiniMax-H3音频驱动对口型数字人，MV创作专用_2091543791437176834.json、视频生成/图生视频/MiniMax-H3音频驱动数字人，MV创作专用_2095437567507386370.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 13 个 workflow 都包含：
- `Any Switch (rgthree)`
- `BasicGuider`
- `CLIPLoader`
- `ComfyMathExpression`
- `Fast Groups Bypasser (rgthree)`
- `H3SigmaRefiner`
- `LoadAudio`
- `LoraLoaderBypassModelOnly`
- `LoraLoaderModelOnly`
- `MiniMaxH3AudioConditioningT8`
- `MiniMaxH3DualClockSamplerT8`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `ModelAttentionBackend`
- `PreviewAny`
- `PrimitiveFloat`
- `RH_Screenwriter`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SolAttnMiniMax`
- `SoundFlow_GetLength`
- `SoundFlow_TrimAudio`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`
- `WujiCleaner`
- `WujiH3PromptEnhancer`
- `ZML_IntegerFloatConverter`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 12/13 个有
- `PrimitiveStringMultiline` —— 12/13 个有
- `RHHiddenNodes` —— 7/13 个有
- `WujiAudioLoader` —— 7/13 个有
- `easy showAnything` —— 7/13 个有
- `Int` —— 5/13 个有
- `CLIPTextEncode` —— 4/13 个有
- `CheckpointLoaderSimple` —— 4/13 个有
- `ConditioningZeroOut` —— 4/13 个有
- `EmptyLatentImage` —— 4/13 个有
- `Image Comparer (rgthree)` —— 4/13 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/13 个有
- `ReferenceLatent` —— 4/13 个有
- `SaveImage` —— 4/13 个有
- `VAEEncode` —— 4/13 个有
- `WujiSampler` —— 4/13 个有
- `WujiUpscaler` —— 4/13 个有
- `CR Text Concatenate` —— 1/13 个有
- `LoadVideo` —— 1/13 个有
- `VHS_LoadVideo` —— 1/13 个有
- `easy promptConcat` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | 512 - 512 | 4 | 100% |
| 高度 | 512 | 512 - 512 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 512，观测区间 512 - 512，4 个样本，取值集中（一致性 100%）
- 高度 中位数 512，观测区间 512 - 512，4 个样本，取值集中（一致性 100%）
