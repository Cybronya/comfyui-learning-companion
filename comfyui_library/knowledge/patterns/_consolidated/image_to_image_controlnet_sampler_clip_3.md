---
name: image_to_image_controlnet_sampler_clip_3
type: Image To Image
frequency: 2
level: weak
coverage: 0.931
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, ControlNetApplyAdvanced, ControlNetLoader, KSampler, LoadImage, RepeatLatentBatch, SaveImage, VAEDecode, VAEEncode]
problems: []
missing: []
members: [图片生成/文生图/1902722563137548289.json, 图片生成/文生图/文生图+CN_Depth_1778001923841003521.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_sampler_clip_3

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/1902722563137548289.json、图片生成/文生图/文生图+CN_Depth_1778001923841003521.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：93%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `KSampler`
- `LoadImage`
- `RepeatLatentBatch`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`

**可变部分**（部分 workflow 才有）：
- `DeepTranslatorTextNode` —— 1/2 个有
- `Joy_caption` —— 1/2 个有
- `Joy_caption_load` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `Zoe-DepthMapPreprocessor` —— 1/2 个有
- `scale` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | - | 2 | 80% |
| Prompt 约束强度(CFG) | 8 | - | 2 | 100% |
| 采样算法 | dpmpp_2m | - | 2 | 50% |
| 调度器 | karras | - | 2 | 50% |
| 重绘幅度 | 0.85 | - | 2 | 82% |
| ControlNet 权重 | 0.925 | - | 2 | 92% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，样本不足，未给区间，2 个样本，取值集中（一致性 80%）
- Prompt 约束强度(CFG) 中位数 8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_2m，2 个样本，一致性 50%
- 调度器 最常用 karras，2 个样本，一致性 50%
- 重绘幅度 中位数 0.85，样本不足，未给区间，2 个样本，取值集中（一致性 82%）
- ControlNet 权重 中位数 0.925，样本不足，未给区间，2 个样本，取值集中（一致性 92%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
