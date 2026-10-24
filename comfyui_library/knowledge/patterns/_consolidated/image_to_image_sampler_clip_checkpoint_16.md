---
name: image_to_image_sampler_clip_checkpoint_16
type: Image To Image
frequency: 2
level: weak
coverage: 0.753
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, ConstrainImage|pysssss, ICLightConditioning, KSampler, LayerMask: SegmentAnythingUltra V2, LoadAndApplyICLightUnet, LoadImage, PreviewImage, SaveImage, VAEDecode, VAEEncode]
problems: []
missing: []
members: [图片生成/图生图/一句话打光调色工作流 一键生图系列_1907267831539621890.json, 图片生成/图生图/打光-调画面色调【可在线运行】iclight_1917394858733146113.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_checkpoint_16

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/一句话打光调色工作流 一键生图系列_1907267831539621890.json、图片生成/图生图/打光-调画面色调【可在线运行】iclight_1917394858733146113.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：75%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ConstrainImage|pysssss`
- `ICLightConditioning`
- `KSampler`
- `LayerMask: SegmentAnythingUltra V2`
- `LoadAndApplyICLightUnet`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`

**可变部分**（部分 workflow 才有）：
- `JjkText` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 28 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 3 | - | 2 | 100% |
| 采样算法 | euler_ancestral | - | 2 | 100% |
| 调度器 | karras | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 28，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 3，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，2 个样本，一致性 100%
- 调度器 最常用 karras，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
