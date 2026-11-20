---
name: text_to_image_sampler_clip_unet_31
type: Text To Image
frequency: 15
level: moderate
coverage: 0.922067
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Anima+Preview3 动漫生图_2047660287687397377.json, 图片生成/文生图/Anima-3.8B-V1.1文生图_2110281763527417857.json, 图片生成/文生图/Anima-Base1.0 +Lora 芙莉莲（提示词指南）_2058148244718444546.json, 图片生成/文生图/Anima-Base1.0 动漫文生图_2067514380631240706.json, 图片生成/文生图/Anima-Base1.0 动漫文生图（提示词指南）_2057295897054236673.json, 图片生成/文生图/Anima-Base1.0 动漫文生图（提示词指南）_2067497247423680513.json, 图片生成/文生图/Anima正式版-文生图工作流_2055330143593345026.json, 图片生成/文生图/Anima正式版-文生图工作流_2084627398477303810.json, 图片生成/文生图/Anima正式版-文生图工作流个人自用_2076592631471230977.json, 图片生成/文生图/Beyond Reality Super Z Image 文生图_2018143805811200001.json, 图片生成/文生图/Qwenimage创意标志logo设计_2055550319697907713.json, 图片生成/文生图/创意卡通logo设计-Qwen image_2015701697498193921.json, 图片生成/文生图/创意卡通logo设计-Qwen image_2082720895461838850.json, 平台全量/logo设计-LOGO-图形LOGO-标志设计-创意LOGO平面设计 创意卡通logo设计 Qwen_2016402061209903106.json, 平台全量/卡通极简logo：一键生成工作流_2000020015850061826.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_31

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（图片生成/文生图/Anima+Preview3 动漫生图_2047660287687397377.json、图片生成/文生图/Anima-3.8B-V1.1文生图_2110281763527417857.json、图片生成/文生图/Anima-Base1.0 +Lora 芙莉莲（提示词指南）_2058148244718444546.json、图片生成/文生图/Anima-Base1.0 动漫文生图_2067514380631240706.json、图片生成/文生图/Anima-Base1.0 动漫文生图（提示词指南）_2057295897054236673.json…）

- **类型**：Text To Image
- **样本数**：15
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 15 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Int` —— 10/15 个有
- `ModelSamplingAuraFlow` —— 9/15 个有
- `LoraLoaderModelOnly` —— 8/15 个有
- `Text` —— 6/15 个有
- `CR Text` —— 5/15 个有
- `ImpactSwitch` —— 5/15 个有
- `easy showAnything` —— 5/15 个有
- `AILab_QwenVL` —— 4/15 个有
- `RH_LLMAPI_NODE` —— 2/15 个有
- `CR Text Concatenate` —— 1/15 个有
- `easy int` —— 1/15 个有
- `easy seed` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 512 - 1152 | 15 | 71% |
| 高度 | 1024 | 512 - 1536 | 15 | 59% |
| 采样步数 | 30 | 8 - 50 | 15 | 68% |
| Prompt 约束强度(CFG) | 3.5 | 1 - 4 | 15 | 71% |
| 采样算法 | euler | - | 15 | 53% |
| 调度器 | simple | - | 15 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 15 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/15 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 512 - 1152，15 个样本
- 高度 中位数 1024，观测区间 512 - 1536，15 个样本
- 采样步数 中位数 30，观测区间 8 - 50，15 个样本
- Prompt 约束强度(CFG) 中位数 3.5，观测区间 1 - 4，15 个样本
- 采样算法 最常用 euler，15 个样本，一致性 53%
- 调度器 最常用 simple，15 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
