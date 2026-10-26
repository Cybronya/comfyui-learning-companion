---
name: unknown_workflow_video_lora_sampler_915
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.7345
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CR Text Replace, EasyCache, EmptyFlux2LatentImage, Fast Groups Bypasser (rgthree), Flux2Scheduler, GetImageSize+, GetImageSizeAndCount, GetNode, ImageFromBatch, ImageFromBatch+, JWInteger, KSamplerAdvanced, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, LoadAudio, LoadImage, LoraLoader, MathExpression|pysssss, ModelPatchTorchSettings, ModelSamplingSD3, PathchSageAttentionKJ, PreviewImage, PrimitiveStringMultiline, ProcessString, Qwen3_VQA, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SeedVR2, SeedVR2BlockSwap, SeedVR2ExtraArgs, SetNode, Text Multiline, UNETLoader, VAEDecode, VAEEncode, VAELoader, VHS_VideoCombine, WanImageToVideo, easy batchAnything, easy cleanGpuUsed, easy imageBatchToImageList, easy imageListToImageBatch, easy promptLine, easy showAnything, wanBlockSwap]
problems: []
missing: []
members: [视频生成/图生视频/ai美女写真视频一键生成_2015727780918464513.json, 视频生成/图生视频/自动分镜视频生成工作流_2036803512243326978.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_915

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/ai美女写真视频一键生成_2015727780918464513.json、视频生成/图生视频/自动分镜视频生成工作流_2036803512243326978.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：73%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CR Text Replace`
- `EasyCache`
- `EmptyFlux2LatentImage`
- `Fast Groups Bypasser (rgthree)`
- `Flux2Scheduler`
- `GetImageSize+`
- `GetImageSizeAndCount`
- `GetNode`
- `ImageFromBatch`
- `ImageFromBatch+`
- `JWInteger`
- `KSamplerAdvanced`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM V2`
- `LoadAudio`
- `LoadImage`
- `LoraLoader`
- `MathExpression|pysssss`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `PreviewImage`
- `PrimitiveStringMultiline`
- `ProcessString`
- `Qwen3_VQA`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SeedVR2`
- `SeedVR2BlockSwap`
- `SeedVR2ExtraArgs`
- `SetNode`
- `Text Multiline`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanImageToVideo`
- `easy batchAnything`
- `easy cleanGpuUsed`
- `easy imageBatchToImageList`
- `easy imageListToImageBatch`
- `easy promptLine`
- `easy showAnything`
- `wanBlockSwap`

**可变部分**（部分 workflow 才有）：
- `Any Switch (rgthree)` —— 1/2 个有
- `CR Integer To String` —— 1/2 个有
- `CR Text` —— 1/2 个有
- `Mute / Bypass Relay (rgthree)` —— 1/2 个有
- `Mute / Bypass Repeater (rgthree)` —— 1/2 个有
- `QwenVisionNode` —— 1/2 个有
- `Reroute (rgthree)` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 2 | 100% |
| Prompt 约束强度(CFG) | 8 | - | 2 | 100% |
| 采样算法 | 1 | - | 2 | 100% |
| 调度器 | euler_ancestral | - | 2 | 100% |
| 重绘幅度 | simple | - | 2 | 100% |
| LoRA 模型强度 | 0.9 | - | 2 | 100% |
| LoRA 文本强度 | 0.9 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，2 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler_ancestral，2 个样本，一致性 100%
- 重绘幅度 最常用 simple，2 个样本，一致性 100%
- LoRA 模型强度 中位数 0.9，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 0.9，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
