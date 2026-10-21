---
name: text_to_image_sampler_clip_unet_29
type: Text To Image
frequency: 12
level: moderate
coverage: 0.95675
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-image 反推提示词出图_2001135324149448705.json, 图片生成/文生图/Z-image 文生图_2006288280186265601.json, 图片生成/文生图/Z-image 最新模型 文生图工作流V1.0_1993835227038629890.json, 图片生成/文生图/Z-image 超清快速文生图_2010897242143592450.json, 图片生成/文生图/Z-image+Qwen3 图像反推_1993867190606692353.json, 图片生成/文生图/Z-image-turbo-文生图（开源之王）_1997492012880433154.json, 图片生成/文生图/Z-image-turbo基础文生图【用于绘世comfyui批量管理系统】_2089190207693344769.json, 图片生成/文生图/Z-image_1996868918985773057.json, 图片生成/文生图/Z_image_turbo快速文生图 自用版_2097176754392756226.json, 图片生成/文生图/Z_image_turbo快速文生图_2051577152918835202.json, 图片生成/文生图/boogu_image_turbo+文生图+提示词反推_2069229283981217794.json, 图片生成/文生图/boogu_image_turbo+文生图+提示词反推_2069585759648174082.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_29

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/文生图/Z-image 反推提示词出图_2001135324149448705.json、图片生成/文生图/Z-image 文生图_2006288280186265601.json、图片生成/文生图/Z-image 最新模型 文生图工作流V1.0_1993835227038629890.json、图片生成/文生图/Z-image 超清快速文生图_2010897242143592450.json、图片生成/文生图/Z-image+Qwen3 图像反推_1993867190606692353.json…）

- **类型**：Text To Image
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 11/12 个有
- `LoadImage` —— 5/12 个有
- `RH_Captioner` —— 3/12 个有
- `RTXVideoSuperResolution` —— 3/12 个有
- `Fast Groups Bypasser (rgthree)` —— 2/12 个有
- `PreviewAny` —— 2/12 个有
- `LayerUtility: ImageScaleByAspectRatio` —— 1/12 个有
- `Qwen3_VQA` —— 1/12 个有
- `Text _O` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1052 | 720 - 1920 | 12 | 68% |
| 高度 | 1536 | 1024 - 1920 | 12 | 74% |
| 采样步数 | 9.5 | 4 - 20 | 12 | 59% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 12 | 100% |
| 采样算法 | euler | - | 12 | 83% |
| 调度器 | simple | - | 12 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1052，观测区间 720 - 1920，12 个样本
- 高度 中位数 1536，观测区间 1024 - 1920，12 个样本
- 采样步数 中位数 9.5，观测区间 4 - 20，12 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，12 个样本，一致性 83%
- 调度器 最常用 simple，12 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 高发问题（6/12 个样本）：Steps较低可能导致细节不足
