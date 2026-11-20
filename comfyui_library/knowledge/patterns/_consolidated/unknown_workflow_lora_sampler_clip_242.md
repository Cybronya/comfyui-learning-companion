---
name: unknown_workflow_lora_sampler_clip_242
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.831
common_nodes: [CLIPLoader, CLIPTextEncode, ComfySwitchNode, EmptyFlux2LatentImage, KSampler, LoraLoaderModelOnly, PrimitiveBoolean, ResolutionSelector, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Moss-Image-SFT 4步加速（文生图）工作流_2114736592190525441.json, 图片生成/文生图/moss image 基础加速工作流_2112459568390426626.json, 平台全量/Juggernaut-Moss-文生图-高质量-加速_2119965665502253058.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_242

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Moss-Image-SFT 4步加速（文生图）工作流_2114736592190525441.json、图片生成/文生图/moss image 基础加速工作流_2112459568390426626.json、平台全量/Juggernaut-Moss-文生图-高质量-加速_2119965665502253058.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfySwitchNode`
- `EmptyFlux2LatentImage`
- `KSampler`
- `LoraLoaderModelOnly`
- `PrimitiveBoolean`
- `ResolutionSelector`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 2/3 个有
- `FloatConstant` —— 2/3 个有
- `INTConstant` —— 2/3 个有
- `Seed (rgthree)` —— 2/3 个有
- `SkipLayerGuidanceDiTSimple` —— 2/3 个有
- `Int` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 50 | 50 - 50 | 3 | 100% |
| Prompt 约束强度(CFG) | 3 | 3 - 3 | 3 | 100% |
| 采样算法 | euler | - | 3 | 67% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 50，观测区间 50 - 50，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 3，观测区间 3 - 3，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 67%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
