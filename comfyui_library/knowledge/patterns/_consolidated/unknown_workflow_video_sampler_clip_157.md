---
name: unknown_workflow_video_sampler_clip_157
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.5525
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, ImageResizeKJv2, KSamplerSelect, LoadImage, ModelSamplingSD3, SamplerCustom, SetNode, TrimVideoLatent, VAEDecodeTiled, VAELoader, VHS_LoadVideo, VHS_VideoCombine, WanAnimate2ToVideo, WanContextWindowsManual]
problems: []
missing: []
members: [平台全量/Wan-Animate-2 动作迁移_2086613839050792961.json, 视频生成/图生视频/CG迷-Wan-Animate-2工作流_2086749147369136130.json, 视频生成/图生视频/Wan Antimate 2动作迁移+全节点注释_2086650842647711746.json, 视频生成/图生视频/Wan-Antimate-2 动作迁移 长视频_2085941636684664834.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_157

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（平台全量/Wan-Animate-2 动作迁移_2086613839050792961.json、视频生成/图生视频/CG迷-Wan-Animate-2工作流_2086749147369136130.json、视频生成/图生视频/Wan Antimate 2动作迁移+全节点注释_2086650842647711746.json、视频生成/图生视频/Wan-Antimate-2 动作迁移 长视频_2085941636684664834.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：55%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `LoadImage`
- `ModelSamplingSD3`
- `SamplerCustom`
- `SetNode`
- `TrimVideoLatent`
- `VAEDecodeTiled`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanAnimate2ToVideo`
- `WanContextWindowsManual`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 3/4 个有
- `PathchSageAttentionKJ` —— 3/4 个有
- `UNETLoader` —— 3/4 个有
- `VideoInfoLoaded` —— 3/4 个有
- `CR Value` —— 1/4 个有
- `ComfyMathExpression` —— 1/4 个有
- `DiffusionModelLoaderKJ` —— 1/4 个有
- `Label (rgthree)` —— 1/4 个有
- `PrimitiveInt` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
