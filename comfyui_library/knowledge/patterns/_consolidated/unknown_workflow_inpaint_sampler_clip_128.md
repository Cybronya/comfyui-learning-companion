---
name: unknown_workflow_inpaint_sampler_clip_128
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8615
common_nodes: [BlendInpaint, CLIPTextEncode, CheckpointLoaderSimple, ConditioningZeroOut, DualCLIPLoader, Florence2Run, GrowMask, INPAINT_ApplyFooocusInpaint, INPAINT_InpaintWithModel, INPAINT_LoadFooocusInpaint, INPAINT_LoadInpaintModel, INPAINT_VAEEncodeInpaintConditioning, Image Comparer (rgthree), ImageScale, ImageToMask, InpaintModelConditioning, KSampler, LoadImage, MaskToImage, SaveImage, ShowText|pysssss, UNETLoader, VAEDecode, VAELoader, easy imageScaleDownToSize]
problems: []
missing: []
members: [平台全量/万物移除物体工作流_Fooocus局部重绘_FLUX高清细化_1914549077521170433.json, 平台全量/移除物体&图片去水印_1921208256222412801.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_clip_128

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/万物移除物体工作流_Fooocus局部重绘_FLUX高清细化_1914549077521170433.json、平台全量/移除物体&图片去水印_1921208256222412801.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：86%

## 共有节点

全部 2 个 workflow 都包含：
- `BlendInpaint`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `Florence2Run`
- `GrowMask`
- `INPAINT_ApplyFooocusInpaint`
- `INPAINT_InpaintWithModel`
- `INPAINT_LoadFooocusInpaint`
- `INPAINT_LoadInpaintModel`
- `INPAINT_VAEEncodeInpaintConditioning`
- `Image Comparer (rgthree)`
- `ImageScale`
- `ImageToMask`
- `InpaintModelConditioning`
- `KSampler`
- `LoadImage`
- `MaskToImage`
- `SaveImage`
- `ShowText|pysssss`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy imageScaleDownToSize`

**可变部分**（部分 workflow 才有）：
- `AIO_Preprocessor` —— 1/2 个有
- `CLIPTextEncodeFlux` —— 1/2 个有
- `ControlNetApply` —— 1/2 个有
- `ControlNetApplyAdvanced` —— 1/2 个有
- `ControlNetLoader` —— 1/2 个有
- `DownloadAndLoadFlorence2Model` —— 1/2 个有
- `Florence2ModelLoader` —— 1/2 个有
- `GetImageSize` —— 1/2 个有
- `IPAdapterAdvanced` —— 1/2 个有
- `IPAdapterUnifiedLoader` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `Mask Fill Holes` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `easy imageSize` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | - | 2 | 80% |
| Prompt 约束强度(CFG) | 4 | - | 2 | 25% |
| 采样算法 | dpmpp_2m | - | 2 | 50% |
| 调度器 | karras | - | 2 | 50% |
| 重绘幅度 | 0.565 | - | 2 | 67% |
| ControlNet 权重 | 0.73 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，样本不足，未给区间，2 个样本，取值集中（一致性 80%）
- Prompt 约束强度(CFG) 中位数 4，样本不足，未给区间，2 个样本，取值分散，一致性仅 25%
- 采样算法 最常用 dpmpp_2m，2 个样本，一致性 50%
- 调度器 最常用 karras，2 个样本，一致性 50%
- 重绘幅度 中位数 0.565，样本不足，未给区间，2 个样本
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
