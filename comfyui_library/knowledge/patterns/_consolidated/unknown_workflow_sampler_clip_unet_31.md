---
name: unknown_workflow_sampler_clip_unet_31
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.912125
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, ModelSamplingSD3, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1980210462413459458.json, 视频生成/图生视频/1981669095458381825.json, 视频生成/图生视频/1985890821373341698.json, 视频生成/图生视频/1972577637715668993.json, 视频生成/图生视频/1975896909040758785.json, 视频生成/图生视频/2016122544050413569.json, 视频生成/图生视频/1976186558992793601.json, 视频生成/图生视频/1977433925884747777.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_31

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/1980210462413459458.json、视频生成/图生视频/1981669095458381825.json、视频生成/图生视频/1985890821373341698.json、视频生成/图生视频/1972577637715668993.json、视频生成/图生视频/1975896909040758785.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `ModelSamplingSD3`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `JWInteger` —— 7/8 个有
- `LoraLoaderModelOnly` —— 7/8 个有
- `PathchSageAttentionKJ` —— 7/8 个有
- `WanImageToVideo` —— 7/8 个有
- `CR Prompt Text` —— 6/8 个有
- `ImageFromBatch+` —— 6/8 个有
- `SaveImage` —— 5/8 个有
- `TT_img_enc` —— 5/8 个有
- `TorchCompileModel` —— 5/8 个有
- `VHS_VideoCombine` —— 3/8 个有
- `PrimitiveFloat` —— 1/8 个有
- `PrimitiveStringMultiline` —— 1/8 个有
- `TT_img_enc_v2` —— 1/8 个有
- `WanFirstLastFrameToVideo` —— 1/8 个有
- `easy int` —— 1/8 个有
- `easy seed` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 8 | 62% |
| Prompt 约束强度(CFG) | 8 | 6 - 10 | 8 | 88% |
| 采样算法 | 1 | 1 - 1 | 8 | 100% |
| 调度器 | euler | - | 8 | 75% |
| 重绘幅度 | simple | - | 8 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，8 个样本，一致性 62%
- Prompt 约束强度(CFG) 中位数 8，观测区间 6 - 10，8 个样本，取值集中（一致性 88%）
- 采样算法 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，8 个样本，一致性 75%
- 重绘幅度 最常用 simple，8 个样本，一致性 100%
