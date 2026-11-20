---
name: unknown_workflow_lora_sampler_clip_59
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.9325
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSamplerAdvanced, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/2030969082719248385.json, 图片生成/文生图/2030992571719229442.json, 图片生成/文生图/2512+2.8D单采_2063254991854456834.json, 图片生成/文生图/2512+zit双采_2063147565729800194.json, 图片生成/文生图/KREA2—文生图_2090377366865539073.json, 图片生成/文生图/amumu_Zimage_真实人像_2014304505898209281.json, 图片生成/文生图/【API】Krea2文生图（三采流）(Lora)_2111986935001604098.json, 图片生成/文生图/【API】Z-Image文生图_2111987255505154050.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_59

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/2030969082719248385.json、图片生成/文生图/2030992571719229442.json、图片生成/文生图/2512+2.8D单采_2063254991854456834.json、图片生成/文生图/2512+zit双采_2063147565729800194.json、图片生成/文生图/KREA2—文生图_2090377366865539073.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSamplerAdvanced`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ModelSamplingAuraFlow` —— 7/8 个有
- `INTConstant` —— 6/8 个有
- `CR Text` —— 5/8 个有
- `ConditioningZeroOut` —— 5/8 个有
- `easy cleanGpuUsed` —— 5/8 个有
- `PreviewImage` —— 4/8 个有
- `PlaySound|pysssss` —— 2/8 个有
- `ResolutionSelector` —— 2/8 个有
- `Seed (rgthree)` —— 2/8 个有
- `SimpleMath+` —— 2/8 个有
- `VAEEncode` —— 2/8 个有
- `CR Prompt Text` —— 1/8 个有
- `Fast Groups Bypasser (rgthree)` —— 1/8 个有
- `ImageScaleBy` —— 1/8 个有
- `RunningHub Deepcleaner` —— 1/8 个有
- `easy seed` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 8 | 100% |
| Prompt 约束强度(CFG) | 8 | 3 - 10 | 8 | 63% |
| 采样算法 | 1 | 1 - 2 | 8 | 71% |
| 调度器 | euler | - | 8 | 62% |
| 重绘幅度 | simple | - | 8 | 62% |
| 宽度 | 1024 | 512 - 2048 | 8 | 57% |
| 高度 | 1536 | 512 - 2048 | 8 | 62% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，8 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 8，观测区间 3 - 10，8 个样本
- 采样算法 中位数 1，观测区间 1 - 2，8 个样本
- 调度器 最常用 euler，8 个样本，一致性 62%
- 重绘幅度 最常用 simple，8 个样本，一致性 62%
- 宽度 中位数 1024，观测区间 512 - 2048，8 个样本
- 高度 中位数 1536，观测区间 512 - 2048，8 个样本
