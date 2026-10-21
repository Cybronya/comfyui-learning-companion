---
name: text_to_image_lora_sampler_clip_86
type: Text To Image
frequency: 11
level: strong
coverage: 0.847182
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, LoraLoaderModelOnly, ModelSamplingAuraFlow, PathchSageAttentionKJ, UNETLoader, VAEDecode, VAELoader, easy cleanGpuUsed]
problems: [Steps较低可能导致细节不足]
missing: [CR Text, easy cleanGpuUsed, ttN concat, CR Text Concatenate]
members: [图片生成/文生图/1965625145698209793.json, 图片生成/文生图/1970876758574698497.json, 图片生成/文生图/1975417957952172034.json, 图片生成/文生图/1988803647096098817.json, 图片生成/文生图/Qwen-文生图+中文字体LORA-极速版_1993314920903147522.json, 图片生成/文生图/光影织就的半透明 3D 模型（小红书爆款头像）_2065372132481265665.json, 图片生成/文生图/文生图+饮品海报LORA-懒人版_2066105345424060418.json, 图片生成/文生图/文生图+饮品海报LORA-懒人版_2069068593173721090.json, 图片生成/文生图/最强书法字体_2086663263693131777.json, 图片生成/文生图/水果文生图的半透明 3D 模型_2069601709332197377.json, 图片生成/文生图/海报_1994037125291114497.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_86

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/文生图/1965625145698209793.json、图片生成/文生图/1970876758574698497.json、图片生成/文生图/1975417957952172034.json、图片生成/文生图/1988803647096098817.json、图片生成/文生图/Qwen-文生图+中文字体LORA-极速版_1993314920903147522.json…）

- **类型**：Text To Image
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PathchSageAttentionKJ`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 10/11 个有
- `Int` —— 10/11 个有
- `JjkText` —— 10/11 个有
- `SaveImage` —— 10/11 个有
- `ImpactSwitch` —— 9/11 个有
- `LoraLoader` —— 7/11 个有
- `CR Text Concatenate` —— 5/11 个有
- `RH_LLMAPI_NODE` —— 2/11 个有
- `CR Text` —— 1/11 个有
- `SaveImagePlus` —— 1/11 个有
- `ShowText` —— 1/11 个有
- `easy showAnything` —— 1/11 个有
- `ttN concat` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 11 | 74% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 11 | 100% |
| 采样算法 | euler | - | 11 | 100% |
| 调度器 | simple | - | 11 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |
| 宽度 | 512 | 512 - 800 | 11 | 85% |
| 高度 | 512 | 512 - 1200 | 11 | 66% |
| LoRA 模型强度 | 0.8 | 0.8 - 1 | 7 | 92% |
| LoRA 文本强度 | 0.8 | 0.8 - 1 | 7 | 92% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，11 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，11 个样本，一致性 100%
- 调度器 最常用 simple，11 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 宽度 中位数 512，观测区间 512 - 800，11 个样本，取值集中（一致性 85%）
- 高度 中位数 512，观测区间 512 - 1200，11 个样本
- LoRA 模型强度 中位数 0.8，观测区间 0.8 - 1，7 个样本，取值集中（一致性 92%）
- LoRA 文本强度 中位数 0.8，观测区间 0.8 - 1，7 个样本，取值集中（一致性 92%）
- 高发问题（11/11 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：CR Text、easy cleanGpuUsed、ttN concat、CR Text Concatenate
