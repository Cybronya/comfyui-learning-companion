---
name: unknown_workflow_sampler_clip_unet_60
type: Unknown Workflow
frequency: 15
level: weak
coverage: 0.895467
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, KSampler, ResolutionSelector, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/MOSS-Image｜Base vs SFT 双模型同参对决·画质横评版_2114209796613296130.json, 图片生成/文生图/MOSS-Image｜色彩深度LoRA·光影与色彩控制实验版_2114557159357902850.json, 图片生成/文生图/MOSS-SFT-观澜_2115634922110148610.json, 图片生成/文生图/MOSS_Krea2_文生图_2113205128068161538.json, 图片生成/文生图/MOSS_Krea2_文生图_2113240561628049409.json, 图片生成/文生图/MOSS文生图2K极速版!_2112525560906870786.json, 图片生成/文生图/MOSS文生图2K极速版!_2113543303009492994.json, 图片生成/文生图/MOSS文生图2K极速版!_2114990704702345217.json, 图片生成/文生图/MOSS文生图2K极速版!_2115228268721958914.json, 图片生成/文生图/MOSS文生图2K极速版!_2115346075061153794.json, 图片生成/文生图/MOSS文生图2K极速版!_2115363371372601346.json, 图片生成/文生图/MOSS文生图2K极速版_2112541313756389378.json, 图片生成/文生图/MOSS文生图2K极速版_2113424816693932034.json, 图片生成/文生图/Moos文生图 你想要的一切_2113432558376673281.json, 平台全量/全新MOSS 2K极速版，文生图进入高清快车道_2118584038364635137.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_60

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（图片生成/文生图/MOSS-Image｜Base vs SFT 双模型同参对决·画质横评版_2114209796613296130.json、图片生成/文生图/MOSS-Image｜色彩深度LoRA·光影与色彩控制实验版_2114557159357902850.json、图片生成/文生图/MOSS-SFT-观澜_2115634922110148610.json、图片生成/文生图/MOSS_Krea2_文生图_2113205128068161538.json、图片生成/文生图/MOSS_Krea2_文生图_2113240561628049409.json…）

- **类型**：Unknown Workflow
- **样本数**：15
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 15 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `KSampler`
- `ResolutionSelector`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 14/15 个有
- `SkipLayerGuidanceDiTSimple` —— 6/15 个有
- `GetNode` —— 2/15 个有
- `Image Comparer (rgthree)` —— 2/15 个有
- `PrimitiveStringMultiline` —— 2/15 个有
- `SetNode` —— 2/15 个有
- `Anything Everywhere3` —— 1/15 个有
- `CR Text` —— 1/15 个有
- `Seed (rgthree)` —— 1/15 个有
- `SeedNode` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 50 | 15 | 23% |
| Prompt 约束强度(CFG) | 1.1 | 1 - 3 | 15 | 48% |
| 采样算法 | euler | - | 15 | 73% |
| 调度器 | simple | - | 15 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 15 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/15 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 50，15 个样本，取值分散，一致性仅 23%
- Prompt 约束强度(CFG) 中位数 1.1，观测区间 1 - 3，15 个样本，取值分散，一致性仅 48%
- 采样算法 最常用 euler，15 个样本，一致性 73%
- 调度器 最常用 simple，15 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
- 高发问题（10/15 个样本）：Steps较低可能导致细节不足
