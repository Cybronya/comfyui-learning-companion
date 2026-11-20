---
name: unknown_workflow_sampler_67
type: Unknown Workflow
frequency: 3
level: weak
coverage: 0.755
common_nodes: [CreateVideo, Float, GetVideoComponents, ImageFromBatch+, JWInteger, LayerUtility: ImageScaleByAspectRatio V2, LoadVideo, PreviewImage, SaveImage, SaveVideo, SparkVSR_SM_KSampler, SparkVSR_SM_Model, SparkVSR_SM_PreRefer, SparkVSR_SM_SRModel, Video Slice, easy cleanGpuUsed]
problems: []
missing: []
members: [平台全量/(单图垫图模式)SeedVr+SparkVSR视频高清放大V2_2037695868807159809.json, 平台全量/(多图垫图模式)SeedVr+SparkVSR视频高清放大V2_2037709282828886018.json, 平台全量/SparkVSR -视频超分_单图垫图稳定不崩_2038504666648027138.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_67

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/(单图垫图模式)SeedVr+SparkVSR视频高清放大V2_2037695868807159809.json、平台全量/(多图垫图模式)SeedVr+SparkVSR视频高清放大V2_2037709282828886018.json、平台全量/SparkVSR -视频超分_单图垫图稳定不崩_2038504666648027138.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：76%

## 共有节点

全部 3 个 workflow 都包含：
- `CreateVideo`
- `Float`
- `GetVideoComponents`
- `ImageFromBatch+`
- `JWInteger`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadVideo`
- `PreviewImage`
- `SaveImage`
- `SaveVideo`
- `SparkVSR_SM_KSampler`
- `SparkVSR_SM_Model`
- `SparkVSR_SM_PreRefer`
- `SparkVSR_SM_SRModel`
- `Video Slice`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 2/3 个有
- `FlashVSR_SM_KSampler` —— 2/3 个有
- `FlashVSR_SM_Model` —— 2/3 个有
- `SeedVR2LoadDiTModel` —— 1/3 个有
- `SeedVR2LoadVAEModel` —— 1/3 个有
- `SeedVR2VideoUpscaler` —— 1/3 个有
- `TextInputBasic` —— 1/3 个有
- `easy batchAnything` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 3.15876e+08 | 8 - 9.1296e+08 | 3 | 8% |
| Prompt 约束强度(CFG) | randomize | - | 3 | 67% |
| 采样算法 | 2 | - | 2 | 100% |
| 调度器 | 3.5 | - | 2 | 100% |
| 重绘幅度 | 11 | 0 - 11 | 3 | 29% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 3.15876e+08，观测区间 8 - 9.1296e+08，3 个样本，取值分散，一致性仅 8%
- Prompt 约束强度(CFG) 最常用 randomize，3 个样本，一致性 67%
- 采样算法 中位数 2，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 中位数 3.5，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 重绘幅度 中位数 11，观测区间 0 - 11，3 个样本，取值分散，一致性仅 29%
- 风险：采样步数 观测到 9.1296e+08，超出安全上限 60（steps 偏高收益递减且显著增加耗时）
- 风险：重绘幅度 观测到 11，超出安全上限 1（denoise 接近 1.0 时接近重新生成，初始潜空间影响被抹平）
- 风险：重绘幅度 观测到 0，低于常用下限 0.1（）
