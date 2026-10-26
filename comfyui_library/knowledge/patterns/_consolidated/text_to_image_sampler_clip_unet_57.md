---
name: text_to_image_sampler_clip_unet_57
type: Text To Image
frequency: 11
level: moderate
coverage: 0.845
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/FLUX2-双图融合_1993897229222084609.json, 图片生成/文生图/Krea2 Turbo 基础文生图_2070831897437097985.json, 图片生成/文生图/Krea2_2070039943791071234.json, 图片生成/文生图/Qwen-image-2.1-文生图_2101847911167520770.json, 图片生成/文生图/Z-IMAGE：文生图，一段话生出好看的美图！_1993890310312968194.json, 图片生成/文生图/Z-Image-Turbo-BF16文生图_2078377958095544321.json, 图片生成/文生图/Z-Image：文生图，极速光影，将文字转化为超现实影像！_1993869296981966849.json, 图片生成/文生图/Z-image文生图_1993984303098953730.json, 图片生成/文生图/最强模型Z-Image：超写实生图_1993922948425777153.json, 图片生成/文生图/百度大模型 文生图ERNIE-image-turbo 人物一致性 自然真实_2044640662099857410.json, 图片生成/文生图/百度大模型ERNIE-image-turbo-文生图  人物一致性 自然真实_2044656791585296386.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_57

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/文生图/FLUX2-双图融合_1993897229222084609.json、图片生成/文生图/Krea2 Turbo 基础文生图_2070831897437097985.json、图片生成/文生图/Krea2_2070039943791071234.json、图片生成/文生图/Qwen-image-2.1-文生图_2101847911167520770.json、图片生成/文生图/Z-IMAGE：文生图，一段话生出好看的美图！_1993890310312968194.json…）

- **类型**：Text To Image
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 11 个 workflow 都包含：
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
- `PreviewImage` —— 9/11 个有
- `JWInteger` —— 5/11 个有
- `JjkText` —— 5/11 个有
- `RH_LLMAPI_NODE` —— 4/11 个有
- `ShowText|pysssss` —— 3/11 个有
- `RH_Translator` —— 2/11 个有
- `CR Prompt Text` —— 1/11 个有
- `Int` —— 1/11 个有
- `QwenImage21Cache` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 8 - 25 | 11 | 56% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 11 | 100% |
| 采样算法 | euler | - | 11 | 91% |
| 调度器 | simple | - | 11 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |
| 宽度 | 1080 | 720 - 1280 | 11 | 84% |
| 高度 | 1920 | 720 - 1920 | 11 | 74% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 8 - 25，11 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，11 个样本，一致性 91%
- 调度器 最常用 simple，11 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 宽度 中位数 1080，观测区间 720 - 1280，11 个样本，取值集中（一致性 84%）
- 高度 中位数 1920，观测区间 720 - 1920，11 个样本
