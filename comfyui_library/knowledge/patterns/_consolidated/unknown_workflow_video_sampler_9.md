---
name: unknown_workflow_video_sampler_9
type: Unknown Workflow
frequency: 14
level: moderate
coverage: 1
common_nodes: [FlashVSR_SM_KSampler, FlashVSR_SM_Model, LayerUtility: ImageScaleByAspectRatio V2, VHS_VideoCombine, VHS_VideoInfoLoaded]
problems: []
missing: []
members: [平台全量/dj模糊视频高清修复_2010686397769850881.json, 平台全量/dj模糊视频高清修复_2010687974538743810.json, 平台全量/dj模糊视频高清修复测试3_2010713966263144449.json, 平台全量/dj模糊视频高清修复测试6_2010719850099904513.json, 平台全量/dj高清_2010125557274513409.json, 平台全量/flashvsr1.1最新版本模糊视频高清修复视频高清放大二次放大视频修复低清视频_2012532636421459970.json, 平台全量/模糊视频高清修复_1981060663512535042.json, 平台全量/模糊视频高清修复_1985626721837821954.json, 平台全量/模糊视频高清修复_1987910941885050881.json, 平台全量/模糊视频高清修复_1991331292088479746.json, 平台全量/模糊视频高清修复_1998311521639890945.json, 平台全量/索拉视频提升清晰度_2002270032128294914.json, 平台全量/索拉视频提升清晰度_2019240481401606145.json, 平台全量/视频高清放大_2014465156461371393.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_9

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（平台全量/dj模糊视频高清修复_2010686397769850881.json、平台全量/dj模糊视频高清修复_2010687974538743810.json、平台全量/dj模糊视频高清修复测试3_2010713966263144449.json、平台全量/dj模糊视频高清修复测试6_2010719850099904513.json、平台全量/dj高清_2010125557274513409.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：中等可信
- **平均知识覆盖**：100%

## 共有节点

全部 14 个 workflow 都包含：
- `FlashVSR_SM_KSampler`
- `FlashVSR_SM_Model`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VHS_VideoCombine`
- `VHS_VideoInfoLoaded`

**可变部分**（部分 workflow 才有）：
- `VHS_LoadVideo` —— 12/14 个有
- `easy cleanGpuUsed` —— 2/14 个有
- `LoadVideoFromUrl` —— 1/14 个有
- `ShowAnything|Mie` —— 1/14 个有
- `VHS_LoadVideoPath` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 1.20033e+09 | 2.71089e+07 - 2.10998e+09 | 14 | 38% |
| Prompt 约束强度(CFG) | randomize | - | 14 | 100% |
| 采样算法 | 1 | 1 - 1 | 14 | 100% |
| 调度器 | 3.5 | 3.5 - 3.5 | 14 | 100% |
| 重绘幅度 | 11 | 7 - 11 | 14 | 80% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 1.20033e+09，观测区间 2.71089e+07 - 2.10998e+09，14 个样本，取值分散，一致性仅 38%
- Prompt 约束强度(CFG) 最常用 randomize，14 个样本，一致性 100%
- 采样算法 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 调度器 中位数 3.5，观测区间 3.5 - 3.5，14 个样本，取值集中（一致性 100%）
- 重绘幅度 中位数 11，观测区间 7 - 11，14 个样本
- 风险：采样步数 观测到 2.10998e+09，超出安全上限 60（steps 偏高收益递减且显著增加耗时）
- 风险：重绘幅度 观测到 11，超出安全上限 1（denoise 接近 1.0 时接近重新生成，初始潜空间影响被抹平）
