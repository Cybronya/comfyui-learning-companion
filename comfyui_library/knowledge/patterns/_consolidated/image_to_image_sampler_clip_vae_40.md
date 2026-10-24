---
name: image_to_image_sampler_clip_vae_40
type: Image To Image
frequency: 2
level: weak
coverage: 0.837
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, NunchakuFluxDiTLoader, PreviewImage, ReferenceLatent, SaveImage, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/nunchaku-flux.1-kontext-dev-扩图-8步快速出图_1954878812870754306.json, 图片生成/图生图/你说我改+一句话改图（kontext图像编辑)_1971800112290787330.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_vae_40

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/nunchaku-flux.1-kontext-dev-扩图-8步快速出图_1954878812870754306.json、图片生成/图生图/你说我改+一句话改图（kontext图像编辑)_1971800112290787330.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：84%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `NunchakuFluxDiTLoader`
- `PreviewImage`
- `ReferenceLatent`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Simple Image Compare` —— 1/2 个有
- `DeepTranslatorTextNode` —— 1/2 个有
- `ImagePadForOutpaint` —— 1/2 个有
- `ImageUpscaleWithModel` —— 1/2 个有
- `PrimitiveInt` —— 1/2 个有
- `UpscaleModelLoader` —— 1/2 个有
- `easy imageConcat` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 181.5 | - | 2 | 11% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 181.5，样本不足，未给区间，2 个样本，取值分散，一致性仅 11%
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 风险：采样步数 观测到 343，超出安全上限 60（steps 偏高收益递减且显著增加耗时）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
