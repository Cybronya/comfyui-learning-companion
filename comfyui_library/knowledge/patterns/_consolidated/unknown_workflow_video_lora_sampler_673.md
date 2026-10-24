---
name: unknown_workflow_video_lora_sampler_673
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.477667
common_nodes: [CLIPLoader, CLIPTextEncode, GetNode, INTConstant, ImageBatchExtendWithOverlap, ImageResizeKJv2, KSamplerAdvanced, LoadImage, LoraLoaderModelOnly, SetNode, VAEDecode, VAEEncode, VAELoader, VHS_VideoCombine, WanImageToVideoSVIPro]
problems: []
missing: []
members: [视频生成/图生视频/宠物吃播_SVI_2_Pro长视频_2018178886772727809.json, 视频生成/图生视频/无限时长-svi 2 pro 长视频生成-图生视频_2006635084027269121.json, 视频生成/文生视频/SVI-pro2.0动画多分镜长视频_2008147706383966209.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_673

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/宠物吃播_SVI_2_Pro长视频_2018178886772727809.json、视频生成/图生视频/无限时长-svi 2 pro 长视频生成-图生视频_2006635084027269121.json、视频生成/文生视频/SVI-pro2.0动画多分镜长视频_2008147706383966209.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：48%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `GetNode`
- `INTConstant`
- `ImageBatchExtendWithOverlap`
- `ImageResizeKJv2`
- `KSamplerAdvanced`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SetNode`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanImageToVideoSVIPro`

**可变部分**（部分 workflow 才有）：
- `ModelPatchTorchSettings` —— 2/3 个有
- `PathchSageAttentionKJ` —— 2/3 个有
- `UNETLoader` —— 2/3 个有
- `AddLabel` —— 1/3 个有
- `CR Prompt Text` —— 1/3 个有
- `DiffusionModelLoaderKJ` —— 1/3 个有
- `Fast Groups Bypasser (rgthree)` —— 1/3 个有
- `Int` —— 1/3 个有
- `JjkText` —— 1/3 个有
- `PainterI2V` —— 1/3 个有
- `PlaySound|pysssss` —— 1/3 个有
- `TTResolutionSelector` —— 1/3 个有
- `easy float` —— 1/3 个有
- `easy indexAnything` —— 1/3 个有
- `easy promptList` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 3 | 67% |
| Prompt 约束强度(CFG) | 8 | 8 - 8 | 3 | 100% |
| 采样算法 | 1 | 1 - 2.5 | 3 | 53% |
| 调度器 | euler | - | 3 | 100% |
| 重绘幅度 | simple | - | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，3 个样本，一致性 67%
- Prompt 约束强度(CFG) 中位数 8，观测区间 8 - 8，3 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 2.5，3 个样本
- 调度器 最常用 euler，3 个样本，一致性 100%
- 重绘幅度 最常用 simple，3 个样本，一致性 100%
