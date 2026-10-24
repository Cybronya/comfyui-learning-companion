---
name: text_to_image_lora_sampler_clip_91
type: Text To Image
frequency: 14
level: moderate
coverage: 0.980786
common_nodes: [CLIPTextEncode, EmptyLatentImage, KSampler, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Flux.室内效果图生成_2055177379538063361.json, 图片生成/文生图/Krea-2-Turbo 文生图_2071991072359796737.json, 图片生成/文生图/Krea2-turbo文生图赛璐璐平涂动漫场景_2085270687903731714.json, 图片生成/文生图/Krea2-turbo文生图赛璐璐平涂动漫风格_2084650330515660801.json, 图片生成/文生图/Krea2动漫人物写实复古风工作流_2073834007481110529.json, 图片生成/文生图/Krea2图图工作流_2072525906350006273.json, 图片生成/文生图/Krea2图图文生图工作流_2095107374737616898.json, 图片生成/文生图/Krea2文生图工作流_2089571875075747842.json, 图片生成/文生图/Z-Image Re-Turbo_2073289018476941314.json, 图片生成/文生图/Z-Image-Turbo 身材优化+丰满LoRA_2001971849082859521.json, 图片生成/文生图/Z-image文生图（昆昆）_2044213811187556353.json, 图片生成/文生图/krea2_最强多风格开源模型！效果堪比闭源模型！_2070422393184677890.json, 图片生成/文生图/最强风格化开源模型-krea2！效果堪比闭源模型！_2070143827293335554.json, 图片生成/文生图/风格化开源模型krea2_2073230611573207041.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_91

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（图片生成/文生图/Flux.室内效果图生成_2055177379538063361.json、图片生成/文生图/Krea-2-Turbo 文生图_2071991072359796737.json、图片生成/文生图/Krea2-turbo文生图赛璐璐平涂动漫场景_2085270687903731714.json、图片生成/文生图/Krea2-turbo文生图赛璐璐平涂动漫风格_2084650330515660801.json、图片生成/文生图/Krea2动漫人物写实复古风工作流_2073834007481110529.json…）

- **类型**：Text To Image
- **样本数**：14
- **可信度**：中等可信
- **平均知识覆盖**：98%

## 共有节点

全部 14 个 workflow 都包含：
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 13/14 个有
- `ConditioningZeroOut` —— 12/14 个有
- `Label (rgthree)` —— 3/14 个有
- `TTResolutionSelector` —— 3/14 个有
- `忽略多组孤海` —— 3/14 个有
- `BaiduTranslateNode` —— 1/14 个有
- `DualCLIPLoader` —— 1/14 个有
- `LatentSwitch` —— 1/14 个有
- `Text` —— 1/14 个有
- `ttN concat` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 20 | 14 | 68% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 14 | 100% |
| 采样算法 | euler | - | 14 | 71% |
| 调度器 | simple | - | 14 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 14 | 100% |
| 宽度 | 1052 | 512 - 1920 | 14 | 62% |
| 高度 | 1260 | 512 - 1920 | 14 | 54% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 19/14 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 20，14 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，14 个样本，一致性 71%
- 调度器 最常用 simple，14 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 宽度 中位数 1052，观测区间 512 - 1920，14 个样本
- 高度 中位数 1260，观测区间 512 - 1920，14 个样本
- 高发问题（19/14 个样本）：Steps较低可能导致细节不足
