---
name: unknown_workflow_video_sampler_clip_264
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.921
common_nodes: [CLIPLoader, CLIPTextEncode, CheckpointLoaderSimple, KSamplerSelect, LTXVConditioning, LTXVImgToVideo, LTXVScheduler, LoadImage, SamplerCustom, TextInput_, VAEDecode, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/最快的视频生成模型+LTX-Video+图生视频-StarAI_1898011763626201090.json, 视频生成/图生视频/🦖 LTXV 0.9.5 极速生视频_1897826288936407042.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_264

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/最快的视频生成模型+LTX-Video+图生视频-StarAI_1898011763626201090.json、视频生成/图生视频/🦖 LTXV 0.9.5 极速生视频_1897826288936407042.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：92%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `KSamplerSelect`
- `LTXVConditioning`
- `LTXVImgToVideo`
- `LTXVScheduler`
- `LoadImage`
- `SamplerCustom`
- `TextInput_`
- `VAEDecode`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `ApplyFBCacheOnModel` —— 1/2 个有
- `ArgosTranslateTextNode` —— 1/2 个有
- `Bjornulf_ShowStringText` —— 1/2 个有
- `DeepTranslatorTextNode` —— 1/2 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有
- `Note Plus (mtb)` —— 1/2 个有
- `PatchModelPatcherOrder` —— 1/2 个有
- `PathchSageAttentionKJ` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
