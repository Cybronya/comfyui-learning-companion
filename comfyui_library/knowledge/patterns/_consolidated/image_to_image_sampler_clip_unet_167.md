---
name: image_to_image_sampler_clip_unet_167
type: Image To Image
frequency: 4
level: strong
coverage: 0.944
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, KSampler, LoadImage, PreviewImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [平台全量/清除遮罩部位_1952989060064342018.json, 平台全量/灵魂画手工作流单人版_1985414602475323394.json, 平台全量/灵魂画手工作流多人版_1986142931411226626.json, 平台全量/灵魂画手白底红唇版_1986144444078587905.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_167

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（平台全量/清除遮罩部位_1952989060064342018.json、平台全量/灵魂画手工作流单人版_1985414602475323394.json、平台全量/灵魂画手工作流多人版_1986142931411226626.json、平台全量/灵魂画手白底红唇版_1986144444078587905.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：94%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
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
- `Int` —— 3/4 个有
- `ModelSamplingFlux` —— 3/4 个有
- `RHHiddenNodes` —— 3/4 个有
- `ImageScaleToTotalPixels` —— 1/4 个有
- `LoraLoaderModelOnly` —— 1/4 个有
- `PathchSageAttentionKJ` —— 1/4 个有
- `easy cleanGpuUsed` —— 1/4 个有
- `workflow>MaskColor` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 10 - 20 | 4 | 75% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 10 - 20，4 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
