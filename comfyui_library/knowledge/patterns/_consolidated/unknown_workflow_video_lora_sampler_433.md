---
name: unknown_workflow_video_lora_sampler_433
type: Unknown Workflow
frequency: 5
level: weak
coverage: 0.9272
common_nodes: [CLIPLoader, CLIPTextEncode, KSamplerAdvanced, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/2036317087181840385.json, 视频生成/图生视频/1955921227057647617.json, 视频生成/图生视频/2067249517136797697.json, 视频生成/图生视频/1957002075188989954.json, 视频生成/图生视频/2032294659132755970.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_433

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/2036317087181840385.json、视频生成/图生视频/1955921227057647617.json、视频生成/图生视频/2067249517136797697.json、视频生成/图生视频/1957002075188989954.json、视频生成/图生视频/2032294659132755970.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：93%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSamplerAdvanced`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/5 个有
- `CLIPVisionEncode` —— 2/5 个有
- `CLIPVisionLoader` —— 2/5 个有
- `ImageResizeKJv2` —— 2/5 个有
- `WanFunInpaintToVideo` —— 2/5 个有
- `WanImageToVideo` —— 2/5 个有
- `ImageBatchExtendWithOverlap` —— 1/5 个有
- `Int` —— 1/5 个有
- `LayerUtility: ImageScaleByAspectRatio` —— 1/5 个有
- `PreviewImage` —— 1/5 个有
- `WanAdvancedI2V` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 5 | 60% |
| Prompt 约束强度(CFG) | 4 | 4 - 20 | 5 | 23% |
| 采样算法 | 1 | 1 - 3.5 | 5 | 33% |
| 调度器 | euler | - | 5 | 100% |
| 重绘幅度 | simple | - | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，5 个样本，一致性 60%
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 20，5 个样本，取值分散，一致性仅 23%
- 采样算法 中位数 1，观测区间 1 - 3.5，5 个样本，取值分散，一致性仅 33%
- 调度器 最常用 euler，5 个样本，一致性 100%
- 重绘幅度 最常用 simple，5 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
