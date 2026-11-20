---
name: unknown_workflow_lora_sampler_clip_141
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.8192
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, MOSSImageControl, PrimitiveInt, SaveImage, TextGenerate, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Moss Image SFT 深度控制洗图_2115612125510070274.json, 图片生成/图生图/Moss-image-洗图_2116055221343449089.json, 图片生成/图生图/Moss-image-深度控制洗图_2115056707008290818.json, 图片生成/图生图/Moss-image-深度控制洗图_2115600577202839553.json, 图片生成/图生图/Moss-image-深度控制洗图_2115939565939810305.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_141

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Moss Image SFT 深度控制洗图_2115612125510070274.json、图片生成/图生图/Moss-image-洗图_2116055221343449089.json、图片生成/图生图/Moss-image-深度控制洗图_2115056707008290818.json、图片生成/图生图/Moss-image-深度控制洗图_2115600577202839553.json、图片生成/图生图/Moss-image-深度控制洗图_2115939565939810305.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MOSSImageControl`
- `PrimitiveInt`
- `SaveImage`
- `TextGenerate`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PrimitiveStringMultiline` —— 4/5 个有
- `ShowText|pysssss` —— 4/5 个有
- `Float` —— 1/5 个有
- `MuyeTextEditOutput` —— 1/5 个有
- `孤海注释` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 40 | 40 - 40 | 5 | 100% |
| Prompt 约束强度(CFG) | 3 | 3 - 3 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 40，观测区间 40 - 40，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 3，观测区间 3 - 3，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
