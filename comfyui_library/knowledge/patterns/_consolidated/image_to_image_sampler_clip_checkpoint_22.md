---
name: image_to_image_sampler_clip_checkpoint_22
type: Image To Image
frequency: 2
level: weak
coverage: 0.8495
common_nodes: [BRIA_RMBG_ModelLoader_Zho, BRIA_RMBG_Zho, CLIPTextEncode, CheckpointLoaderSimple, ImageResize+, ImageResizeKJ, Int, KSampler, LayerMask: MaskPreview, LayerUtility: ColorImage, LayerUtility: ColorPicker, LayerUtility: ImageBlendAdvance V2, LoadImage, PreviewImage, SaveImage, VAEDecode, VAEEncode, [Comfy3D] Load Diffusers Pipeline, [Comfy3D] MVDream Model]
problems: []
missing: []
members: [平台全量/一张图像生成多视图工作流_1838912367244591105.json, 平台全量/图像生成3D模型（3D-Pack）_1838817194473058306.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_checkpoint_22

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/一张图像生成多视图工作流_1838912367244591105.json、平台全量/图像生成3D模型（3D-Pack）_1838817194473058306.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：85%

## 共有节点

全部 2 个 workflow 都包含：
- `BRIA_RMBG_ModelLoader_Zho`
- `BRIA_RMBG_Zho`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ImageResize+`
- `ImageResizeKJ`
- `Int`
- `KSampler`
- `LayerMask: MaskPreview`
- `LayerUtility: ColorImage`
- `LayerUtility: ColorPicker`
- `LayerUtility: ImageBlendAdvance V2`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`
- `[Comfy3D] Load Diffusers Pipeline`
- `[Comfy3D] MVDream Model`

**可变部分**（部分 workflow 才有）：
- `InvertMask` —— 1/2 个有
- `Joy_caption` —— 1/2 个有
- `Joy_caption_load` —— 1/2 个有
- `MaskPreview+` —— 1/2 个有
- `[Comfy3D] Convert 3DGS to Mesh with NeRF and Marching Cubes` —— 1/2 个有
- `[Comfy3D] Large Multiview Gaussian Model` —— 1/2 个有
- `[Comfy3D] Load Large Multiview Gaussian Model` —— 1/2 个有
- `[Comfy3D] Preview 3DMesh` —— 1/2 个有
- `[Comfy3D] Save 3D Mesh` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 17.5 | - | 2 | 86% |
| Prompt 约束强度(CFG) | 7.04 | - | 2 | 100% |
| 采样算法 | euler_ancestral | - | 2 | 100% |
| 调度器 | normal | - | 2 | 100% |
| 重绘幅度 | 0.215 | - | 2 | 60% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 17.5，样本不足，未给区间，2 个样本，取值集中（一致性 86%）
- Prompt 约束强度(CFG) 中位数 7.04，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，2 个样本，一致性 100%
- 调度器 最常用 normal，2 个样本，一致性 100%
- 重绘幅度 中位数 0.215，样本不足，未给区间，2 个样本
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
