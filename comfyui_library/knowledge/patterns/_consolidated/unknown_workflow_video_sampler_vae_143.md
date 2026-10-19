---
name: unknown_workflow_video_sampler_vae_143
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.577333
common_nodes: [LoadWanVideoT5TextEncoder, PrimitiveInt, Text Multiline, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoExperimentalArgs, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1989234021240549377.json, 视频生成/图生视频/1907098991245582337.json, 视频生成/文生视频/03-01-02-WAN2.1-文生视频-kijai_1989233864696541185.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_143

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/1989234021240549377.json、视频生成/图生视频/1907098991245582337.json、视频生成/文生视频/03-01-02-WAN2.1-文生视频-kijai_1989233864696541185.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：58%

## 共有节点

全部 3 个 workflow 都包含：
- `LoadWanVideoT5TextEncoder`
- `PrimitiveInt`
- `Text Multiline`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoExperimentalArgs`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `GIMMVFI_interpolate` —— 2/3 个有
- `GetNode` —— 2/3 个有
- `ImageResizeKJ` —— 2/3 个有
- `LoadImage` —— 2/3 个有
- `RIFE VFI` —— 2/3 个有
- `SetNode` —— 2/3 个有
- `WanVideoClipVisionEncode` —— 2/3 个有
- `WanVideoEnhanceAVideo` —— 2/3 个有
- `WanVideoImageToVideoEncode` —— 2/3 个有
- `WanVideoLoraSelectMulti` —— 2/3 个有
- `WanVideoSetRadialAttention` —— 2/3 个有
- `Bool` —— 1/3 个有
- `CLIPVisionLoader` —— 1/3 个有
- `LoadWanVideoClipTextEncoder` —— 1/3 个有
- `WanVideoEmptyEmbeds` —— 1/3 个有
- `easy ifElse` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
