---
name: text_to_image_sampler_clip_unet_34
type: Text To Image
frequency: 11
level: moderate
coverage: 0.977727
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/电商生成真实人物图片 MagicWanImage_1991348310250467330.json, 图片生成/文生图/电锯人漫画画风_2100390025178472449.json, 图片生成/文生图/画安-Z-Image基本文生图_2080862730688491521.json, 图片生成/文生图/真实人像Kook_Flux_klein工作流_2019756687074267138.json, 图片生成/文生图/维琳娜·艾嘉德ANIMA专属工作流(图图lora)_2068391183554007042.json, 图片生成/文生图/视频生成-生成人物图片_2012034993660370945.json, 图片生成/文生图/超写实人像生成 Magic-Wan-Image V2_1990394619835944962.json, 图片生成/文生图/造相-Z-Image-Turbo 文生图高清图像_1998205959757553665.json, 图片生成/文生图/闽粤纹样-文生图-纹样模型v1-48G_2022317374753476610.json, 图片生成/文生图/闽粤纹样-文生图-纹样模型v2-48G_2022345848922841089.json, 图片生成/文生图/闽粤纹样-文生图-纹样模型v3-48G_2022344333025878018.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_34

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/文生图/电商生成真实人物图片 MagicWanImage_1991348310250467330.json、图片生成/文生图/电锯人漫画画风_2100390025178472449.json、图片生成/文生图/画安-Z-Image基本文生图_2080862730688491521.json、图片生成/文生图/真实人像Kook_Flux_klein工作流_2019756687074267138.json、图片生成/文生图/维琳娜·艾嘉德ANIMA专属工作流(图图lora)_2068391183554007042.json…）

- **类型**：Text To Image
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：98%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 8/11 个有
- `ModelSamplingAuraFlow` —— 5/11 个有
- `Int` —— 3/11 个有
- `ttN text` —— 3/11 个有
- `ModelSamplingSD3` —— 2/11 个有
- `RH_Translator` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1080 | 864 - 1376 | 11 | 89% |
| 高度 | 1536 | 768 - 1920 | 11 | 79% |
| 采样步数 | 8 | 7 - 45 | 11 | 20% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 11 | 35% |
| 采样算法 | euler | - | 11 | 73% |
| 调度器 | simple | - | 11 | 55% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1080，观测区间 864 - 1376，11 个样本，取值集中（一致性 89%）
- 高度 中位数 1536，观测区间 768 - 1920，11 个样本
- 采样步数 中位数 8，观测区间 7 - 45，11 个样本，取值分散，一致性仅 20%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，11 个样本，取值分散，一致性仅 35%
- 采样算法 最常用 euler，11 个样本，一致性 73%
- 调度器 最常用 simple，11 个样本，一致性 55%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 高发问题（7/11 个样本）：Steps较低可能导致细节不足
