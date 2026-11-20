---
name: unknown_workflow_sampler_2
type: Unknown Workflow
frequency: 17
level: strong
coverage: 1
common_nodes: [FlashVSR_SM_KSampler, FlashVSR_SM_Model, GetVideoComponents, ImageFromBatch+, JWInteger, LayerUtility: ImageScaleByAspectRatio V2, LoadVideo]
problems: []
missing: []
members: [图片生成/图生图/(全能视频S 25S满血版)FlashVSR Smthem版视频模糊变高清V1_1981405858833809409.json, 平台全量/(全能视频S 25S满血版)FlashVSR Smthem版视频模糊变高清V3_1981339891692986370.json, 平台全量/(全能视频S 25S满血版)FlashVSR Smthem版视频模糊变高清V3_1992849877795229697.json, 平台全量/(满血版)FlashVSR Smthem版视频模糊变高清V2_1980931638844674050.json, 平台全量/03-17-02-WAN2.1-图像视频高清放大-FlashVSR_1997944962325053442.json, 平台全量/Comfy挑战赛10（时光的回响）-FlashVsr视频快速高清V3_1995440630174298113.json, 平台全量/Comfy挑战赛9（云境创想）-FlashVsr视频快速高清V3_1986444390153519105.json, 平台全量/FlashVSR Smthem版视频高清 V1 浮云_2000459359534579713.json, 平台全量/FlashVSR视频极速高清放大V1.1_1981378773293645825.json, 平台全量/FlashVSR高清放大+插帧 工作流最新版 林耀4.12_2043252298549301249.json, 平台全量/Seedance2.0 Flashvsr 480P高清放大到1080P_2043150684639469570.json, 平台全量/Seedance2.0 Flashvsr 480P高清放大到1080P_2084198101111361537.json, 平台全量/VSR放大高清 浮云3.9_2030932744414433282.json, 平台全量/VSR高清放大+补针工作流 浮云（1280P）林耀_2017078648938958850.json, 平台全量/【AI小兵哥】FlashVSR-视频高清放大工作流_1981554742952378369.json, 平台全量/视频高清放大工作流_2070664583118942210.json, 视频生成/图生视频/最新高清放大 补针工作流 浮云（1280P）_1997959216243597313.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_2

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（图片生成/图生图/(全能视频S 25S满血版)FlashVSR Smthem版视频模糊变高清V1_1981405858833809409.json、平台全量/(全能视频S 25S满血版)FlashVSR Smthem版视频模糊变高清V3_1981339891692986370.json、平台全量/(全能视频S 25S满血版)FlashVSR Smthem版视频模糊变高清V3_1992849877795229697.json、平台全量/(满血版)FlashVSR Smthem版视频模糊变高清V2_1980931638844674050.json、平台全量/03-17-02-WAN2.1-图像视频高清放大-FlashVSR_1997944962325053442.json…）

- **类型**：Unknown Workflow
- **样本数**：17
- **可信度**：强结论
- **平均知识覆盖**：100%

## 共有节点

全部 17 个 workflow 都包含：
- `FlashVSR_SM_KSampler`
- `FlashVSR_SM_Model`
- `GetVideoComponents`
- `ImageFromBatch+`
- `JWInteger`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadVideo`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 15/17 个有
- `VHS_VideoCombine` —— 15/17 个有
- `SaveVideo` —— 14/17 个有
- `ImageConcanate` —— 10/17 个有
- `MathExpression_UTK` —— 3/17 个有
- `RIFE VFI` —— 3/17 个有
- `LoadImage` —— 2/17 个有
- `LayerUtility: PurgeVRAM` —— 1/17 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8.61494e+08 | 3.84961e+08 - 2.10262e+09 | 17 | 48% |
| Prompt 约束强度(CFG) | randomize | - | 17 | 94% |
| 采样算法 | 2 | 2 - 2 | 17 | 100% |
| 调度器 | 3.5 | 3.5 - 3.5 | 17 | 100% |
| 重绘幅度 | 11 | 11 - 11 | 17 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 8.61494e+08，观测区间 3.84961e+08 - 2.10262e+09，17 个样本，取值分散，一致性仅 48%
- Prompt 约束强度(CFG) 最常用 randomize，17 个样本，一致性 94%
- 采样算法 中位数 2，观测区间 2 - 2，17 个样本，取值集中（一致性 100%）
- 调度器 中位数 3.5，观测区间 3.5 - 3.5，17 个样本，取值集中（一致性 100%）
- 重绘幅度 中位数 11，观测区间 11 - 11，17 个样本，取值集中（一致性 100%）
- 风险：采样步数 观测到 2.10262e+09，超出安全上限 60（steps 偏高收益递减且显著增加耗时）
- 风险：重绘幅度 观测到 11，超出安全上限 1（denoise 接近 1.0 时接近重新生成，初始潜空间影响被抹平）
