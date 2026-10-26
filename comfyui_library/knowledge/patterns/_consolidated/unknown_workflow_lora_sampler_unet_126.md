---
name: unknown_workflow_lora_sampler_unet_126
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.900167
common_nodes: [CLIPLoader, ConditioningZeroOut, CropWithPadInfo, KSampler, LoadImage, LoraLoaderModelOnly, QwenEditConfigPreparer, QwenEditOutputExtractor, SaveImage, TextEncodeQwenImageEditPlusCustom_lrzjason, UNETLoader, VAELoader]
problems: [Steps较低可能导致细节不足, 发现KSampler但没有VAEDecode]
missing: []
members: [图片生成/图生图/漫画转真人-ai智能体专用_2007622755214172161.json, 图片生成/图生图/超好用-qwen最强换装_2093635203448270849.json, 图片生成/图生图/超火的抖音带货一键换装工作流_2045945164983705601.json, 图片生成/图生图/遮罩编辑 Qwen Edit 2511_2004128942560845826.json, 图片生成/图生图/👾怪獸-千问换装两种方式-支持遮罩 👾_1989627553197551617.json, 图片生成/图生图/🦖anything2real 2601_2008120044538040321.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_126

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/漫画转真人-ai智能体专用_2007622755214172161.json、图片生成/图生图/超好用-qwen最强换装_2093635203448270849.json、图片生成/图生图/超火的抖音带货一键换装工作流_2045945164983705601.json、图片生成/图生图/遮罩编辑 Qwen Edit 2511_2004128942560845826.json、图片生成/图生图/👾怪獸-千问换装两种方式-支持遮罩 👾_1989627553197551617.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `ConditioningZeroOut`
- `CropWithPadInfo`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `QwenEditConfigPreparer`
- `QwenEditOutputExtractor`
- `SaveImage`
- `TextEncodeQwenImageEditPlusCustom_lrzjason`
- `UNETLoader`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PrimitiveStringMultiline` —— 5/6 个有
- `Image Comparer (rgthree)` —— 4/6 个有
- `VAEDecode` —— 4/6 个有
- `QwenEditAdaptiveLongestEdge` —— 3/6 个有
- `ImageScaleBy` —— 2/6 个有
- `Seed Everywhere` —— 2/6 个有
- `VAEDecodeTiled` —— 2/6 个有
- `Anything Everywhere3` —— 1/6 个有
- `Fast Groups Bypasser (rgthree)` —— 1/6 个有
- `LayerUtility: PurgeVRAM` —— 1/6 个有
- `MaskFillHoles` —— 1/6 个有
- `ResizeLongestToNode` —— 1/6 个有
- `SetNode` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 6 | 65% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | beta57 | - | 6 | 83% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |
| 发现KSampler但没有VAEDecode | 2/6 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，6 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 beta57，6 个样本，一致性 83%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（7/6 个样本）：Steps较低可能导致细节不足
