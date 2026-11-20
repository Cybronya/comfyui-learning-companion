---
name: image_to_image_sampler_clip_unet_50
type: Image To Image
frequency: 8
level: strong
coverage: 0.915125
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Z-Image-Turbo-洗图工作流_1994007499646894081.json, 图片生成/图生图/Z-Image_ 图像反推生图_1999281406482280449.json, 图片生成/图生图/Z-Image超真实网红打造-洗图_1998985187780386817.json, 图片生成/图生图/Z-image 平替Flux2 图片反推_1994616402810114049.json, 图片生成/图生图/Z-image自动洗图-图生图image to image_1994249998170865666.json, 图片生成/图生图/z-image【超强图片编辑】图像编辑_1994750669573791745.json, 图片生成/图生图/z-image图生图-洗图工作流_1994593121038180354.json, 图片生成/文生图/Z-image洗图换明星脸_1993904921521094658.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_50

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/Z-Image-Turbo-洗图工作流_1994007499646894081.json、图片生成/图生图/Z-Image_ 图像反推生图_1999281406482280449.json、图片生成/图生图/Z-Image超真实网红打造-洗图_1998985187780386817.json、图片生成/图生图/Z-image 平替Flux2 图片反推_1994616402810114049.json、图片生成/图生图/Z-image自动洗图-图生图image to image_1994249998170865666.json…）

- **类型**：Image To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 7/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 7/8 个有
- `Qwen3_VQA` —— 6/8 个有
- `ImageConcanate` —— 4/8 个有
- `LayerUtility: PurgeVRAM` —— 4/8 个有
- `PreviewImage` —— 2/8 个有
- `easy float` —— 2/8 个有
- `easy int` —— 2/8 个有
- `AILab_QwenVL` —— 1/8 个有
- `Any To Any` —— 1/8 个有
- `CR Text` —— 1/8 个有
- `RH_Captioner` —— 1/8 个有
- `VHS_VideoCombine` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 8 - 10 | 8 | 93% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | euler | - | 8 | 100% |
| 调度器 | simple | - | 8 | 88% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 8 - 10，8 个样本，取值集中（一致性 93%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，8 个样本，一致性 100%
- 调度器 最常用 simple，8 个样本，一致性 88%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
