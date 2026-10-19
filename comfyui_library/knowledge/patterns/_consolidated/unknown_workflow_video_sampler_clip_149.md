---
name: unknown_workflow_video_sampler_clip_149
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.9105
common_nodes: [CLIPLoader, CLIPTextEncode, INTConstant, ImageResizeKJv2, ImageStitch, KSamplerAdvanced, LoadImage, ModelSamplingSD3, PreviewImage, PrimitiveStringMultiline, Seed (rgthree), UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, easy showAnything, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters]
problems: []
missing: []
members: [视频生成/图生视频/2034945354898083841.json, 视频生成/图生视频/2036038473215381506.json, 视频生成/图生视频/2034940280880762881.json, 视频生成/图生视频/2057420747668283393.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_149

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/2034945354898083841.json、视频生成/图生视频/2036038473215381506.json、视频生成/图生视频/2034940280880762881.json、视频生成/图生视频/2057420747668283393.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `INTConstant`
- `ImageResizeKJv2`
- `ImageStitch`
- `KSamplerAdvanced`
- `LoadImage`
- `ModelSamplingSD3`
- `PreviewImage`
- `PrimitiveStringMultiline`
- `Seed (rgthree)`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `easy showAnything`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`

**可变部分**（部分 workflow 才有）：
- `CLIPVisionEncode` —— 2/4 个有
- `CLIPVisionLoader` —— 2/4 个有
- `LatentFromBatch` —— 2/4 个有
- `WanFirstMiddleLastFrameToVideo` —— 2/4 个有
- `WanFunInpaintToVideo` —— 2/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 4 | 100% |
| Prompt 约束强度(CFG) | 12 | 12 - 12 | 4 | 100% |
| 采样算法 | 1 | 1 - 1 | 4 | 100% |
| 调度器 | euler | - | 4 | 100% |
| 重绘幅度 | simple | - | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，4 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 12，观测区间 12 - 12，4 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，4 个样本，一致性 100%
- 重绘幅度 最常用 simple，4 个样本，一致性 100%
