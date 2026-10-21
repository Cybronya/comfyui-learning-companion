---
name: unknown_workflow_sampler_clip_checkpoint_14
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.901
common_nodes: [CLIPLoader, CLIPTextEncode, CheckpointLoaderSimple, KSamplerSelect, LTXVConditioning, LTXVScheduler, SamplerCustom, VAEDecode]
problems: []
missing: []
members: [comfyui-workflow-templates-json/ltxv_image_to_video.json, comfyui-workflow-templates-json/ltxv_text_to_video.json, 视频生成/图生视频/1897315393487196161.json, 视频生成/图生视频/1898011763626201090.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_checkpoint_14

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（comfyui-workflow-templates-json/ltxv_image_to_video.json、comfyui-workflow-templates-json/ltxv_text_to_video.json、视频生成/图生视频/1897315393487196161.json、视频生成/图生视频/1898011763626201090.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `KSamplerSelect`
- `LTXVConditioning`
- `LTXVScheduler`
- `SamplerCustom`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `LTXVImgToVideo` —— 3/4 个有
- `LoadImage` —— 3/4 个有
- `CreateVideo` —— 2/4 个有
- `SaveVideo` —— 2/4 个有
- `TextInput_` —— 2/4 个有
- `VHS_VideoCombine` —— 2/4 个有
- `ApplyFBCacheOnModel` —— 1/4 个有
- `Bjornulf_ShowStringText` —— 1/4 个有
- `EmptyLTXVLatentVideo` —— 1/4 个有
- `Note Plus (mtb)` —— 1/4 个有
- `PatchModelPatcherOrder` —— 1/4 个有
- `PathchSageAttentionKJ` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
