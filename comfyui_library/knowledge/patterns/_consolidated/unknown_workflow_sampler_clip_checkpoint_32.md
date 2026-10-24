---
name: unknown_workflow_sampler_clip_checkpoint_32
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.7385
common_nodes: [BrushNet, BrushNetLoader, CLIPTextEncode, CheckpointLoaderSimple, GroundingDinoModelLoader (segment anything), GroundingDinoSAMSegment (segment anything), InvertMask, KSampler, LoadImage, MaskToImage, PreviewImage, SaveImage, VAEDecode]
problems: []
missing: []
members: [图片生成/图生图/万能产品换背景_1917445565649453057.json, 图片生成/文生图/CG迷-BrushNet产品更换背景工作流_1926938617195958274.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_checkpoint_32

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/万能产品换背景_1917445565649453057.json、图片生成/文生图/CG迷-BrushNet产品更换背景工作流_1926938617195958274.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：74%

## 共有节点

全部 2 个 workflow 都包含：
- `BrushNet`
- `BrushNetLoader`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `GroundingDinoModelLoader (segment anything)`
- `GroundingDinoSAMSegment (segment anything)`
- `InvertMask`
- `KSampler`
- `LoadImage`
- `MaskToImage`
- `PreviewImage`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 1/2 个有
- `ImageScale` —— 1/2 个有
- `LoraLoader` —— 1/2 个有
- `SAMLoader` —— 1/2 个有
- `SAMModelLoader (segment anything)` —— 1/2 个有
- `WD14Tagger|pysssss` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 27.5 | - | 2 | 91% |
| Prompt 约束强度(CFG) | 6.75 | - | 2 | 89% |
| 采样算法 | dpmpp_2s_ancestral | - | 2 | 50% |
| 调度器 | sgm_uniform | - | 2 | 50% |
| 重绘幅度 | 1 | - | 2 | 100% |
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 27.5，样本不足，未给区间，2 个样本，取值集中（一致性 91%）
- Prompt 约束强度(CFG) 中位数 6.75，样本不足，未给区间，2 个样本，取值集中（一致性 89%）
- 采样算法 最常用 dpmpp_2s_ancestral，2 个样本，一致性 50%
- 调度器 最常用 sgm_uniform，2 个样本，一致性 50%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
