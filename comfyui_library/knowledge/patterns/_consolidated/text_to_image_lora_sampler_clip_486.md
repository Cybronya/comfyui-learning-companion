---
name: text_to_image_lora_sampler_clip_486
type: Text To Image
frequency: 4
level: strong
coverage: 0.72525
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, Float, ImpactConditionalBranch, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoraLoaderModelOnly, PathchSageAttentionKJ, PrimitiveBoolean, PrimitiveInt, RepeatLatentBatch, SaveImage, Seed (rgthree), TTResolutionSelector, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy float]
problems: []
missing: []
members: [图片生成/文生图/Aesthetic-1b 文生图 工作流+全节点注释_2076383759691247618.json, 图片生成/文生图/anima对比测试 美学1.1（提示词）_2077102169794371585.json, 图片生成/文生图/anima对比测试（提示词）_2076232276131803138.json, 平台全量/anima miaomiao 8step测试_2078387870901039105.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_486

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/Aesthetic-1b 文生图 工作流+全节点注释_2076383759691247618.json、图片生成/文生图/anima对比测试 美学1.1（提示词）_2077102169794371585.json、图片生成/文生图/anima对比测试（提示词）_2076232276131803138.json、平台全量/anima miaomiao 8step测试_2078387870901039105.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：73%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `Float`
- `ImpactConditionalBranch`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoraLoaderModelOnly`
- `PathchSageAttentionKJ`
- `PrimitiveBoolean`
- `PrimitiveInt`
- `RepeatLatentBatch`
- `SaveImage`
- `Seed (rgthree)`
- `TTResolutionSelector`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy float`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 3/4 个有
- `CheckpointLoaderSimple` —— 3/4 个有
- `Fast Groups Bypasser (rgthree)` —— 3/4 个有
- `LayerUtility: ImageReel` —— 3/4 个有
- `LayerUtility: ImageReelComposit` —— 3/4 个有
- `LoadImage` —— 3/4 个有
- `easy promptList` —— 3/4 个有
- `SimpleMath+` —— 2/4 个有
- `easy anythingIndexSwitch` —— 2/4 个有
- `easy int` —— 2/4 个有
- `JjkText` —— 1/4 个有
- `SDVN Translate` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 896 | 896 - 896 | 4 | 100% |
| 高度 | 1152 | 1152 - 1152 | 4 | 100% |
| 采样步数 | 36 | 36 - 36 | 4 | 100% |
| Prompt 约束强度(CFG) | 4 | 4 - 4 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 0.65 | 0.65 - 0.65 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 896，观测区间 896 - 896，4 个样本，取值集中（一致性 100%）
- 高度 中位数 1152，观测区间 1152 - 1152，4 个样本，取值集中（一致性 100%）
- 采样步数 中位数 36，观测区间 36 - 36，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 0.65，观测区间 0.65 - 0.65，4 个样本，取值集中（一致性 100%）
