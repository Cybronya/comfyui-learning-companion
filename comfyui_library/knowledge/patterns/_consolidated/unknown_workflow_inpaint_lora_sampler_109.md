---
name: unknown_workflow_inpaint_lora_sampler_109
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8515
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DifferentialDiffusion, DualCLIPLoader, FluxGuidance, ImageCrop, ImageGenResolutionFromImage, ImagePadForOutpaint, InpaintModelConditioning, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, PreviewImage, RMBG, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [平台全量/ACE++角色一致性保持电影分镜，儿童绘本，小说插画_1915633426651611138.json, 平台全量/ACE角色一致性+视频分镜制作【AI小王子】_1915422040600281089.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_lora_sampler_109

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/ACE++角色一致性保持电影分镜，儿童绘本，小说插画_1915633426651611138.json、平台全量/ACE角色一致性+视频分镜制作【AI小王子】_1915422040600281089.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：85%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `FluxGuidance`
- `ImageCrop`
- `ImageGenResolutionFromImage`
- `ImagePadForOutpaint`
- `InpaintModelConditioning`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `RMBG`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ArgosTranslateTextNode` —— 1/2 个有
- `CR Text` —— 1/2 个有
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `Image Comparer (rgthree)` —— 1/2 个有
- `LayerUtility: PurgeVRAM V2` —— 1/2 个有
- `Note Plus (mtb)` —— 1/2 个有
- `RHHiddenNodes` —— 1/2 个有
- `ShowText|pysssss` —— 1/2 个有
- `TextInput_` —— 1/2 个有
- `easy makeImageForICLora` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | beta | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 beta，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
