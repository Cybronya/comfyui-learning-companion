---
name: image_to_image_sampler_clip_unet_99
type: Image To Image
frequency: 5
level: weak
coverage: 1
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/flux.2-三图融合-标准版-（必收藏）_2052738645555200002.json, 图片生成/图生图/flux.2-去除水印-标准版-（必收藏）_2056999199815847938.json, 图片生成/图生图/flux2_klein_2077688220808208385.json, 图片生成/图生图/klein 洗图工作流_2041123980865708033.json, 图片生成/图生图/最强Qwan中文图像洗图工作流_1954158265661833217.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_99

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/flux.2-三图融合-标准版-（必收藏）_2052738645555200002.json、图片生成/图生图/flux.2-去除水印-标准版-（必收藏）_2056999199815847938.json、图片生成/图生图/flux2_klein_2077688220808208385.json、图片生成/图生图/klein 洗图工作流_2041123980865708033.json、图片生成/图生图/最强Qwan中文图像洗图工作流_1954158265661833217.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：100%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/5 个有
- `ReferenceLatent` —— 3/5 个有
- `ModelSamplingAuraFlow` —— 2/5 个有
- `CFGNorm` —— 1/5 个有
- `GoogleTranslator` —— 1/5 个有
- `RH_Captioner` —— 1/5 个有
- `Seed (rgthree)` —— 1/5 个有
- `easy cleanGpuUsed` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 6 - 20 | 5 | 57% |
| Prompt 约束强度(CFG) | 1 | 1 - 5 | 5 | 27% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 80% |
| 重绘幅度 | 1 | 0.7 - 1 | 5 | 87% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 6 - 20，5 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 5，5 个样本，取值分散，一致性仅 27%
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 0.7 - 1，5 个样本，取值集中（一致性 87%）
