---
name: unknown_workflow_video_sampler_30
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.7465
common_nodes: [AILab_QwenVL, CR Text, CR Text Concatenate, Compare, FlashVSR_SM_KSampler, FlashVSR_SM_Model, GetImageSize, GetVideoComponents, ImageResize+, LayerUtility: PurgeVRAM V2, LoadImage, PrimitiveBoolean, RHHiddenNodes, ShowText|pysssss, Text Multiline, VHS_VideoCombine, easy ifElse, easy imageConcat]
problems: []
missing: []
members: [视频生成/图生视频/1982163769721798658.json, 视频生成/文生视频/【规格化提示词】Sroa2文生视频-FlashVSR放大_1981838740345757698.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_30

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/1982163769721798658.json、视频生成/文生视频/【规格化提示词】Sroa2文生视频-FlashVSR放大_1981838740345757698.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：75%

## 共有节点

全部 2 个 workflow 都包含：
- `AILab_QwenVL`
- `CR Text`
- `CR Text Concatenate`
- `Compare`
- `FlashVSR_SM_KSampler`
- `FlashVSR_SM_Model`
- `GetImageSize`
- `GetVideoComponents`
- `ImageResize+`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `PrimitiveBoolean`
- `RHHiddenNodes`
- `ShowText|pysssss`
- `Text Multiline`
- `VHS_VideoCombine`
- `easy ifElse`
- `easy imageConcat`

**可变部分**（部分 workflow 才有）：
- `CM_BoolToInt` —— 1/2 个有
- `RH_Sora2_I2V` —— 1/2 个有
- `RH_Sora2_T2V` —— 1/2 个有
- `easy textSwitch` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 1.23011e+09 | - | 2 | 63% |
| Prompt 约束强度(CFG) | randomize | - | 2 | 100% |
| 采样算法 | 1 | - | 2 | 100% |
| 调度器 | 3 | - | 2 | 100% |
| 重绘幅度 | 11 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 1.23011e+09，样本不足，未给区间，2 个样本
- Prompt 约束强度(CFG) 最常用 randomize，2 个样本，一致性 100%
- 采样算法 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 中位数 3，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 重绘幅度 中位数 11，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 风险：采样步数 观测到 1.68591e+09，超出安全上限 60（steps 偏高收益递减且显著增加耗时）
- 风险：重绘幅度 观测到 11，超出安全上限 1（denoise 接近 1.0 时接近重新生成，初始潜空间影响被抹平）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
