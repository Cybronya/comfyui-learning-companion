---
name: text_to_image_sampler_clip_unet_28
type: Text To Image
frequency: 16
level: weak
coverage: 0.930188
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Anima+Preview3 动漫生图_2047660287687397377.json, 图片生成/文生图/Anima-3.8B-V1.1文生图_2110281763527417857.json, 图片生成/文生图/Anima-Base1.0 +Lora 芙莉莲（提示词指南）_2058148244718444546.json, 图片生成/文生图/Anima-Base1.0 动漫文生图_2067514380631240706.json, 图片生成/文生图/Anima-Base1.0 动漫文生图（提示词指南）_2057295897054236673.json, 图片生成/文生图/Anima-Base1.0 动漫文生图（提示词指南）_2067497247423680513.json, 图片生成/文生图/Beyond Reality Super Z Image 文生图_2018143805811200001.json, 图片生成/文生图/Qwen Image 2512文生图_2016788115049947137.json, 图片生成/文生图/Qwen Image 2512文生图_2039178765472899073.json, 图片生成/文生图/Qwen Image 2512文生图_2047443732449988609.json, 图片生成/文生图/Qwen Image 2512文生图_2048284006793351169.json, 图片生成/文生图/Qwen Image 2512文生图_2048288138644164609.json, 图片生成/文生图/Qwen Image 2512文生图_2055456154658066434.json, 图片生成/文生图/Qwenimage创意标志logo设计_2055550319697907713.json, 图片生成/文生图/创意卡通logo设计-Qwen image_2015701697498193921.json, 图片生成/文生图/创意卡通logo设计-Qwen image_2082720895461838850.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_28

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（图片生成/文生图/Anima+Preview3 动漫生图_2047660287687397377.json、图片生成/文生图/Anima-3.8B-V1.1文生图_2110281763527417857.json、图片生成/文生图/Anima-Base1.0 +Lora 芙莉莲（提示词指南）_2058148244718444546.json、图片生成/文生图/Anima-Base1.0 动漫文生图_2067514380631240706.json、图片生成/文生图/Anima-Base1.0 动漫文生图（提示词指南）_2057295897054236673.json…）

- **类型**：Text To Image
- **样本数**：16
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：93%

## 共有节点

全部 16 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Int` —— 14/16 个有
- `LoraLoaderModelOnly` —— 12/16 个有
- `ModelSamplingAuraFlow` —— 10/16 个有
- `ImpactSwitch` —— 9/16 个有
- `CFGNorm` —— 6/16 个有
- `CR Text` —— 5/16 个有
- `Text` —— 4/16 个有
- `AILab_QwenVL` —— 3/16 个有
- `easy showAnything` —— 3/16 个有
- `CR Text Concatenate` —— 1/16 个有
- `CompressImages` —— 1/16 个有
- `RH_LLMAPI_NODE` —— 1/16 个有
- `easy int` —— 1/16 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | 512 - 1152 | 16 | 64% |
| 高度 | 512 | 512 - 1536 | 16 | 55% |
| 采样步数 | 20 | 8 - 50 | 16 | 36% |
| Prompt 约束强度(CFG) | 2.25 | 1 - 4 | 16 | 42% |
| 采样算法 | euler | - | 16 | 69% |
| 调度器 | simple | - | 16 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 16 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/16 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 512，观测区间 512 - 1152，16 个样本
- 高度 中位数 512，观测区间 512 - 1536，16 个样本
- 采样步数 中位数 20，观测区间 8 - 50，16 个样本，取值分散，一致性仅 36%
- Prompt 约束强度(CFG) 中位数 2.25，观测区间 1 - 4，16 个样本，取值分散，一致性仅 42%
- 采样算法 最常用 euler，16 个样本，一致性 69%
- 调度器 最常用 simple，16 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，16 个样本，取值集中（一致性 100%）
