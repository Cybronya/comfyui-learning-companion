---
name: unknown_workflow_video_sampler_12
type: Unknown Workflow
frequency: 10
level: strong
coverage: 0.4565
common_nodes: [FlashVSR_SM_KSampler, FlashVSR_SM_Model, GetImageSize, GetNode, ImageConcatMulti, SetNode, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, easy int, easy seed]
problems: []
missing: []
members: [平台全量/1119alan测-FlashVSR-视频高清_1990979079866359810.json, 平台全量/1119alan测-FlashVSR-视频高清_1991046779506466817.json, 平台全量/FlashVSR 视频高清修复_2047850947459682305.json, 平台全量/FlashVSR 视频高清放大+补帧  视频高清修复Video Upscal_2014573613071998978.json, 平台全量/FlashVSR-新一代视频高清ai_1984868119032250369.json, 平台全量/FlashVSR-视频放大-高清修复-速度快，显存占用低_1990038267808673793.json, 平台全量/FlashVSR-视频高清ai_2011168559925301249.json, 平台全量/flashvsr-全能视频S高清_2007802894275321857.json, 视频生成/图生视频/FlashVSR-视频放大 高清视频放大 最强视频放大神器 高清修复-速度快 显存占用低_2006193866545827841.json, 视频生成/图生视频/FlashVSR-视频放大-高清修复-速度快，显存占用低_2000859857857245185.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_12

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（平台全量/1119alan测-FlashVSR-视频高清_1990979079866359810.json、平台全量/1119alan测-FlashVSR-视频高清_1991046779506466817.json、平台全量/FlashVSR 视频高清修复_2047850947459682305.json、平台全量/FlashVSR 视频高清放大+补帧  视频高清修复Video Upscal_2014573613071998978.json、平台全量/FlashVSR-新一代视频高清ai_1984868119032250369.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：46%

## 共有节点

全部 10 个 workflow 都包含：
- `FlashVSR_SM_KSampler`
- `FlashVSR_SM_Model`
- `GetImageSize`
- `GetNode`
- `ImageConcatMulti`
- `SetNode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `easy int`
- `easy seed`

**可变部分**（部分 workflow 才有）：
- `PrimitiveString` —— 7/10 个有
- `StringConcatenate` —— 7/10 个有
- `Label (rgthree)` —— 6/10 个有
- `Bookmark (rgthree)` —— 5/10 个有
- `ImageResizeKJ` —— 5/10 个有
- `ImageResizeKJv2` —— 5/10 个有
- `AddLabel` —— 3/10 个有
- `SDVN Any Show` —— 3/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8.27727e+08 | 1.75293e+08 - 1.46652e+09 | 10 | 51% |
| Prompt 约束强度(CFG) | randomize | - | 10 | 100% |
| 采样算法 | 2 | 2 - 2 | 10 | 100% |
| 调度器 | 3.5 | 3.5 - 3.5 | 10 | 100% |
| 重绘幅度 | 11 | 11 - 11 | 10 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 8.27727e+08，观测区间 1.75293e+08 - 1.46652e+09，10 个样本
- Prompt 约束强度(CFG) 最常用 randomize，10 个样本，一致性 100%
- 采样算法 中位数 2，观测区间 2 - 2，10 个样本，取值集中（一致性 100%）
- 调度器 中位数 3.5，观测区间 3.5 - 3.5，10 个样本，取值集中（一致性 100%）
- 重绘幅度 中位数 11，观测区间 11 - 11，10 个样本，取值集中（一致性 100%）
- 风险：采样步数 观测到 1.46652e+09，超出安全上限 60（steps 偏高收益递减且显著增加耗时）
- 风险：重绘幅度 观测到 11，超出安全上限 1（denoise 接近 1.0 时接近重新生成，初始潜空间影响被抹平）
