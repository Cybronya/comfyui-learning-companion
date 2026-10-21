---
name: unknown_workflow_sampler_clip_unet_34
type: Unknown Workflow
frequency: 13
level: moderate
coverage: 0.902846
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSamplerAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Z-image，文生图_2009572089073766402.json, 图片生成/文生图/Zimage生图-随机增强-两步法_2004931976354299905.json, 图片生成/文生图/krea2-感性质感文生图_2077573493826347010.json, 图片生成/文生图/krea2-成熟之美文生图_2077737335516651521.json, 图片生成/文生图/krea2-混血女模文生图，_2085359376507957250.json, 图片生成/文生图/krea2-纤姿文生图_2091439477406396417.json, 图片生成/文生图/krea2-肌肉男身段文生图_2099416655523827714.json, 图片生成/文生图/krea2文生图二采放大_2078759847776051201.json, 图片生成/文生图/【krea2-Anima】文生图_2077588539222618113.json, 图片生成/文生图/【krea2-turbo-bf16】Bkz人像摄影应用_2082316590745477122.json, 图片生成/文生图/【krea2-turbo-bf16】Bkz人像摄影应用_2098212483956822017.json, 视频生成/文生视频/krea2-感性质感文生图_api_2077744663007682562.json, 视频生成/文生视频/krea2-黑珍珠文生图_2078481829623062530.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_34

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/文生图/Z-image，文生图_2009572089073766402.json、图片生成/文生图/Zimage生图-随机增强-两步法_2004931976354299905.json、图片生成/文生图/krea2-感性质感文生图_2077573493826347010.json、图片生成/文生图/krea2-成熟之美文生图_2077737335516651521.json、图片生成/文生图/krea2-混血女模文生图，_2085359376507957250.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 13 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSamplerAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 12/13 个有
- `LoraLoaderModelOnly` —— 12/13 个有
- `JjkText` —— 10/13 个有
- `ModelSamplingAuraFlow` —— 10/13 个有
- `ResolutionSelector` —— 10/13 个有
- `solarL_SaveImagesToZip` —— 10/13 个有
- `LatentUpscaleBy` —— 3/13 个有
- `ttN text` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 13 | 92% |
| Prompt 约束强度(CFG) | 8 | 8 - 15 | 13 | 77% |
| 采样算法 | 1 | 1 - 1 | 13 | 100% |
| 调度器 | euler_ancestral | - | 13 | 54% |
| 重绘幅度 | simple | - | 13 | 85% |
| 宽度 | 1080 | 512 - 1440 | 13 | 59% |
| 高度 | 1920 | 512 - 2560 | 13 | 39% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，13 个样本，一致性 92%
- Prompt 约束强度(CFG) 中位数 8，观测区间 8 - 15，13 个样本
- 采样算法 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler_ancestral，13 个样本，一致性 54%
- 重绘幅度 最常用 simple，13 个样本，一致性 85%
- 宽度 中位数 1080，观测区间 512 - 1440，13 个样本
- 高度 中位数 1920，观测区间 512 - 2560，13 个样本，取值分散，一致性仅 39%
- 风险：Prompt 约束强度(CFG) 观测到 15，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
