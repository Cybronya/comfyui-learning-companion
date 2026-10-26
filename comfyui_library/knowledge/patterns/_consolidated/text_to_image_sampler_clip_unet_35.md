---
name: text_to_image_sampler_clip_unet_35
type: Text To Image
frequency: 14
level: moderate
coverage: 0.987
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSampler, LoadImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader, scale]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/cheems大狗拆分-klein_2032421634149191681.json, 图片生成/图生图/cheems小狗拆分-klein_2032696662476460034.json, 图片生成/图生图/dnf立绘-klein_2094651972447199233.json, 图片生成/图生图/沙雕古风角色-klein_2083342088791486465.json, 图片生成/图生图/沙雕角色-klein_2032423622459006977.json, 图片生成/图生图/角色转cheems大狗-klein_2032694011659558914.json, 图片生成/图生图/角色转cheems小-klein_2033068803185184770.json, 图片生成/图生图/角色转dro-klein_2037310245491449857.json, 图片生成/图生图/金色法相-klein_2086299055189221378.json, 图片生成/文生图/传奇风格场景-klein_2083539437392318465.json, 图片生成/文生图/传奇风格场景制作｜klein文生图图生图_2091780106510491649.json, 图片生成/文生图/传奇风格场景生成｜klein文生图图生图直出_2091608413749993473.json, 图片生成/文生图/沙雕场景-klein_2083534277521793026.json, 图片生成/文生图/沙雕角色6-klein_2091476898760187905.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_35

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（图片生成/图生图/cheems大狗拆分-klein_2032421634149191681.json、图片生成/图生图/cheems小狗拆分-klein_2032696662476460034.json、图片生成/图生图/dnf立绘-klein_2094651972447199233.json、图片生成/图生图/沙雕古风角色-klein_2083342088791486465.json、图片生成/图生图/沙雕角色-klein_2032423622459006977.json…）

- **类型**：Text To Image
- **样本数**：14
- **可信度**：中等可信
- **平均知识覆盖**：99%

## 共有节点

全部 14 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `scale`

**可变部分**（部分 workflow 才有）：
- `LoraLoader` —— 8/14 个有
- `LoraLoaderModelOnly` —— 6/14 个有
- `easy anythingIndexSwitch` —— 6/14 个有
- `HAIGC_SaveImagesToZip` —— 4/14 个有
- `RMBG` —— 4/14 个有
- `JjkText` —— 2/14 个有
- `solarL_SaveImagesToZip` —— 2/14 个有
- `孤海注释` —— 2/14 个有
- `ImageScaleBy` —— 1/14 个有
- `PIP_图像联结` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | 1 - 1 | 8 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 8 | 100% |
| 采样步数 | 4 | 2 - 5 | 14 | 85% |
| Prompt 约束强度(CFG) | 1 | 1 - 4.5 | 14 | 18% |
| 采样算法 | euler | - | 14 | 86% |
| 调度器 | simple | - | 14 | 86% |
| 重绘幅度 | 1 | 1 - 1 | 14 | 100% |
| 宽度 | 1024 | 80 - 1920 | 14 | 38% |
| 高度 | 896 | 80 - 1200 | 14 | 53% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 17/14 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- LoRA 模型强度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 2 - 5，14 个样本，取值集中（一致性 85%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4.5，14 个样本，取值分散，一致性仅 18%
- 采样算法 最常用 euler，14 个样本，一致性 86%
- 调度器 最常用 simple，14 个样本，一致性 86%
- 重绘幅度 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 80 - 1920，14 个样本，取值分散，一致性仅 38%
- 高度 中位数 896，观测区间 80 - 1200，14 个样本
- 高发问题（17/14 个样本）：Steps较低可能导致细节不足
