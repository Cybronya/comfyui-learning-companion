---
name: unknown_workflow_video_sampler_vae_174
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 1
common_nodes: [LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/文生视频/通义万相 文生图工作流-小宣喧 -RH_1894608598201204738.json, 视频生成/文生视频/通义万相Wan2.1文生视频高清补帧放大_1897231501354815489.json, 视频生成/文生视频/阿里万象文生视频_1894633919931920385.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_174

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/文生视频/通义万相 文生图工作流-小宣喧 -RH_1894608598201204738.json、视频生成/文生视频/通义万相Wan2.1文生视频高清补帧放大_1897231501354815489.json、视频生成/文生视频/阿里万象文生视频_1894633919931920385.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：100%

## 共有节点

全部 3 个 workflow 都包含：
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
- `CR Text` —— 1/3 个有
- `CR Upscale Image` —— 1/3 个有
- `LoadAudio` —— 1/3 个有
- `RIFE VFI` —— 1/3 个有
- `WanVideoTorchCompileSettings` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
