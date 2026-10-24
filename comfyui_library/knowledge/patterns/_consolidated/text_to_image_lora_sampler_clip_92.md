---
name: text_to_image_lora_sampler_clip_92
type: Text To Image
frequency: 14
level: moderate
coverage: 0.880214
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSampler, LoraLoaderModelOnly, ModelSamplingAuraFlow, PathchSageAttentionKJ, SaveImage, VAEDecode, VAELoader, easy cleanGpuUsed]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen 千问文生图_2000589481319202818.json, 图片生成/文生图/Qwen-Image 4步文生图【极速版v2】_1956241572574756865.json, 图片生成/文生图/Qwen-Image8步加速Lora4倍加速文生图支持中文输出堪比Seedream，简直不要太强啦_1953340351912312834.json, 图片生成/文生图/Qwen-文生图+中文字体LORA-极速版_1955571767731523585.json, 图片生成/文生图/Qwen-文生图+中文字体LORA-极速版_1993314920903147522.json, 图片生成/文生图/Qwen千问文生图-动漫短剧_1979863423804674049.json, 图片生成/文生图/光影织就的半透明 3D 模型（小红书爆款头像）_2065372132481265665.json, 图片生成/文生图/文生图+饮品海报LORA-懒人版_2066105345424060418.json, 图片生成/文生图/文生图+饮品海报LORA-懒人版_2069068593173721090.json, 图片生成/文生图/最强书法字体_2086663263693131777.json, 图片生成/文生图/最新书法字Qwen_1959956985607303170.json, 图片生成/文生图/水果文生图的半透明 3D 模型_2069601709332197377.json, 图片生成/文生图/海报_1994037125291114497.json, 图片生成/文生图/火锅海报：漫锅烟火_1970876758574698497.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_92

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（图片生成/文生图/Qwen 千问文生图_2000589481319202818.json、图片生成/文生图/Qwen-Image 4步文生图【极速版v2】_1956241572574756865.json、图片生成/文生图/Qwen-Image8步加速Lora4倍加速文生图支持中文输出堪比Seedream，简直不要太强啦_1953340351912312834.json、图片生成/文生图/Qwen-文生图+中文字体LORA-极速版_1955571767731523585.json、图片生成/文生图/Qwen-文生图+中文字体LORA-极速版_1993314920903147522.json…）

- **类型**：Text To Image
- **样本数**：14
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 14 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PathchSageAttentionKJ`
- `SaveImage`
- `VAEDecode`
- `VAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `JjkText` —— 13/14 个有
- `LoraLoader` —— 12/14 个有
- `UNETLoader` —— 12/14 个有
- `ImpactSwitch` —— 11/14 个有
- `Int` —— 11/14 个有
- `CR Text Concatenate` —— 6/14 个有
- `PreviewImage` —— 2/14 个有
- `TextCombinerTwo` —— 2/14 个有
- `UnetLoaderGGUF` —— 2/14 个有
- `CR SDXL Aspect Ratio` —— 1/14 个有
- `DF_Text_Box` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.8 | 0.4 - 1 | 12 | 81% |
| LoRA 文本强度 | 0.8 | 0.4 - 1 | 12 | 76% |
| 采样步数 | 4 | 4 - 8 | 14 | 76% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 14 | 100% |
| 采样算法 | euler | - | 14 | 86% |
| 调度器 | simple | - | 14 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 14 | 100% |
| 宽度 | 512 | 512 - 800 | 14 | 80% |
| 高度 | 512 | 512 - 1200 | 14 | 60% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 14/14 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- LoRA 模型强度 中位数 0.8，观测区间 0.4 - 1，12 个样本，取值集中（一致性 81%）
- LoRA 文本强度 中位数 0.8，观测区间 0.4 - 1，12 个样本
- 采样步数 中位数 4，观测区间 4 - 8，14 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，14 个样本，一致性 86%
- 调度器 最常用 simple，14 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 宽度 中位数 512，观测区间 512 - 800，14 个样本，取值集中（一致性 80%）
- 高度 中位数 512，观测区间 512 - 1200，14 个样本
- 高发问题（14/14 个样本）：Steps较低可能导致细节不足
