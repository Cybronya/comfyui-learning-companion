---
name: unknown_workflow_controlnet_lora_sampler_24
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.702
common_nodes: [Any Switch (rgthree), CLIPLoaderGGUF, CLIPTextEncode, CR Text, CannyEdgePreprocessor, ConditioningZeroOut, DWPreprocessor, DepthAnythingV2Preprocessor, EmptyLatentImage, Fast Groups Bypasser (rgthree), HEDPreprocessor, INTConstant, KSamplerAdvanced, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, LoadImage, LoraLoaderModelOnly, ModelPatchLoader, ModelSamplingAuraFlow, PlaySound|pysssss, PreviewImage, QwenImageDiffsynthControlnet, SaveImage, UNETLoader, UnetLoaderGGUF, VAEDecode, VAELoader, easy seed]
problems: []
missing: []
members: [图片生成/图生图/Z Image 完全体｜Z 双采融合采样 ComfyUI 一体化工作流_2059558369454813185.json, 图片生成/图生图/Z_Image_完全体_Z_双采融合采样一体化工作流_2068563391140159490.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_lora_sampler_24

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Z Image 完全体｜Z 双采融合采样 ComfyUI 一体化工作流_2059558369454813185.json、图片生成/图生图/Z_Image_完全体_Z_双采融合采样一体化工作流_2068563391140159490.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：70%

## 共有节点

全部 2 个 workflow 都包含：
- `Any Switch (rgthree)`
- `CLIPLoaderGGUF`
- `CLIPTextEncode`
- `CR Text`
- `CannyEdgePreprocessor`
- `ConditioningZeroOut`
- `DWPreprocessor`
- `DepthAnythingV2Preprocessor`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `HEDPreprocessor`
- `INTConstant`
- `KSamplerAdvanced`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelPatchLoader`
- `ModelSamplingAuraFlow`
- `PlaySound|pysssss`
- `PreviewImage`
- `QwenImageDiffsynthControlnet`
- `SaveImage`
- `UNETLoader`
- `UnetLoaderGGUF`
- `VAEDecode`
- `VAELoader`
- `easy seed`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 2 | 100% |
| Prompt 约束强度(CFG) | 3 | - | 2 | 100% |
| 采样算法 | 1 | - | 2 | 100% |
| 调度器 | res_multistep | - | 2 | 100% |
| 重绘幅度 | simple | - | 2 | 100% |
| 宽度 | 800 | - | 2 | 100% |
| 高度 | 1416 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，2 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 3，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 最常用 res_multistep，2 个样本，一致性 100%
- 重绘幅度 最常用 simple，2 个样本，一致性 100%
- 宽度 中位数 800，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1416，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
