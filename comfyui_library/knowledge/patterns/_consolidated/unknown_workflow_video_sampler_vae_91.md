---
name: unknown_workflow_video_sampler_vae_91
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.966667
common_nodes: [LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/文生视频/1894738475621482497.json, 视频生成/文生视频/WAN2.1 万相文生视频_2012869543177228289.json, 视频生成/文生视频/WAN2.1 万相文生视频_2013157670638850049.json, 视频生成/文生视频/1935600068689068033.json, 视频生成/文生视频/1934871279478448130.json, 视频生成/文生视频/1935156530729951234.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_91

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/文生视频/1894738475621482497.json、视频生成/文生视频/WAN2.1 万相文生视频_2012869543177228289.json、视频生成/文生视频/WAN2.1 万相文生视频_2013157670638850049.json、视频生成/文生视频/1935600068689068033.json、视频生成/文生视频/1934871279478448130.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：97%

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
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `RIFE VFI` —— 5/6 个有
- `ImageUpscaleWithModel` —— 3/6 个有
- `SeargePromptText` —— 3/6 个有
- `UpscaleModelLoader` —— 3/6 个有
- `WanVideoLoraSelect` —— 3/6 个有
- `easy cleanGpuUsed` —— 3/6 个有
- `Video_Upscale_With_Model` —— 2/6 个有
- `WanVideoEnhanceAVideo` —— 2/6 个有
- `WanVideoVRAMManagement` —— 2/6 个有
- `Label (rgthree)` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
