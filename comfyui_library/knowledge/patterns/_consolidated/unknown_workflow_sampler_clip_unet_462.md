---
name: unknown_workflow_sampler_clip_unet_462
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.87
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, EmptyLatentImage, KSamplerSelect, PreviewImage, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [平台全量/Flux一句话文生图系列1：3D多视图_1866377276320600066.json, 平台全量/提示词智能扩充+flux文生图_1828362579197743105.json, 平台全量/魔法猫_1851096789679042561.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_462

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/Flux一句话文生图系列1：3D多视图_1866377276320600066.json、平台全量/提示词智能扩充+flux文生图_1828362579197743105.json、平台全量/魔法猫_1851096789679042561.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `KSamplerSelect`
- `PreviewImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `RH_Prompter` —— 2/3 个有
- `ShowText|pysssss` —— 2/3 个有
- `Translate2Chinese|fofo` —— 2/3 个有
- `FluxGuidance` —— 1/3 个有
- `Label (rgthree)` —— 1/3 个有
- `LayerUtility: TextJoin` —— 1/3 个有
- `easy prompt` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 800 - 1024 | 3 | 89% |
| 高度 | 1280 | 1200 - 1280 | 3 | 97% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 800 - 1024，3 个样本，取值集中（一致性 89%）
- 高度 中位数 1280，观测区间 1200 - 1280，3 个样本，取值集中（一致性 97%）
