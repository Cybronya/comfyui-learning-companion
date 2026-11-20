---
name: unknown_workflow_lora_sampler_unet_149
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.8722
common_nodes: [CLIPLoader, ConditioningZeroOut, KSampler, LoadImage, LoraLoaderModelOnly, PrimitiveStringMultiline, QwenEditAdaptiveLongestEdge, QwenEditConfigPreparer, QwenMultiangleCameraNode, TextEncodeQwenImageEditPlusCustom_lrzjason, UNETLoader, VAEDecodeTiled, VAELoader]
problems: [Steps较低可能导致细节不足, 发现KSampler但没有VAEDecode]
missing: []
members: [图片生成/图生图/Qwen2511多角度摄像控制 可视化控制_2010991722142113794.json, 图片生成/图生图/Qwen2511多角度摄像控制 多图版_2009838445824315394.json, 图片生成/图生图/Qwen2511多角度摄像控制 多图版_2010070277836771329.json, 图片生成/图生图/Qwen2511多角度摄像控制_2009539361712381954.json, 图片生成/图生图/qwen2511可视化视角改变_2010931487297769474.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_149

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Qwen2511多角度摄像控制 可视化控制_2010991722142113794.json、图片生成/图生图/Qwen2511多角度摄像控制 多图版_2009838445824315394.json、图片生成/图生图/Qwen2511多角度摄像控制 多图版_2010070277836771329.json、图片生成/图生图/Qwen2511多角度摄像控制_2009539361712381954.json、图片生成/图生图/qwen2511可视化视角改变_2010931487297769474.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `ConditioningZeroOut`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PrimitiveStringMultiline`
- `QwenEditAdaptiveLongestEdge`
- `QwenEditConfigPreparer`
- `QwenMultiangleCameraNode`
- `TextEncodeQwenImageEditPlusCustom_lrzjason`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `SaveImage` —— 4/5 个有
- `easy promptList` —— 3/5 个有
- `easy showAnything` —— 3/5 个有
- `KOOK_SaveJPGImage` —— 1/5 个有
- `LayerUtility: ImageReel` —— 1/5 个有
- `LayerUtility: ImageReelComposit` —— 1/5 个有
- `PreviewImage` —— 1/5 个有
- `PrimitiveInt` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | beta57 | - | 5 | 80% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |
| 发现KSampler但没有VAEDecode | 5/5 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 beta57，5 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（6/5 个样本）：Steps较低可能导致细节不足
- 高发问题（5/5 个样本）：发现KSampler但没有VAEDecode
