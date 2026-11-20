---
name: unknown_workflow_upscale_clip_unet_10
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.767
common_nodes: [Anything Everywhere, Anything Everywhere3, CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, Image Comparer (rgthree), LoadImage, SaveImage, UNETLoader, UltimateSDUpscale, UpscaleModelLoader, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/高清放大-SD采样放大-Flux_1959995975022620674.json, 平台全量/sd放大-修复放大_1958106365090738177.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_clip_unet_10

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/高清放大-SD采样放大-Flux_1959995975022620674.json、平台全量/sd放大-修复放大_1958106365090738177.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：77%

## 共有节点

全部 2 个 workflow 都包含：
- `Anything Everywhere`
- `Anything Everywhere3`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `Image Comparer (rgthree)`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `UltimateSDUpscale`
- `UpscaleModelLoader`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConstrainImage|pysssss` —— 1/2 个有
- `Float` —— 1/2 个有
- `JWImageResizeByShorterSide` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `PreviewImage` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
