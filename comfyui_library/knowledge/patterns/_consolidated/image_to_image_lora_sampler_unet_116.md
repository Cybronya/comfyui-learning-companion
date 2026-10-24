---
name: image_to_image_lora_sampler_unet_116
type: Image To Image
frequency: 5
level: strong
coverage: 0.777
common_nodes: [CFGNorm, CLIPLoader, CR Prompt Text, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ReferenceLatent, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy promptLine, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/002.Qwen编辑之王020.单图自动多角度_2034850323080159233.json, 图片生成/图生图/Qwen Edit 2511 多景别镜头 13镜（普通版）_2008008936619773954.json, 图片生成/图生图/Qwen-Edit-2511-一键多角度，多场景分镜_2003696921707487234.json, 图片生成/图生图/Qwen-Edit-2511-一键多角度，多场景分镜_2054221184434229250.json, 数字人/数字人/qwen-edit-Lora分镜生图 场景生图_2092240467063824386.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_116

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/002.Qwen编辑之王020.单图自动多角度_2034850323080159233.json、图片生成/图生图/Qwen Edit 2511 多景别镜头 13镜（普通版）_2008008936619773954.json、图片生成/图生图/Qwen-Edit-2511-一键多角度，多场景分镜_2003696921707487234.json、图片生成/图生图/Qwen-Edit-2511-一键多角度，多场景分镜_2054221184434229250.json、数字人/数字人/qwen-edit-Lora分镜生图 场景生图_2092240467063824386.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：78%

## 共有节点

全部 5 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `CR Prompt Text`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ReferenceLatent`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy promptLine`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `INTConstant` —— 4/5 个有
- `JWStringConcat` —— 4/5 个有
- `Qwen3_VQA` —— 4/5 个有
- `Fast Groups Bypasser (rgthree)` —— 3/5 个有
- `PlaySound|pysssss` —— 3/5 个有
- `Text Multiline` —— 3/5 个有
- `CR Prompt List` —— 1/5 个有
- `CR Text` —— 1/5 个有
- `JjkText` —— 1/5 个有
- `Prompt_Edit` —— 1/5 个有
- `ShowText|pysssss` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 5 | 67% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler_ancestral | - | 5 | 60% |
| 调度器 | FlowMatchEulerDiscreteScheduler | - | 5 | 60% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，5 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，5 个样本，一致性 60%
- 调度器 最常用 FlowMatchEulerDiscreteScheduler，5 个样本，一致性 60%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（8/5 个样本）：Steps较低可能导致细节不足
