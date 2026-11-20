---
name: text_to_image_sampler_clip_unet_33
type: Text To Image
frequency: 15
level: strong
coverage: 0.949
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/KREA-2文生图_2115069647262404610.json, 图片生成/文生图/Krea 2 分层控制_2072527998418513922.json, 图片生成/文生图/Krea 2_2072697671621636097.json, 图片生成/文生图/Krea2 MJ美学图像-文生图_2116112144793165825.json, 图片生成/文生图/Krea2 MJ美学图像-文生图_2116149383204003841.json, 图片生成/文生图/Krea2 MJ美学图像_2114539143459074050.json, 图片生成/文生图/Krea2-全能文生图2K直出-MJ平替_2082660207729143809.json, 图片生成/文生图/Krea2-双图风格融合-T8版_2070051493448867842.json, 图片生成/文生图/comfyui出MJ最强版_2114958228521050114.json, 图片生成/文生图/comfyui出MJ最强版_2114995340066779137.json, 图片生成/文生图/comfyui出MJ最强版_2115259228259700738.json, 图片生成/文生图/comfyui出MJ最强版_2115267453298241538.json, 图片生成/文生图/电影级质感（图像） 一键生成_2113423908694224898.json, 平台全量/Krea文生图-MJ风格_2117462267443892226.json, 平台全量/Krea文生图-MJ风格_2117497335365324801.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_33

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（图片生成/文生图/KREA-2文生图_2115069647262404610.json、图片生成/文生图/Krea 2 分层控制_2072527998418513922.json、图片生成/文生图/Krea 2_2072697671621636097.json、图片生成/文生图/Krea2 MJ美学图像-文生图_2116112144793165825.json、图片生成/文生图/Krea2 MJ美学图像-文生图_2116149383204003841.json…）

- **类型**：Text To Image
- **样本数**：15
- **可信度**：强结论
- **平均知识覆盖**：95%

## 共有节点

全部 15 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ResolutionSelector` —— 14/15 个有
- `CR Prompt Text` —— 13/15 个有
- `ConditioningKrea2Rebalance` —— 12/15 个有
- `LoraLoaderModelOnly` —— 12/15 个有
- `SetNode` —— 8/15 个有
- `CR Text` —— 4/15 个有
- `CR Text Concatenate` —— 3/15 个有
- `LoadImage` —— 2/15 个有
- `孤海注释` —— 2/15 个有
- `QwenImagePromptOptimizer` —— 1/15 个有
- `RH_LLMAPI_Pro_Node` —— 1/15 个有
- `ShowText|pysssss` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 10 | 15 | 94% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 15 | 100% |
| 采样算法 | euler | - | 15 | 80% |
| 调度器 | simple | - | 15 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 15 | 100% |
| 宽度 | 1024 | 512 - 1024 | 15 | 87% |
| 高度 | 1024 | 512 - 1192 | 15 | 86% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 14/15 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 10，15 个样本，取值集中（一致性 94%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，15 个样本，一致性 80%
- 调度器 最常用 simple，15 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 512 - 1024，15 个样本，取值集中（一致性 87%）
- 高度 中位数 1024，观测区间 512 - 1192，15 个样本，取值集中（一致性 86%）
- 高发问题（14/15 个样本）：Steps较低可能导致细节不足
