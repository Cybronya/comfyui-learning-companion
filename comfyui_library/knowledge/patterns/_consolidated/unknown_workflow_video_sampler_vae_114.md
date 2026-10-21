---
name: unknown_workflow_video_sampler_vae_114
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.8214
common_nodes: [LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoEnhanceAVideo, WanVideoModelLoader, WanVideoSampler, WanVideoTeaCache, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/文生视频/1961757456491810818.json, 视频生成/文生视频/1947899164087713793.json, 视频生成/文生视频/1947915366925250562.json, 视频生成/文生视频/1945700815371739138.json, 视频生成/文生视频/1940772323597434882.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_114

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/文生视频/1961757456491810818.json、视频生成/文生视频/1947899164087713793.json、视频生成/文生视频/1947915366925250562.json、视频生成/文生视频/1945700815371739138.json、视频生成/文生视频/1940772323597434882.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 5 个 workflow 都包含：
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEmptyEmbeds`
- `WanVideoEnhanceAVideo`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `WanVideoTextEncode` —— 4/5 个有
- `Int` —— 2/5 个有
- `LoadImageFromUrl` —— 2/5 个有
- `Note Plus (mtb)` —— 2/5 个有
- `SimpleMath+` —— 2/5 个有
- `WanVideoSLG` —— 2/5 个有
- `WanVideoVRAMManagement` —— 2/5 个有
- `easy showAnything` —— 2/5 个有
- `Label (rgthree)` —— 1/5 个有
- `WanVideoApplyNAG` —— 1/5 个有
- `WanVideoTextEncodeSingle` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
