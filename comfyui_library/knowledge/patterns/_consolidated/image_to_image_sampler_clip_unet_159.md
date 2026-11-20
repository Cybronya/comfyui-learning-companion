---
name: image_to_image_sampler_clip_unet_159
type: Image To Image
frequency: 4
level: strong
coverage: 0.71875
common_nodes: [Anything Everywhere3, BiRefNet_Hugo, CLIPLoader, CLIPTextEncode, FillMaskWithColor, GetNode, Int, JjkText, KSampler, LayerMask: SegmentAnythingUltra V2, LayerUtility: ImageScaleByAspectRatio V2, Light-Tool: SimpleTextConnect, LoadImage, SaveImage, SetNode, ShowText, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/安心换装_2054884798916775938.json, 图片生成/图生图/换装 支持大尺度_2042534464424779777.json, 平台全量/Flux2-Klein换装0402_2039168975560515585.json, 平台全量/换装-FireRed 1.1_2039251921885728770.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_159

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/安心换装_2054884798916775938.json、图片生成/图生图/换装 支持大尺度_2042534464424779777.json、平台全量/Flux2-Klein换装0402_2039168975560515585.json、平台全量/换装-FireRed 1.1_2039251921885728770.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：72%

## 共有节点

全部 4 个 workflow 都包含：
- `Anything Everywhere3`
- `BiRefNet_Hugo`
- `CLIPLoader`
- `CLIPTextEncode`
- `FillMaskWithColor`
- `GetNode`
- `Int`
- `JjkText`
- `KSampler`
- `LayerMask: SegmentAnythingUltra V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Light-Tool: SimpleTextConnect`
- `LoadImage`
- `SaveImage`
- `SetNode`
- `ShowText`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CFGNorm` —— 3/4 个有
- `LoraLoaderModelOnly` —— 3/4 个有
- `ModelSamplingAuraFlow` —— 3/4 个有
- `TextEncodeQwenImageEditPlus` —— 3/4 个有
- `ConditioningZeroOut` —— 1/4 个有
- `LayerUtility: PurgeVRAM V2` —— 1/4 个有
- `PreviewImage` —— 1/4 个有
- `ReferenceLatent` —— 1/4 个有
- `easy imageSplitGrid` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 4 - 6 | 4 | 84% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | er_sde | - | 4 | 75% |
| 调度器 | FlowMatchEulerDiscreteScheduler | - | 4 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 4 - 6，4 个样本，取值集中（一致性 84%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，4 个样本，一致性 75%
- 调度器 最常用 FlowMatchEulerDiscreteScheduler，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
