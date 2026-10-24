---
name: unknown_workflow_sampler_clip_unet_297
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.88725
common_nodes: [BiRefNetRMBG, CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, Flux2Scheduler, GetImageSize, GetNode, KSamplerSelect, LoadImage, RHLLMChatNode, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, SetNode, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/爆分游戏组件-卷轴_2084885638360428545.json, 图片生成/图生图/爆分游戏组件-数字_2085273251034517506.json, 图片生成/图生图/爆分游戏组件-横幅_2084518617588256769.json, 图片生成/图生图/爆分游戏组件-道具图标_2085295867472465922.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_297

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/爆分游戏组件-卷轴_2084885638360428545.json、图片生成/图生图/爆分游戏组件-数字_2085273251034517506.json、图片生成/图生图/爆分游戏组件-横幅_2084518617588256769.json、图片生成/图生图/爆分游戏组件-道具图标_2085295867472465922.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 4 个 workflow 都包含：
- `BiRefNetRMBG`
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `Flux2Scheduler`
- `GetImageSize`
- `GetNode`
- `KSamplerSelect`
- `LoadImage`
- `RHLLMChatNode`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageScaleToTotalPixels` —— 3/4 个有
- `PreviewTextNode` —— 3/4 个有
- `easy showAnything` —— 3/4 个有
- `CR Text` —— 2/4 个有
- `CR Text Concatenate` —— 2/4 个有
- `EmptyLatentImage` —— 2/4 个有
- `ImageConcanate` —— 2/4 个有
- `PreviewAny` —— 2/4 个有
- `PreviewBridge` —— 2/4 个有
- `Text Load Line From File` —— 2/4 个有
- `ImageCompositeMasked` —— 1/4 个有
- `ImageFromBatch+` —— 1/4 个有
- `Int` —— 1/4 个有
- `LayerUtility: ColorImage` —— 1/4 个有
- `MaskPreview+` —— 1/4 个有
- `PreviewImage` —— 1/4 个有
- `PrimitiveInt` —— 1/4 个有
- `ShowText|pysssss` —— 1/4 个有
- `YUAN_TXTParagraphSplitter` —— 1/4 个有
- `easy cleanGpuUsed` —— 1/4 个有
- `easy clearCacheAll` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 480 | - | 2 | 75% |
| 高度 | 320 | - | 2 | 88% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 480，样本不足，未给区间，2 个样本
- 高度 中位数 320，样本不足，未给区间，2 个样本，取值集中（一致性 88%）
