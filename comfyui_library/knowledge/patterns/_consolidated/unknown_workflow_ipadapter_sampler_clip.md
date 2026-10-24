---
name: unknown_workflow_ipadapter_sampler_clip
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.5858
common_nodes: [CLIPTextEncodeSDXL, CheckpointLoaderSimple, DF_Text_Box, EmptyLatentImage, FluxResolutionNode, IPAdapterMS, IPAdapterUnifiedLoader, JjkText, KSamplerAdvanced, LoadImage, PrepImageForClipVision, PreviewImage, RH_Prompter, SaveImage, ShowText|pysssss, TextCombinerTwo, VAEDecode]
problems: []
missing: []
members: [图片生成/文生图/文生图_风格—简笔_1913109580585598977.json, 图片生成/文生图/文生风格图像_1877291536911429634.json, 图片生成/文生图/文生风格图像_1983362425695182849.json, 图片生成/文生图/文生风格图像_1983464540010684418.json, 图片生成/文生图/文生风格图像_1983727590538158082.json]
source: knowledge_consolidation
---

# unknown_workflow_ipadapter_sampler_clip

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/文生图_风格—简笔_1913109580585598977.json、图片生成/文生图/文生风格图像_1877291536911429634.json、图片生成/文生图/文生风格图像_1983362425695182849.json、图片生成/文生图/文生风格图像_1983464540010684418.json、图片生成/文生图/文生风格图像_1983727590538158082.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：59%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPTextEncodeSDXL`
- `CheckpointLoaderSimple`
- `DF_Text_Box`
- `EmptyLatentImage`
- `FluxResolutionNode`
- `IPAdapterMS`
- `IPAdapterUnifiedLoader`
- `JjkText`
- `KSamplerAdvanced`
- `LoadImage`
- `PrepImageForClipVision`
- `PreviewImage`
- `RH_Prompter`
- `SaveImage`
- `ShowText|pysssss`
- `TextCombinerTwo`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `AV_VAELoader` —— 1/5 个有
- `HD UltimateSDUpscale` —— 1/5 个有
- `PrimereUpscaleModel` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | 512 - 512 | 5 | 100% |
| 高度 | 512 | 512 - 512 | 5 | 100% |
| 采样步数 | randomize | - | 5 | 80% |
| Prompt 约束强度(CFG) | 45 | 45 - 50 | 5 | 96% |
| 采样算法 | 6.5 | 6.5 - 6.5 | 5 | 100% |
| 调度器 | dpmpp_3m_sde_gpu | - | 5 | 80% |
| 重绘幅度 | karras | - | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 512，观测区间 512 - 512，5 个样本，取值集中（一致性 100%）
- 高度 中位数 512，观测区间 512 - 512，5 个样本，取值集中（一致性 100%）
- 采样步数 最常用 randomize，5 个样本，一致性 80%
- Prompt 约束强度(CFG) 中位数 45，观测区间 45 - 50，5 个样本，取值集中（一致性 96%）
- 采样算法 中位数 6.5，观测区间 6.5 - 6.5，5 个样本，取值集中（一致性 100%）
- 调度器 最常用 dpmpp_3m_sde_gpu，5 个样本，一致性 80%
- 重绘幅度 最常用 karras，5 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 50，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
