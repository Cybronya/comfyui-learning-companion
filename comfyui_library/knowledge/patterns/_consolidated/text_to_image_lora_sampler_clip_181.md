---
name: text_to_image_lora_sampler_clip_181
type: Text To Image
frequency: 10
level: strong
coverage: 0.9211
common_nodes: [CLIPTextEncode, CR Prompt Text, ConditioningZeroOut, EmptyLatentImage, KSampler, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader, easy seed]
problems: []
missing: []
members: [图片生成/文生图/Z-image-turbo Qwen3 Engeneering&Flow Dpo智能提示词文生图_2028048520451723266.json, 图片生成/文生图/Z-image-turbo Qwen3 Engeneering&Flow Dpo智能提示词文生图_2028109823568519170.json, 图片生成/文生图/Z-image-turbo Qwen3 Engeneering&Flow Dpo智能提示词文生图_2028696139326820353.json, 图片生成/文生图/z-image-turbo flow dpo+Engineering v4文生图V_2027986503468584961.json, 图片生成/文生图/z-image-turbo flow dpo+Engineering v4文生图_2028108512752046081.json, 图片生成/文生图/z-image-turbo flow dpo版文生图V1_2026993376582701058.json, 图片生成/文生图/z-image-turbo 写实光影增强版_2027561008427962370.json, 图片生成/文生图/z-image-turbo-flow-dpo版文生图_2027731924940230658.json, 图片生成/文生图/文生图z-image-turbo+D-OPSD+全节点注释_2056647828327452673.json, 图片生成/文生图/文生图【Z-image优化】_2028088570845597698.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_181

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/文生图/Z-image-turbo Qwen3 Engeneering&Flow Dpo智能提示词文生图_2028048520451723266.json、图片生成/文生图/Z-image-turbo Qwen3 Engeneering&Flow Dpo智能提示词文生图_2028109823568519170.json、图片生成/文生图/Z-image-turbo Qwen3 Engeneering&Flow Dpo智能提示词文生图_2028696139326820353.json、图片生成/文生图/z-image-turbo flow dpo+Engineering v4文生图V_2027986503468584961.json、图片生成/文生图/z-image-turbo flow dpo+Engineering v4文生图_2028108512752046081.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPTextEncode`
- `CR Prompt Text`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy seed`

**可变部分**（部分 workflow 才有）：
- `CLIPLoaderGGUF` —— 6/10 个有
- `CLIPLoader` —— 4/10 个有
- `RH_LLMAPI_NODE` —— 4/10 个有
- `easy showAnything` —— 4/10 个有
- `LoadImage` —— 3/10 个有
- `Int` —— 2/10 个有
- `CR Text` —— 1/10 个有
- `CustomAddLabel` —— 1/10 个有
- `Float` —— 1/10 个有
- `ImpactSwitch` —— 1/10 个有
- `MathExpression|pysssss` —— 1/10 个有
- `RHHiddenNodes` —— 1/10 个有
- `Switch any [Crystools]` —— 1/10 个有
- `easy compare` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1080 | 1024 - 2000 | 10 | 70% |
| 高度 | 1920 | 1080 - 2048 | 10 | 76% |
| 采样步数 | 10 | 10 - 10 | 10 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 10 | 100% |
| 采样算法 | euler | - | 10 | 100% |
| 调度器 | simple | - | 10 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1080，观测区间 1024 - 2000，10 个样本
- 高度 中位数 1920，观测区间 1080 - 2048，10 个样本
- 采样步数 中位数 10，观测区间 10 - 10，10 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，10 个样本，一致性 100%
- 调度器 最常用 simple，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
