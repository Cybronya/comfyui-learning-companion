---
name: unknown_workflow_inpaint_lora_sampler_42
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.863
common_nodes: [CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, DownloadAndLoadFlorence2Model, DualCLIPLoader, Florence2Run, FluxGuidance, InpaintModelConditioning, KSampler, LayerMask: MaskGrow, LoadImage, LoraLoaderModelOnly, MaskPreview+, PreviewImage, ReActorRestoreFace, SaveImage, StyleModelApply, StyleModelLoader, UNETLoader, VAEDecode, VAELoader, easy imageInsetCrop, easy makeImageForICLora]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/人物真实换脸 换头 升级版Realistic Face Swapping_2096411533252317186.json, 图片生成/图生图/换脸升级【100%相同，无需PS】_1946417084219973633.json, 平台全量/叠图融合 - F.1_1900259214646980610.json, 平台全量/换脸-ace100换脸_1976957191250944002.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_lora_sampler_42

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/人物真实换脸 换头 升级版Realistic Face Swapping_2096411533252317186.json、图片生成/图生图/换脸升级【100%相同，无需PS】_1946417084219973633.json、平台全量/叠图融合 - F.1_1900259214646980610.json、平台全量/换脸-ace100换脸_1976957191250944002.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `DownloadAndLoadFlorence2Model`
- `DualCLIPLoader`
- `Florence2Run`
- `FluxGuidance`
- `InpaintModelConditioning`
- `KSampler`
- `LayerMask: MaskGrow`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MaskPreview+`
- `PreviewImage`
- `ReActorRestoreFace`
- `SaveImage`
- `StyleModelApply`
- `StyleModelLoader`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy imageInsetCrop`
- `easy makeImageForICLora`

**可变部分**（部分 workflow 才有）：
- `LayerMask: PersonMaskUltra V2` —— 3/4 个有
- `PreviewBridge` —— 3/4 个有
- `Compositor3` —— 2/4 个有
- `CompositorConfig3` —— 2/4 个有
- `CompositorTools3` —— 2/4 个有
- `FastCanvas` —— 2/4 个有
- `FastCanvasTool` —— 2/4 个有
- `GetImageSize+` —— 2/4 个有
- `ImageScale` —— 2/4 个有
- `ImitationHueNode` —— 2/4 个有
- `LayerUtility: CropByMask V2` —— 2/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/4 个有
- `Mask Fill Holes` —— 2/4 个有
- `MaskPreview` —— 2/4 个有
- `RMBG` —— 2/4 个有
- `ConditioningZeroOut` —— 1/4 个有
- `LayerMask: SegmentAnythingUltra V2` —— 1/4 个有
- `ShowText|pysssss` —— 1/4 个有
- `easy cleanGpuUsed` —— 1/4 个有
- `easy humanSegmentation` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 14 | 8 - 20 | 4 | 57% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | sgm_uniform | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 14，观测区间 8 - 20，4 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 sgm_uniform，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（2/4 个样本）：Steps较低可能导致细节不足
