---
name: text_to_image_sampler_clip_unet_221
type: Text To Image
frequency: 2
level: weak
coverage: 0.9025
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, LoadImage, PreviewAny, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Anima参考图像出图_2056595509397250049.json, 图片生成/文生图/Z-Image-Turbo-洗图升级版（每次6张）_1994584620748378114.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_221

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/Anima参考图像出图_2056595509397250049.json、图片生成/文生图/Z-Image-Turbo-洗图升级版（每次6张）_1994584620748378114.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `PreviewAny`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `AILab_QwenVL` —— 1/2 个有
- `Florence2ModelLoader` —— 1/2 个有
- `Florence2Run` —— 1/2 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有
- `PIP_StringConcatenation` —— 1/2 个有
- `easy string` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1412 | - | 2 | 64% |
| 高度 | 1272 | - | 2 | 85% |
| 采样步数 | 23 | - | 2 | 35% |
| Prompt 约束强度(CFG) | 2.75 | - | 2 | 36% |
| 采样算法 | er_sde | - | 2 | 50% |
| 调度器 | beta | - | 2 | 50% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1412，样本不足，未给区间，2 个样本
- 高度 中位数 1272，样本不足，未给区间，2 个样本，取值集中（一致性 85%）
- 采样步数 中位数 23，样本不足，未给区间，2 个样本，取值分散，一致性仅 35%
- Prompt 约束强度(CFG) 中位数 2.75，样本不足，未给区间，2 个样本，取值分散，一致性仅 36%
- 采样算法 最常用 er_sde，2 个样本，一致性 50%
- 调度器 最常用 beta，2 个样本，一致性 50%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（1/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
