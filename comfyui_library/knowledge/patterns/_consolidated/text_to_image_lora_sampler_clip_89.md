---
name: text_to_image_lora_sampler_clip_89
type: Text To Image
frequency: 14
level: moderate
coverage: 0.928643
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Krea2-二次元模型总控-云端版_2095727543704965121.json, 图片生成/文生图/Krea2-云上天宫_2095745487965081602.json, 图片生成/文生图/krea2-trubo-青绿水彩风格+水墨风格+光影效果彩色极简素描风格_2069757903887753218.json, 图片生成/文生图/krea2-多风格手动文生图_2072150661021659138.json, 图片生成/文生图/krea2-多风格手动文生图_2085615556467716097.json, 图片生成/文生图/krea2-多风格手动文生图_2085620387404140546.json, 图片生成/文生图/krea2-多风格手动文生图_2085623883734020097.json, 图片生成/文生图/krea2-多风格手动文生图_2086705686548926466.json, 图片生成/文生图/krea2-多风格手动文生图_2086707015786786817.json, 图片生成/文生图/krea2-多风格手动文生图_2086728368371884033.json, 图片生成/文生图/krea2-多风格手动文生图_2086731072540336130.json, 图片生成/文生图/krea2_最强多风格开源模型！效果堪比闭源模型！_2070422393184677890.json, 图片生成/文生图/最强风格化开源模型-krea2！效果堪比闭源模型！_2070143827293335554.json, 图片生成/文生图/风格化开源模型krea2_2073230611573207041.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_89

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（图片生成/文生图/Krea2-二次元模型总控-云端版_2095727543704965121.json、图片生成/文生图/Krea2-云上天宫_2095745487965081602.json、图片生成/文生图/krea2-trubo-青绿水彩风格+水墨风格+光影效果彩色极简素描风格_2069757903887753218.json、图片生成/文生图/krea2-多风格手动文生图_2072150661021659138.json、图片生成/文生图/krea2-多风格手动文生图_2085615556467716097.json…）

- **类型**：Text To Image
- **样本数**：14
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 14 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 13/14 个有
- `Label (rgthree)` —— 11/14 个有
- `TTResolutionSelector` —— 11/14 个有
- `Fast Groups Bypasser (rgthree)` —— 10/14 个有
- `忽略多组孤海` —— 3/14 个有
- `PreviewImage` —— 2/14 个有
- `PrimitiveInt` —— 2/14 个有
- `PrimitiveStringMultiline` —— 2/14 个有
- `ImageConcatMulti` —— 1/14 个有
- `StringConcatenate` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | 512 - 2560 | 14 | 26% |
| 高度 | 512 | 512 - 1984 | 14 | 33% |
| 采样步数 | 8 | 8 - 8 | 14 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 14 | 100% |
| 采样算法 | euler | - | 14 | 100% |
| 调度器 | simple | - | 14 | 93% |
| 重绘幅度 | 1 | 1 - 1 | 14 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 29/14 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 512，观测区间 512 - 2560，14 个样本，取值分散，一致性仅 26%
- 高度 中位数 512，观测区间 512 - 1984，14 个样本，取值分散，一致性仅 33%
- 采样步数 中位数 8，观测区间 8 - 8，14 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，14 个样本，一致性 100%
- 调度器 最常用 simple，14 个样本，一致性 93%
- 重绘幅度 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 高发问题（29/14 个样本）：Steps较低可能导致细节不足
