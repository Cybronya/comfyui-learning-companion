---
name: unknown_workflow_video_upscale_latent_upscale_92
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.8115
common_nodes: [CFGGuider, CLIPTextEncode, DualCLIPLoader, EmptyImage, EmptyLTXVLatentVideo, GetImageSize, ImageScaleBy, KSampler, KSamplerSelect, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocess, LTXVScheduler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LayerUtility: PurgeVRAM V2, LoadImage, LoraLoaderModelOnly, PrimitiveInt, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoaderKJ, VHS_VideoCombine, easy positive]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/LTX2.3-新 VBVR LoRA + Distilled 1.1 稳定版(KJ)_2044347277359190017.json, 视频生成/图生视频/LTX2.3图生视频(KJ版)_2029845727714742273.json, 视频生成/图生视频/LTX2.3图生视频-KJ版_2031200896784273410.json, 视频生成/图生视频/高质量首尾帧视频LTX2.3-音频画面直出_2032282259331489794.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_92

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/LTX2.3-新 VBVR LoRA + Distilled 1.1 稳定版(KJ)_2044347277359190017.json、视频生成/图生视频/LTX2.3图生视频(KJ版)_2029845727714742273.json、视频生成/图生视频/LTX2.3图生视频-KJ版_2031200896784273410.json、视频生成/图生视频/高质量首尾帧视频LTX2.3-音频画面直出_2032282259331489794.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyImage`
- `EmptyLTXVLatentVideo`
- `GetImageSize`
- `ImageScaleBy`
- `KSampler`
- `KSamplerSelect`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVScheduler`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PrimitiveInt`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoaderKJ`
- `VHS_VideoCombine`
- `easy positive`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/4 个有
- `MathExpression|pysssss` —— 3/4 个有
- `Qwen3_VQA` —— 3/4 个有
- `RH_Translator` —— 3/4 个有
- `ShowText|pysssss` —— 3/4 个有
- `TextGenerateLTX2Prompt` —— 3/4 个有
- `TextListSplit` —— 3/4 个有
- `ManualSigmas` —— 2/4 个有
- `ResizeImagesByLongerEdge` —— 2/4 个有
- `VAEDecodeTiled` —— 2/4 个有
- `Any Switch (rgthree)` —— 1/4 个有
- `Any To String (mtb)` —— 1/4 个有
- `CR Text` —— 1/4 个有
- `Fast Groups Bypasser (rgthree)` —— 1/4 个有
- `GetNode` —— 1/4 个有
- `ImageAndMaskResizeNode` —— 1/4 个有
- `ImageConcanate` —— 1/4 个有
- `ImageConcatMulti` —— 1/4 个有
- `ImpactConditionalBranch` —— 1/4 个有
- `ImpactSwitch` —— 1/4 个有
- `IntToString` —— 1/4 个有
- `LTXVFirstLastFrameControl_TTP` —— 1/4 个有
- `LTXVImgToVideoInplaceKJ` —— 1/4 个有
- `PreviewAny` —— 1/4 个有
- `RH_LLMAPI_NODE` —— 1/4 个有
- `RunningHub Deepcleaner` —— 1/4 个有
- `SetNode` —— 1/4 个有
- `SimpleToggleNode` —— 1/4 个有
- `Text Find and Replace` —— 1/4 个有
- `ToFloat` —— 1/4 个有
- `easy anythingIndexSwitch` —— 1/4 个有
- `easy showAnything` —— 1/4 个有
- `llama_cpp_instruct_adv` —— 1/4 个有
- `llama_cpp_model_loader` —— 1/4 个有
- `ttN concat` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 0.35 | 0.3 - 0.35 | 4 | 94% |
| 宽度 | 97 | 97 - 97 | 4 | 100% |
| 高度 | 25 | 25 - 25 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 0.35，观测区间 0.3 - 0.35，4 个样本，取值集中（一致性 94%）
- 宽度 中位数 97，观测区间 97 - 97，4 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
