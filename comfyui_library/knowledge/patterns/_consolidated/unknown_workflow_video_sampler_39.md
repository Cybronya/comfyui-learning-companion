---
name: unknown_workflow_video_sampler_39
type: Unknown Workflow
frequency: 4
level: strong
coverage: 1
common_nodes: [FlashVSR_SM_KSampler, FlashVSR_SM_Model, ImageFromBatch+, LayerUtility: ImageScaleByAspectRatio V2, VHS_LoadVideo, VHS_VideoCombine]
problems: []
missing: []
members: [平台全量/FlashVSR Smthem版视频模糊变高清V3_2001085342960713730.json, 平台全量/FlashVSR视频超分高清放大工作流_2041784686841696257.json, 平台全量/my_flash_vsr_2_or_3_2052580464786980865.json, 平台全量/（随变）seedance2.0一键高清化V4（9_16竖版）_2021763436232843265.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_39

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（平台全量/FlashVSR Smthem版视频模糊变高清V3_2001085342960713730.json、平台全量/FlashVSR视频超分高清放大工作流_2041784686841696257.json、平台全量/my_flash_vsr_2_or_3_2052580464786980865.json、平台全量/（随变）seedance2.0一键高清化V4（9_16竖版）_2021763436232843265.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：100%

## 共有节点

全部 4 个 workflow 都包含：
- `FlashVSR_SM_KSampler`
- `FlashVSR_SM_Model`
- `ImageFromBatch+`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VHS_LoadVideo`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `ImageConcanate` —— 3/4 个有
- `JWInteger` —— 3/4 个有
- `GetVideoComponents` —— 2/4 个有
- `CreateVideo` —— 1/4 个有
- `SaveImage` —— 1/4 个有
- `SaveVideo` —— 1/4 个有
- `VHS_SelectEveryNthImage` —— 1/4 个有
- `VideoInfoSource` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 1.38391e+09 | 6.75763e+08 - 1.95201e+09 | 4 | 64% |
| Prompt 约束强度(CFG) | randomize | - | 4 | 100% |
| 采样算法 | 2 | 2 - 2 | 4 | 100% |
| 调度器 | 3.5 | 3.5 - 3.5 | 4 | 100% |
| 重绘幅度 | 11 | 11 - 11 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 1.38391e+09，观测区间 6.75763e+08 - 1.95201e+09，4 个样本
- Prompt 约束强度(CFG) 最常用 randomize，4 个样本，一致性 100%
- 采样算法 中位数 2，观测区间 2 - 2，4 个样本，取值集中（一致性 100%）
- 调度器 中位数 3.5，观测区间 3.5 - 3.5，4 个样本，取值集中（一致性 100%）
- 重绘幅度 中位数 11，观测区间 11 - 11，4 个样本，取值集中（一致性 100%）
- 风险：采样步数 观测到 1.95201e+09，超出安全上限 60（steps 偏高收益递减且显著增加耗时）
- 风险：重绘幅度 观测到 11，超出安全上限 1（denoise 接近 1.0 时接近重新生成，初始潜空间影响被抹平）
