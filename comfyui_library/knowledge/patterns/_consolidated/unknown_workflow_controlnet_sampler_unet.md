---
name: unknown_workflow_controlnet_sampler_unet
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.772
common_nodes: [AIO_Preprocessor, CLIPLoader, ControlNetLoader, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, ModelSamplingAuraFlow, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen-lmage-CN深度_线稿_软边缘_姿态等多种控制_InstantX_CN版_1962434744128507905.json, 图片生成/图生图/千问InstantX_Controlnet超好用_1960648751469723649.json, 图片生成/文生图/CG迷-千问Qwen Controlnet Union工作流_1960971357423112194.json, 图片生成/文生图/Qwen image_ControlNet模式_1961414481920331777.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_sampler_unet

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Qwen-lmage-CN深度_线稿_软边缘_姿态等多种控制_InstantX_CN版_1962434744128507905.json、图片生成/图生图/千问InstantX_Controlnet超好用_1960648751469723649.json、图片生成/文生图/CG迷-千问Qwen Controlnet Union工作流_1960971357423112194.json、图片生成/文生图/Qwen image_ControlNet模式_1961414481920331777.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：77%

## 共有节点

全部 4 个 workflow 都包含：
- `AIO_Preprocessor`
- `CLIPLoader`
- `ControlNetLoader`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPTextEncode` —— 3/4 个有
- `ControlNetApplyAdvanced` —— 3/4 个有
- `EmptySD3LatentImage` —— 3/4 个有
- `LoraLoaderModelOnly` —— 3/4 个有
- `Anything Everywhere` —— 2/4 个有
- `CR Text` —— 2/4 个有
- `Fast Groups Bypasser (rgthree)` —— 2/4 个有
- `Image Comparer (rgthree)` —— 2/4 个有
- `SetUnionControlNetType` —— 2/4 个有
- `Anything Everywhere3` —— 1/4 个有
- `ControlNetApplySD3` —— 1/4 个有
- `DWPreprocessor` —— 1/4 个有
- `EmptyLatentImage` —— 1/4 个有
- `PathchSageAttentionKJ` —— 1/4 个有
- `RH_Captioner` —— 1/4 个有
- `SaveLatent` —— 1/4 个有
- `TextEncodeQwenImageEdit` —— 1/4 个有
- `easy cleanGpuUsed` —— 1/4 个有
- `easy showAnything` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.7 | 0.6 - 0.75 | 4 | 92% |
| 采样步数 | 14 | 4 - 20 | 4 | 45% |
| Prompt 约束强度(CFG) | 2 | 1 - 2.5 | 4 | 65% |
| 采样算法 | euler | - | 4 | 50% |
| 调度器 | simple | - | 4 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 768 | - | 1 | 100% |
| 高度 | 1280 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- ControlNet 权重 中位数 0.7，观测区间 0.6 - 0.75，4 个样本，取值集中（一致性 92%）
- 采样步数 中位数 14，观测区间 4 - 20，4 个样本，取值分散，一致性仅 45%
- Prompt 约束强度(CFG) 中位数 2，观测区间 1 - 2.5，4 个样本
- 采样算法 最常用 euler，4 个样本，一致性 50%
- 调度器 最常用 simple，4 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（2/4 个样本）：Steps较低可能导致细节不足
