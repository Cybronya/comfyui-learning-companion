---
name: text_to_image_lora_sampler_clip_340
type: Text To Image
frequency: 6
level: strong
coverage: 0.8665
common_nodes: [CLIPLoader, CLIPTextEncode, CR Prompt Text, CheckpointLoaderSimple, ConditioningZeroOut, EmptyLatentImage, JDCN_StringToList, KSampler, LayerUtility: PurgeVRAM, LoraLoaderModelOnly, ProcessString, SaveImage, Seed (rgthree), Text Concatenate, VAEDecode, VAELoader, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/Z-Image DetailDeamonZ lora权重XYZ对比测试工作流V1_1999495076600479745.json, 图片生成/文生图/Red-Z-Image+Detail Deamon去网红感真实文生图(Pruned+Lora版)_1999788853470916609.json, 图片生成/文生图/Red-Z-Image+Detail Deamon去网红感真实文生图V1(Pruned+Lora版)_1999758914910646273.json, 图片生成/文生图/Red-Z-Image去网红感真实文生图V1(Pruned+Lora可调权重版)_1998475968048168961.json, 图片生成/文生图/Red-Z-Image去网红感真实文生图V1(满血版)_1998238134959767554.json, 图片生成/文生图/Z-image文生图_2035961089313214465.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_340

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Z-Image DetailDeamonZ lora权重XYZ对比测试工作流V1_1999495076600479745.json、图片生成/文生图/Red-Z-Image+Detail Deamon去网红感真实文生图(Pruned+Lora版)_1999788853470916609.json、图片生成/文生图/Red-Z-Image+Detail Deamon去网红感真实文生图V1(Pruned+Lora版)_1999758914910646273.json、图片生成/文生图/Red-Z-Image去网红感真实文生图V1(Pruned+Lora可调权重版)_1998475968048168961.json、图片生成/文生图/Red-Z-Image去网红感真实文生图V1(满血版)_1998238134959767554.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `CheckpointLoaderSimple`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `JDCN_StringToList`
- `KSampler`
- `LayerUtility: PurgeVRAM`
- `LoraLoaderModelOnly`
- `ProcessString`
- `SaveImage`
- `Seed (rgthree)`
- `Text Concatenate`
- `VAEDecode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `Float` —— 4/6 个有
- `JWFloat` —— 3/6 个有
- `AddLabel` —— 1/6 个有
- `DF_Get_latent_size` —— 1/6 个有
- `DuckHideNode` —— 1/6 个有
- `EmptyImage` —— 1/6 个有
- `JWInteger` —— 1/6 个有
- `MathExpression|pysssss` —— 1/6 个有
- `easy batchAnything` —— 1/6 个有
- `easy forLoopEnd` —— 1/6 个有
- `easy forLoopStart` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1080 | 1080 - 1080 | 6 | 100% |
| 高度 | 1920 | 1920 - 1920 | 6 | 100% |
| 采样步数 | 10 | 10 - 10 | 6 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 83% |
| 调度器 | simple | - | 6 | 83% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1080，观测区间 1080 - 1080，6 个样本，取值集中（一致性 100%）
- 高度 中位数 1920，观测区间 1920 - 1920，6 个样本，取值集中（一致性 100%）
- 采样步数 中位数 10，观测区间 10 - 10，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 83%
- 调度器 最常用 simple，6 个样本，一致性 83%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
