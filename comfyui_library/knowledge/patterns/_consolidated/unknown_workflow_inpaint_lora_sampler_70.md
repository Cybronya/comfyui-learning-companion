---
name: unknown_workflow_inpaint_lora_sampler_70
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.780667
common_nodes: [BackgroundEraseNetwork, CFGZeroStarAndInit, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, DifferentialDiffusion, DualCLIPLoader, FluxGuidance, ImageResize+, InpaintModelConditioning, KSampler, LayerMask: MaskGrow, LayerUtility: ColorImage, LayerUtility: ColorPicker, LayerUtility: CropByMask V2, LayerUtility: ICMask, LayerUtility: ICMaskCropBack, LayerUtility: ImageBlend, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: RestoreCropBox, LoadImage, LoraLoaderModelOnly, MaskToImage, PreviewImage, SaveImage, StyleModelApply, StyleModelLoader, UNETLoader, VAEDecode, VAELoader, easy imageSize]
problems: [Steps较低可能导致细节不足]
missing: []
members: [平台全量/fizz-动漫人物细节替换_1908391965518344194.json, 平台全量/fizz-换脸-真人_1908331553137504257.json, 平台全量/fizz-衣服_物品替换_1908373817931276289.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_lora_sampler_70

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/fizz-动漫人物细节替换_1908391965518344194.json、平台全量/fizz-换脸-真人_1908331553137504257.json、平台全量/fizz-衣服_物品替换_1908373817931276289.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：78%

## 共有节点

全部 3 个 workflow 都包含：
- `BackgroundEraseNetwork`
- `CFGZeroStarAndInit`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `FluxGuidance`
- `ImageResize+`
- `InpaintModelConditioning`
- `KSampler`
- `LayerMask: MaskGrow`
- `LayerUtility: ColorImage`
- `LayerUtility: ColorPicker`
- `LayerUtility: CropByMask V2`
- `LayerUtility: ICMask`
- `LayerUtility: ICMaskCropBack`
- `LayerUtility: ImageBlend`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: RestoreCropBox`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MaskToImage`
- `PreviewImage`
- `SaveImage`
- `StyleModelApply`
- `StyleModelLoader`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy imageSize`

**可变部分**（部分 workflow 才有）：
- `CropFace` —— 1/3 个有
- `ImitationHueNode` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | beta | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
