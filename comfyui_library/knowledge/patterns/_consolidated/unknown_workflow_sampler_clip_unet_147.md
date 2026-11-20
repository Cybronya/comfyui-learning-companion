---
name: unknown_workflow_sampler_clip_unet_147
type: Unknown Workflow
frequency: 9
level: strong
coverage: 0.948444
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/(9图)Flux3_klein_图像编辑，_2116837309923549186.json, 图片生成/图生图/AI试戴美甲-穿戴甲换甲工作流_2094418586373804033.json, 图片生成/图生图/Flux 3_Image_Klein开源版-多图参考生图_2111065019705286658.json, 图片生成/图生图/Flux3 图片强化_2114538601471111169.json, 图片生成/图生图/Flux3_图片强化_2115290001650053121.json, 图片生成/图生图/Flux3_图片强化_2115432565548077057.json, 图片生成/图生图/Flux3_图片强化_2115657791212969985.json, 图片生成/图生图/Flux3单图编辑工作流_2111001547005054977.json, 图片生成/文生图/flux3编辑工作流_2110955588506181634.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_147

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/(9图)Flux3_klein_图像编辑，_2116837309923549186.json、图片生成/图生图/AI试戴美甲-穿戴甲换甲工作流_2094418586373804033.json、图片生成/图生图/Flux 3_Image_Klein开源版-多图参考生图_2111065019705286658.json、图片生成/图生图/Flux3 图片强化_2114538601471111169.json、图片生成/图生图/Flux3_图片强化_2115290001650053121.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：95%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ReferenceMultiLatent` —— 8/9 个有
- `ConditioningZeroOut` —— 7/9 个有
- `EmptyFlux2LatentImage` —— 3/9 个有
- `PrimitiveStringMultiline` —— 3/9 个有
- `ResolutionSelector` —— 3/9 个有
- `CR Prompt Text` —— 2/9 个有
- `Image Comparer (rgthree)` —— 2/9 个有
- `LayerUtility: ImageReel` —— 2/9 个有
- `LayerUtility: ImageReelComposit` —— 2/9 个有
- `EmptySD3LatentImage` —— 1/9 个有
- `Label (rgthree)` —— 1/9 个有
- `PreviewImage` —— 1/9 个有
- `TextEncodeQwenImageEditPlus` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 16 | 16 - 25 | 8 | 83% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | euler | - | 8 | 100% |
| 调度器 | simple | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 16，观测区间 16 - 25，8 个样本，取值集中（一致性 83%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，8 个样本，一致性 100%
- 调度器 最常用 simple，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
