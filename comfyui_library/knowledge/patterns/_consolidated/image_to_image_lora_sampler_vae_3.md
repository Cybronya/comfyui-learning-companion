---
name: image_to_image_lora_sampler_vae_3
type: Image To Image
frequency: 18
level: strong
coverage: 0.860889
common_nodes: [CFGNorm, CLIPLoader, INTConstant, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ReferenceLatent, SaveImage, TextEncodeQwenImageEditPlus, VAEDecode, VAEEncode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/QWEN-2511-单图编辑_2034569294645829633.json, 图片生成/图生图/Qwen 2511 人物多角度_2006195322162257922.json, 图片生成/图生图/Qwen Edit 2511 多景别镜头 人物一致性 Qwen-Edit-2511_2008163925614923777.json, 图片生成/图生图/Qwen Edit 2511 多景别镜头 人物一致性 Qwen-Edit-2511_2008170111630319618.json, 图片生成/图生图/Qwen-Edit-2511多视角批量出图_2007857356884942850.json, 图片生成/图生图/Qwen-EditPuls2026人物一致+多景镜头_2008018510336757762.json, 图片生成/图生图/QwenEditPro人物一致+多景镜头_2008728248536010754.json, 图片生成/图生图/人物一致性-多角度拍摄-Qwen-Edit_2008006545811968002.json, 图片生成/图生图/多效果镜头生成_2047203964155863042.json, 图片生成/图生图/多景别镜头+人物一致性-Qwen-Edit-2511_2005167400913956866.json, 图片生成/图生图/多景别镜头+人物一致性-Qwen-Edit-2511_2015609642864353282.json, 图片生成/图生图/多景别镜头+人物一致性-Qwen-Edit-2511_2016403566423973890.json, 图片生成/图生图/多景别镜头+人物一致性-Qwen-Edit-2511_2026173155269681154.json, 图片生成/图生图/多景别镜头+人物一致性-Qwen-Edit-2511_2034831330676051970.json, 图片生成/图生图/多景别镜头+人物一致性-Qwen-Edit-2511_2042404283752124417.json, 图片生成/图生图/多景别镜头+人物一致性-亿薪AI_2017302740229165057.json, 图片生成/图生图/多角度镜头+人物一致性-Qwen-Edit-2511 高清图_2027287031117783041.json, 图片生成/图生图/打斗场景+多效果镜头生成-Qwen-Edit-2511_2005094114679025666.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_vae_3

> 由 `engine/knowledge_consolidation` 从 18 个 workflow 归纳得出（图片生成/图生图/QWEN-2511-单图编辑_2034569294645829633.json、图片生成/图生图/Qwen 2511 人物多角度_2006195322162257922.json、图片生成/图生图/Qwen Edit 2511 多景别镜头 人物一致性 Qwen-Edit-2511_2008163925614923777.json、图片生成/图生图/Qwen Edit 2511 多景别镜头 人物一致性 Qwen-Edit-2511_2008170111630319618.json、图片生成/图生图/Qwen-Edit-2511多视角批量出图_2007857356884942850.json…）

- **类型**：Image To Image
- **样本数**：18
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 18 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `INTConstant`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ReferenceLatent`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode`
- `VAEEncode`

**可变部分**（部分 workflow 才有）：
- `UNETLoader` —— 17/18 个有
- `VAELoader` —— 17/18 个有
- `easy promptLine` —— 17/18 个有
- `CR Prompt Text` —— 16/18 个有
- `GetNode` —— 16/18 个有
- `SetNode` —— 16/18 个有
- `easy showAnything` —— 16/18 个有
- `PlaySound|pysssss` —— 13/18 个有
- `Qwen3_VQA` —— 2/18 个有
- `RHHiddenNodes` —— 2/18 个有
- `CheckpointLoaderSimple` —— 1/18 个有
- `DuckHideNode` —— 1/18 个有
- `PreviewImage` —— 1/18 个有
- `easy imageBatchToImageList` —— 1/18 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 6 | 18 | 89% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 18 | 100% |
| 采样算法 | euler_ancestral | - | 18 | 100% |
| 调度器 | FlowMatchEulerDiscreteScheduler | - | 18 | 94% |
| 重绘幅度 | 1 | 1 - 1 | 18 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 18/18 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 6，18 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，18 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，18 个样本，一致性 100%
- 调度器 最常用 FlowMatchEulerDiscreteScheduler，18 个样本，一致性 94%
- 重绘幅度 中位数 1，观测区间 1 - 1，18 个样本，取值集中（一致性 100%）
- 高发问题（18/18 个样本）：Steps较低可能导致细节不足
