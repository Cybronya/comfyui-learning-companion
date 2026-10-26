---
name: text_to_image_lora_sampler_clip_260
type: Text To Image
frequency: 8
level: moderate
coverage: 0.92925
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/qwen-Image2512 文生360°全景图_2068269476730200066.json, 图片生成/文生图/Qwen2512油亮丝袜马油连裤袜美女_2018144682206826497.json, 图片生成/文生图/Qwen2512长腿背影美女壁纸_2019744706971832322.json, 图片生成/文生图/Qwen2512黑丝大雷JK美女_2018170744202600449.json, 图片生成/文生图/Qwen2512黑丝甜妹JK美女_2018135200768724993.json, 图片生成/文生图/RealQwenImage V2真人短剧_漫剧角色生图_2014221903111659521.json, 图片生成/文生图/RealQwenImage V2真实人像_2013446508443607041.json, 图片生成/文生图/RealQwenImage1.0真实人像出图_2012887003628572673.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_260

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/qwen-Image2512 文生360°全景图_2068269476730200066.json、图片生成/文生图/Qwen2512油亮丝袜马油连裤袜美女_2018144682206826497.json、图片生成/文生图/Qwen2512长腿背影美女壁纸_2019744706971832322.json、图片生成/文生图/Qwen2512黑丝大雷JK美女_2018170744202600449.json、图片生成/文生图/Qwen2512黑丝甜妹JK美女_2018135200768724993.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PrimitiveStringMultiline` —— 4/8 个有
- `Seed (rgthree)` —— 3/8 个有
- `PreviewImage` —— 2/8 个有
- `INTConstant` —— 1/8 个有
- `PIP_StringConcatenation` —— 1/8 个有
- `PanoramaViewerNode` —— 1/8 个有
- `RH_LLMAPI_NODE` —— 1/8 个有
- `TTResolutionSelector` —— 1/8 个有
- `easy showAnything` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 896 | 768 - 2048 | 8 | 60% |
| 高度 | 1024 | 1024 - 1824 | 8 | 71% |
| 采样步数 | 14 | 9 - 30 | 8 | 61% |
| Prompt 约束强度(CFG) | 2.1 | 1 - 6 | 8 | 35% |
| 采样算法 | euler | - | 8 | 100% |
| 调度器 | simple | - | 8 | 88% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 896，观测区间 768 - 2048，8 个样本
- 高度 中位数 1024，观测区间 1024 - 1824，8 个样本
- 采样步数 中位数 14，观测区间 9 - 30，8 个样本
- Prompt 约束强度(CFG) 中位数 2.1，观测区间 1 - 6，8 个样本，取值分散，一致性仅 35%
- 采样算法 最常用 euler，8 个样本，一致性 100%
- 调度器 最常用 simple，8 个样本，一致性 88%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
