---
name: unknown_workflow_sampler_5
type: Unknown Workflow
frequency: 14
level: moderate
coverage: 0.987357
common_nodes: [CreateVideo, FlashVSR_SM_KSampler, FlashVSR_SM_Model, GetVideoComponents, ImageFromBatch+, JWInteger, LayerUtility: ImageScaleByAspectRatio V2, LoadVideo, SaveVideo]
problems: []
missing: []
members: [平台全量/FlashVSR Smthem版视频模糊变高清(48G)_2028758013741375489.json, 平台全量/FlashVSR视频放大_2085314726308966402.json, 平台全量/FlashVSR采样增强细节超分 720P→4K_2085387604899483649.json, 平台全量/Flashvsr 480P放大到1080P_2056342068007628801.json, 平台全量/MiniMax H3 480P高清放大到1080P_2084900519344164866.json, 平台全量/MiniMax H3 480P高清放大到1080P_2084914733051891713.json, 平台全量/Seedance 2.0-首尾帧获取+视频高清修复_2021599529472106498.json, 平台全量/Seedance 2.0视频高清化+首尾帧获取V1_2020826565638103041.json, 平台全量/Seedance 2.0视频高清化+首尾帧获取V1_2021025288397787138.json, 平台全量/Seedance 2.0视频高清化+首尾帧获取V1_2021050540028862466.json, 平台全量/Seedance 2.0视频高清化+首尾帧获取V1_2021474178897022977.json, 平台全量/视频高清化+首尾帧提取取 V1.0_2029378641993404418.json, 数字人/数字人/数字人视频高清化+首尾帧提取取 V1.0_2021579573317607426.json, 视频生成/图生视频/图生视频+视频高清放大  最强王者！ Seedance1.5Pro 首尾帧图生视频_2021792060466008066.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_5

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（平台全量/FlashVSR Smthem版视频模糊变高清(48G)_2028758013741375489.json、平台全量/FlashVSR视频放大_2085314726308966402.json、平台全量/FlashVSR采样增强细节超分 720P→4K_2085387604899483649.json、平台全量/Flashvsr 480P放大到1080P_2056342068007628801.json、平台全量/MiniMax H3 480P高清放大到1080P_2084900519344164866.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：中等可信
- **平均知识覆盖**：99%

## 共有节点

全部 14 个 workflow 都包含：
- `CreateVideo`
- `FlashVSR_SM_KSampler`
- `FlashVSR_SM_Model`
- `GetVideoComponents`
- `ImageFromBatch+`
- `JWInteger`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadVideo`
- `SaveVideo`

**可变部分**（部分 workflow 才有）：
- `GetImageSizeAndCount` —— 8/14 个有
- `SaveImage` —— 8/14 个有
- `ImageConcanate` —— 7/14 个有
- `VHS_VideoCombine` —— 7/14 个有
- `CR Text` —— 1/14 个有
- `Fast Groups Bypasser (rgthree)` —— 1/14 个有
- `GetImageSize` —— 1/14 个有
- `ImageResizeKJv2` —— 1/14 个有
- `LoadImage` —— 1/14 个有
- `PreviewAny` —— 1/14 个有
- `RH_Doubao_Seedance_1_5_Pro` —— 1/14 个有
- `easy mathInt` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 1.14569e+09 | 3.93445e+07 - 1.94319e+09 | 14 | 51% |
| Prompt 约束强度(CFG) | randomize | - | 14 | 100% |
| 采样算法 | 2 | 2 - 2 | 14 | 100% |
| 调度器 | 3.5 | 1.5 - 3.5 | 14 | 85% |
| 重绘幅度 | 11 | 11 - 11 | 14 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 1.14569e+09，观测区间 3.93445e+07 - 1.94319e+09，14 个样本
- Prompt 约束强度(CFG) 最常用 randomize，14 个样本，一致性 100%
- 采样算法 中位数 2，观测区间 2 - 2，14 个样本，取值集中（一致性 100%）
- 调度器 中位数 3.5，观测区间 1.5 - 3.5，14 个样本，取值集中（一致性 85%）
- 重绘幅度 中位数 11，观测区间 11 - 11，14 个样本，取值集中（一致性 100%）
- 风险：采样步数 观测到 1.94319e+09，超出安全上限 60（steps 偏高收益递减且显著增加耗时）
- 风险：重绘幅度 观测到 11，超出安全上限 1（denoise 接近 1.0 时接近重新生成，初始潜空间影响被抹平）
