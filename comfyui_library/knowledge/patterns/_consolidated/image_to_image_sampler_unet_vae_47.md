---
name: image_to_image_sampler_unet_vae_47
type: Image To Image
frequency: 3
level: strong
coverage: 0.666667
common_nodes: [CFGNorm, CLIPLoader, ConditioningZeroOut, EmptyLatentImage, GetImageSize, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, ReferenceLatent, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/QWEN2511 一键绘制多姿势多角度人物写真_2008450833016430594.json, 图片生成/图生图/Qwen - edit - 2511 单图编辑 +双图编辑 系列合集_2005632033193947137.json, 图片生成/图生图/猫咪跳舞 形象定制_2012823277353308162.json]
source: knowledge_consolidation
---

# image_to_image_sampler_unet_vae_47

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/QWEN2511 一键绘制多姿势多角度人物写真_2008450833016430594.json、图片生成/图生图/Qwen - edit - 2511 单图编辑 +双图编辑 系列合集_2005632033193947137.json、图片生成/图生图/猫咪跳舞 形象定制_2012823277353308162.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：67%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `GetImageSize`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `ReferenceLatent`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 2/3 个有
- `LoraLoaderModelOnly` —— 2/3 个有
- `Primitive integer [Crystools]` —— 2/3 个有
- `SetNode` —— 2/3 个有
- `CR Prompt Text` —— 1/3 个有
- `Fast Groups Bypasser (rgthree)` —— 1/3 个有
- `Image Comparer (rgthree)` —— 1/3 个有
- `ImpactSwitch` —— 1/3 个有
- `JjkText` —— 1/3 个有
- `RHHiddenNodes` —— 1/3 个有
- `easy bookmark` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 3 | 100% |
| 高度 | 1920 | 1824 - 1920 | 3 | 98% |
| 采样步数 | 4 | 4 - 9 | 3 | 58% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler_ancestral | - | 3 | 100% |
| 调度器 | FlowMatchEulerDiscreteScheduler | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，3 个样本，取值集中（一致性 100%）
- 高度 中位数 1920，观测区间 1824 - 1920，3 个样本，取值集中（一致性 98%）
- 采样步数 中位数 4，观测区间 4 - 9，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，3 个样本，一致性 100%
- 调度器 最常用 FlowMatchEulerDiscreteScheduler，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（5/3 个样本）：Steps较低可能导致细节不足
