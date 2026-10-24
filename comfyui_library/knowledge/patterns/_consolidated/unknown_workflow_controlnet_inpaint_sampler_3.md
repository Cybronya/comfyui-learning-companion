---
name: unknown_workflow_controlnet_inpaint_sampler_3
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.882
common_nodes: [AnyLineArtPreprocessor_aux, ApplyInstantID, CLIPTextEncode, CheckpointLoaderSimple, ControlNetApplyAdvanced, ControlNetLoader, ImageColorMatch+, InpaintCrop, InpaintModelConditioning, InpaintStitch, InstantIDFaceAnalysis, InstantIDModelLoader, KSampler, LayerMask: PersonMaskUltra V2, LoadImage, MaskBlur+, PreviewImage, SaveImage, VAEDecode]
problems: []
missing: []
members: [图片生成/图生图/InstantID_人物换脸-参考图版_1968356042298011650.json, 图片生成/图生图/啊癫InstantID批量快速换脸 泛用性极高_1934417412018364418.json, 图片生成/图生图/换脸照片 硕阳_2016426629295247362.json, 图片生成/图生图/自然换脸通用性超高 基础InstantID模特换脸2_1935190585428856833.json, 图片生成/图生图/自然换脸通用性超高 基础InstantID模特换脸_1895377628063268866.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_inpaint_sampler_3

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/InstantID_人物换脸-参考图版_1968356042298011650.json、图片生成/图生图/啊癫InstantID批量快速换脸 泛用性极高_1934417412018364418.json、图片生成/图生图/换脸照片 硕阳_2016426629295247362.json、图片生成/图生图/自然换脸通用性超高 基础InstantID模特换脸2_1935190585428856833.json、图片生成/图生图/自然换脸通用性超高 基础InstantID模特换脸_1895377628063268866.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 5 个 workflow 都包含：
- `AnyLineArtPreprocessor_aux`
- `ApplyInstantID`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `ImageColorMatch+`
- `InpaintCrop`
- `InpaintModelConditioning`
- `InpaintStitch`
- `InstantIDFaceAnalysis`
- `InstantIDModelLoader`
- `KSampler`
- `LayerMask: PersonMaskUltra V2`
- `LoadImage`
- `MaskBlur+`
- `PreviewImage`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `Bjornulf_ShowInt` —— 1/5 个有
- `RHBatchImages:` —— 1/5 个有
- `RHExtractImage` —— 1/5 个有
- `RHUploadZip` —— 1/5 个有
- `easy batchAnything` —— 1/5 个有
- `easy forLoopEnd` —— 1/5 个有
- `easy forLoopStart` —— 1/5 个有
- `easy imageCount` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.45 | 0.45 - 0.45 | 5 | 100% |
| 采样步数 | 15 | 15 - 20 | 5 | 88% |
| Prompt 约束强度(CFG) | 1.5 | 1.5 - 1.5 | 5 | 100% |
| 采样算法 | euler_ancestral | - | 5 | 100% |
| 调度器 | sgm_uniform | - | 5 | 100% |
| 重绘幅度 | 0.6 | 0.15 - 0.6 | 5 | 65% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 0.45，观测区间 0.45 - 0.45，5 个样本，取值集中（一致性 100%）
- 采样步数 中位数 15，观测区间 15 - 20，5 个样本，取值集中（一致性 88%）
- Prompt 约束强度(CFG) 中位数 1.5，观测区间 1.5 - 1.5，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，5 个样本，一致性 100%
- 调度器 最常用 sgm_uniform，5 个样本，一致性 100%
- 重绘幅度 中位数 0.6，观测区间 0.15 - 0.6，5 个样本
