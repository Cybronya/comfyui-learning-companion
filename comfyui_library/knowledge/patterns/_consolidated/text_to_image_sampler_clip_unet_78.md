---
name: text_to_image_sampler_clip_unet_78
type: Text To Image
frequency: 6
level: strong
coverage: 0.842
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, FluxKVCache, ImageScaleToTotalPixels, ImpactSwitch, Int, JjkShowText, KSampler, PreviewImage, SaveImage, Text Multiline, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Krea 2 半梦叠影的幻觉艺术文生图_2074468255678418946.json, 图片生成/文生图/Krea 2 的叠影幻觉艺术_2077750687034859522.json, 图片生成/文生图/Krea2 胶片影像：输入描述词，一键复刻色偏、光晕与颗粒_2075134670349619201.json, 图片生成/文生图/剪映叠影效果：Krea 2 的幻觉艺术_2103381595498569729.json, 图片生成/文生图/半梦叠影：Krea 2 的幻觉艺术_2071797017155817473.json, 图片生成/文生图/半梦叠影：Krea 2 的幻觉艺术_2083810829476122625.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_78

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/Krea 2 半梦叠影的幻觉艺术文生图_2074468255678418946.json、图片生成/文生图/Krea 2 的叠影幻觉艺术_2077750687034859522.json、图片生成/文生图/Krea2 胶片影像：输入描述词，一键复刻色偏、光晕与颗粒_2075134670349619201.json、图片生成/文生图/剪映叠影效果：Krea 2 的幻觉艺术_2103381595498569729.json、图片生成/文生图/半梦叠影：Krea 2 的幻觉艺术_2071797017155817473.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `FluxKVCache`
- `ImageScaleToTotalPixels`
- `ImpactSwitch`
- `Int`
- `JjkShowText`
- `KSampler`
- `PreviewImage`
- `SaveImage`
- `Text Multiline`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LatentColorMatchSimple` —— 5/6 个有
- `RH_LLMAPI_NODE` —— 5/6 个有
- `Text` —— 5/6 个有
- `TextCombinerTwo` —— 5/6 个有
- `CR Prompt Text` —— 1/6 个有
- `INTConstant` —— 1/6 个有
- `LoraLoaderModelOnly` —— 1/6 个有
- `llama_cpp_instruct_adv` —— 1/6 个有
- `llama_cpp_model_loader` —— 1/6 个有
- `llama_cpp_parameters` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 4 - 6 | 6 | 87% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler_ancestral | - | 6 | 100% |
| 调度器 | simple | - | 6 | 83% |
| 重绘幅度 | 0.6 | 0.6 - 1 | 6 | 78% |
| 宽度 | 768 | 768 - 1024 | 6 | 88% |
| 高度 | 1024 | 768 - 1024 | 6 | 90% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 12/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 4 - 6，6 个样本，取值集中（一致性 87%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 83%
- 重绘幅度 中位数 0.6，观测区间 0.6 - 1，6 个样本
- 宽度 中位数 768，观测区间 768 - 1024，6 个样本，取值集中（一致性 88%）
- 高度 中位数 1024，观测区间 768 - 1024，6 个样本，取值集中（一致性 90%）
- 高发问题（12/6 个样本）：Steps较低可能导致细节不足
