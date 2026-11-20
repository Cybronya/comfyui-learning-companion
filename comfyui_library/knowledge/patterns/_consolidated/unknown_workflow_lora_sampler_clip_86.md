---
name: unknown_workflow_lora_sampler_clip_86
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.422714
common_nodes: [BerniniConditioning, CLIPLoader, CLIPTextEncode, GetNode, KSamplerAdvanced, Label (rgthree), LayerUtility: TextBox, LoadImage, LoraLoaderModelOnly, MaxNode, PrimitiveInt, ResizeImageMaskNode, SetNode, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/工作流基础系列31.3-Bernini+图像编辑（i2i）工作流_2067577195912060930.json, 平台全量/工作流基础系列31.5-Bernini+视频编辑（v2v）工作流_2067577237934792705.json, 平台全量/工作流基础系列31.6-Bernini+带有参考图的视频编辑（rv2v）工作流_2067581483438665730.json, 平台全量/工作流基础系列31.7-Bernini+图片插入视频编辑（ads2v）工作流_2067581498508800002.json, 平台全量/工作流基础系列31.8-Bernini+视频插入视频编辑（ads2v）工作流_2067581514430377986.json, 视频生成/图生视频/工作流基础系列31.2-Bernini+图生视频（i2v）工作流_2067574598878715906.json, 视频生成/图生视频/工作流基础系列31.4-Bernini+多参考图生视频（r2v）工作流_2067577219454693378.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_86

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/工作流基础系列31.3-Bernini+图像编辑（i2i）工作流_2067577195912060930.json、平台全量/工作流基础系列31.5-Bernini+视频编辑（v2v）工作流_2067577237934792705.json、平台全量/工作流基础系列31.6-Bernini+带有参考图的视频编辑（rv2v）工作流_2067581483438665730.json、平台全量/工作流基础系列31.7-Bernini+图片插入视频编辑（ads2v）工作流_2067581498508800002.json、平台全量/工作流基础系列31.8-Bernini+视频插入视频编辑（ads2v）工作流_2067581514430377986.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：42%

## 共有节点

全部 7 个 workflow 都包含：
- `BerniniConditioning`
- `CLIPLoader`
- `CLIPTextEncode`
- `GetNode`
- `KSamplerAdvanced`
- `Label (rgthree)`
- `LayerUtility: TextBox`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MaxNode`
- `PrimitiveInt`
- `ResizeImageMaskNode`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `VHS_VideoCombine` —— 6/7 个有
- `GetVideoComponents` —— 4/7 个有
- `LoadVideo` —— 4/7 个有
- `easy imageCount` —— 4/7 个有
- `easy showAnything` —— 3/7 个有
- `PreviewImage` —— 2/7 个有
- `PrimitiveFloat` —— 2/7 个有
- `ImageFromBatch` —— 1/7 个有
- `ImageResizeKJv2` —— 1/7 个有
- `SaveImage` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 7 | 71% |
| Prompt 约束强度(CFG) | 6 | 6 - 10 | 7 | 75% |
| 采样算法 | 1 | 1 - 1 | 7 | 100% |
| 调度器 | euler | - | 7 | 100% |
| 重绘幅度 | simple | - | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，7 个样本，一致性 71%
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 10，7 个样本
- 采样算法 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，7 个样本，一致性 100%
- 重绘幅度 最常用 simple，7 个样本，一致性 100%
