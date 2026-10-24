---
name: unknown_workflow_upscale_face_detailer_lora
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.773
common_nodes: [CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, FaceDetailer, Fast Groups Bypasser (rgthree), Image Comparer (rgthree), ImpactInt, Int, JjkText, JoinStringMulti, KSamplerAdvanced, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, PrimitiveStringMultiline, SEGSOrderedFilterDetailerHookProvider, SaveImage, ShowText|pysssss, UNETLoader, UltimateSDUpscale, UltralyticsDetectorProvider, UpscaleModelLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Anima图生图双采全能工作流-加速_反推_高清_2070388365610020865.json, 图片生成/文生图/Anima文生图双采全能工作流_2070706809408675842.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_face_detailer_lora

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Anima图生图双采全能工作流-加速_反推_高清_2070388365610020865.json、图片生成/文生图/Anima文生图双采全能工作流_2070706809408675842.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：77%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `FaceDetailer`
- `Fast Groups Bypasser (rgthree)`
- `Image Comparer (rgthree)`
- `ImpactInt`
- `Int`
- `JjkText`
- `JoinStringMulti`
- `KSamplerAdvanced`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `PrimitiveStringMultiline`
- `SEGSOrderedFilterDetailerHookProvider`
- `SaveImage`
- `ShowText|pysssss`
- `UNETLoader`
- `UltimateSDUpscale`
- `UltralyticsDetectorProvider`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 1/2 个有
- `LoadImage` —— 1/2 个有
- `RH_Captioner` —— 1/2 个有
- `WD14Tagger|pysssss` —— 1/2 个有
- `easy textSwitch` —— 1/2 个有
- `llama_cpp_instruct_adv` —— 1/2 个有
- `llama_cpp_model_loader` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 2 | 50% |
| Prompt 约束强度(CFG) | 20 | - | 2 | 100% |
| 采样算法 | 2.5 | - | 2 | 40% |
| 调度器 | euler | - | 2 | 50% |
| 重绘幅度 | simple | - | 2 | 100% |
| 宽度 | 1280 | - | 2 | 100% |
| 高度 | 1920 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，2 个样本，一致性 50%
- Prompt 约束强度(CFG) 中位数 20，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 中位数 2.5，样本不足，未给区间，2 个样本，取值分散，一致性仅 40%
- 调度器 最常用 euler，2 个样本，一致性 50%
- 重绘幅度 最常用 simple，2 个样本，一致性 100%
- 宽度 中位数 1280，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1920，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
