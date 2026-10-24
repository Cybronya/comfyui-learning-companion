---
name: image_to_image_controlnet_face_detailer_sampler_2
type: Image To Image
frequency: 2
level: weak
coverage: 0.857
common_nodes: [AIO_Preprocessor, Anything Everywhere3, CLIPTextEncode, CheckpointLoaderSimple, ControlNetApplyAdvanced, ControlNetLoader, FaceDetailer, JanusImageUnderstanding, JanusModelLoader, JjkText, JoinStrings, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, SAMLoader, SaveImage, ShowText|pysssss, UltralyticsDetectorProvider, VAEDecode, VAEEncode]
problems: []
missing: []
members: [图片生成/图生图/动漫转真人｜润色_1952906622270115842.json, 图片生成/图生图/卡通转真人_1927009560664428545.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_face_detailer_sampler_2

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/动漫转真人｜润色_1952906622270115842.json、图片生成/图生图/卡通转真人_1927009560664428545.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：86%

## 共有节点

全部 2 个 workflow 都包含：
- `AIO_Preprocessor`
- `Anything Everywhere3`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `FaceDetailer`
- `JanusImageUnderstanding`
- `JanusModelLoader`
- `JjkText`
- `JoinStrings`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `SAMLoader`
- `SaveImage`
- `ShowText|pysssss`
- `UltralyticsDetectorProvider`
- `VAEDecode`
- `VAEEncode`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.4 | - | 2 | 100% |
| 采样步数 | 30 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 5.5 | - | 2 | 100% |
| 采样算法 | euler_ancestral | - | 2 | 100% |
| 调度器 | sgm_uniform | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 0.4，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 30，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 5.5，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，2 个样本，一致性 100%
- 调度器 最常用 sgm_uniform，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
