---
name: unknown_workflow_upscale_lora_sampler_86
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.845
common_nodes: [BatchImagesNode, CLIPLoader, EmptyLatentImage, ImageConcatMulti, KSampler, LoadImage, LoadImageGoohai, LoraLoaderModelOnly, MuyeTextEditOutput, PreviewImage, QwenImage21Cache, ResolutionSelector, SaveImage, SplitImageWithAlpha, TextEncodeQwenImage21, TextGenerate, UNETLoader, VAEDecode, VAELoader, VOSR2ModelLoader, VOSR2Upscale, 忽略多组孤海]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Image 2.1 BFS换脸 换头工作流_2105665836672442370.json, 图片生成/图生图/Qwen_image_2.1_BFS换脸_换头工作流_2105336964957425665.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_86

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Qwen Image 2.1 BFS换脸 换头工作流_2105665836672442370.json、图片生成/图生图/Qwen_image_2.1_BFS换脸_换头工作流_2105336964957425665.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：84%

## 共有节点

全部 2 个 workflow 都包含：
- `BatchImagesNode`
- `CLIPLoader`
- `EmptyLatentImage`
- `ImageConcatMulti`
- `KSampler`
- `LoadImage`
- `LoadImageGoohai`
- `LoraLoaderModelOnly`
- `MuyeTextEditOutput`
- `PreviewImage`
- `QwenImage21Cache`
- `ResolutionSelector`
- `SaveImage`
- `SplitImageWithAlpha`
- `TextEncodeQwenImage21`
- `TextGenerate`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VOSR2ModelLoader`
- `VOSR2Upscale`
- `忽略多组孤海`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | - | 2 | 100% |
| 高度 | 1024 | - | 2 | 100% |
| 采样步数 | 8 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | deis_2m | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 deis_2m，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
