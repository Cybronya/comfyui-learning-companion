---
name: text_to_image_video_lora_sampler_209
type: Text To Image
frequency: 2
level: weak
coverage: 0.639
common_nodes: [CLIPLoader, CLIPTextEncode, CR Prompt Text, EmptyLatentImage, FL_RIFE, Fast Groups Bypasser (rgthree), GetNode, ImageResizeKJv2, JjkText, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM, LoadImage, LoraLoaderModelOnly, MathExpression|pysssss, ModelPassThrough, ModelPatchTorchSettings, ModelSamplingSD3, PainterI2V, PathchSageAttentionKJ, PlaySound|pysssss, PreviewAny, PreviewAudio, PreviewImage, SetNode, SomethingToString, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanMoeKSampler, WujiAudioLoader, easy cleanGpuUsed, easy getNode, easy int, easy setNode, easy showAnything, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters, llama_cpp_unload_model, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/Wan2.2自动反推Remix3.0图生视频处理工作流_2101727233776902146.json, 视频生成/图生视频/Wan2.2自动反推图生视频｜Remix3.0人物特效一键出片_2103065382646018049.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_209

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/Wan2.2自动反推Remix3.0图生视频处理工作流_2101727233776902146.json、视频生成/图生视频/Wan2.2自动反推图生视频｜Remix3.0人物特效一键出片_2103065382646018049.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：64%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `EmptyLatentImage`
- `FL_RIFE`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `ImageResizeKJv2`
- `JjkText`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MathExpression|pysssss`
- `ModelPassThrough`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `PainterI2V`
- `PathchSageAttentionKJ`
- `PlaySound|pysssss`
- `PreviewAny`
- `PreviewAudio`
- `PreviewImage`
- `SetNode`
- `SomethingToString`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanMoeKSampler`
- `WujiAudioLoader`
- `easy cleanGpuUsed`
- `easy getNode`
- `easy int`
- `easy setNode`
- `easy showAnything`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`
- `llama_cpp_unload_model`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `CR Text Concatenate` —— 1/2 个有
- `SaveImage` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 4.5 | - | 2 | 100% |
| 采样算法 | er_sde | - | 2 | 100% |
| 调度器 | beta | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |
| 宽度 | 80 | - | 2 | 100% |
| 高度 | 80 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，2 个样本，一致性 100%
- 调度器 最常用 beta，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 80，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
