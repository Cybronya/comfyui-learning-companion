---
name: unknown_workflow_inpaint_sampler_clip_70
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.94975
common_nodes: [CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, DualCLIPLoader, FluxGuidance, InpaintModelConditioning, KSampler, LoadImage, SaveImage, StyleModelApply, StyleModelLoader, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/flux redux参考_1894318351114502145.json, 平台全量/F.1 生成任何特效字体 Generate any effect font_1864135884689047554.json, 平台全量/IC_Mask 节点(Flux Fill + Redux转移)工作流示例 icmask_exampl_1899405977442013186.json, 平台全量/LayerUtility_ IC Mask_1871110764130861058.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_clip_70

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/flux redux参考_1894318351114502145.json、平台全量/F.1 生成任何特效字体 Generate any effect font_1864135884689047554.json、平台全量/IC_Mask 节点(Flux Fill + Redux转移)工作流示例 icmask_exampl_1899405977442013186.json、平台全量/LayerUtility_ IC Mask_1871110764130861058.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：95%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `DualCLIPLoader`
- `FluxGuidance`
- `InpaintModelConditioning`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `StyleModelApply`
- `StyleModelLoader`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 3/4 个有
- `DepthAnythingV2Preprocessor` —— 2/4 个有
- `EmptySD3LatentImage` —— 2/4 个有
- `LayerMask: MaskGrow` —— 2/4 个有
- `LayerMask: SegmentAnythingUltra V2` —— 2/4 个有
- `LayerUtility: CropByMask V2` —— 2/4 个有
- `LayerUtility: ICMask` —— 2/4 个有
- `LayerUtility: ICMaskCropBack` —— 2/4 个有
- `LayerUtility: RestoreCropBox` —— 2/4 个有
- `ImageResizeKJ` —— 1/4 个有
- `RH_Captioner` —— 1/4 个有
- `preview_mask` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 22.5 | 20 - 25 | 4 | 89% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | beta | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 22.5，观测区间 20 - 25，4 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 beta，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
