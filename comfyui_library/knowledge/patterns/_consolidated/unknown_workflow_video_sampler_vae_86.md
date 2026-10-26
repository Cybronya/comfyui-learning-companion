---
name: unknown_workflow_video_sampler_vae_86
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.944333
common_nodes: [LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/文生视频/WAN2.1 万相文生视频_1894738475621482497.json, 视频生成/文生视频/WAN2.1 万相文生视频_2012869543177228289.json, 视频生成/文生视频/WAN2.1 万相文生视频_2013157670638850049.json, 视频生成/文生视频/Wan文生视频工作流-KJ版_1894761032408313857.json, 视频生成/文生视频/wanvideo_T2V_文生视频kijai版_1894655158603677697.json, 视频生成/文生视频/【自定义Wan2.1万相】文生视频_1901660787495346177.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_86

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/文生视频/WAN2.1 万相文生视频_1894738475621482497.json、视频生成/文生视频/WAN2.1 万相文生视频_2012869543177228289.json、视频生成/文生视频/WAN2.1 万相文生视频_2013157670638850049.json、视频生成/文生视频/Wan文生视频工作流-KJ版_1894761032408313857.json、视频生成/文生视频/wanvideo_T2V_文生视频kijai版_1894655158603677697.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 6 个 workflow 都包含：
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEmptyEmbeds`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `WanVideoTorchCompileSettings` —— 5/6 个有
- `ImageUpscaleWithModel` —— 4/6 个有
- `RIFE VFI` —— 4/6 个有
- `UpscaleModelLoader` —— 4/6 个有
- `SeargePromptText` —— 3/6 个有
- `easy cleanGpuUsed` —— 3/6 个有
- `Note Plus (mtb)` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
