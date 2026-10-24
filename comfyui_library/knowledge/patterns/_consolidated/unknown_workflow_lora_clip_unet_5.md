---
name: unknown_workflow_lora_clip_unet_5
type: Unknown Workflow
frequency: 9
level: strong
coverage: 0.941889
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-瑶光-极简_2058833587327299585.json, 图片生成/文生图/ZImage+LoRA文生图+VAE增加细节1_2084738891352993793.json, 图片生成/文生图/ZImage+LoRA文生图+VAE增加细节_2009160034600620034.json, 图片生成/文生图/ZImage+LoRA文生图+VAE增加细节画风控制人物设计1_2084734701411069953.json, 图片生成/文生图/ZImage+LoRA文生图_1995124156607946754.json, 图片生成/文生图/ZImage+LoRA文生图_1995546242350514177.json, 图片生成/文生图/ZImage+LoRA文生图_1999307207806251009.json, 图片生成/文生图/ZImage+LoRA文生图_2005473457250988034.json, 图片生成/文生图/ZImage+短剧定妆图_1995416936924295169.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_clip_unet_5

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/文生图/Z-瑶光-极简_2058833587327299585.json、图片生成/文生图/ZImage+LoRA文生图+VAE增加细节1_2084738891352993793.json、图片生成/文生图/ZImage+LoRA文生图+VAE增加细节_2009160034600620034.json、图片生成/文生图/ZImage+LoRA文生图+VAE增加细节画风控制人物设计1_2084734701411069953.json、图片生成/文生图/ZImage+LoRA文生图_1995124156607946754.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：94%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `KSampler` —— 8/9 个有
- `ModelSamplingAuraFlow` —— 8/9 个有
- `PreviewImage` —— 3/9 个有
- `FLS_SamplerV4` —— 1/9 个有
- `ImpactSwitch` —— 1/9 个有
- `RH_LLMAPI_NODE` —— 1/9 个有
- `ShowText|pysssss` —— 1/9 个有
- `easy promptLine` —— 1/9 个有
- `孤海注释` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 9 | 8 | 67% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | euler | - | 8 | 100% |
| 调度器 | simple | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 9，8 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，8 个样本，一致性 100%
- 调度器 最常用 simple，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 高发问题（8/9 个样本）：Steps较低可能导致细节不足
