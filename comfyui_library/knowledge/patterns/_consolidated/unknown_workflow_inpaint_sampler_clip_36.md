---
name: unknown_workflow_inpaint_sampler_clip_36
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.8655
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DifferentialDiffusion, DualCLIPLoader, FluxGuidance, GrowMaskWithBlur, ImageComposite+, ImagePadForOutpaintMasked, InpaintModelConditioning, Int, KSampler, LayerMask: MaskGrow, LoadImage, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/全能图片G-Image2 场景一致性V5-视野更大-VR全景-360全景 -720全景_2055632914653696002.json, 图片生成/图生图/场景一致性V3-效果更好-VR全景-360全景 -720全景_2046457662132461570.json, 图片生成/图生图/场景一致性V4-视野更大-VR全景-360全景 -720全景_2054937327281156098.json, 图片生成/图生图/无限画布-VR全景-360全景_2047980025533702145.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_clip_36

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/全能图片G-Image2 场景一致性V5-视野更大-VR全景-360全景 -720全景_2055632914653696002.json、图片生成/图生图/场景一致性V3-效果更好-VR全景-360全景 -720全景_2046457662132461570.json、图片生成/图生图/场景一致性V4-视野更大-VR全景-360全景 -720全景_2054937327281156098.json、图片生成/图生图/无限画布-VR全景-360全景_2047980025533702145.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `FluxGuidance`
- `GrowMaskWithBlur`
- `ImageComposite+`
- `ImagePadForOutpaintMasked`
- `InpaintModelConditioning`
- `Int`
- `KSampler`
- `LayerMask: MaskGrow`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `SeedVR2` —— 3/4 个有
- `easy cleanGpuUsed` —— 3/4 个有
- `RHHiddenNodes` —— 2/4 个有
- `RH_Nano_Banana2_Gemini31Flash` —— 2/4 个有
- `CustomAddLabel` —— 1/4 个有
- `FlashVSRNode` —— 1/4 个有
- `RH_RhartImageG2ImageToImage` —— 1/4 个有
- `RH_RhartImageG2OfficialImageToImage` —— 1/4 个有
- `RTXVideoSuperResolution` —— 1/4 个有
- `RunningHub Deepcleaner` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 30 - 30 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | er_sde | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 30，观测区间 30 - 30，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
