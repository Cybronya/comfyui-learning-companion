---
name: text_to_image_lora_sampler_clip_466
type: Text To Image
frequency: 4
level: moderate
coverage: 0.84225
common_nodes: [CLIPLoader, CLIPTextEncode, CR Prompt Text, EmptyLatentImage, Fast Groups Bypasser (rgthree), Image Comparer (rgthree), JoinStringMulti, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, LoraLoaderModelOnly, ModelSamplingAuraFlow, PainterFluxImageEdit, SaveImage, UNETLoader, VAEDecode, VAELoader, easy imageColorMatch]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Anima文生图_2072678854979837953.json, 图片生成/文生图/Anima正式版-文生图工作流-提示词模版_2056942036279975937.json, 图片生成/文生图/Anima正式版-文生图工作流_2057761171805130754.json, 数字人/数字人/Anima正式版-文生图工作流_2067103556976603138.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_466

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/Anima文生图_2072678854979837953.json、图片生成/文生图/Anima正式版-文生图工作流-提示词模版_2056942036279975937.json、图片生成/文生图/Anima正式版-文生图工作流_2057761171805130754.json、数字人/数字人/Anima正式版-文生图工作流_2067103556976603138.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 4 个 workflow 都包含：
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
- `1hew_ImageToURL` —— 2/4 个有
- `API_PromptHelper` —— 2/4 个有
- `DuckQREncodeNode` —— 2/4 个有
- `ShowText|pysssss` —— 2/4 个有
- `easy saveText` —— 2/4 个有
- `easy showAnything` —— 2/4 个有
- `CR Text` —— 1/4 个有
- `RH_LLMAPI_Pro_Node` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 17 | 4 - 30 | 4 | 24% |
| Prompt 约束强度(CFG) | 3 | 1 - 5 | 4 | 33% |
| 采样算法 | er_sde | - | 4 | 50% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 1024 | 1024 - 1024 | 4 | 100% |
| 高度 | 1536 | 1536 - 1536 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 17，观测区间 4 - 30，4 个样本，取值分散，一致性仅 24%
- Prompt 约束强度(CFG) 中位数 3，观测区间 1 - 5，4 个样本，取值分散，一致性仅 33%
- 采样算法 最常用 er_sde，4 个样本，一致性 50%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 1024 - 1024，4 个样本，取值集中（一致性 100%）
- 高度 中位数 1536，观测区间 1536 - 1536，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
