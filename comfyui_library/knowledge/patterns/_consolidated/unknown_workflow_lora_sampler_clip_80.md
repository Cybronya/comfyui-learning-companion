---
name: unknown_workflow_lora_sampler_clip_80
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.872286
common_nodes: [ACEPlusLoraProcessor, CLIPTextEncode, DifferentialDiffusion, DualCLIPLoader, FluxGuidance, ImageCrop, KSampler, LoadImage, LoraLoaderModelOnly, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/ACE++_Localedit_repainting_only_图像编辑（重绘）_1956957594424369154.json, 图片生成/图生图/ACE++_Localedit_repainting_ref_redux_参考+Redux重绘_1956959999537680386.json, 图片生成/图生图/ACE++_Localedit_repainting_reference_参考重绘_1956953313319247874.json, 图片生成/图生图/ACE++_localedit_图像编辑基础（重上色+Canny）_1956941547046625281.json, 图片生成/图生图/OneReward万物迁移+subject_1970483302937337858.json, 图片生成/图生图/OneReward万物迁移subject x seg_1970486904108032002.json, 平台全量/最新万物迁移  Redux+Fill+AceLocal_1922304939438309377.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_80

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/ACE++_Localedit_repainting_only_图像编辑（重绘）_1956957594424369154.json、图片生成/图生图/ACE++_Localedit_repainting_ref_redux_参考+Redux重绘_1956959999537680386.json、图片生成/图生图/ACE++_Localedit_repainting_reference_参考重绘_1956953313319247874.json、图片生成/图生图/ACE++_localedit_图像编辑基础（重上色+Canny）_1956941547046625281.json、图片生成/图生图/OneReward万物迁移+subject_1970483302937337858.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 7 个 workflow 都包含：
- `ACEPlusLoraProcessor`
- `CLIPTextEncode`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `FluxGuidance`
- `ImageCrop`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ACEPlusLoraConditioning` —— 6/7 个有
- `GrowMaskWithBlur` —— 6/7 个有
- `LoadImageFromUrl` —— 6/7 个有
- `MaskPreview+` —— 6/7 个有
- `Note Plus (mtb)` —— 6/7 个有
- `RMBG` —— 5/7 个有
- `CLIPVisionEncode` —— 4/7 个有
- `CLIPVisionLoader` —— 4/7 个有
- `StyleModelApply` —— 4/7 个有
- `StyleModelLoader` —— 4/7 个有
- `Anything Everywhere` —— 1/7 个有
- `GroundingDinoModelLoader (segment anything2)` —— 1/7 个有
- `GroundingDinoSAM2Segment (segment anything2)` —— 1/7 个有
- `InpaintModelConditioning` —— 1/7 个有
- `LayerMask: MaskPreview` —— 1/7 个有
- `LayerMask: SegmentAnythingUltra V2` —— 1/7 个有
- `SAM2ModelLoader (segment anything2)` —— 1/7 个有
- `SetNode` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 28 | 28 - 28 | 7 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | normal | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 28，观测区间 28 - 28，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 normal，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
