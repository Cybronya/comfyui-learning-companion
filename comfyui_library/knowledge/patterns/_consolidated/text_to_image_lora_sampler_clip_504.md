---
name: text_to_image_lora_sampler_clip_504
type: Text To Image
frequency: 3
level: moderate
coverage: 0.863
common_nodes: [CLIPLoader, CLIPTextEncode, CR Prompt Text, EmptyLatentImage, Fast Groups Bypasser (rgthree), Image Comparer (rgthree), JoinStringMulti, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, LoraLoaderModelOnly, ModelSamplingAuraFlow, PainterFluxImageEdit, SaveImage, UNETLoader, VAEDecode, VAELoader, easy imageColorMatch]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Anima文生图_2072678854979837953.json, 图片生成/文生图/Anima正式版-文生图工作流-提示词模版_2056942036279975937.json, 图片生成/文生图/Anima正式版-文生图工作流_2057761171805130754.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_504

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Anima文生图_2072678854979837953.json、图片生成/文生图/Anima正式版-文生图工作流-提示词模版_2056942036279975937.json、图片生成/文生图/Anima正式版-文生图工作流_2057761171805130754.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `Image Comparer (rgthree)`
- `JoinStringMulti`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM V2`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PainterFluxImageEdit`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy imageColorMatch`

**可变部分**（部分 workflow 才有）：
- `1hew_ImageToURL` —— 1/3 个有
- `API_PromptHelper` —— 1/3 个有
- `CR Text` —— 1/3 个有
- `DuckQREncodeNode` —— 1/3 个有
- `RH_LLMAPI_Pro_Node` —— 1/3 个有
- `ShowText|pysssss` —— 1/3 个有
- `easy saveText` —— 1/3 个有
- `easy showAnything` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 30 | 3 | 3% |
| Prompt 约束强度(CFG) | 1 | 1 - 5 | 3 | 19% |
| 采样算法 | euler_ancestral | - | 3 | 67% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 1024 | 1024 - 1024 | 3 | 100% |
| 高度 | 1536 | 1536 - 1536 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 30，3 个样本，取值分散，一致性仅 3%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 5，3 个样本，取值分散，一致性仅 19%
- 采样算法 最常用 euler_ancestral，3 个样本，一致性 67%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 1024 - 1024，3 个样本，取值集中（一致性 100%）
- 高度 中位数 1536，观测区间 1536 - 1536，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
