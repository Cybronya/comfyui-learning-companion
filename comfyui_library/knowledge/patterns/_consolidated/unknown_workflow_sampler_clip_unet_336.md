---
name: unknown_workflow_sampler_clip_unet_336
type: Unknown Workflow
frequency: 3
level: strong
coverage: 1
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Flux2_Klei扩图_2012528392184274946.json, 图片生成/文生图/Flux2_Klein 三图编辑_2012088869042262018.json, 图片生成/文生图/Flux2_Klein 多图编辑_2012086737983508482.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_336

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Flux2_Klei扩图_2012528392184274946.json、图片生成/文生图/Flux2_Klein 三图编辑_2012088869042262018.json、图片生成/文生图/Flux2_Klein 多图编辑_2012086737983508482.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：100%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSamplerSelect`
- `LoadImage`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 2/3 个有
- `ImageScaleToTotalPixels` —— 2/3 个有
- `FluxKontextImageScale` —— 1/3 个有
- `GetImage` —— 1/3 个有
- `ImageBlendV1` —— 1/3 个有
- `ImagePadForOutpaint` —— 1/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/3 个有
- `RHHiddenNodes` —— 1/3 个有
- `SimpleMathDual+` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 640 | 640 - 640 | 3 | 100% |
| 高度 | 512 | 512 - 512 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 640，观测区间 640 - 640，3 个样本，取值集中（一致性 100%）
- 高度 中位数 512，观测区间 512 - 512，3 个样本，取值集中（一致性 100%）
