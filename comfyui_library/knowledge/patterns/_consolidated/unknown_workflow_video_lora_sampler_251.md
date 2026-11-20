---
name: unknown_workflow_video_lora_sampler_251
type: Unknown Workflow
frequency: 10
level: strong
coverage: 0.485
common_nodes: [CLIPLoader, CLIPTextEncode, CR Prompt Text, CR Text Concatenate, FL_RIFE, Fast Groups Bypasser (rgthree), GetNode, ImageResizeKJv2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM, LoadImage, LoraLoaderModelOnly, MathExpression|pysssss, ModelPassThrough, ModelPatchTorchSettings, ModelSamplingSD3, PainterI2V, PathchSageAttentionKJ, PlaySound|pysssss, PreviewAny, PreviewAudio, PreviewImage, SetNode, SomethingToString, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanMoeKSampler, WujiAudioLoader, easy cleanGpuUsed, easy getNode, easy int, easy setNode, easy showAnything, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters, llama_cpp_unload_model]
problems: []
missing: []
members: [图片生成/反推提示词/Wan2.2 自动反推 Remix3.0 图生视频_2115773159633940481.json, 图片生成/反推提示词/Wan2.2 自动反推 Remix3.0 图生视频_2115789545584287745.json, 平台全量/Wan2.2 图片自动反推 Remix3.0 图生视频_2119030328743522305.json, 平台全量/Wan2.2 图片自动反推 Remix3.0 图生视频_2119034762986876930.json, 视频生成/图生视频/Wan2.2 自动反推 Remix3.0 图生视频_2102709527157231617.json, 视频生成/图生视频/Wan2.2 自动反推 Remix3.0 图生视频_2102729176808775681.json, 视频生成/图生视频/Wan2.2_自动反推_Remix3.0_图生视频_2115984231787745282.json, 视频生成/图生视频/Wan2.2_自动反推_Remix3.0_图生视频_2115997166782205954.json, 视频生成/图生视频/❽「Wan2.2」自动反推 Remix3.0 图生视频_2103038735767138305.json, 视频生成/图生视频/❽「Wan2.2」自动反推 Remix3.0 图生视频「9.19」_2050600975479648258.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_251

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/反推提示词/Wan2.2 自动反推 Remix3.0 图生视频_2115773159633940481.json、图片生成/反推提示词/Wan2.2 自动反推 Remix3.0 图生视频_2115789545584287745.json、平台全量/Wan2.2 图片自动反推 Remix3.0 图生视频_2119030328743522305.json、平台全量/Wan2.2 图片自动反推 Remix3.0 图生视频_2119034762986876930.json、视频生成/图生视频/Wan2.2 自动反推 Remix3.0 图生视频_2102709527157231617.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：48%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `CR Text Concatenate`
- `FL_RIFE`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `ImageResizeKJv2`
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

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 10 | 100% |
| Prompt 约束强度(CFG) | 4 | 4 - 4 | 10 | 100% |
| 采样算法 | 1 | 1 - 1 | 10 | 100% |
| 调度器 | 1 | 1 - 1 | 10 | 100% |
| 重绘幅度 | res_multistep | - | 10 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，10 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 4，10 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 调度器 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 重绘幅度 最常用 res_multistep，10 个样本，一致性 100%
