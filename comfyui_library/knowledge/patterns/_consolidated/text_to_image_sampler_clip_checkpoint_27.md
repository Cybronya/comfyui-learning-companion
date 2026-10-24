---
name: text_to_image_sampler_clip_checkpoint_27
type: Text To Image
frequency: 2
level: weak
coverage: 0.903
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, EmptyLatentImage, KSampler, PortraitMaster_中文版, PreviewImage, SaveImage, VAEDecode]
problems: []
missing: []
members: [图片生成/文生图/生成人物图像(肖像大师）_2076571370456182786.json, 图片生成/文生图/肖像大师-根据提示词生成人物肖像_2061354886461218818.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_checkpoint_27

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/生成人物图像(肖像大师）_2076571370456182786.json、图片生成/文生图/肖像大师-根据提示词生成人物肖像_2061354886461218818.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `KSampler`
- `PortraitMaster_中文版`
- `PreviewImage`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `SeedVR2LoadDiTModel` —— 1/2 个有
- `SeedVR2LoadVAEModel` —— 1/2 个有
- `SeedVR2VideoUpscaler` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 768 | - | 2 | 100% |
| 高度 | 1280 | - | 2 | 100% |
| 采样步数 | 20 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 7.5 | - | 2 | 93% |
| 采样算法 | dpmpp_2m | - | 2 | 50% |
| 调度器 | normal | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 768，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1280，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 20，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 7.5，样本不足，未给区间，2 个样本，取值集中（一致性 93%）
- 采样算法 最常用 dpmpp_2m，2 个样本，一致性 50%
- 调度器 最常用 normal，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
