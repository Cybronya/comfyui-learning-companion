---
name: unknown_workflow_video_lora_sampler_636
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.711667
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, ComfyMathExpression, ConditioningZeroOut, DiffusionModelLoaderKJ, ImageFromBatch, KSamplerAdvanced, LatentCutToBatch, LoadAudio, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, RebatchImages, SkipLayerGuidanceDiTSimple, TrimAudioDuration, VAEDecode, VAELoader, VHS_VideoCombine, WanDancerEncodeAudio, WanDancerPadKeyframesList, WanDancerVideo]
problems: []
missing: []
members: [视频生成/图生视频/Wan-Dancer 音乐生成舞蹈视频_2082813510517616641.json, 视频生成/图生视频/2078147776503959554.json, 视频生成/图生视频/2082031766499586050.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_636

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/Wan-Dancer 音乐生成舞蹈视频_2082813510517616641.json、视频生成/图生视频/2078147776503959554.json、视频生成/图生视频/2082031766499586050.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：71%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `ComfyMathExpression`
- `ConditioningZeroOut`
- `DiffusionModelLoaderKJ`
- `ImageFromBatch`
- `KSamplerAdvanced`
- `LatentCutToBatch`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `RebatchImages`
- `SkipLayerGuidanceDiTSimple`
- `TrimAudioDuration`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanDancerEncodeAudio`
- `WanDancerPadKeyframesList`
- `WanDancerVideo`

**可变部分**（部分 workflow 才有）：
- `CM_IntToFloat` —— 2/3 个有
- `GetNode` —— 2/3 个有
- `Int` —— 2/3 个有
- `ResizeImageMaskNode` —— 2/3 个有
- `SetNode` —— 2/3 个有
- `StringConcatenate` —— 2/3 个有
- `ComfyNumberConvert` —— 1/3 个有
- `ExtractSpecificLines` —— 1/3 个有
- `INTConstant` —— 1/3 个有
- `ImageResizeKJv2` —— 1/3 个有
- `JjkText` —— 1/3 个有
- `KepStringLiteral` —— 1/3 个有
- `Label (rgthree)` —— 1/3 个有
- `PreviewAny` —— 1/3 个有
- `ProcessString` —— 1/3 个有
- `easy seed` —— 1/3 个有
- `easy showAnything` —— 1/3 个有
- `llama_cpp_instruct_adv` —— 1/3 个有
- `llama_cpp_model_loader` —— 1/3 个有
- `llama_cpp_parameters` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 3 | 67% |
| Prompt 约束强度(CFG) | 6 | 6 - 6 | 3 | 100% |
| 采样算法 | 1 | 1 - 1 | 3 | 100% |
| 调度器 | euler | - | 3 | 100% |
| 重绘幅度 | simple | - | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，3 个样本，一致性 67%
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 6，3 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，3 个样本，一致性 100%
- 重绘幅度 最常用 simple，3 个样本，一致性 100%
