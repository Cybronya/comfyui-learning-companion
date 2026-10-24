---
name: text_to_image_lora_sampler_clip_526
type: Text To Image
frequency: 3
level: strong
coverage: 0.868
common_nodes: [AILab_QwenVL, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, Fast Groups Bypasser (rgthree), FluxGuidance, Image Comparer (rgthree), JjkText, JoinStrings, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, Lora Loader, RH_RhartImageNG31FlashImageToImage, SaveImage, UNETLoader, VAEDecode, VAELoader, easy showAnything]
problems: []
missing: []
members: [图片生成/文生图/文生图_图生图_全能图片三合一工作流_1955452266036674562.json, 图片生成/文生图/文生图_图生图_全能图片三合一工作流_2069693848510623745.json, 图片生成/文生图/文生图_图生图_全能图片三合一工作流_2069699625069666305.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_526

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/文生图_图生图_全能图片三合一工作流_1955452266036674562.json、图片生成/文生图/文生图_图生图_全能图片三合一工作流_2069693848510623745.json、图片生成/文生图/文生图_图生图_全能图片三合一工作流_2069699625069666305.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 3 个 workflow 都包含：
- `AILab_QwenVL`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `FluxGuidance`
- `Image Comparer (rgthree)`
- `JjkText`
- `JoinStrings`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `Lora Loader`
- `RH_RhartImageNG31FlashImageToImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy showAnything`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 15 | 15 - 15 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler_ancestral | - | 3 | 100% |
| 调度器 | FlowMatchEulerDiscreteScheduler | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 1080 | 1080 - 1080 | 3 | 100% |
| 高度 | 1560 | 1560 - 1560 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 15，观测区间 15 - 15，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，3 个样本，一致性 100%
- 调度器 最常用 FlowMatchEulerDiscreteScheduler，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 1080，观测区间 1080 - 1080，3 个样本，取值集中（一致性 100%）
- 高度 中位数 1560，观测区间 1560 - 1560，3 个样本，取值集中（一致性 100%）
