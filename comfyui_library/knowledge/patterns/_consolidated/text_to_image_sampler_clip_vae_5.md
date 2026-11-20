---
name: text_to_image_sampler_clip_vae_5
type: Text To Image
frequency: 19
level: moderate
coverage: 0.994158
common_nodes: [CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, VAEDecode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/test1_2081667502253371394.json, 图片生成/文生图/vibex-simple-txt2img-workflow_2101489827303743489.json, 图片生成/文生图/workflow_Qwen_image_character_2033556347710607362.json, 图片生成/文生图/【AI小王子】10.文生图工作流_2046802677945868290.json, 图片生成/文生图/【琉梦】基础文生图__光辉illustrious文生图__动漫文生图__极简_2044808427158904833.json, 图片生成/文生图/【遇见AI】SD1.5文生图基础工作流_2011308014015352833.json, 图片生成/文生图/【遇见AI】SD1.5版LCM lora_2016051847970168833.json, 图片生成/文生图/【遇见AI】SDXL版LCM lora_2016057417993293826.json, 图片生成/文生图/冷冬圣诞夜漫画风_2096584608396693506.json, 图片生成/文生图/别墅庭院风_2063986622978420738.json, 图片生成/文生图/动漫_2070124661043716097.json, 图片生成/文生图/动漫女孩_2101663777623207938.json, 图片生成/文生图/动漫美少女_2072470520804761601.json, 图片生成/文生图/卡通3D形象生成器_1916402793215623169.json, 图片生成/文生图/咖啡馆漫画风_2101655459567591426.json, 图片生成/文生图/场景生成_2039074931979325441.json, 图片生成/文生图/基础工作流_1914506513556172801.json, 图片生成/文生图/基础文生图_2013094085589999617.json, 图片生成/文生图/基础文生图_2070347149732306945.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_vae_5

> 由 `engine/knowledge_consolidation` 从 19 个 workflow 归纳得出（图片生成/文生图/test1_2081667502253371394.json、图片生成/文生图/vibex-simple-txt2img-workflow_2101489827303743489.json、图片生成/文生图/workflow_Qwen_image_character_2033556347710607362.json、图片生成/文生图/【AI小王子】10.文生图工作流_2046802677945868290.json、图片生成/文生图/【琉梦】基础文生图__光辉illustrious文生图__动漫文生图__极简_2044808427158904833.json…）

- **类型**：Text To Image
- **样本数**：19
- **可信度**：中等可信
- **平均知识覆盖**：99%

## 共有节点

全部 19 个 workflow 都包含：
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `CheckpointLoaderSimple` —— 18/19 个有
- `Load Lora` —— 2/19 个有
- `VAELoader` —— 2/19 个有
- `CheckpointLoader` —— 1/19 个有
- `RHHiddenNodes` —— 1/19 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 768 | 512 - 1280 | 19 | 70% |
| 高度 | 1024 | 512 - 1920 | 19 | 60% |
| 采样步数 | 20 | 8 - 50 | 19 | 50% |
| Prompt 约束强度(CFG) | 7 | 1.5 - 8 | 19 | 59% |
| 采样算法 | euler | - | 19 | 68% |
| 调度器 | normal | - | 19 | 63% |
| 重绘幅度 | 1 | 1 - 1 | 19 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/19 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 768，观测区间 512 - 1280，19 个样本
- 高度 中位数 1024，观测区间 512 - 1920，19 个样本
- 采样步数 中位数 20，观测区间 8 - 50，19 个样本，取值分散，一致性仅 50%
- Prompt 约束强度(CFG) 中位数 7，观测区间 1.5 - 8，19 个样本
- 采样算法 最常用 euler，19 个样本，一致性 68%
- 调度器 最常用 normal，19 个样本，一致性 63%
- 重绘幅度 中位数 1，观测区间 1 - 1，19 个样本，取值集中（一致性 100%）
