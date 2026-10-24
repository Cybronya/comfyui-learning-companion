---
name: unknown_workflow_lora_sampler_clip_85
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.9225
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSamplerAdvanced, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/2030969082719248385.json, 图片生成/文生图/2030992571719229442.json, 图片生成/文生图/2512+2.8D单采_2063254991854456834.json, 图片生成/文生图/2512+zit双采_2063147565729800194.json, 图片生成/文生图/KREA2—文生图_2090377366865539073.json, 图片生成/文生图/amumu_Zimage_真实人像_2014304505898209281.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_85

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/2030969082719248385.json、图片生成/文生图/2030992571719229442.json、图片生成/文生图/2512+2.8D单采_2063254991854456834.json、图片生成/文生图/2512+zit双采_2063147565729800194.json、图片生成/文生图/KREA2—文生图_2090377366865539073.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 6 个 workflow 都包含：
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
- `ModelSamplingAuraFlow` —— 5/6 个有
- `INTConstant` —— 4/6 个有
- `CR Text` —— 3/6 个有
- `ConditioningZeroOut` —— 3/6 个有
- `PreviewImage` —— 3/6 个有
- `easy cleanGpuUsed` —— 3/6 个有
- `SimpleMath+` —— 2/6 个有
- `VAEEncode` —— 2/6 个有
- `CR Prompt Text` —— 1/6 个有
- `Fast Groups Bypasser (rgthree)` —— 1/6 个有
- `ImageScaleBy` —— 1/6 个有
- `RunningHub Deepcleaner` —— 1/6 个有
- `easy seed` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 6 | 100% |
| Prompt 约束强度(CFG) | 9 | 8 - 10 | 6 | 89% |
| 采样算法 | 1 | 1 - 1 | 6 | 100% |
| 调度器 | euler | - | 6 | 50% |
| 重绘幅度 | simple | - | 6 | 50% |
| 宽度 | 1024 | 1024 - 2048 | 6 | 69% |
| 高度 | 1536 | 1536 - 2048 | 6 | 88% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，6 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 9，观测区间 8 - 10，6 个样本，取值集中（一致性 89%）
- 采样算法 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，6 个样本，一致性 50%
- 重绘幅度 最常用 simple，6 个样本，一致性 50%
- 宽度 中位数 1024，观测区间 1024 - 2048，6 个样本
- 高度 中位数 1536，观测区间 1536 - 2048，6 个样本，取值集中（一致性 88%）
