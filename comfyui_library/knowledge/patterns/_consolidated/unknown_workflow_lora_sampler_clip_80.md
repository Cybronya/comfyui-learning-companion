---
name: unknown_workflow_lora_sampler_clip_80
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.886
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSamplerAdvanced, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Krea2 动画人物文生图_2090097765106933761.json, 视频生成/文生视频/krea2-感性质感文生图_api_2077744663007682562.json, 视频生成/文生视频/krea2-黑珍珠文生图_2078481829623062530.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_80

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Krea2 动画人物文生图_2090097765106933761.json、视频生成/文生视频/krea2-感性质感文生图_api_2077744663007682562.json、视频生成/文生视频/krea2-黑珍珠文生图_2078481829623062530.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSamplerAdvanced`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `JjkText` —— 2/3 个有
- `ModelSamplingAuraFlow` —— 2/3 个有
- `ResolutionSelector` —— 2/3 个有
- `solarL_SaveImagesToZip` —— 2/3 个有
- `Seed (rgthree)` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 3 | 100% |
| Prompt 约束强度(CFG) | 8 | 8 - 8 | 3 | 100% |
| 采样算法 | 1 | 1 - 1 | 3 | 100% |
| 调度器 | euler_ancestral | - | 3 | 67% |
| 重绘幅度 | simple | - | 3 | 100% |
| 宽度 | 512 | 512 - 544 | 3 | 97% |
| 高度 | 512 | 512 - 960 | 3 | 68% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，3 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 8，观测区间 8 - 8，3 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler_ancestral，3 个样本，一致性 67%
- 重绘幅度 最常用 simple，3 个样本，一致性 100%
- 宽度 中位数 512，观测区间 512 - 544，3 个样本，取值集中（一致性 97%）
- 高度 中位数 512，观测区间 512 - 960，3 个样本
