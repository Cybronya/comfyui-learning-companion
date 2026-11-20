---
name: text_to_image_sampler_clip_unet_245
type: Text To Image
frequency: 2
level: weak
coverage: 0.969
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSampler, LoadImage, RH_Captioner, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/图片反推+Z-image-文生图_1994210901769256962.json, 图片生成/文生图/造相 Z-image 反推生图_2073282608397643777.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_245

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/图片反推+Z-image-文生图_1994210901769256962.json、图片生成/文生图/造相 Z-image 反推生图_2073282608397643777.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：97%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `RH_Captioner`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `AspectRatio` —— 1/2 个有
- `GetImageSize` —— 1/2 个有
- `ImageScaleToTotalPixels` —— 1/2 个有
- `RH_Prompter` —— 1/2 个有
- `RH_Translator` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | - | 2 | 89% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 50% |
| 重绘幅度 | 1 | - | 2 | 100% |
| 宽度 | 1472 | - | 2 | 70% |
| 高度 | 1052 | - | 2 | 97% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 9，样本不足，未给区间，2 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 50%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 1472，样本不足，未给区间，2 个样本
- 高度 中位数 1052，样本不足，未给区间，2 个样本，取值集中（一致性 97%）
- 高发问题（1/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
