---
name: unknown_workflow_sampler_clip_unet_53
type: Unknown Workflow
frequency: 15
level: moderate
coverage: 0.9236
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSamplerAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Z-image-turbo与base模型融合文生图_2018686787765407745.json, 图片生成/文生图/Z-image-造相增强随机性-蓝色多脑盒_1999680352287326209.json, 图片生成/文生图/Z-image文生图Beyond Reality 人像写真_2003868030209826818.json, 图片生成/文生图/Z-image文生图（加强随机性）_1999686713578487809.json, 图片生成/文生图/Z-image欧美人像-文生图_2043349863571660801.json, 图片生成/文生图/krea2-感性质感文生图_2077573493826347010.json, 图片生成/文生图/krea2-成熟之美文生图_2077737335516651521.json, 图片生成/文生图/krea2-混血女模文生图，_2085359376507957250.json, 图片生成/文生图/krea2-纤姿文生图_2091439477406396417.json, 图片生成/文生图/krea2-肌肉男身段文生图_2099416655523827714.json, 图片生成/文生图/【krea2-Anima】文生图_2077588539222618113.json, 图片生成/文生图/【krea2-turbo-bf16】Bkz人像摄影应用_2082316590745477122.json, 图片生成/文生图/【krea2-turbo-bf16】Bkz人像摄影应用_2098212483956822017.json, 视频生成/文生视频/krea2-感性质感文生图_api_2077744663007682562.json, 视频生成/文生视频/krea2-黑珍珠文生图_2078481829623062530.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_53

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（图片生成/文生图/Z-image-turbo与base模型融合文生图_2018686787765407745.json、图片生成/文生图/Z-image-造相增强随机性-蓝色多脑盒_1999680352287326209.json、图片生成/文生图/Z-image文生图Beyond Reality 人像写真_2003868030209826818.json、图片生成/文生图/Z-image文生图（加强随机性）_1999686713578487809.json、图片生成/文生图/Z-image欧美人像-文生图_2043349863571660801.json…）

- **类型**：Unknown Workflow
- **样本数**：15
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 15 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSamplerAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 13/15 个有
- `ModelSamplingAuraFlow` —— 12/15 个有
- `LoraLoaderModelOnly` —— 11/15 个有
- `JjkText` —— 10/15 个有
- `ResolutionSelector` —— 10/15 个有
- `solarL_SaveImagesToZip` —— 10/15 个有
- `CR Prompt Text` —— 2/15 个有
- `LatentUpscaleBy` —— 2/15 个有
- `JDCN_StringToList` —— 1/15 个有
- `ProcessString` —— 1/15 个有
- `easy int` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 928 | 512 - 1440 | 15 | 61% |
| 高度 | 1664 | 512 - 2560 | 15 | 45% |
| 采样步数 | randomize | - | 15 | 100% |
| Prompt 约束强度(CFG) | 8 | 8 - 20 | 15 | 66% |
| 采样算法 | 1 | 1 - 2 | 15 | 77% |
| 调度器 | euler_ancestral | - | 15 | 47% |
| 重绘幅度 | simple | - | 15 | 80% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 928，观测区间 512 - 1440，15 个样本
- 高度 中位数 1664，观测区间 512 - 2560，15 个样本，取值分散，一致性仅 45%
- 采样步数 最常用 randomize，15 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 8，观测区间 8 - 20，15 个样本
- 采样算法 中位数 1，观测区间 1 - 2，15 个样本
- 调度器 最常用 euler_ancestral，15 个样本，一致性 47%
- 重绘幅度 最常用 simple，15 个样本，一致性 80%
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
