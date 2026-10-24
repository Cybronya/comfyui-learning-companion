---
name: unknown_workflow_lora_sampler_clip_207
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.936667
common_nodes: [AnyLineArtPreprocessor_aux, Anything Everywhere, BNK_CLIPTextEncodeAdvanced, CheckpointLoaderSimple, EmptyLatentImage, FreeU_V2, Image Filter Adjustments, ImageScaleBy, KSamplerAdvanced //Inspire, LoadImage, LoraLoader, PatchModelAddDownscale, Prompts Everywhere, RescaleCFG, SaveImage, VAEDecode, VAELoader, easy getNode, easy imageSize, easy seed, easy setNode, ttN text]
problems: []
missing: []
members: [图片生成/文生图/千府AI建筑立面工作流(高级版)_1898700526715129858.json, 图片生成/文生图/千府AI效果图工作流_1900041366724816897.json, 图片生成/文生图/千府AI鸟瞰图通用工作流_1899689387444322305.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_207

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/千府AI建筑立面工作流(高级版)_1898700526715129858.json、图片生成/文生图/千府AI效果图工作流_1900041366724816897.json、图片生成/文生图/千府AI鸟瞰图通用工作流_1899689387444322305.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：94%

## 共有节点

全部 3 个 workflow 都包含：
- `AnyLineArtPreprocessor_aux`
- `Anything Everywhere`
- `BNK_CLIPTextEncodeAdvanced`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `FreeU_V2`
- `Image Filter Adjustments`
- `ImageScaleBy`
- `KSamplerAdvanced //Inspire`
- `LoadImage`
- `LoraLoader`
- `PatchModelAddDownscale`
- `Prompts Everywhere`
- `RescaleCFG`
- `SaveImage`
- `VAEDecode`
- `VAELoader`
- `easy getNode`
- `easy imageSize`
- `easy seed`
- `easy setNode`
- `ttN text`

**可变部分**（部分 workflow 才有）：
- `CLIPVisionLoader` —— 2/3 个有
- `CR Apply Multi-ControlNet` —— 2/3 个有
- `CR Multi-ControlNet Stack` —— 2/3 个有
- `ControlNetLoader` —— 2/3 个有
- `DepthAnythingV2Preprocessor` —— 2/3 个有
- `IPAdapterMS` —— 2/3 个有
- `IPAdapterModelLoader` —— 2/3 个有
- `IPAdapterUnifiedLoader` —— 2/3 个有
- `PrepImageForClipVision` —— 2/3 个有
- `AIO_Preprocessor` —— 1/3 个有
- `ControlNetApply` —— 1/3 个有
- `ControlNetApplyAdvanced` —— 1/3 个有
- `Image Comparer (rgthree)` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.6 | 0.6 - 0.6 | 3 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 512 | 512 - 512 | 3 | 100% |
| 高度 | 512 | 512 - 512 | 3 | 100% |
| 采样步数 | randomize | - | 3 | 100% |
| Prompt 约束强度(CFG) | 30 | 30 - 30 | 3 | 100% |
| 采样算法 | 3 | 3 - 3 | 3 | 100% |
| 调度器 | lcm | - | 3 | 100% |
| 重绘幅度 | karras | - | 3 | 100% |
| ControlNet 权重 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 0.6，观测区间 0.6 - 0.6，3 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 512，观测区间 512 - 512，3 个样本，取值集中（一致性 100%）
- 高度 中位数 512，观测区间 512 - 512，3 个样本，取值集中（一致性 100%）
- 采样步数 最常用 randomize，3 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 30，观测区间 30 - 30，3 个样本，取值集中（一致性 100%）
- 采样算法 中位数 3，观测区间 3 - 3，3 个样本，取值集中（一致性 100%）
- 调度器 最常用 lcm，3 个样本，一致性 100%
- 重绘幅度 最常用 karras，3 个样本，一致性 100%
- ControlNet 权重 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 风险：Prompt 约束强度(CFG) 观测到 30，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
