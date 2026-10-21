---
name: unknown_workflow_video_sampler_vae_115
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 1
common_nodes: [LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/文生视频/1901660787495346177.json, 视频生成/文生视频/【遇见AI】wan2.1文生视频基础流，不带加速_2061012769037701122.json, 视频生成/文生视频/1907671581512855554.json, 视频生成/文生视频/1894627522200645634.json, 视频生成/文生视频/1894633919931920385.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_115

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/文生视频/1901660787495346177.json、视频生成/文生视频/【遇见AI】wan2.1文生视频基础流，不带加速_2061012769037701122.json、视频生成/文生视频/1907671581512855554.json、视频生成/文生视频/1894627522200645634.json、视频生成/文生视频/1894633919931920385.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：100%

## 共有节点

全部 5 个 workflow 都包含：
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `WanVideoEmptyEmbeds`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `WanVideoBlockSwap` —— 4/5 个有
- `WanVideoTorchCompileSettings` —— 2/5 个有
- `ImageUpscaleWithModel` —— 1/5 个有
- `Note Plus (mtb)` —— 1/5 个有
- `Primitive string [Crystools]` —— 1/5 个有
- `RIFE VFI` —— 1/5 个有
- `UpscaleModelLoader` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
