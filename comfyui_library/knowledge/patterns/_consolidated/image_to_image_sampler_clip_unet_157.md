---
name: image_to_image_sampler_clip_unet_157
type: Image To Image
frequency: 3
level: strong
coverage: 0.820333
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, FluxKontextImageScale, KSampler, LoadImage, PreviewImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/flux-context-多图可控生成_1939341869128269826.json, 图片生成/文生图/flux_kontext_dev_basic_8G可用_1954455056802312194.json, 图片生成/文生图/根据提示词修改图片_2000153948931715074.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_157

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/flux-context-多图可控生成_1939341869128269826.json、图片生成/文生图/flux_kontext_dev_basic_8G可用_1954455056802312194.json、图片生成/文生图/根据提示词修改图片_2000153948931715074.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `FluxKontextImageScale`
- `KSampler`
- `LoadImage`
- `PreviewImage`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptySD3LatentImage` —— 2/3 个有
- `ImageStitch` —— 2/3 个有
- `Compositor3` —— 1/3 个有
- `CompositorConfig3` —— 1/3 个有
- `GLM_Translation_Text` —— 1/3 个有
- `GetImageSize+` —— 1/3 个有
- `Lora Loader` —— 1/3 个有
- `RMBG` —— 1/3 个有
- `TeaCache` —— 1/3 个有
- `TextInput_` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
