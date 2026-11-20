---
name: unknown_workflow_video_upscale_sampler_9
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.866333
common_nodes: [ImageFromBatch+, Int, LayerUtility: ImageScaleByAspectRatio V2, MuyeTextEditOutput, PreviewImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SparkVSR_SM_KSampler, SparkVSR_SM_Model, SparkVSR_SM_PreRefer, VHS_LoadVideo, VHS_VideoCombine]
problems: []
missing: []
members: [图片生成/图生图/YJ-APP-SparkVSR -视频高清放大_2038642175445045250.json, 平台全量/SparkVSR  视频高清放大_2039248941459443714.json, 平台全量/SparkVSR -视频高清放大_2038507957574438913.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_sampler_9

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/YJ-APP-SparkVSR -视频高清放大_2038642175445045250.json、平台全量/SparkVSR  视频高清放大_2039248941459443714.json、平台全量/SparkVSR -视频高清放大_2038507957574438913.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 3 个 workflow 都包含：
- `ImageFromBatch+`
- `Int`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `MuyeTextEditOutput`
- `PreviewImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SparkVSR_SM_KSampler`
- `SparkVSR_SM_Model`
- `SparkVSR_SM_PreRefer`
- `VHS_LoadVideo`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `SimpleMath+` —— 2/3 个有
- `VHS_VideoInfoSource` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 3 | 100% |
| Prompt 约束强度(CFG) | 0 | 0 - 0 | 3 | 100% |
| 采样算法 | 32x32 | - | 3 | 100% |
| 调度器 | 0x0 | - | 3 | 100% |
| 重绘幅度 | 0 | 0 - 0 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 0，观测区间 0 - 0，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 32x32，3 个样本，一致性 100%
- 调度器 最常用 0x0，3 个样本，一致性 100%
- 重绘幅度 中位数 0，观测区间 0 - 0，3 个样本，取值集中（一致性 100%）
- 风险：Prompt 约束强度(CFG) 观测到 0，低于常用下限 1（CFG 过低可能导致 Prompt 约束不足、结果偏离描述）
- 风险：重绘幅度 观测到 0，低于常用下限 0.1（）
