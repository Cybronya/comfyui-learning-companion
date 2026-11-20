---
name: unknown_workflow_video_sampler_22
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.934
common_nodes: [FlashVSR_SM_KSampler, FlashVSR_SM_Model, LayerUtility: ImageScaleByAspectRatio V2, VHS_LoadVideo, VHS_VideoCombine]
problems: []
missing: []
members: [平台全量/seedance2.0 视频高清放大_2021176268426842114.json, 平台全量/seedance2.0 视频高清放大_2021767550123646978.json, 平台全量/模糊视频高清修复_1988873319648735234.json, 平台全量/真实好用！seedance2.0 视频高清放大 最强视频编辑王者！_2021795658616807426.json, 平台全量/视频放大指定放大倍数+FlashVSR_SM_KSampler+全节点注释_2059521612285833217.json, 平台全量/视频高清放大-FlashVSR_1990259324381523970.json, 平台全量/🦖FlashVSR视频高清 （满血）_1995343776853975041.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_22

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（平台全量/seedance2.0 视频高清放大_2021176268426842114.json、平台全量/seedance2.0 视频高清放大_2021767550123646978.json、平台全量/模糊视频高清修复_1988873319648735234.json、平台全量/真实好用！seedance2.0 视频高清放大 最强视频编辑王者！_2021795658616807426.json、平台全量/视频放大指定放大倍数+FlashVSR_SM_KSampler+全节点注释_2059521612285833217.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 7 个 workflow 都包含：
- `FlashVSR_SM_KSampler`
- `FlashVSR_SM_Model`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VHS_LoadVideo`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `VHS_VideoInfo` —— 4/7 个有
- `LoadImage` —— 3/7 个有
- `VHS_VideoInfoSource` —— 3/7 个有
- `easy int` —— 2/7 个有
- `LayerUtility: PurgeVRAM V2` —— 1/7 个有
- `RHHiddenNodes` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 1.4097e+09 | 1.2003e+09 - 1.53811e+09 | 7 | 91% |
| Prompt 约束强度(CFG) | randomize | - | 7 | 100% |
| 采样算法 | 2 | 1 - 2 | 7 | 81% |
| 调度器 | 3.5 | 3.5 - 3.5 | 7 | 100% |
| 重绘幅度 | 11 | 11 - 11 | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 1.4097e+09，观测区间 1.2003e+09 - 1.53811e+09，7 个样本，取值集中（一致性 91%）
- Prompt 约束强度(CFG) 最常用 randomize，7 个样本，一致性 100%
- 采样算法 中位数 2，观测区间 1 - 2，7 个样本，取值集中（一致性 81%）
- 调度器 中位数 3.5，观测区间 3.5 - 3.5，7 个样本，取值集中（一致性 100%）
- 重绘幅度 中位数 11，观测区间 11 - 11，7 个样本，取值集中（一致性 100%）
- 风险：采样步数 观测到 1.53811e+09，超出安全上限 60（steps 偏高收益递减且显著增加耗时）
- 风险：重绘幅度 观测到 11，超出安全上限 1（denoise 接近 1.0 时接近重新生成，初始潜空间影响被抹平）
