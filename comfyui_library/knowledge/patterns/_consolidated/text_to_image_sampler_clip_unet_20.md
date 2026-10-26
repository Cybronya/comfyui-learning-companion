---
name: text_to_image_sampler_clip_unet_20
type: Text To Image
frequency: 19
level: weak
coverage: 0.966316
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Krea2_反推生图_自动尺寸_2087151855494328321.json, 图片生成/文生图/Krea2动漫人物写实复古风工作流_2073834007481110529.json, 图片生成/文生图/Krea2图图工作流_2072525906350006273.json, 图片生成/文生图/Krea2图图文生图工作流_2095107374737616898.json, 图片生成/文生图/Krea2文生图工作流_2089571875075747842.json, 图片生成/文生图/Z-Image-Turbo + Lora 文生图_2008180292552495105.json, 图片生成/文生图/Z-iamge文生图千问VL反推无需提示词自动文生图_1993913264711155713.json, 图片生成/文生图/Z-image-turbo 2.5D奶油风格生图Lora_2055258113829294081.json, 图片生成/文生图/Z-image-turbo基础文生图【用于绘世comfyui批量管理系统】_2089190207693344769.json, 图片生成/文生图/Z-image建筑文生图工作流_1993985159852654594.json, 图片生成/文生图/boogu turbo反推文生图_2070395337566679041.json, 图片生成/文生图/boogu turbo反推文生图_2070430959291428865.json, 图片生成/文生图/boogu turbo反推文生图无需提示词_2070351358628294658.json, 图片生成/文生图/boogu turbo反推文生图无需提示词_2070418685847760898.json, 图片生成/文生图/krea turbo反推文生图_2070393483688505346.json, 图片生成/文生图/krea2反推文生图_2070420567852937217.json, 图片生成/文生图/krea2反推文生图_2070466486245879810.json, 图片生成/文生图/krea2反推文生图无需提示词_2070349490783088642.json, 图片生成/文生图/ovis image文生图-图生图海报_2000224221550739457.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_20

> 由 `engine/knowledge_consolidation` 从 19 个 workflow 归纳得出（图片生成/文生图/Krea2_反推生图_自动尺寸_2087151855494328321.json、图片生成/文生图/Krea2动漫人物写实复古风工作流_2073834007481110529.json、图片生成/文生图/Krea2图图工作流_2072525906350006273.json、图片生成/文生图/Krea2图图文生图工作流_2095107374737616898.json、图片生成/文生图/Krea2文生图工作流_2089571875075747842.json…）

- **类型**：Text To Image
- **样本数**：19
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：97%

## 共有节点

全部 19 个 workflow 都包含：
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
- `AILab_QwenVL` —— 12/19 个有
- `LoadImage` —— 12/19 个有
- `LoraLoaderModelOnly` —— 8/19 个有
- `CR Text` —— 6/19 个有
- `RTXVideoSuperResolution` —— 2/19 个有
- `GetImageSize+` —— 1/19 个有
- `ImageScaleToTotalPixels` —— 1/19 个有
- `Text Concatenate` —— 1/19 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 50 | 19 | 14% |
| Prompt 约束强度(CFG) | 1 | 1 - 5 | 19 | 26% |
| 采样算法 | euler | - | 19 | 53% |
| 调度器 | simple | - | 19 | 95% |
| 重绘幅度 | 1 | 0.58 - 1 | 19 | 90% |
| 宽度 | 1024 | 512 - 2048 | 19 | 72% |
| 高度 | 1536 | 512 - 1920 | 19 | 74% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 13/19 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 50，19 个样本，取值分散，一致性仅 14%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 5，19 个样本，取值分散，一致性仅 26%
- 采样算法 最常用 euler，19 个样本，一致性 53%
- 调度器 最常用 simple，19 个样本，一致性 95%
- 重绘幅度 中位数 1，观测区间 0.58 - 1，19 个样本，取值集中（一致性 90%）
- 宽度 中位数 1024，观测区间 512 - 2048，19 个样本
- 高度 中位数 1536，观测区间 512 - 1920，19 个样本
- 高发问题（13/19 个样本）：Steps较低可能导致细节不足
