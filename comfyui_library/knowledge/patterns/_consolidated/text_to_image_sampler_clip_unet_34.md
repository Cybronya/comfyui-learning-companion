---
name: text_to_image_sampler_clip_unet_34
type: Text To Image
frequency: 13
level: moderate
coverage: 0.933846
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Anima+Preview3 动漫生图_2047660287687397377.json, 图片生成/文生图/Anima-3.8B-V1.1文生图_2110281763527417857.json, 图片生成/文生图/Anima-Base1.0 +Lora 芙莉莲（提示词指南）_2058148244718444546.json, 图片生成/文生图/Anima-Base1.0 动漫文生图_2067514380631240706.json, 图片生成/文生图/Anima-Base1.0 动漫文生图（提示词指南）_2057295897054236673.json, 图片生成/文生图/Anima-Base1.0 动漫文生图（提示词指南）_2067497247423680513.json, 图片生成/文生图/Anima_V10-Turbo 10-Step｜10步极速文生图_2079037824149573634.json, 图片生成/文生图/Anima正式版-文生图工作流_2055330143593345026.json, 图片生成/文生图/Anima正式版-文生图工作流_2084627398477303810.json, 图片生成/文生图/Beyond Reality Super Z Image 文生图_2018143805811200001.json, 图片生成/文生图/Qwenimage创意标志logo设计_2055550319697907713.json, 图片生成/文生图/创意卡通logo设计-Qwen image_2015701697498193921.json, 图片生成/文生图/创意卡通logo设计-Qwen image_2082720895461838850.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_34

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/文生图/Anima+Preview3 动漫生图_2047660287687397377.json、图片生成/文生图/Anima-3.8B-V1.1文生图_2110281763527417857.json、图片生成/文生图/Anima-Base1.0 +Lora 芙莉莲（提示词指南）_2058148244718444546.json、图片生成/文生图/Anima-Base1.0 动漫文生图_2067514380631240706.json、图片生成/文生图/Anima-Base1.0 动漫文生图（提示词指南）_2057295897054236673.json…）

- **类型**：Text To Image
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 13 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Int` —— 8/13 个有
- `LoraLoaderModelOnly` —— 7/13 个有
- `ModelSamplingAuraFlow` —— 6/13 个有
- `CR Text` —— 5/13 个有
- `Text` —— 4/13 个有
- `AILab_QwenVL` —— 3/13 个有
- `ImpactSwitch` —— 3/13 个有
- `easy showAnything` —— 3/13 个有
- `CR Text Concatenate` —— 1/13 个有
- `PDRatioSelector` —— 1/13 个有
- `RH_LLMAPI_NODE` —— 1/13 个有
- `easy int` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 512 - 1152 | 13 | 75% |
| 高度 | 1024 | 248 - 1536 | 13 | 57% |
| 采样步数 | 30 | 8 - 50 | 13 | 58% |
| Prompt 约束强度(CFG) | 3.5 | 1 - 4 | 13 | 62% |
| 采样算法 | euler | - | 13 | 54% |
| 调度器 | simple | - | 13 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 13 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 512 - 1152，13 个样本
- 高度 中位数 1024，观测区间 248 - 1536，13 个样本
- 采样步数 中位数 30，观测区间 8 - 50，13 个样本
- Prompt 约束强度(CFG) 中位数 3.5，观测区间 1 - 4，13 个样本
- 采样算法 最常用 euler，13 个样本，一致性 54%
- 调度器 最常用 simple，13 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
