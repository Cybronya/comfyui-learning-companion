---
name: unknown_workflow_lora_sampler_clip_83
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.9325
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSamplerAdvanced, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/2512+2.8D单采_2063254991854456834.json, 图片生成/文生图/2512+zit双采_2063147565729800194.json, 图片生成/文生图/KREA2—文生图_2090377366865539073.json, 图片生成/文生图/amumu_Zimage_真实人像_2014304505898209281.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_83

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/2512+2.8D单采_2063254991854456834.json、图片生成/文生图/2512+zit双采_2063147565729800194.json、图片生成/文生图/KREA2—文生图_2090377366865539073.json、图片生成/文生图/amumu_Zimage_真实人像_2014304505898209281.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSamplerAdvanced`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 3/4 个有
- `INTConstant` —— 3/4 个有
- `PreviewImage` —— 2/4 个有
- `SimpleMath+` —— 2/4 个有
- `VAEEncode` —— 2/4 个有
- `easy cleanGpuUsed` —— 2/4 个有
- `CR Prompt Text` —— 1/4 个有
- `ConditioningZeroOut` —— 1/4 个有
- `Fast Groups Bypasser (rgthree)` —— 1/4 个有
- `ImageScaleBy` —— 1/4 个有
- `RunningHub Deepcleaner` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 4 | 100% |
| Prompt 约束强度(CFG) | 9 | 8 - 10 | 4 | 89% |
| 采样算法 | 1 | 1 - 1 | 4 | 100% |
| 调度器 | res_2s | - | 4 | 50% |
| 重绘幅度 | beta57 | - | 4 | 50% |
| 宽度 | 1024 | 1024 - 1024 | 4 | 100% |
| 高度 | 1536 | 1536 - 1536 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，4 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 9，观测区间 8 - 10，4 个样本，取值集中（一致性 89%）
- 采样算法 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 调度器 最常用 res_2s，4 个样本，一致性 50%
- 重绘幅度 最常用 beta57，4 个样本，一致性 50%
- 宽度 中位数 1024，观测区间 1024 - 1024，4 个样本，取值集中（一致性 100%）
- 高度 中位数 1536，观测区间 1536 - 1536，4 个样本，取值集中（一致性 100%）
