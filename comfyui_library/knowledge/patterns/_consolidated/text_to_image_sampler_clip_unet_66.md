---
name: text_to_image_sampler_clip_unet_66
type: Text To Image
frequency: 10
level: moderate
coverage: 0.9692
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Krea2_反推生图_自动尺寸_2087151855494328321.json, 图片生成/文生图/Z-iamge文生图千问VL反推无需提示词自动文生图_1993913264711155713.json, 图片生成/文生图/Z-image 超清快速30秒文生图 省时省币_2038518587316506625.json, 图片生成/文生图/Z-image 超清快速文生图_2008571327392784386.json, 图片生成/文生图/Z-image-turbo 2.5D奶油风格生图Lora_2055258113829294081.json, 图片生成/文生图/Z-image建筑文生图工作流_1993985159852654594.json, 图片生成/文生图/boogu turbo反推文生图_2070395337566679041.json, 图片生成/文生图/boogu turbo反推文生图_2070430959291428865.json, 图片生成/文生图/boogu turbo反推文生图无需提示词_2070351358628294658.json, 图片生成/文生图/boogu turbo反推文生图无需提示词_2070418685847760898.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_66

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/文生图/Krea2_反推生图_自动尺寸_2087151855494328321.json、图片生成/文生图/Z-iamge文生图千问VL反推无需提示词自动文生图_1993913264711155713.json、图片生成/文生图/Z-image 超清快速30秒文生图 省时省币_2038518587316506625.json、图片生成/文生图/Z-image 超清快速文生图_2008571327392784386.json、图片生成/文生图/Z-image-turbo 2.5D奶油风格生图Lora_2055258113829294081.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 8/10 个有
- `AILab_QwenVL` —— 7/10 个有
- `LoadImage` —— 7/10 个有
- `CR Text` —— 6/10 个有
- `LoraLoaderModelOnly` —— 5/10 个有
- `GetImageSize+` —— 1/10 个有
- `ImageScaleToTotalPixels` —— 1/10 个有
- `RTXVideoSuperResolution` —— 1/10 个有
- `Text Concatenate` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 10 | 10 | 89% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 10 | 100% |
| 采样算法 | euler | - | 10 | 90% |
| 调度器 | simple | - | 10 | 90% |
| 重绘幅度 | 1 | 0.58 - 1 | 10 | 87% |
| 宽度 | 1024 | 512 - 2048 | 10 | 67% |
| 高度 | 1536 | 512 - 1920 | 10 | 76% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 10，10 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，10 个样本，一致性 90%
- 调度器 最常用 simple，10 个样本，一致性 90%
- 重绘幅度 中位数 1，观测区间 0.58 - 1，10 个样本，取值集中（一致性 87%）
- 宽度 中位数 1024，观测区间 512 - 2048，10 个样本
- 高度 中位数 1536，观测区间 512 - 1920，10 个样本
- 高发问题（7/10 个样本）：Steps较低可能导致细节不足
