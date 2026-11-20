---
name: unknown_workflow_video_sampler_clip_199
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.917333
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CR Text, CR Text Concatenate, CR Text Replace, ImageResizeKJv2, Int, IntToString, KSamplerAdvanced, LoadImage, MathExpression|pysssss, PreviewAny, RHHiddenNodes, RIFE VFI, Text, VAEDecode, VAELoader, VHS_VideoCombine, easy int]
problems: []
missing: []
members: [视频生成/图生视频/Wan2.2动漫模型DaSiWa9-图生视频_2008712516989358081.json, 视频生成/图生视频/Wan2.2动漫模型DaSiWaV9-首尾帧生视频_2034471810380603394.json, 视频生成/图生视频/wan2.2动漫模型DasiwaV10-图生视频_2041336224299884545.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_199

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/Wan2.2动漫模型DaSiWa9-图生视频_2008712516989358081.json、视频生成/图生视频/Wan2.2动漫模型DaSiWaV9-首尾帧生视频_2034471810380603394.json、视频生成/图生视频/wan2.2动漫模型DasiwaV10-图生视频_2041336224299884545.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CR Text`
- `CR Text Concatenate`
- `CR Text Replace`
- `ImageResizeKJv2`
- `Int`
- `IntToString`
- `KSamplerAdvanced`
- `LoadImage`
- `MathExpression|pysssss`
- `PreviewAny`
- `RHHiddenNodes`
- `RIFE VFI`
- `Text`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `Qwen3_VQA_Plus` —— 2/3 个有
- `LayerUtility: ImageMaskScaleAs` —— 1/3 个有
- `PainterI2V` —— 1/3 个有
- `PainterI2V-up WAN2.2 LatentMotion Enhancer by paicat1` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `WanFirstLastFrameToVideo` —— 1/3 个有
- `easy imageConcat` —— 1/3 个有
- `llama_cpp_instruct_adv` —— 1/3 个有
- `llama_cpp_model_loader` —— 1/3 个有
- `llama_cpp_parameters` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 3 | 100% |
| Prompt 约束强度(CFG) | 6 | 6 - 8 | 3 | 86% |
| 采样算法 | 1 | 1 - 1 | 3 | 100% |
| 调度器 | euler | - | 3 | 67% |
| 重绘幅度 | simple | - | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，3 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 8，3 个样本，取值集中（一致性 86%）
- 采样算法 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，3 个样本，一致性 67%
- 重绘幅度 最常用 simple，3 个样本，一致性 100%
