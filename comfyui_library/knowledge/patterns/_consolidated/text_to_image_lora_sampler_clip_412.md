---
name: text_to_image_lora_sampler_clip_412
type: Text To Image
frequency: 5
level: strong
coverage: 0.8816
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen Image 2.1文生图处理生成工具_2102470456296169473.json, 图片生成/文生图/Qwen Image 2.1文生图处理生成工具_2102510005793673217.json, 图片生成/文生图/Qwen Image 2.1文生图处理生成工具_2102545063422283778.json, 图片生成/文生图/Qwen Image 2.1文生图工作流，最强开源模型中文提示词直接出图_2102861587425091586.json, 图片生成/文生图/Qwen image 2.1文生图基础款｜角色设计海报制作｜文字直出创意图_2112075461353365506.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_412

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/Qwen Image 2.1文生图处理生成工具_2102470456296169473.json、图片生成/文生图/Qwen Image 2.1文生图处理生成工具_2102510005793673217.json、图片生成/文生图/Qwen Image 2.1文生图处理生成工具_2102545063422283778.json、图片生成/文生图/Qwen Image 2.1文生图工作流，最强开源模型中文提示词直接出图_2102861587425091586.json、图片生成/文生图/Qwen image 2.1文生图基础款｜角色设计海报制作｜文字直出创意图_2112075461353365506.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `TextGenerateLTX2Prompt` —— 4/5 个有
- `easy showAnything` —— 4/5 个有
- `ResolutionSelector` —— 3/5 个有
- `SaveImageAdvanced` —— 3/5 个有
- `Text` —— 2/5 个有
- `CR Text Concatenate` —— 1/5 个有
- `ComfySwitchNode` —— 1/5 个有
- `DF_Text_Box` —— 1/5 个有
- `GoohaiRatioAndResolution` —— 1/5 个有
- `ImpactSwitch` —— 1/5 个有
- `RH_LLMAPI_Pro_Node` —— 1/5 个有
- `Text Multiline` —— 1/5 个有
- `easy ifElse` —— 1/5 个有
- `布尔孤海` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 5 | 100% |
| 高度 | 80 | 80 - 80 | 5 | 100% |
| 采样步数 | 4 | 4 - 4 | 5 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 5 | 100% |
| 采样算法 | er_sde | - | 5 | 100% |
| 调度器 | beta | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，5 个样本，一致性 100%
- 调度器 最常用 beta，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
