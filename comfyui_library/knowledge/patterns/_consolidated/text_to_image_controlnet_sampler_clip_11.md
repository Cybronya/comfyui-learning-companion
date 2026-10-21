---
name: text_to_image_controlnet_sampler_clip_11
type: Text To Image
frequency: 2
level: weak
coverage: 0.906
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, ControlNetApplyAdvanced, ControlNetLoader, EmptyLatentImage, KSampler, LoadImage, PreviewImage, SaveImage, VAEDecode]
problems: []
missing: []
members: [图片生成/文生图/文生图+CN_Depth_Openpose_1778002614114390018.json, 视频生成/文生视频/ControlNet预处理器_2016518079005593601.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_sampler_clip_11

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/文生图+CN_Depth_Openpose_1778002614114390018.json、视频生成/文生视频/ControlNet预处理器_2016518079005593601.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `AIO_Preprocessor` —— 1/2 个有
- `DWPreprocessor` —— 1/2 个有
- `GetImageSize` —— 1/2 个有
- `ImageResize+` —— 1/2 个有
- `WD14Tagger|pysssss` —— 1/2 个有
- `Zoe-DepthMapPreprocessor` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 640 | - | 2 | 80% |
| 高度 | 768 | - | 2 | 67% |
| ControlNet 权重 | 0.9 | - | 2 | 89% |
| 采样步数 | 20 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 7.495 | - | 2 | 93% |
| 采样算法 | dpmpp_2m | - | 2 | 50% |
| 调度器 | karras | - | 2 | 50% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 640，样本不足，未给区间，2 个样本，取值集中（一致性 80%）
- 高度 中位数 768，样本不足，未给区间，2 个样本
- ControlNet 权重 中位数 0.9，样本不足，未给区间，2 个样本，取值集中（一致性 89%）
- 采样步数 中位数 20，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 7.495，样本不足，未给区间，2 个样本，取值集中（一致性 93%）
- 采样算法 最常用 dpmpp_2m，2 个样本，一致性 50%
- 调度器 最常用 karras，2 个样本，一致性 50%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
