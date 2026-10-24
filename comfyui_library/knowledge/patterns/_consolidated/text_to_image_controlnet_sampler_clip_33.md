---
name: text_to_image_controlnet_sampler_clip_33
type: Text To Image
frequency: 2
level: weak
coverage: 0.8045
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, ControlNetApplyAdvanced, ControlNetLoader, EmptyLatentImage, KSampler, LoadImage, OpenposePreprocessor, SaveImage, VAEDecode]
problems: []
missing: []
members: [图片生成/文生图/拍同款姿势（文生图）_1846060559706767361.json, 图片生成/文生图/文生图 SDXL+CONTRONET-_1982688056933269506.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_sampler_clip_33

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/拍同款姿势（文生图）_1846060559706767361.json、图片生成/文生图/文生图 SDXL+CONTRONET-_1982688056933269506.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：80%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `OpenposePreprocessor`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `CR Text Concatenate` —— 1/2 个有
- `CannyEdgePreprocessor` —— 1/2 个有
- `DeepTranslatorCLIPTextEncodeNode` —— 1/2 个有
- `DepthAnythingPreprocessor` —— 1/2 个有
- `JjkText` —— 1/2 个有
- `PreviewImage` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 22.5 | - | 2 | 89% |
| Prompt 约束强度(CFG) | 7.5 | - | 2 | 93% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | normal | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |
| ControlNet 权重 | 0.75 | - | 2 | 67% |
| 宽度 | 648 | - | 2 | 79% |
| 高度 | 768 | - | 2 | 67% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 22.5，样本不足，未给区间，2 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 7.5，样本不足，未给区间，2 个样本，取值集中（一致性 93%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 normal，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 0.75，样本不足，未给区间，2 个样本
- 宽度 中位数 648，样本不足，未给区间，2 个样本
- 高度 中位数 768，样本不足，未给区间，2 个样本
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
